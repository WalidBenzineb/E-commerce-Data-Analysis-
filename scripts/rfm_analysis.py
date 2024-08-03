import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

def perform_rfm_analysis(df):
    latest_date = df['orderDate'].max()
    rfm = df.groupby('accountId').agg({
        'orderDate': lambda x: (latest_date - x.max()).days,
        'orderId': 'count',
        'price': lambda x: (x * df.loc[x.index, 'quantity_x']).sum()
    })
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    
    # Visualize RFM distribution
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))
    sns.histplot(rfm['Recency'], ax=ax1, kde=True)
    ax1.set_title('Recency Distribution')
    ax1.set_xlabel('Days since last purchase')
    sns.histplot(rfm['Frequency'], ax=ax2, kde=True)
    ax2.set_title('Frequency Distribution')
    ax2.set_xlabel('Number of purchases')
    sns.histplot(rfm['Monetary'], ax=ax3, kde=True)
    ax3.set_title('Monetary Distribution')
    ax3.set_xlabel('Total amount spent')
    plt.tight_layout()
    plt.savefig('outputs/figures/rfm_distribution.png')
    plt.close()

    # Customer Segmentation
    rfm['R_Quartile'] = pd.qcut(rfm['Recency'], q=4, labels=['1', '2', '3', '4'])
    rfm['F_Quartile'] = pd.qcut(rfm['Frequency'], q=4, labels=['4', '3', '2', '1'])
    rfm['M_Quartile'] = pd.qcut(rfm['Monetary'], q=4, labels=['4', '3', '2', '1'])
    rfm['RFM_Score'] = rfm['R_Quartile'].astype(str) + rfm['F_Quartile'].astype(str) + rfm['M_Quartile'].astype(str)
    rfm['Customer_Segment'] = rfm['RFM_Score'].map(segment_customers)

    # Visualize Customer Segments
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Customer_Segment', data=rfm)
    plt.title('Customer Segments Distribution')
    plt.savefig(os.path.join('outputs', 'figures', 'customer_segments.png'))
    plt.close()

    return rfm

def segment_customers(score):
    if score in ['111', '112', '121', '122', '123', '132', '211', '212', '114', '141']:
        return 'Best Customers'
    elif score in ['133', '134', '143', '244', '334', '343', '344', '144']:
        return 'Lost Customers'
    elif score in ['311', '411', '421', '412', '423']:
        return 'New Customers'
    else:
        return 'Average Customers'

if __name__ == "__main__":
    from data_preprocessing import load_and_process_data
    data = load_and_process_data()
    rfm_results = perform_rfm_analysis(data)
    print("RFM analysis complete. Shape of RFM results:", rfm_results.shape)