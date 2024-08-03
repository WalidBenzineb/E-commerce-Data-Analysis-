import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Assuming full_orders dataframe is available from previous analysis

# Calculate total revenue per customer
customer_revenue = full_orders.groupby('accountId')['price'].sum().reset_index()

# Calculate recency, frequency, and monetary value
rfm = full_orders.groupby('accountId').agg({
    'orderDate': lambda x: (pd.Timestamp('2024-06-28') - x.max()).days,
    'orderId': 'count',
    'price': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Combine RFM with revenue data
clv_data = pd.merge(rfm, customer_revenue, on='accountId')

# Normalize the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
clv_normalized = scaler.fit_transform(clv_data[['Recency', 'Frequency', 'Monetary']])

# Perform K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clv_data['Cluster'] = kmeans.fit_predict(clv_normalized)

# Calculate average values for each cluster
cluster_avg = clv_data.groupby('Cluster').mean()

# Visualize clusters
plt.figure(figsize=(12, 8))
scatter = plt.scatter(clv_data['Recency'], clv_data['Monetary'], 
                      c=clv_data['Cluster'], s=clv_data['Frequency']*10, 
                      alpha=0.6, cmap='viridis')
plt.xlabel('Recency (days)')
plt.ylabel('Monetary Value ($)')
plt.title('Customer Segments based on RFM')
plt.colorbar(scatter, label='Cluster')
plt.savefig(os.path.join('outputs', 'figures', 'clv_clusters.png'))
plt.close()

print("Customer Lifetime Value Clusters:")
print(cluster_avg)

# Predict future value (simple model)
avg_order_value = clv_data['Monetary'] / clv_data['Frequency']
purchase_frequency = clv_data['Frequency'] / ((clv_data['Recency'].max() - clv_data['Recency']) / 365)
clv_data['Predicted_Annual_Value'] = avg_order_value * purchase_frequency * 12  # Assuming 12 months

print("\nTop 10 Customers by Predicted Annual Value:")
print(clv_data.sort_values('Predicted_Annual_Value', ascending=False).head(10)[['Predicted_Annual_Value']])