#A tuple is a collection which is ordered and unchangable. It allows duplicate values
#A tuple with one value needs a tailing coma, without that its going to be trated as a single string
#Create Tuple

fruits = ('Mangoe', 'Grape', 'Strawberry', 'Pineapple')



print(fruits, type(fruits))
print(fruits[1])


#A set is a collection thats unordered and unchangable. It does not allow duplicate values

#Create set

fruitSet = {'Apple', 'Mangoe', 'Pear', 'Grape'}

fruitSet.add('Straw')

print(fruitSet)