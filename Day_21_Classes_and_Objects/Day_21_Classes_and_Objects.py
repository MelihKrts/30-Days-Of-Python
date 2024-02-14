# Day 21 Classes and Objects
num = 10
print(type(num))


# Creating a Class
class Person:
    pass


print(Person)

# Creating a Object
p = Person()
print(p)

# Class Constructor


class Person:
    def __init__(self, name):
        self.name = name


p = Person("Asabeneh")
print(p.name)
print(p)


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person("Asabeneh", "Yetayeh", 250, "Finland", "Helsinki")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Object Methods


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.country} {self.city}"


p = Person("Asabeneh", "Yetayeh", 250, "Finland", "Helsinki")
print(p.person_info())

# Object Deafult Methods


class Person:
    def __init__(
        self,
        firstname="Asabeneh",
        lastname="Yetayeh",
        age=250,
        country="Finland",
        city="Helsinki",
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} is years old. He lives in {self.age}, {self.country}"


p1 = Person()
print(p1.person_info())

p2 = Person("John", "Doe", 30, "Nomanland", "Noman City")
print(p2.person_info())


# Method to modify class default values


class Person:
    def __init__(
        self,
        firstname="Asabeneh",
        lastname="Yetayeh",
        age=250,
        country="Finland",
        city="Helsinki",
    ):

        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}."

    def add_skill(self, skill):
        self.skills.append(skill)


p1 = Person()
print(p1.person_info())
p1.add_skill("HTML")
p1.add_skill("CSS")
p1.add_skill("JavaScript")

p2 = Person("John", "Doe", 30, "Nomanland", "Noman City")
print(p2.person_info())
print(p1.skills)
print(p2.skills)


# Inheritance


class Student(Person):
    pass


s1 = Student("Eyob", "Yetayeh", 30, "Finland", "Helsinki")
s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo")
print(s1.person_info())
s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)

# Overriding parent method


class Student(Person):
    def __init__(self, firstname="Asabeneh", lastname="Yetayeh", age=250, country="Finland", city="Helsinki",gender="male"):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f"{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in  {self.city}, {self.country}"


s1 = Student("Eyob", "Yetayeh", 30, "Finland", "Helsinki", "male")
s2 = Student("Lidiya", "Teklemariam", 28, "Finland", "Espoo", "female")
print(s1.person_info())

s1.add_skill("JavaScript")
s1.add_skill("React")
s1.add_skill("Python")
print(s1.skills)

print(s2.person_info())
s2.add_skill("Organizing")
s2.add_skill("Marketing")
s2.add_skill("Digital Marketing")
print(s2.skills)
