# Day 19 File Handling Exercise Solution

# Exercise Level 1 Solution

# Level 1 Solution

# 1.1


def find_count_ln_word(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            return num_lines, num_words
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None, None


file_paths = [
    "./data/obama_speech.txt",
    "./data/michelle_obama_speech.txt",
    "./data/donald_speech.txt",
    "./data/melania_trump_speech.txt",
]

for file_path in file_paths:
    num_lines, num_words = find_count_ln_word(file_path)
    if num_lines is not None and num_words is not None:
        print(f"File: {file_path}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print()


# 1.2

import json
from collections import Counter
from pprint import pprint


def most_spoken_languages(filename, n):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract languages spoken in each country
        languages = [lang for country in data for lang in country["languages"]]

        # Count occurrences of each language
        language_counter = Counter(languages)

        # Get the top N most spoken languages
        top_languages = language_counter.most_common(n)

        return top_languages
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None


# Example usage
print(most_spoken_languages(filename="./data/countries_data.json", n=10))
print(most_spoken_languages(filename="./data/countries_data.json", n=3))


# 1.3
import json


def most_populated_countries(filename, n):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Sort countries based on population
        sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)

        # Select the top N most populated countries
        top_countries = sorted_countries[:n]

        return top_countries
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None


# Example usage
def print_output(data):
    print("[")
    for country in data:
        print(
            "{'country': '%s', 'population': %d},"
            % (country.get("name", "N/A"), country.get("population", 0))
        )
    print("]")


print_output(most_populated_countries(filename="./data/countries_data.json", n=10))
print_output(most_populated_countries(filename="./data/countries_data.json", n=3))


# ---------------------------------------------------------------------------------------------------------------


# Exercise Level 2 Solution

# Level 2 Solution

# 2.1

import re


def extract_emails(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
            # Regular expression to match email patterns
            email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            # Find all email addresses in the text
            emails = re.findall(email_pattern, data)
            return emails
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None


# Example usage
email_addresses = extract_emails("./data/email_exchanges_big.txt")
if email_addresses:
    pprint(email_addresses)


# 2.2
def find_most_common_words(data, n):
    # If the input is a file path, read the content of the file
    if isinstance(data, str):
        try:
            with open(data, "r", encoding="utf-8") as file:
                text = file.read()
        except FileNotFoundError:
            print(f"File '{data}' not found.")
            return None
    else:
        text = data

    # Tokenize the text into words
    words = re.findall(r"\b\w+\b", text.lower())

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Sort the words by their frequencies in descending order
    most_common_words = word_counts.most_common(n)

    return most_common_words


print(find_most_common_words("./data/obama_speech.txt", 10))
print(find_most_common_words("./data/michelle_obama_speech.txt", 10))
print(find_most_common_words("./data/donald_speech.txt", 10))
print(find_most_common_words("./data/melania_trump_speech.txt", 10))

# 2.3

stop_words = [
    "i",
    "me",
    "my",
    "myself",
    "we",
    "our",
    "ours",
    "ourselves",
    "you",
    "you're",
    "you've",
    "you'll",
    "you'd",
    "your",
    "yours",
    "yourself",
    "yourselves",
    "he",
    "him",
    "his",
    "himself",
    "she",
    "she's",
    "her",
    "hers",
    "herself",
    "it",
    "it's",
    "its",
    "itself",
    "they",
    "them",
    "their",
    "theirs",
    "themselves",
    "what",
    "which",
    "who",
    "whom",
    "this",
    "that",
    "that'll",
    "these",
    "those",
    "am",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "being",
    "have",
    "has",
    "had",
    "having",
    "do",
    "does",
    "did",
    "doing",
    "a",
    "an",
    "the",
    "and",
    "but",
    "if",
    "or",
    "because",
    "as",
    "until",
    "while",
    "of",
    "at",
    "by",
    "for",
    "with",
    "about",
    "against",
    "between",
    "into",
    "through",
    "during",
    "before",
    "after",
    "above",
    "below",
    "to",
    "from",
    "up",
    "down",
    "in",
    "out",
    "on",
    "off",
    "over",
    "under",
    "again",
    "further",
    "then",
    "once",
    "here",
    "there",
    "when",
    "where",
    "why",
    "how",
    "all",
    "any",
    "both",
    "each",
    "few",
    "more",
    "most",
    "other",
    "some",
    "such",
    "no",
    "nor",
    "not",
    "only",
    "own",
    "same",
    "so",
    "than",
    "too",
    "very",
    "s",
    "t",
    "can",
    "will",
    "just",
    "don",
    "don't",
    "should",
    "should've",
    "now",
    "d",
    "ll",
    "m",
    "o",
    "re",
    "ve",
    "y",
    "ain",
    "aren",
    "aren't",
    "couldn",
    "couldn't",
    "didn",
    "didn't",
    "doesn",
    "doesn't",
    "hadn",
    "hadn't",
    "hasn",
    "hasn't",
    "haven",
    "haven't",
    "isn",
    "isn't",
    "ma",
    "mightn",
    "mightn't",
    "mustn",
    "mustn't",
    "needn",
    "needn't",
    "shan",
    "shan't",
    "shouldn",
    "shouldn't",
    "wasn",
    "wasn't",
    "weren",
    "weren't",
    "won",
    "won't",
    "wouldn",
    "wouldn't",
]


def clean_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text.lower())
    return cleaned_text


def remove_stop_words(text):
    # Tokenize the text
    words = text.split()
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words


def check_text_similarity(text1, text2):
    # Clean the texts
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)

    # Remove stop words
    filtered_text1 = remove_stop_words(cleaned_text1)
    filtered_text2 = remove_stop_words(cleaned_text2)

    # Calculate similarity using cosine similarity
    vector1 = Counter(filtered_text1)
    vector2 = Counter(filtered_text2)

    intersection = set(vector1.keys()) & set(vector2.keys())
    numerator = sum(vector1[x] * vector2[x] for x in intersection)

    sum1 = sum(vector1[x] ** 2 for x in vector1.keys())
    sum2 = sum(vector2[x] ** 2 for x in vector2.keys())
    denominator = (sum1 * sum2) ** 0.5

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


# Example usage
text1 = "Michelle's speech text goes here"
text2 = "Melania's speech text goes here"

similarity = check_text_similarity(text1, text2)
print("Similarity between the texts:", similarity)


# 2.4


def find_most_repeated_words(file_path, n=10):
    try:
        # Read the contents of the file
        with open(file_path, "r") as file:
            text = file.read()

        # Tokenize the text into words
        words = text.split()

        # Count the occurrences of each word
        word_counts = Counter(words)

        # Sort the words by their frequencies in descending order
        most_repeated_words = word_counts.most_common(n)

        return most_repeated_words
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


# Example usage
most_repeated_words = find_most_repeated_words("./data/romeo_and_juliet.txt", n=10)
if most_repeated_words:
    print("10 most repeated words in Romeo and Juliet:")
    for word, count in most_repeated_words:
        print(f"{word}: {count}")


# 2.5

import csv


def count_lines_with_python(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if "python" in row[1].lower():
                count += 1
    return count


def count_lines_with_javascript(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if "javascript" in row[1].lower():
                count += 1
    return count


def count_lines_with_java_not_javascript(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if "java" in row[1].lower() and "javascript" not in row[1].lower():
                count += 1
    return count


# Example usage
file_path = "./data/hacker_news.csv"
python_count = count_lines_with_python(file_path)
javascript_count = count_lines_with_javascript(file_path)
java_not_javascript_count = count_lines_with_java_not_javascript(file_path)

print("Number of lines containing 'python' or 'Python':", python_count)
print(
    "Number of lines containing 'JavaScript', 'javascript', or 'Javascript':",
    javascript_count,
)
print(
    "Number of lines containing 'Java' but not 'JavaScript':", java_not_javascript_count
)
