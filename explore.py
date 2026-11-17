# Reflection
# 1.
# 2.
# 3.

print(f"-----Exercise 1-----")
import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print(f"-----Exercise 2-----")
south = df[df['region'] == 'South']

print(len(south))
print(south.head())

print(f"-----Exercise 3-----")
top5 = df.sort_values('revenue', ascending=False).head(5)
print(top5)

print(f"-----Exercise 4-----")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())

print(f"-----Exercise 5-----")
df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())

print(f"-----Exercise 6-----")
print(df['region'].unique())
print(df['region'].value_counts())

print(f"-----Exercise 7-----")
subset = df[['region', 'product', 'revenue']]

print(subset.shape)

print(f"-----Exercise 8-----")
import os

df.to_csv('data/explored.csv', index=False)
print("File exists:", os.path.exists('data/explored.csv'))
