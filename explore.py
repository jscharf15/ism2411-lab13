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

print(f"-----Exercise 5-----")

print(f"-----Exercise 6-----")

print(f"-----Exercise 7-----")

print(f"-----Exercise 8-----")
