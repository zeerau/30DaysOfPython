
# #Day 4 exercises
# print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
# sentence = ["coding","for","all"]
# print(' '.join(sentence))

# company = "Coding For All"
# print(company)

# print(len(company))

# print(company.upper())
# print(company.lower())

# # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# #(slice) out the first word of Coding For All string.
# print(company[company.index(" "):])

# # 10
# print(company.find("coding"))

# # 11
# print(company.replace("Coding", "Python"))
# print("Coding For All".replace("Coding","Python"))
#  #12
# print("Python for Everyone".replace("Everyone", "All"))

# #13 

# print("Coding For All".split(" ,"))

#14
print("Facebook Google Microsoft Apple IBM Oracle Amazon".split(" "))

#15 
print("Coding For All"[0])

# 16
print("Coding For All"[-1])

# 17
print("Coding For All"[10])

# 18

print("Coding For All".index("C"))
print("Coding For All".index("F"))
print("Coding For All People".rfind("l"))
print("You cannot end a sentence with because because because is a conjunction".index("because"))
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[sentence.index("because"):sentence.rindex("because")+len("because")])
print("Coding For All".startswith("Coding"))
print("Coding For All".endswith("Coding"))

string = '   Coding For All      '
string = string.strip()

print(string)

# The variable thirty_days_of_python returns True when using isidentifier() method

lst = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
separator = ' # '
result = separator.join(lst)
print(result)

sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
result2 = sentence1 + "\n" + sentence2
print(result2)

line1 = "Name\tAge\tCountry\tCity"
line2 = "Asabeneh\t250\tFinland\tHelsinki"

print(line1)
print(line2)

radius = 10
area = 3.14 * radius ** 2
circle_area = "The area of a circle with radius {} is {:.0f} meters square.".format(radius, area)

print(circle_area)

add = 8 + 6
sub = 8 - 6
mul = 8 * 6
div = 8 / 6
mod = 8 % 6
floor_div = 8 // 6
power = 8 ** 6
formatted_string = "{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {:.2f}\n{} % {} = {}\n{} // {} = {}\n{} ** {} = {}".format(8, 6, add, 8, 6, sub, 8, 6, mul, 8, 6, div, 8, 6, mod, 8, 6, floor_div, 8, 6, power)

print(formatted_string)
