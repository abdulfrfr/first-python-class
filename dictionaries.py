#A dictionary is a collection which is unordered, changable  and indexed. No duplicate members allowed, it's just like JSon files in javascript

#Create dictionary

person = {
    'first_name': 'Abdul',
    'last_name' : 'frfr',
    'age' : '20'
}

#Get value

print(person['first_name'])

# Add member, key or value

person['phone'] = '07025557114'

# Get all memebers or keys

print(person.keys())

# Get all items
print(person.items())

# delete a key

del( person['phone'])
person.pop('age')

# Clear


print(person)

# copy a dictionary

person2 = person.copy()

person2['added'] = 'True'

# Get length

print(len(person2))

print(person2)


# Lists of dictionaries

people = [
    {'name': 'Abdul frfr', 'age' : '20'},
    {'name': 'Salam frfr', 'age' : '17'},
]

print(people)

print(people[1]['name'])

