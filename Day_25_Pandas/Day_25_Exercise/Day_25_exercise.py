# Day 25 Exercise Solution

# Exercise Solution

# 1
import pandas as pd

df = pd.read_csv("hacker_news.csv")
print(df)

# 2
print(df.head())

# 3
print(df.tail())
num_rows = len(df)

# tail alternative
last_five_rows = df.iloc[num_rows - 5 : num_rows]
print(last_five_rows)

# It's good to be curious :D

specific_rows = df.iloc[[3, 5, 7, 15000, 9999]]
print(specific_rows)

# 4
title = df["title"]
print(title)

# 5
rows_and_columns_count = df.shape
print("Rows and Columns number:", rows_and_columns_count)

# 5.1
filtered_data = df.loc[
    df["title"].str.contains("python", case=False)
]  # case(case-sensitive)
print(filtered_data["title"])
print("----------------------")
print(filtered_data)

# 5.2
filtered_javascript = df.loc[df["title"].str.contains("JavaScript", case=False)]
print(filtered_javascript["title"])
print("----------------------")
print(filtered_javascript)

# 5.3
print(df.info())
print(df.describe)
print(df.isnull().sum())
print(df["title"].value_counts)
print(df.columns)
import matplotlib.pyplot as plt

df["num_points"].plot(kind="hist", bins=20)
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.title('Distribution of Scores')
plt.show()