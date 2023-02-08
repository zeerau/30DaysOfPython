# Empty dictionary dog
dog = {}

# Adding keys and values to dog
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 3

# Empty dictionary student
student = {}

# Adding keys and values to student
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 25
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Java', 'C++']
student['country'] = 'USA'
student['city'] = 'New York'
student['address'] = '123 Main Street'

# Length of the student dictionary
len(student)  # Output: 9

# Value of skills and its data type
skills = student['skills']
print(type(skills))  # Output: <class 'list'>

# Modifying skills values
student['skills'].append('R')
student['skills'].append('SQL')

# Get dictionary keys as list
keys = list(student.keys())
print(keys)

# Get dictionary values as list
values = list(student.values())
print(values)

# Convert dictionary to list of tuples using items() method
student_list = list(student.items())
print(student_list)

# Delete one item from the dictionary
del student['address']

# Delete the dictionary
del student
