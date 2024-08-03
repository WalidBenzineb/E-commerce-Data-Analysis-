# E-commerce Data Analysis Project

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Technical Setup](#technical-setup)
- [Analysis and Insights](#analysis-and-insights)
  - [Customer Demographics and Segmentation](#customer-demographics-and-segmentation)
  - [RFM Analysis and Customer Retention](#rfm-analysis-and-customer-retention)
  - [Product Performance and Cross-Selling](#product-performance-and-cross-selling)
  - [Sales Trends and Payment Preferences](#sales-trends-and-payment-preferences)
- [Code Explanation](#code-explanation)
- [Implementation Plan](#implementation-plan)
- [Conclusion](#conclusion)

## Project Overview

This project analyzes an e-commerce dataset to uncover actionable insights for business growth and optimization. The analysis covers customer behavior, product performance, sales trends, and market basket analysis.

## Dataset Description

The dataset consists of several CSV files:
- `orders.csv`: Contains order information (orderId, accountId, orderDate, etc.)
- `order_details.csv`: Links orders to products and quantities
- `products.csv`: Product information (productId, name, category, price, etc.)
- `users.csv`: Customer demographic data
- `transactions.csv`: Payment transaction details

## Technical Setup

### Folder Structure
```bash
e-commerce-Data-Analysis/
│
├── data/
│   ├── orders.csv
│   ├── order_details.csv
│   ├── products.csv
│   ├── users.csv
│   └── transactions.csv
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── rfm_analysis.py
│   ├── cohort_analysis.py
│   ├── product_analysis.py
│   ├── sales_analysis.py
│   └── main.py
│
├── outputs/
│   ├── figures/
│   └── reports/
│
├── requirements.txt
└── README.md
```
Copy
### Script Descriptions

1. `data_preprocessing.py`:
   - Loads and merges data from CSV files
   - Cleans and preprocesses the data (e.g., handling missing values, date conversions)
   - Outputs a cleaned, merged dataset for further analysis

2. `rfm_analysis.py`:
   - Performs RFM (Recency, Frequency, Monetary) analysis
   - Segments customers based on RFM scores
   - Generates RFM distribution visualizations

3. `cohort_analysis.py`:
   - Conducts cohort analysis to track customer retention
   - Creates cohort heatmaps and retention curves

4. `product_analysis.py`:
   - Analyzes top-selling product categories
   - Performs market basket analysis using association rules
   - Generates product performance visualizations

5. `sales_analysis.py`:
   - Analyzes monthly sales trends
   - Examines payment method preferences
   - Creates sales trend and payment method distribution visualizations

6. `main.py`:
   - Orchestrates the entire analysis pipeline
   - Calls functions from other scripts in the appropriate order
   - Generates the final report

### How to Use

1. Clone the repository
2. Install required packages:
pip install -r requirements.txt
3. Place your CSV data files in the `data/` directory.
4. Run the main analysis script:
python scripts/main.py
5. View the results in the `outputs/` directory:
   - Visualizations will be in `outputs/figures/`
   - The final report will be in `outputs/reports/`

### Requirements

The project requires the following Python packages:
- pandas
- matplotlib
- seaborn
- scikit-learn
- mlxtend

# Analysis and Insights
## Customer Demographics and Segmentation
![customer_segments](https://github.com/user-attachments/assets/f81a5c05-78bf-4136-a0d9-7b93c829d1e8)
![age_distribution](https://github.com/user-attachments/assets/17f634a7-360c-437e-8f1f-cd5cb840e728)

### Graph Analysis:

**Age Distribution:**

* Right-skewed distribution with a significant peak in the 65+ age group.
* Notable dip in the 18-24 age group, followed by a rise in the 25-34 group.
* Relatively consistent customer numbers in the 35-64 age ranges.

**Customer Segments:**

* "Average Customers" form the largest segment, followed by "Lost Customers".
* "Best Customers" and "New Customers" are smaller but crucial segments.

**Key Insights and Actions:**

* Develop an "Easy Shop" interface for the 65+ demographic, emphasizing accessibility features.
* Create targeted campaigns for the 25-34 age group, focusing on mobile and social media integration.
* Implement a stratified loyalty program to move customers from "Average" to "Best" segments.

## RFM Analysis and Customer Retention
![rfm_distribution](https://github.com/user-attachments/assets/f41bd2f6-7e9d-4575-a2da-d5da19513a0c)
![cohort_analysis](https://github.com/user-attachments/assets/bac17602-fa9e-4073-9b93-259edd15bdf9)

### Graph Analysis:

- **RFM Distribution:**

    * Recency: Relatively even distribution with a slight peak around 200-250 days.
    * Frequency: Right-skewed distribution with most customers making 2-4 purchases.
    * Monetary: Highly right-skewed, indicating a small number of high-value customers.


- **Cohort Analysis:**

    - Rapid decline in customer retention across all cohorts after the first month.
    - Retention rates stabilize at a very low level (1-2%) for most cohorts after 2-3 months.


 **Key Insights and Actions:**

- Implement a "Second Purchase" campaign targeting customers 150 days after their first purchase.
- Develop a VIP program for high monetary value customers (top 10% of spenders).
- Create a re-engagement series for customers approaching the 180-day mark since last purchase.

## Product Performance and Cross-Selling
![top_product_categories](https://github.com/user-attachments/assets/b48f7dbe-4c4a-45eb-9478-372b57da2abc)
![association_rules](https://github.com/user-attachments/assets/283e7f32-949e-4cb5-9b5b-d078a75a22a2)

### Graph Analysis:

-**Top Product Categories:**

   - Relatively even distribution among the top 10 categories.
   - Tuna, Ball, and Chips are the top three categories, each with sales just over $1.2 million.
   - Gradual decrease in sales from the top to the 10th category, but all exceed $1 million in sales.

- **Association Rules:**

    - Most rules have low support (frequency) but varying levels of confidence.
    - A few rules show high confidence (near 1.0) with relatively higher support.
    - Larger points (higher lift) are scattered across different support and confidence levels.

- **Key Insights and Actions:**

    - Create cross-category bundles, especially combining top sellers from different categories (e.g., Tuna + Chips).
    - Implement a recommendation system based on high-confidence association rules.
    - Optimize inventory management focusing on the top 5 categories to ensure consistent availability.

## Sales Trends and Payment Preferences
![seasonal_trends](https://github.com/user-attachments/assets/db1de1bf-d041-44b6-82a3-20bc80ab8e61)
![payment_methods](https://github.com/user-attachments/assets/02030714-0a0e-412b-b5e1-578ec6c4b8f4)

### Graph Analysis:

- **Monthly Sales Trend:**

    - Significant fluctuations in monthly sales.
    - Notable peak in January 2024, reaching nearly $3 million in sales.
    - Concerning downward trend from February to May 2024.

- **Payment Methods Distribution:**

    - Relatively even distribution across payment methods.
    - PayPal leads slightly at 26.8%, followed closely by Cash on Delivery (25.3%) and Pay Later (25.0%).
    - Credit Card usage is the lowest at 22.8%, but not significantly behind other methods.

- **Key Insights and Actions:**

    - Plan a major promotional campaign for January 2025 to capitalize on the observed sales spike.
    - Investigate and address the causes of the sales decline from February to May 2024.
    - Introduce incentives for credit card usage to balance payment methods and potentially reduce operational costs.

## Code Explanation
### Data Preprocessing
```python
# Merge dataframes
full_orders = pd.merge(orders, order_details, on='orderId')
full_orders = pd.merge(full_orders, products, on='productId')
full_orders = pd.merge(full_orders, users, left_on='accountId', right_on='id')

# Convert date columns
date_columns = ['orderDate', 'payDate', 'shippingDate', 'birthDate', 'createDate', 'publishedDate']
for col in date_columns:
    full_orders[col] = pd.to_datetime(full_orders[col])
```
This code merges multiple dataframes to create a comprehensive view of each order, including product and user information. It also converts date strings to datetime objects for easier manipulation.
### RFM Analysis
```python
def rfm_analysis(df):
    latest_date = df['orderDate'].max()
    rfm = df.groupby('accountId').agg({
        'orderDate': lambda x: (latest_date - x.max()).days,
        'orderId': 'count',
        'price': lambda x: (x * df.loc[x.index, 'quantity_x']).sum()
    })
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm

rfm = rfm_analysis(full_orders)
```
This function calculates Recency (days since last order), Frequency (number of orders), and Monetary value (total spend) for each customer.
### Cohort Analysis
```python
ydef get_month(x):
    return datetime(x.year, x.month, 1)

full_orders['cohort'] = full_orders.groupby('accountId')['orderDate'].transform('min').apply(get_month)
full_orders['cohort_index'] = (full_orders['orderDate'].dt.to_period('M') - 
                               full_orders['cohort'].dt.to_period('M')).apply(lambda x: x.n)

cohort_data = full_orders.groupby(['cohort', 'cohort_index'])['accountId'].nunique().reset_index()
cohort_table = cohort_data.pivot(index='cohort', columns='cohort_index', values='accountId')
cohort_pct = cohort_table.div(cohort_table.iloc[:, 0], axis=0)
This code creates cohorts based on the first purchase month and calculates retention rates for each cohort over time.
Market Basket Analysis
pythonCopydef encode_units(x):
    if x <= 0:
        return False
    if x >= 1:
        return True

basket = full_orders.groupby(['orderId', 'productName'])['quantity_x'].sum().unstack().reset_index().fillna(0)
basket_sets = basket.applymap(encode_units)

frequent_itemsets = apriori(basket_sets, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
This code performs market basket analysis using the Apriori algorithm to find frequent itemsets and generate association rules.
```
## Implementation Plan
### Q3 2024:

- Launch the "Easy Shop" interface for 65+ demographic
- Develop and implement the stratified loyalty program
  
### Q4 2024:

- Create and launch the "Second Purchase" campaign
- Prepare for the January 2025 promotional campaign

### Q1 2025:

- Implement the cross-category bundling strategy
- Roll out the recommendation system based on association rules

### Q2 2025:

- Introduce new payment incentives to balance payment methods
- Launch the re-engagement series for at-risk customers

# Contact Information
Walid Benzineb - benzinebwal@gmail.com

# Conclusion
This comprehensive analysis provides a data-driven foundation for strategic decision-making in our e-commerce business. By leveraging these insights and implementing the suggested actions, we can expect improvements in customer retention, average order value, and overall sales performance. The technical approach demonstrated here ensures that our strategies are based on robust data analysis and can be continually refined as new data becomes available.
