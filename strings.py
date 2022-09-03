# strings are being surrounded by single or double quotes just like in javascript

name = 'Abdul'
age = 20

# concactinating 
# variables are being concactinated with the plus(+) sign just like in javascript


print('Hello my name is ' + name)
print('Hello my name is ' + name + ' and i am ' + str(age) + ' years old')

'''
print('Hello my name is ' + name + ' and i am ' + age + ' years old')

the codes above is going to throw an error because only strings can be concactinated unless we convert the int variable into 
a string like the code below

print('Hello my name is ' + name + ' and i am ' + str(age) + ' years old')
'''

#string formating


#areguments by position

'''
we can also contactinate strings and int together by using the format method 
like the code below
'''



print('My name is {name} and i am {age}'.format(name=name, age=age))

# or

print(f'My name is {name} and i am {age}')


#String Methods

n = 'abdul frfr'

#capitalize string

print(n.capitalize())

#uppercase

print(n.upper())

#lowercase

print(n.lower())

# swapcase

print(n.swapcase())

#get length

print(len(n))

#replace string

print(n.replace('abdul', 'everyone'))

#count a letter

sub = 'r'
print(n.count(sub))

#to check if it starts with a particular word

print(n.startswith('hello'))

#to check if it ends with a letter or a word

print(n.endswith('v'))

#split the strings which is going to turn it into n array

print(n.split())

#find position of a character or a string

print(n.find('r'))

#check if your variable is alphanumeric

print(n.isalnum())

#check if your variable is only alphabets

print(n.isalpha())

#check if your variable is all numbers

print(n.isnumeric())