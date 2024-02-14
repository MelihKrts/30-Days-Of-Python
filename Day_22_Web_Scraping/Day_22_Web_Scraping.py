# Day 22 Web Scraping

import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20221208074039/https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)
status = response.status_code
print(status)

content = response.content  # we get all the content from the website
soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.get_text())
print(soup.body)  # gives the whole page on the website
print(response.status_code)


tables = soup.find_all(
    "table", {"cellpadding": 3}
)  # We are targeting the table with cellpadding attribute with the value of 3

# we can select using id, class or HTML tag, for more information check the beautifulsoup doc
table = tables[0]
for td in table.find("tr").find_all("td"):
    print(td.text)
