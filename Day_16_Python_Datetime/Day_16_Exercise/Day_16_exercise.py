# Day 16 Python Datetime Exercise Solutiıon

# 1
from datetime import datetime

time = datetime.now()
day = time.day
month = time.month
year = time.year
hour = time.hour
minute = time.minute
timestap = datetime.timestamp(time)

print(f"Current day: {day}/{month}/{year} {hour}/{minute}")
print("Timestap:", timestap)

# 2
now = datetime.now()
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted time:", time)

# 3
today = "5 December 2019"

str_to_time = datetime.strptime(today, "%d %B %Y")
print(str_to_time)

# 4
from datetime import date

current_year = datetime.now()
new_year = datetime(2025, 1, 1)

result = new_year - current_year
print("Time left for new year:", result)


# 5
unix_year = date(year=1970, month=1, day=1)
current_year = date(year=2024, month=2, day=9)
result = current_year - unix_year
print("Unix year:", result)


# 6

# Time series analysis: The datetime module is essential for handling time-related data in time series analysis tasks such as data manipulation, indexing, and plotting.

# Timestamping activities in an application: You can use the datetime module to timestamp events or activities within an application, providing a record of when specific actions occurred.

# Handling time-sensitive operations: Many applications require time-sensitive operations such as scheduling tasks, setting timeouts, or implementing time-based logic. The datetime module facilitates handling these operations.

# Date and time arithmetic: The datetime module provides functionalities for performing arithmetic operations on dates and times, such as addition, subtraction, and comparison, which are useful in various applications.

# Logging: When logging events in an application, including timestamps can be valuable for tracking and debugging purposes. The datetime module enables the inclusion of timestamps in log entries.

# Data filtering and aggregation: In data processing tasks, you often need to filter or aggregate data based on specific time intervals. The datetime module assists in parsing, filtering, and grouping data by time.

# Generating reports: When generating reports or summaries that involve time-related data, the datetime module helps format dates and times according to the desired output format.

# Implementing countdowns or timers: Applications that involve countdowns, timers, or reminders rely on the datetime module to calculate durations, schedule events, and trigger notifications.

# Handling time zones: The datetime module provides support for working with time zones, allowing applications to convert between different time zones and handle daylight saving time adjustments.

# Integration with databases: When working with databases, storing and querying timestamp data is a common requirement. The datetime module is used to manage timestamps and interact with databases efficiently.