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