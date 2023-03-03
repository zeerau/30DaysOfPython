import requests
import string
from collections import Counter
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text

# Remove punctuation and convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.lower()

# Split text into individual words
words = text.split()

# Count the frequency of each word
word_counts = Counter(words)

# Sort the words by frequency and select the top 10
top_words = word_counts.most_common(10)

print(top_words)




cats_api = 'https://api.thecatapi.com/v1/breeds'

# Retrieve data from API
response = requests.get(cats_api)
data = response.json()

# Extract weight and lifespan data from each cat breed
weights = []
lifespans = []
countries = []
breeds = []
for cat in data:
    weight = cat['weight']['metric']
    weight = float(weight.split()[0])
    weights.append(weight)
    lifespan = cat['life_span']
    if lifespan != '':
        lifespan = float(lifespan.split()[0])
        lifespans.append(lifespan)
    else:
        lifespans.append(np.nan)
    country = cat['origin']
    countries.append(country)
    breed = cat['name']
    breeds.append(breed)

# Compute statistics for weight and lifespan
weight_mean = np.mean(weights)
weight_std = np.std(weights)
weight_min = np.min(weights)
weight_max = np.max(weights)
weight_median = np.median(weights)

lifespan_mean = np.nanmean(lifespans)
lifespan_std = np.nanstd(lifespans)
lifespan_min = np.nanmin(lifespans)
lifespan_max = np.nanmax(lifespans)
lifespan_median = np.nanmedian(lifespans)

# Create frequency table for country and breed
df = pd.DataFrame({'Country': countries, 'Breed': breeds})
freq_table = df.groupby(['Country', 'Breed']).size().reset_index(name='Frequency')

# Print results
print('Weight Statistics (in kg):')
print(f'Mean: {weight_mean:.2f}')
print(f'Standard Deviation: {weight_std:.2f}')
print(f'Minimum: {weight_min:.2f}')
print(f'Maximum: {weight_max:.2f}')
print(f'Median: {weight_median:.2f}\n')

print('Lifespan Statistics (in years):')
print(f'Mean: {lifespan_mean:.2f}')
print(f'Standard Deviation: {lifespan_std:.2f}')
print(f'Minimum: {lifespan_min:.2f}')
print(f'Maximum: {lifespan_max:.2f}')
print(f'Median: {lifespan_median:.2f}\n')

print('Frequency Table:')
print(freq_table)




countries_api = 'https://restcountries.eu/rest/v2/all'

# Retrieve data from API
response = requests.get(countries_api)
data = response.json()

# Create pandas DataFrame from data
df = pd.DataFrame(data)

# Find the 10 largest countries
largest_countries = df.nlargest(10, 'area')[['name', 'area']]
print('The 10 largest countries:')
print(largest_countries)

# Find the 10 most spoken languages
languages = df.explode('languages')
top_languages = languages.groupby('languages').size().reset_index(name='count')
top_languages = top_languages.nlargest(10, 'count')
print('\nThe 10 most spoken languages:')
print(top_languages[['languages', 'count']])

# Find the total number of languages
num_languages = languages['languages'].nunique()
print(f'\nThe total number of languages in the countries API is {num_languages}.')






# Define UCI website URL
UCI_URL = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send HTTP GET request to the website and retrieve content
response = requests.get(UCI_URL)
content = response.content

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all links to datasets and print their text (i.e., the names of the datasets)
links = soup.select('table[border="1"] td[valign="top"] a[href^="datasets/"]')
for link in links:
    print(link.text.strip())
