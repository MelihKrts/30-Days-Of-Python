# Day 22 Web Scraping Exercise Solution

# Exercise Solution

# 1

import requests
from bs4 import BeautifulSoup
import json

# url = "http://www.bu.edu/president/boston-university-facts-stats/"
# response = requests.get(url)
# if response.status_code == 200:
#     content = response.content
#     soup = BeautifulSoup(content, "html.parser")
#     sections = soup.find_all("div", class_="facts-wrapper")

#     data = []
#     for section in sections:
#         category = section.find("h5").text.strip()
#         facts = section.find_all("li")
#         category_data = {"category": category}
#         for fact in facts:
#             key = fact.find("p").text.strip()
#             value = fact.find("span").text.strip()
#             category_data[key] = value
#         data.append(category_data)

#     with open("scraped.json", "w") as f:
#         json.dump(data, f, indent=4)
#         print("Data saved to bu_stats.json")
# else:
#     print("Failed to fetch the webpage")


# 2

# url = "https://web.archive.org/web/20221208074039/https://archive.ics.uci.edu/ml/datasets.php"
# response = requests.get(url)
# if response.status_code == 200:
#     content = response.content
#     soup = BeautifulSoup(content, "html.parser")
#     tables = soup.find_all("table")

#     data = []
#     for table in tables:
#         anchor = table.find("a")
#         if anchor:
#             category = anchor.text
#             rows = table.find_all("tr")
#             category_data = {"category": category, "data": []}
#             for row in rows:
#                 cells = row.find_all("td")
#                 if len(cells) == 2:
#                     key = cells[0].text.strip()
#                     value = cells[1].text.strip()
#                     category_data["data"].append({key: value})
#             data.append(category_data)

#     with open("scraped_dataset.json", "w") as f:
#         json.dump(data, f, indent=4)
#         print("Data saved to scraped_dataset.json")
# else:
#     print("Failed to fetch the webpage")


# 3
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("table", class_="wikitable")
    if table:
        rows = table.find_all("tr")[1:]  # Skip the header row
        data = []
        for index, row in enumerate(rows, start=1):
            cells = row.find_all(["th", "td"])
            if len(cells) >= 7:
                number = cells[0].text.strip()
                presidency = cells[1].text.strip()
                presidency_dates = cells[2].text.strip()
                name = cells[3].text.strip()
                party = cells[4].text.strip()
                election = cells[5].text.strip()
                vice_president = cells[6].text.strip()
                data.append(
                    {
                        "No": str(index),
                        "Presidency[a]": presidency_dates,
                        "Presidency[a].1": "",
                        "Name(Birth–Death)": name,
                        "Party[b].1": party,
                        "Election": election,
                        "Vice President": vice_president,
                    }
                )

        with open("presidents.json", "w") as f:
            json.dump(data, f, indent=4)
            print("Data saved to presidents.json")
    else:
        print("Table not found on the webpage")
else:
    print("Failed to fetch the webpage")
