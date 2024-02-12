# Day 20 Python Package Manager Exercise Solution

# 1
import requests, re, statistics
from collections import Counter, defaultdict


def most_frequent_words():
    url = "https://web.archive.org/web/20221125063850/https://www.gutenberg.org/files/1112/1112.txt"
    response = requests.get(url)
    text = response.text
    words = re.findall(r"\b\w+\b", text.lower())
    word_counts = Counter(words)
    most_occur = word_counts.most_common(10)
    return most_occur


print(most_frequent_words())


# 2


def find_cats():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weights = []
        for cat in data:
            if "weight" in cat and "metric" in cat["weight"]:
                weight_str = cat["weight"]["metric"]
                weight = float(weight_str.split()[0])
                if weight_str.endswith("kg"):
                    weight *= 1000
                weights.append(weight)

        if weights:
            min_weight = min(weights)
            max_weight = max(weights)
            mean_weight = statistics.mean(weights)
            median_weight = statistics.median(weights)
            std_dev_weight = statistics.stdev(weights)

            return {
                "min_weight": min_weight,
                "max_weight": max_weight,
                "mean_weight": mean_weight,
                "median_weight": median_weight,
                "std_dev_weight": std_dev_weight,
            }
        else:
            return "No weight data found for cats."
    else:
        return "Failed to fetch data from the API."


print(find_cats())


# 2.1
def find_lifespan():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lifes = []
        for cat_life in data:
            if "life_span" in cat_life:
                lifespan_str = cat_life["life_span"]
                life = float(lifespan_str.split()[0])
                lifes.append(life)
        if lifes:
            min_lifes = min(lifes)
            max_lifes = max(lifes)
            mean_lifes = statistics.mean(lifes)
            median_lifes = statistics.median(lifes)
            std_lifes = statistics.stdev(lifes)
            return {
                "min_lifes": min_lifes,
                "max_lifes": max_lifes,
                "mean_lifes": mean_lifes,
                "median_lifes": median_lifes,
                "std_lifes": std_lifes,
            }


print(find_lifespan())

# 2.2


def frequnecy_table():
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        frequnecy_table = defaultdict(int)

        for cat_info in data:
            if "origin" in cat_info and "name" in cat_info:
                country = cat_info["origin"]
                breed = cat_info["name"]
                key = f"{country} - {breed}"
                frequnecy_table[key] += 1
        return frequnecy_table


frequnecy_table = frequnecy_table()

for key, value in frequnecy_table.items():
    print(f"{key}, {value}")
print()


# 3
def country():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sorted_countries = sorted(data, key=lambda x: x.get("area", 0), reverse=True)
        sorted_countries_language = sorted(data, key=lambda x: len(x.get("languages",[])), reverse=True)
        largest_countries = sorted_countries[:10]
        most_langugae = sorted_countries_language[:10]
        return largest_countries, most_langugae, data


largest_countries, most_countries_language, all_countries_data = country()

print("10 Largest Countries:")
for country in largest_countries:
    print(f"{country["name"]["common"]}: {country.get("area","N/A")} sq. km")

print("n\10 Most Spoken Languages: ")
for country in most_countries_language:
    print(f"{country['name']}: {', '.join(country.get('languages', []))}")

total_language = set()
for country in all_countries_data:
    total_language.update(country.get("languages",[]))

print("\nTotal number of languages in the countries API: ", len(total_language))


# 4
from bs4 import BeautifulSoup

url = "https://archive.ics.uci.edu/ml/datasets.php "
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("div")
for link in links:
    print(link.get_text())

