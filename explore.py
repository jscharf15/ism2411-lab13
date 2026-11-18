# Reflection
# 1. A boolean filter evaluates a condition (True/False) for every row and discards the Falses.
# 2. Single brackets return a series, a single one-dimensional column of values. While double brackets return a dataframe, a table that has just one column in it.
# 3. The most compelling reason is that pandas lets you write the steps once and rerun them on new data instantly. 

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
df_subset = df[['region', 'product', 'revenue']]

print(df_subset.shape)

print(f"-----Exercise 8-----")
import os

df.to_csv('data/explored.csv', index=False)
print("File exists:", os.path.exists('data/explored.csv'))
