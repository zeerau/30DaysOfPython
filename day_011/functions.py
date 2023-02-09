import math

def add_two_numbers(a, b):
    return a + b

def area_of_circle(radius):
    return math.pi * radius * radius

def add_all_nums(*args):
    result = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "All arguments should be number types"
        result += arg
    return result

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "The equation has no real solutions."
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
    return capitalized_lst

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(1, n+1))

def sum_of_odds(n):
    return sum([i for i in range(1, n+1) if i % 2 != 0])

def sum_of_even(n):
    return sum([i for i in range(1, n+1) if i % 2 == 0])

def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("The number of odds are {}.".format(odds))
    print("The number of evens are {}.".format(evens))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_empty(obj):
    if obj:
        return False
    else:
        return True

def calculate_mean(lst):
    return sum(lst)/len(lst)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    if n % 2 == 0:
        median1 = sorted_lst[n//2 - 1]
        median2 = sorted_lst[n//2]
        median = (median1 + median2)/2
    else:
        median = sorted_lst[n//2]
    return median

def calculate_mode(lst):
    from collections import Counter
    n = len(lst)
    data = Counter(lst)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        return "No mode found"
    else:
        return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    variance = sum([((x - mean) ** 2) for x in lst]) / len(lst)
    return variance

def calculate_std(lst):
    import math
    variance = calculate_variance(lst)
    std = math.sqrt(variance)
    return std



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_list_unique(lst):
    return len(lst) == len(set(lst))

def is_list_homogeneous(lst):
    if len(lst) == 0:
        return False
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
    return True

def is_valid_variable(var):
    try:
        eval(var)
        return True
    except:
        return False
