# Day 19 File Handling
# f = open("./reading_file_example.txt")
# print(f)

# read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method

# f = open("./reading_file_example.txt")
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.

# f = open("./reading_file_example.txt")
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# readline(): read only the first line

# f = open("./reading_file_example.txt")
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open("./reading_file_example.txt")
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# readlines alternavite
f = open("./reading_file_example.txt")
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# using with closes the files by itself
with open("./reading_file_example.txt") as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


# Opening Files for Writing and Updating

# "a" append: will append to end of the file
# "w" write: will overwrite any existing content, if the file does not exist it creates.

# with open("./reading_file_example.txt", "a") as f:
#     f.write("This text has to be appended at the end")

# The method below creates a new file, if the file does not exist
# with open("./writing_file_example.txt", "w") as f:
#     f.write("This text will be written in a newly created file")


# Deleting Files
import os

if os.path.exists("./example.txt"):
    os.remove("./example.txt")
else:
    print("The file does not exist")


# File Types

# Changing JSON a dictionary
import json

person_json = """{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}"""

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct["name"])


# Changing Dictionary to JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"],
}
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)


person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"],
}
with open("./json_example.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# CSV file

# CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

import csv

with open("./csv_example.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are: {", ".join(row)}")
        else:
            print(f"\t{row[0]}is a teachers. He Lives in {row[1]}, {row[2]}")
            line_count = +1
    print(f"Number of lines:  {line_count}")


# File xlsx
# import xlrd # pip install xlrd

# excel_book = xlrd.open_workbook("sample.xls")
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

# File XML
import xml.etree.ElementTree as ET

tree = ET.parse("./xml_example.xml")
root = tree.getroot()
print("Root tag:", root.tag)
print("Attribute:", root.attrib)
for child in root:
    print("field", child.tag)
