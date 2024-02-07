# Day 12 Modules Exercise Solution

# Exercise Solution

# Level 1 Solution

# 1.1
import random, string


def random_user_id(n):
    character = string.ascii_lowercase + string.digits
    id = "".join(random.choice(character) for i in range(6))
    return id


print(random_user_id(6))


def random_usr(n):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(n))


# 1.2
def user_id_gen_by_user():
    character_input = int(input("Enter a character length number: "))
    ID_input = int(input("Enter number of IDs which are supposed: "))
    for _ in range(ID_input):
        print(random_usr(character_input))


user_id_gen_by_user()


# 1.3
def rgb_color_gen():
    min = 0
    max = 255

    red = random.randint(min, max)
    green = random.randint(min, max)
    blue = random.randint(min, max)
    rgb = "rgb({}, {}, {}).".format(red, green, blue)
    return rgb


print(rgb_color_gen())


# ------------------------------------------------------------------------------------------------------------------

# Exercise Level 2 Solution

# Level 2 Solution

# 2.1


def list_of_hexa_colors(num_clr):
    colors = []
    character = string.hexdigits
    for _ in range(num_clr):
        joined = "#" + "".join(random.choice(character) for _ in range(6))
        colors.append(joined)
    return colors


print(list_of_hexa_colors(2))


# 2.2
def list_of_rgb(num_clr):
    min = 0
    max = 255
    rgb_colors = []
    for _ in range(num_clr):
        red = random.randint(min, max)
        green = random.randint(min, max)
        blue = random.randint(min, max)
        rgb = "rgb({}, {}, {})".format(red, green, blue)
        rgb_colors.append(rgb)
    return rgb_colors


print(list_of_rgb(2))


# 2.3
def generate_colors(color_format, num_clr):
    min = 0
    max = 255
    colors = []
    hexa_rnd = string.hexdigits + string.ascii_lowercase
    if color_format == "hexa":
        for _ in range(num_clr):
            color = "#" + "".join(random.choice(hexa_rnd) for _ in range(6))
            colors.append(color)
    elif color_format == "rgb":
        for _ in range(num_clr):
            red = random.randint(min, max)
            green = random.randint(min, max)
            blue = random.randint(min, max)
            rgb = "rgb({}, {}, {})".format(red, green, blue)
            colors.append(rgb)
    return colors


print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))

print(generate_colors("rgb", 3))
print(generate_colors("rgb", 3))


# ------------------------------------------------------------------------------------------------------------------


# Exercise Level 3 Solution

# Level 3 Solution

# 3.1


def shuffle_list(lst):
    shuffle_ls = lst[:]
    random.shuffle(shuffle_ls)
    return shuffle_ls


my_list = [1, 2, 3, 4, 5]
print(shuffle_list(my_list))


# 3.2
def rnd_number_list_unique():
    return random.sample(range(10), 7)


print(rnd_number_list_unique())
