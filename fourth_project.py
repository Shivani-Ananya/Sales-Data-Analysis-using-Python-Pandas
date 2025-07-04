import pandas as pd
from tabulate import tabulate

df = pd.read_csv(r'D:\sairam\programming language\python\learning it\fourth project\sales_data.txt')

pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("\nMissing values check:")
print(tabulate(pd.DataFrame(df.isnull().sum(), columns=['Missing Count']), headers='keys', tablefmt='plain'))

df.set_index('Date', inplace=True)

print("\n 1. Group by Category and sum of Sales")
grouped = df.groupby('Category')['Sales'].sum()
print(tabulate(grouped.reset_index(), headers='keys', tablefmt='plain'))

print("\n 2. Pivot table for Quantity by Product and Category")
pivot = pd.pivot_table(df, values='Quantity', index='Product', columns='Category', aggfunc=['sum', 'mean'])
pivot.columns = ['_'.join(map(str, col)).strip() for col in pivot.columns.values]
print(tabulate(pivot.reset_index(), headers='keys', tablefmt='plain'))

print("\n 3. Group by Quantity and aggregate sum and mean of Price")
agg_price = df.groupby('Quantity')['Price'].agg(['sum', 'mean']).reset_index()
print(tabulate(agg_price, headers='keys', tablefmt='plain'))

print("\n 4. Max Sales per Product")
grouped = df.groupby('Product')['Sales'].max()
print(tabulate(grouped.reset_index(), headers='keys', tablefmt='plain'))

print("\n 5. Pivot table for Sales by Product and Category")
pivot_sales = pd.pivot_table(df, values='Sales', index='Product', columns='Category', aggfunc='sum')
pivot_sales.columns = [str(col) for col in pivot_sales.columns]  
print(tabulate(pivot_sales.reset_index(), headers='keys', tablefmt='plain'))

print("\n 6. Group by Product: sum and mean of Price")
price_stats = df.groupby('Product')['Price'].agg(['sum', 'mean']).reset_index()
print(tabulate(price_stats, headers='keys', tablefmt='plain'))

df['moving_avg'] = df['Sales'].rolling(window=3).mean()
print("\n 7. 3-day moving average of Sales")
print(tabulate(df.reset_index(), headers='keys', tablefmt='plain'))

df.reset_index().to_csv(r'D:\sairam\programming language\python\learning it\fourth project\sales_data_final.csv', index=False)
print("\n 8. Final DataFrame exported as 'sales_data_final.csv'")
