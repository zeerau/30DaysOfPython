import requests
from bs4 import BeautifulSoup
import json
# url = 'https://archive.ics.uci.edu/ml/datasets.php'

# # Lets use the requests get method to fetch the data from url

# response = requests.get(url)
# # lets check the status
# status = response.status_code
# print(status)

# content = response.content # we get all the content from the website
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse


# tables = soup.find_all('table', {'cellpadding':'3'})
# # We are targeting the table with cellpadding attribute with the value of 3
# # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
#     print(td.text)

url2 = 'http://www.bu.edu/president/boston-university-facts-stats/'

response2 = requests.get(url2)
content = response2.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser')

tables = soup.findAll('div', {"class": "facts-wrapper"})

list_of_tables = []

for i in tables:
    keys = []
    values = []
    temp_dict = {}
    i = str(i)
    category = i[i.find('<h5>') + 4: i.find('</h5>')]
    temp_dict['Category'] = category
    all_key_start_indexes = [x+7 for x in range(len(i)) if i.startswith('"text">', x)]
    all_key_end_indexes = [x for x in range(len(i)) if i.startswith('</p>', x)]

    for l in range(len(all_key_start_indexes)):
        keys.append(i[all_key_start_indexes[l]:all_key_end_indexes[l]])

    all_values_start_indexes = []
    for v in range(len(i)):
        if i.startswith('value">', v):
            all_values_start_indexes.append(v+7)
        if i.startswith('value-text">', v):
            all_values_start_indexes.append(v+12)
    all_values_end_indexes = [x for x in range(len(i)) if i.startswith('</span>', x)]

    for m in range(len(all_values_end_indexes)):
        values.append(i[all_values_start_indexes[m]:all_values_end_indexes[m]])

    for r in range(len(keys)):
        temp_dict[keys[r]] = values[r]
    list_of_tables.append(temp_dict)

with open('data.json', 'w') as f:
  json.dump(list_of_tables, f)



