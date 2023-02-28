# day 18 exerises

import re

from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph) # find all words in the paragraph

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_frequent_word = max(word_count, key=word_count.get)
print("The most frequent word is:", most_frequent_word)




text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."""

txtpattern = r'-?\d+'  # matches any integer, with optional negative sign

numbers = [int(num) for num in re.findall(txtpattern, text)]
furthest_distance = max(numbers) - min(numbers)

print("The numbers extracted from the text are:", numbers)
print("The distance between the two furthest particles is:", furthest_distance)



def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))




def clean_text(text):
    # Remove special characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    # Remove extra whitespaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def most_frequent_words(text, n=3):
    # Split the text into words
    words = text.split()
    # Count the frequency of each word
    counter = Counter(words)
    # Return the top n most frequent words as a list of (count, word) tuples
    return counter.most_common(n)

    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))