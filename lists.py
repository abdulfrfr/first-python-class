#A list is a changeable and ordered collection of data. Allows duplicate members.

numbers = [1, 2, 3, 4, 5]

alphas = ['a', 'b', 'c', 'd', 'e', 'abdul', 'banana', 'mangoes']


#print a specific data from a list
print(alphas[7])


#Get length of a list
print(len(alphas))

#add to the list

alphas.append('added')

#remove from list

alphas.remove('d')

#insert to list to a specific location

numbers.insert(2, 15)

#delete from list on a specific location

numbers.pop(0)

#reverse list

alphas.reverse()

alphas.sort()

alphas.sort(reverse=True)

alphas[2] = 'blueberry'

print(alphas)
print(numbers)