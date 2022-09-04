#A tuple is a collection which is ordered and unchangable. It allows duplicate values
#A tuple with one value needs a tailing coma, without that its going to be trated as a single string


 #Create Tuple

fruits = ('Mangoe', 'Grape', 'Strawberry', 'Pineapple')

fruits2 = ('Mangoe', 'Grape', 'Strawberry', 'Pineapple')

# trying to change a vlue in tuple will through an error just like the code below
#fruits[1] = 'Banana'

print(fruits, type(fruits))

# to get a value at a specific position
print(fruits[1])

# delete tuple
del fruits2

# to get the length of a tuple
print(len(fruits))


# A set is a collection thats unordered and unchangable. It does not allow duplicate values
# Adding a duplicate will not throw an error but will not make any effect on your set
#Create set

fruitSet = {'Apple', 'Mangoe', 'Pear', 'Grape'}

# add to a set
fruitSet.add('Straw')

# check if a value is in a set

print('Apple' in fruitSet) # this will throw a True of False depending on wether that value is in the set

# remove from set
fruitSet.remove('Mangoe')

# 'fruitSet.clear()' will empty your set but will keep it existing

# 'del fruitSet' will delete the entire set and make it non existing

print(fruitSet)