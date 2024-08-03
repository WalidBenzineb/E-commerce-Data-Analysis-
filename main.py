import os
from scripts.data_preprocessing import load_and_process_data
from scripts.rfm_analysis import perform_rfm_analysis
from scripts.product_analysis import perform_product_analysis
from scripts.customer_analysis import perform_customer_analysis
from scripts.sales_analysis import perform_sales_analysis

def create_directories():
    """Create necessary directories for outputs if they don't exist."""
    directories = ['outputs', 'outputs/figures', 'outputs/reports']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    # Create necessary directories
    create_directories()
    
    # Load and preprocess data
    data = load_and_process_data()
    
    # Perform analyses
    rfm_results = perform_rfm_analysis(data)
    category_sales, association_rules = perform_product_analysis(data)
    cohort_analysis, age_distribution = perform_customer_analysis(data)
    payment_methods, sales_trends = perform_sales_analysis(data)
    
    # Generate report
    generate_report(rfm_results, category_sales, association_rules, cohort_analysis, 
                    age_distribution, payment_methods, sales_trends)

def generate_report(rfm, category_sales, rules, cohort, age_dist, payment, sales):
    report = f"""
    E-commerce Data Analysis Report

    1. RFM Analysis
       - Average Recency: {rfm['Recency'].mean():.2f} days
       - Average Frequency: {rfm['Frequency'].mean():.2f} orders
       - Average Monetary Value: ${rfm['Monetary'].mean():.2f}
    
    2. Customer Segmentation
    {rfm['Customer_Segment'].value_counts(normalize=True).to_string()}

    3. Top 5 Product Categories
    {category_sales.head().to_string()}

    4. Market Basket Analysis
       - Top 5 association rules:
    {rules.sort_values('lift', ascending=False).head().to_string()}

    5. Payment Method Distribution
    {payment.to_string()}

    6. Age Distribution
    {age_dist.to_string()}

    Visualizations have been saved as PNG files in the outputs/figures directory.
    """

    with open('outputs/reports/ecommerce_analysis_report.txt', 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()
    print("Analysis complete. Report and visualizations have been saved.")