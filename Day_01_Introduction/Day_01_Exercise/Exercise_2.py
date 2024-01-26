# Exercise Level 3 Solution

# 3.1

# Number
import math

int = 100
print(int)

float = 2.95
print(float)

complex = 1j
print(complex)

# String
string = "It is a example string text"
print(string)

# Boolean
my_boolean = True
print(f"It is light on {my_boolean}")

# List
list = [0, 1, 2, 3, 3.96, "Turkey", "Apple", False]
print(list)

# Tuple
print(("Mercury", "Venus", "Earth", "Mars"))  # planets

# Set
print((27, 81, 9, 3))

# Dictionary
print(
    {
        "firstName": "Melih",
        "lastName": "Karatas",
        "age": 23,
        "skiils": ["JS", "React", "Python"],
    }
)

# Euclidian distance


def euclidian(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


dot1 = (2, 3)
dot2 = (10, 8)

distance = euclidian(dot1[0], dot1[1], dot2[0], dot2[1])
print(f"Euclidean distance between two points: {distance}")
