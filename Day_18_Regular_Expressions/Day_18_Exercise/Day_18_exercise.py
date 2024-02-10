# Day 18 Regular Expressions Exercise Solution

# Exercise Level 1 Solution

# Level 1

import re
from collections import Counter
from pprint import pprint

# 1.1
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

words = re.findall(r"\b\w+\b", paragraph.lower())
word_count = Counter(words)

word_count_list = [(count, word) for word, count in word_count.items()]
word_count_list.sort(reverse=True)
pprint(word_count_list)

# 1.2
paragraph = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."""

regex_pattern = r"[-+]?\d+"

matches = re.findall(regex_pattern, paragraph)
matches_convert = [int(match) for match in matches]
matches_convert.sort()

distance = abs(matches_convert[-1] - matches_convert[0])

print("Points:", matches)
print("Sorted_Points:", matches_convert)
print("Distance:", distance)


# ------------------------------------------------------------------------------------------------------------------

# Level 2 Solution

# 2.1


def is_variable(variable_name):
    regex_pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(regex_pattern, variable_name))


print(is_variable("first_name"))
print(is_variable("first-name"))
print(is_variable("1first_name"))
print(is_variable("firstname"))


# ------------------------------------------------------------------------------------------------------------------


# Level 3 Solution

# 3.1

sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""


def clean_text(variable):
    regex_pattern = r"[^\w\s]"
    matches = re.sub(regex_pattern, "", variable)
    return matches


print(clean_text(sentence))


def most_frequent_words(text):
    splitted = text.split()
    word_counts = Counter(splitted)
    most_occur = word_counts.most_common(3)
    return most_occur


cleaned_sentence = clean_text(sentence)
print(most_frequent_words(cleaned_sentence))
