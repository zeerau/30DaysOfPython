# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Intel', 'Cisco', 'HP'])
it_companies.remove('Facebook')

# remove method will raise a KeyError if the specified element is not found in the set, whereas discard method will not raise any error and simply do nothing if the element is not found.

print(A.union(B))
c = A.intersection(B)
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B


age_set = set(age)
#The length of the set age_set is less than or equal to the length of the list age. This is because sets do not allow duplicate elements, so after converting the list to a set, some of the elements may have been removed.


#String: An ordered collection of characters, used to represent text.

# List: An ordered collection of elements that can be of different data types, including other lists.

# Tuple: An ordered, immutable collection of elements that can be of different data types.

# Set: An unordered collection of unique elements, without duplicates and that can be of different data types.

sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print(unique_words)