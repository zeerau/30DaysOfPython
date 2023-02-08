age = int(input("Enter your age: "))
if age >= 18:
   print("You are old enough to drive.")
else:
   years_to_wait = 18 - age
   print(f"You need to wait for {years_to_wait} year(s) to be able to drive.")

my_age = 28
your_age = int(input("Enter your age: "))

if my_age == your_age:
   print("We are the same age.")
elif my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
      print("I am 1 year older than you.")
    else:
      print(f"I am {difference} years older than you.")
else:
    difference = your_age - my_age
if difference == 1:
   print("You are 1 year older than me.")
else:
   print(f"You are {difference} years older than me.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
   print("a is greater than b.")
elif a < b:
   print("a is smaller than b.")
else:
   print("a is equal to b.")

score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
  grade = 'A'
elif score >= 70 and score <= 89:
  grade = 'B'
elif score >= 60 and score <= 69:
  grade = 'C'
elif score >= 50 and score <= 59:
  grade = 'D'
elif score >= 0 and score <= 49:
  grade = 'F'
else:
  grade = "Invalid score. Scores must be between 0 and 100."

print("Your grade is:", grade)


month = input("Enter the name of the month: ")

if month == "September" or month == "October" or month == "November":
  season = "Autumn"
elif month == "December" or month == "January" or month == "February":
  season = "Winter"
elif month == "March" or month == "April" or month == "May":
  season = "Spring"
elif month == "June" or month == "July" or month == "August":
  season = "Summer"
else:
  season = "Invalid month. Please enter a valid month name."

print("The season is:", season)

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit name: ")

if new_fruit in fruits:
  print("That fruit already exists in the list.")
else:
  fruits.append(new_fruit)
print("The modified fruit list is:", fruits)


person = {
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
'street': 'Space street',
'zipcode': '02210'
}
}

if 'skills' in person:
  middle_index = len(person['skills']) // 2
middle_skill = person['skills'][middle_index]
print("The middle skill is:", middle_skill)

if 'skills' in person:
  has_python_skill = 'Python' in person['skills']
print("Has Python skill:", has_python_skill)

if 'skills' in person:
  skills = person['skills']
if skills == ['JavaScript', 'React']:
  title = "He is a front end developer."
elif skills == ['Node', 'Python', 'MongoDB']:
  title = "He is a back end developer."
elif skills == ['React', 'Node', 'MongoDB']:
  title = "He is a full stack developer."
else:
  title = "Unknown title."
print(title)

if person['is_married'] and person['country'] == 'Finland':
  print(person['first_name'], person['last_name'], "lives in", person['country'] + ". He is married.")