import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def perform_sales_analysis(df):
    # Payment Method Analysis
    payment_method_counts = df['paymentMethod'].value_counts()

    # Visualize Payment Methods
    plt.figure(figsize=(10, 6))
    payment_method_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Distribution of Payment Methods')
    plt.ylabel('')
    plt.savefig('outputs/figures/payment_methods.png')
    plt.close()

    # Seasonal Trend Analysis
    df['month'] = df['orderDate'].dt.to_period('M')
    monthly_sales = df.groupby('month').agg({
        'price': lambda x: (x * df.loc[x.index, 'quantity_x']).sum()
    }).reset_index()
    monthly_sales['month'] = monthly_sales['month'].astype(str)

    # Visualize Seasonal Trends
    plt.figure(figsize=(15, 6))
    sns.lineplot(x='month', y='price', data=monthly_sales)
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join('outputs', 'figures', 'seasonal_trends.png'))
    plt.close()

    return payment_method_counts, monthly_sales

if __name__ == "__main__":
    from data_preprocessing import load_and_process_data
    data = load_and_process_data()
    payment_methods, sales_trends = perform_sales_analysis(data)
    print("Sales analysis complete.")
    print("Payment method distribution:")
    print(payment_methods)