# # The difference between map, filter, and reduce:

#     map: The map function takes in a function and a list, and returns a new list with the function applied to each element in the original list.
#     filter: The filter function takes in a function and a list, and returns a new list with only the elements for which the function returns True.
#     reduce: The reduce function takes in a function and a list, and returns a single value obtained by performing some operation on the elements of the list.

# The difference between higher order function, closure, and decorator:

#     Higher order function: A higher order function is a function that takes in a function as an argument or returns a function as a result.
#     Closure: A closure is a function that remembers the values in the enclosing scope even if they are not present in memory.
#     Decorator: A decorator is a special type of function that is used to modify or extend the behavior of another function, usually by wrapping the function in a new function.

# Definition of a call function before map, filter or reduce: A call function is a function that is used to call another function. It can be used before map, filter or reduce to provide the functions that will be applied to the elements of the list.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

uppercase_countries = list(map(lambda x: x.upper(), countries))
print(uppercase_countries)

square_numbers = list(map(lambda x: x**2, numbers))
print(square_numbers)

uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)

countries_with_land = list(filter(lambda x: 'land' in x, countries))
print(countries_with_land)

countries_with_six_characters = list(filter(lambda x: len(x) == 6, countries))
print(countries_with_six_characters)

