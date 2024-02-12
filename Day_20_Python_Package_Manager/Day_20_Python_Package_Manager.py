# Day 20 Python Package Manager
import numpy

print(numpy.version.version)

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))

np_arrs = np_arr * 2
print(np_arrs)

np_arrs_sum = np_arr + 2
print(np_arr)

import webbrowser

url_lists = [
    "http://www.python.org",
    "https://www.linkedin.com/in/asabeneh/",
    "https://github.com/Asabeneh",
    "https://twitter.com/Asabeneh",
]

for url in url_lists:
    webbrowser.open_new_tab(url)


import requests
from pprint import pprint

url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
response = requests.get(url)
print(response)
print(requests.codes)
print(response.headers)
print(response.text)

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
pprint(countries[:1])


# Creating a Package

from Mypackage import arithmetics

arithmetics.add_numbers(1, 2, 3, 4, 5)

arithmetics.subtract(5, 3)
arithmetics.multiple(5, 3)
arithmetics.division(5, 3)
arithmetics.remainder(5, 3)
arithmetics.power(5, 3)

