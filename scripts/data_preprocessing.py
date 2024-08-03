import pandas as pd
from datetime import datetime

def load_and_process_data():
    # Load the data
    order_details = pd.read_csv('data/orderdetails.csv', sep=';')
    orders = pd.read_csv('data/orders.csv', sep=';')
    products = pd.read_csv('data/products.csv', sep=';')
    transactions = pd.read_csv('data/transaction.csv', sep=';')
    users = pd.read_csv('data/User.csv', sep=';')

    # Merge relevant dataframes
    orders_with_details = pd.merge(orders, order_details, on='orderId')
    orders_with_products = pd.merge(orders_with_details, products, on='productId')
    full_orders = pd.merge(orders_with_products, users, left_on='accountId', right_on='id')

    # Convert date columns to datetime
    date_columns = ['orderDate', 'payDate', 'shippingDate', 'birthDate', 'createDate', 'publishedDate']
    for col in date_columns:
        full_orders[col] = pd.to_datetime(full_orders[col])

    return full_orders

if __name__ == "__main__":
    processed_data = load_and_process_data()
    print("Data preprocessing complete. Shape of processed data:", processed_data.shape)