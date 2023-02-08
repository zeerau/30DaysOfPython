
empty_tuple = ()


sisters = ("ummu", "basma")
brothers = ("uwaisu", "jaafar")

siblings = sisters + brothers

number_of_siblings = len(siblings)

family_members = siblings + ("Dad", "Mom")

print(family_members)

siblings, parents = family_members[:len(siblings)], family_members[len(siblings):]

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'celery', 'cucumber')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)

middle_items_tp = food_stuff_tp[len(food_stuff_tp)//2-1:len(food_stuff_tp)//2+1]
middle_items_lt = food_stuff_lt[len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1]

first_last_3_items = food_stuff_lt[:3] + food_stuff_lt[-3:]

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is in the nordic_countries tuple
is_estonia_nordic = 'Estonia' in nordic_countries

# Check if 'Iceland' is in the nordic_countries tuple
is_iceland_nordic = 'Iceland' in nordic_countries
