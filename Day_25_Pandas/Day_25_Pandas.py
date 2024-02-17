# Day 25 Pandas

import pandas as pd
import numpy as np

# Creating Pandas Series with Default Index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)


# Creating Pandas Series with Custom Index
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

fruits = ["Orange", "Banana", "Mango"]
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)


# Creating Pandas Series from a Dictionary
dct = {"name": "Asabeneh", "country": "Finland", "city": "Helsinki"}
s = pd.Series(dct)
print(s)


# Creating a Constant Pandas Series
s = pd.Series(10, index=[1, 2, 3])
print(s)


# Creating a Pandas Series Using Linspace
s = pd.Series(np.linspace(5, 20, 10))
print(s)


# DataFrames

# Pandas data frames can be created in different ways

# Creating DataFrames from List of Lists
data = [
    ["Asabeneh", "Finland", "Helsinki"],
    ["David", "UK", "London"],
    ["John", "Sweden", "Stockholm"],
]
df = pd.DataFrame(data, columns=["Names", "Country", "City"])
print(df)


# Creatind DataFrame Using Dictionary
data = {
    "Name": ["Asabeneh", "David", "John"],
    "Country": ["Finland", "UK", "Sweden"],
    "City": ["Helsinki", "London", "Stockholm"],
}
df = pd.DataFrame(data)
print(df)


# Creating DataFrames from a List of Dictionaries

data = [
    {"Name": "Asabeneh", "Country": "Finland", "City": "Helsinki"},
    {"Name": "David", "Country": "UK", "City": "Helsinki"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"},
]
df = pd.DataFrame(data)
print(df)


# Reading CSV File Using Pandas
df = pd.read_csv("weight-height.csv")
print(df)

# Data Exploration

# Let us read only the first 5 rows using head()

print(df.head())
# give five rows we can increase the number of rows by passing argument to the head() method

# Let us also explore the last recordings of the dataframe using the tail() methods

print(df.tail())
# tails give the last five rows, we can increase the rows by passing argument to tail method

print(df.shape)


# Let us get all the columns using columns
print(df.columns)


# Let us get a specific column using the column key
heights = df["Height"]
print(heights)

weights = df["Weight"]
print(weights)


print(len(heights) == len(weights))


# The describe() method provides a descriptive statistical values of a dataset.
print(heights.describe())
print(weights.describe())
print(df.describe())

# Similar to describe(), the info() method also give information about the dataset.

# Modifying a DataFrame
data = [
    {"Name": "Asabeneh", "Country": "Finland", "City": "Helsinki"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "SWeden", "City": "Stockholm"},
]
df = pd.DataFrame(data)
print(df)


# Adding a New Column
weights = [74, 78, 69]
df["Weight"] = weights

heights = [173, 175, 169]
df["Height"] = heights
print(df)


# Modifying column values
df["Height"] = df["Height"] * 0.01


def calculate_bmi():
    weights = df["Weight"]
    heights = df["Height"]
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi


bmi = calculate_bmi()
df["BMI"] = bmi
print(df)


# Formating DataFrames Columns
df["BMI"] = round(df["BMI"], 1)
print(df)


birth_year = ["1769", "1985", "1990"]
current_year = pd.Series(2024, index=[0, 1, 2])
df["Birth Year"] = birth_year
df["Current Year"] = current_year
print(df)

# Checking data types of Columns value
print(df.Weight.dtype)
df["Birth Year"].dtype
df["Birth Year"] = df["Birth Year"].astype(int)
print(df["Birth Year"].dtype)

df["Current Year"] = df["Current Year"].astype("int")
df["Current Year"].dtype

ages = df["Current Year"] - df["Birth Year"]
print(ages)

df["Ages"] = ages
print(df)

mean = (35 + 30) / 2
print("Mean:", mean)


# Boolean Indexing
print(df[df["Ages"] > 120])
print(df[df["Ages"] < 120])
