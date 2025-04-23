# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %%
df = pd.read_csv("Sales Dataset.csv",encoding='UTF-8')
df.info()

# %%
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.info()

# %%
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day
df['Weekday'] = df['Order Date'].dt.weekday 

df['Year-Month'] = df['Order Date'].dt.to_period('M')
print('\nCategorias únicas:')
print(df['Category'].unique())
print(df['Sub-Category'].unique())
print(df['PaymentMode'].unique())

# %% [markdown]
# Explore analysis

# %%
# total sales per year

sales_per_year = df.groupby('Year').agg({
    'Amount': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
}).reset_index()
sales_per_year['Profit Margin'] = sales_per_year['Profit']/sales_per_year['Amount']
print('\nSales per Year:')
sales_per_year.round(2)

# %%
df.info()

# %%
# Analysis per Category

category_analysis = df.groupby(['Category','Sub-Category']).agg({
    'Amount': ['sum','count'],
    'Profit': 'sum',
    'Quantity': 'sum'
}).sort_values(('Amount','sum'), ascending=True)
category_analysis['Profit Margin'] = category_analysis[('Profit','sum')]/category_analysis[('Amount','sum')]
category_analysis.round(2)

# %% [markdown]
# Visualized the data

# %%
sns.set_style('whitegrid')

plt.figure(figsize=(10,4))
sns.barplot(x='Year',y='Amount',data=sales_per_year,palette='bright',hue='Year',legend=False)
plt.title('Annual Sales')
plt.ylabel('Total Sales')
plt.xlabel('Year')
plt.show()

# %%
top_subcategories = category_analysis.head(10).reset_index()
plt.figure(figsize=(12,4))
sns.barplot(x=('Amount','sum'),y='Sub-Category',hue='Category',data=top_subcategories,palette='viridis')
plt.title('Top 10 sub-category sales', fontsize=16)
plt.xlabel('Total Sales')
plt.ylabel('')
plt.show()

# %%
print(sales_per_year.head().reset_index(drop=True))
print(category_analysis.head().reset_index(drop=False))


