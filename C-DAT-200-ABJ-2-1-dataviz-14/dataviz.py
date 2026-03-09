import pandas as pd
df = pd.read_csv('products.csv')
df1 = pd.read_csv('departments.csv')
df2 = pd.read_csv('order_products.csv')
df3 = pd.read_csv('orders.csv')
df4 = pd.read_csv('aisles.csv')
df2.isnull().sum()


print(df2)