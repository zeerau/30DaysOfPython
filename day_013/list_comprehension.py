numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
result = [num for num in numbers if num <= 0]
print(result)


list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
result = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(result)

result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [[country[0][0].upper(), country[0][0][:3].upper(), country[0][1].upper()] for country in countries]
print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]
print(result)
