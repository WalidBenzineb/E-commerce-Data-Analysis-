import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def perform_product_analysis(df):
    # Product Category Analysis
    category_sales = df.groupby('productCategory').agg({
        'price': lambda x: (x * df.loc[x.index, 'quantity_x']).sum()
    }).sort_values('price', ascending=False)

    # Visualize Top Product Categories
    plt.figure(figsize=(12, 6))
    category_sales.head(10)['price'].plot(kind='bar')
    plt.title('Top 10 Product Categories by Sales')
    plt.xlabel('Product Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('outputs/figures/top_product_categories.png')
    plt.close()

    # Market Basket Analysis
    basket = df.groupby(['orderId', 'productName'])['quantity_x'].sum().unstack().reset_index().fillna(0)
    basket = basket.set_index('orderId')
    basket_sets = basket.apply(lambda x: x.map(encode_units))

    frequent_itemsets = apriori(basket_sets, min_support=0.001, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

    # Visualize Association Rules
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="support", y="confidence", size="lift", data=rules)
    plt.title('Association Rules - Support vs Confidence')
    plt.xlabel('Support (frequency of itemset)')
    plt.ylabel('Confidence (strength of rule)')
    plt.savefig(os.path.join('outputs', 'figures', 'association_rules.png'))
    plt.close()

    return category_sales, rules

def encode_units(x):
    return x > 0

if __name__ == "__main__":
    from data_preprocessing import load_and_process_data
    data = load_and_process_data()
    category_sales, rules = perform_product_analysis(data)
    print("Product analysis complete.")
    print("Top 5 product categories:")
    print(category_sales.head())