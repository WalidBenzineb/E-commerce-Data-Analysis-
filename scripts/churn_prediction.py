import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming full_orders dataframe is available from previous analysis

# Define churn (e.g., no purchase in last 90 days)
last_purchase_date = full_orders.groupby('accountId')['orderDate'].max()
churn_threshold = pd.Timestamp('2024-06-28') - pd.Timedelta(days=90)
is_churned = (last_purchase_date < churn_threshold).astype(int)

# Prepare features
features = full_orders.groupby('accountId').agg({
    'orderDate': lambda x: (pd.Timestamp('2024-06-28') - x.max()).days,
    'orderId': 'count',
    'price': ['sum', 'mean'],
    'paymentMethod': lambda x: x.value_counts().index[0]
})
features.columns = ['recency', 'frequency', 'total_spend', 'avg_order_value', 'preferred_payment']
features['churned'] = is_churned

# Encode categorical variables
features = pd.get_dummies(features, columns=['preferred_payment'])

# Split data
X = features.drop('churned', axis=1)
y = features['churned']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("Churn Prediction Model Performance:")
print(classification_report(y_test, y_pred))

# Feature importance
importance = pd.DataFrame({'feature': X.columns, 'importance': model.feature_importances_})
importance = importance.sort_values('importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=importance.head(10))
plt.title('Top 10 Important Features for Churn Prediction')
plt.savefig(os.path.join('outputs', 'figures', 'churn_feature_importance.png'))
plt.close()

print("\nTop 5 Important Features for Churn Prediction:")
print(importance.head())