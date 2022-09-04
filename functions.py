# A function is a block of code which runs only when its been called, it does not use curly brackets like javascript function does, it uses indentation with tabs or spaces

# create a function

my_name = 'abdul frfr'

def say_abdul(): print(my_name)

say_abdul()

# Retuen values
def getSum(sum1, sum2):
    total = sum1 + sum2
    return total

print(getSum(2,5))


# lambda functions
# lambda functions are short and anonymous functions
# they are similar to arrow functions in javascripts

anotherSum = lambda num1, num2 : num1 + num2

print(anotherSum(3,1))