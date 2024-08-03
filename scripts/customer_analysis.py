import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def perform_customer_analysis(df):
    # Cohort Analysis
    df['order_month'] = df['orderDate'].dt.to_period('M')
    df['cohort'] = df.groupby('accountId')['orderDate'].transform('min').dt.to_period('M')
    df['cohort_index'] = (df['order_month'] - df['cohort']).apply(lambda x: x.n)

    cohort_data = df.groupby(['cohort', 'cohort_index'])['accountId'].nunique().reset_index()
    cohort_table = cohort_data.pivot(index='cohort', columns='cohort_index', values='accountId')
    cohort_pct = cohort_table.div(cohort_table.iloc[:, 0], axis=0)

    # Visualize Cohort Analysis
    plt.figure(figsize=(15, 8))
    sns.heatmap(cohort_pct, annot=True, cmap='YlGnBu', fmt='.2%')
    plt.title('Customer Cohort Analysis: Retention Rates')
    plt.xlabel('Months Since First Purchase')
    plt.ylabel('Cohort (First Purchase Month)')
    plt.tight_layout()
    plt.savefig('outputs/figures/cohort_analysis.png')
    plt.close()

    # Customer Demographics Analysis
    current_year = datetime.now().year
    df['age'] = current_year - df['birthDate'].dt.year
    df['age_group'] = pd.cut(df['age'], bins=[0, 18, 25, 35, 45, 55, 65, 100], 
                             labels=['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'])

    # Visualize Age Distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(x='age_group', data=df)
    plt.title('Age Distribution of Customers')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.savefig(os.path.join('outputs', 'figures', 'age_distribution.png'))
    plt.close()

    return cohort_pct, df['age_group'].value_counts()

if __name__ == "__main__":
    from data_preprocessing import load_and_process_data
    data = load_and_process_data()
    cohort_analysis, age_distribution = perform_customer_analysis(data)
    print("Customer analysis complete.")
    print("Age distribution:")
    print(age_distribution)