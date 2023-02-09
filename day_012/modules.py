import random
import string

def random_user_id():
    user_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return user_id

def user_id_gen_by_user():
    num_characters = int(input("Enter the number of characters in the ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    characters = string.ascii_lowercase + string.digits
    for i in range(num_ids):
        user_id = ''.join(random.choices(characters, k=num_characters))
        print(user_id)

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'
print(random_user_id()) # 1ee33d (for example)

print(user_id_gen_by_user())
# Enter the number of characters in the ID: 5
# Enter the number of IDs to generate: 5
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

print(user_id_gen_by_user())
# Enter the number of characters in the ID: 16
# Enter the number of IDs to generate: 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr

print(rgb_color_gen()) # rgb(125,244,255) (for example)


def list_of_hexa_colors(num_colors):
    hexa_chars = string.hexdigits[:16]
    hexa_colors = []
    for i in range(num_colors):
        color = ''.join(random.choices(hexa_chars, k=6))
        hexa_colors.append(color)
    return hexa_colors

def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for i in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append((r, g, b))
    return rgb_colors

def generate_colors(num_colors, color_type):
    if color_type == "hex":
        return list_of_hexa_colors(num_colors)
    elif color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type. Please choose either 'hex' or 'rgb'."

print(list_of_hexa_colors(5)) # ['2b7ace', '5c1638', '918f7d', 'a0f5c2', 'f7e43b'] (for example)

print(list_of_rgb_colors(5)) # [(125, 244, 255), (100, 90, 200), (255, 10, 40), (200, 200, 100), (0, 100, 255)] (for example)

print(generate_colors(5, "hex")) # ['2b7ace', '5c1638', '918f7d', 'a0f5c2', 'f7e43b'] (for example)

print(generate_colors(5, "rgb")) # [(125, 244, 255), (100, 90, 200), (255, 10, 40), (200, 200, 100), (0, 100, 255)] (for example)

print(generate_colors(5, "abc")) # Invalid color type. Please choose either 'hex' or 'rgb'.


def shuffle_list(input_list):
    shuffled_list = random.sample(input_list, len(input_list))
    return shuffled_list

def unique_random_numbers():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle_list(input_list)) # [10, 7, 4, 1, 5, 9, 6] (for example)

print(unique_random_numbers()) # [6, 4, 3, 1, 0, 9, 8] (for example)
