#A dictionary is a collection which is unordered, changable  and indexed. No duplicate members allowed, it's just like JSon files in javascript

#Create dictionary

person = {
    'first_name': 'Abdul',
    'last_name' : 'frfr',
    'age' : '20'
}

#Get value

print(person['first_name'])
print(person.get('last_name'))

# Add member, key or value

person['phone'] = '07025557114'

# Get all keys; this will give you all the value's variables only
# like so ['first_name', 'last_name', 'age']

print(person.keys())

# Get all values; this will give you a value and it's key each in a different bracket
# like so [('first_name', 'abdul'), ('last_name', 'frfr'), ('age', '17')]
print(person.items())

# delete a key and it value

del( person['phone'])
person.pop('age')




print(person)

# copy a dictionary; this works just like the way a spread operator works in javascript
person2 = person.copy()


# Adding a key and value
person2['added'] = 'True'

# Get length

print(len(person2))

# clear a dictionary; this will clear all data from a dictionary but keep it variable for modifications
person2.clear()


print(person2)


# Lists of dictionaries

people = [
    {'name': 'Abdul frfr', 'age' : '20'},
    {'name': 'Salam frfr', 'age' : '17'},
]

print(people)

print(people[1]['name'])

