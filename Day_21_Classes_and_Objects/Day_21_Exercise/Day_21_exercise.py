# Day 21 Classes and Objects Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1


ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]

import statistics as stats

from collections import Counter


class Statistics:

    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return stats.mean(self.data)

    def median(self):
        return stats.median(self.data)

    def mode(self):
        return stats.mode(self.data)

    def variance(self):
        return stats.variance(self.data)

    def std_dev(self):
        return stats.stdev(self.data)

    def fre_dist(self):
        return Counter(self.data)

    def describe(self):
        return f"Count: {self.count()}\nSum: {self.sum()}\nMin: {self.min()}\nMax: {self.max()}\nRange: {self.range()}\nMean: {self.median()}\nMedian: {self.median()}\nMode: {self.mode()}\nVariance: {self.variance()}\nStandard Deviation: {self.std_dev()}\nFrequency Distribution: {self.fre_dist()}"


data = Statistics(ages)
print(data.describe())


# ---------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution


# Level 2 Solution

# 2.1


class PersonAcccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        self.income = []
        self.expense = set()

    def account_info(self):
        income_str = ", ".join([f"{desc} {amount}" for desc, amount in self.incomes])
        expense_str = ", ".join([f"{desc} {amount}" for desc, amount in self.expense])

        return f"Firstname: {self.firstname}\nLastname: {self.lastname}\nIncome: {{{income_str}}}\nExpense: {{{expense_str}}}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}\nAccount Balance: {self.account_balance()}"

    def add_income(self, description, income):
        self.incomes.add((description, income))

    def add_expense(self, description, expense):
        self.expense.add((description, expense))

    def total_income(self):
        return sum(amount for desc, amount in self.incomes)

    def total_expense(self):
        return sum(amount for desc, amount in self.expense)

    def account_balance(self):
        return self.total_income() - self.total_expense()


person = PersonAcccount("John", "Doe", {("Salary:", 5000)}, {})

person.add_income("Prim:", 1500)
person.add_income("Influencer:", 600.05)

person.add_expense("Credit debt:", 3500)
person.add_expense("Rent:", 1660)
person.add_expense("Taxes:", 1400)
person.add_expense("Food:", 940)

print(person.account_info())
