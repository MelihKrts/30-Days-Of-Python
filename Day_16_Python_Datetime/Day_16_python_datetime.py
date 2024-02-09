# Day 16 Python Datetime
import datetime

# print(dir(datetime))

# Getting Datetime Information

from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestap = now.timestamp()
print(day, month, year, hour, minute)
print("timestap", timestap)
print(f"{day}/{month}/{year}, {hour}:{minute}")


# Formatting Date Output Using strftime
new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second

print(day, month, year, hour, minute)
print(f"{day}/{month}/{year}, {hour}:{minute}")
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time_one:", time_one)

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time_two", time_two)

# String to Time Using strptime
date_string = "5 December, 2019"
print("date_string=", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object=", date_object)

# Using date from datetime
from datetime import date

d = date(2020, 1, 1)
print(d)
print("Current date:", d.today())
today = date.today()
print("Current Year:", today.year)
print("Current Month:", today.month)
print("Current Day:", today.day)

# Time Objects to Represent time
from datetime import time

a = time()
print("a = ", a)

b = time(10, 30, 50)
print("b = ", b)

c = time(hour=10, minute=30, second=50)
print("c = ", c)

d = time(10, 30, 50, 200555)
print("d = ", d)


# Difference Between Two points in Time Using

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print("Time Left for new year:", time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print("Time left for new year:", diff)

# Difference Between Two Points in Time Using timedelata
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 = ", t3)
