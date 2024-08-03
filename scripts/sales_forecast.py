import pandas as pd
import os
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Assuming monthly_sales dataframe is available from previous analysis

# Convert month to datetime
monthly_sales['month'] = pd.to_datetime(monthly_sales['month'])
monthly_sales.set_index('month', inplace=True)

# Fit ARIMA model
model = ARIMA(monthly_sales['price'], order=(1,1,1))
results = model.fit()

# Forecast future sales
forecast = results.forecast(steps=6)  # Forecasting next 6 months

# Visualize the forecast
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales['price'], label='Historical Sales')
plt.plot(pd.date_range(start=monthly_sales.index[-1], periods=7, freq='M')[1], 
         forecast, color='red', label='Forecast')
plt.fill_between(pd.date_range(start=monthly_sales.index[-1], periods=7, freq='M')[1],
                 forecast - 1.96  forecast.std_error,
                 forecast + 1.96  forecast.std_error, color='pink', alpha=0.3)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Forecast')
plt.legend()
plt.savefig(os.path.join('outputs', 'figures', 'sales_forecast.png'))
plt.close()

print(Sales Forecast for the Next 6 Months)
print(forecast)