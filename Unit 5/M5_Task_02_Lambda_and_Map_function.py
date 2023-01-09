# Lambda or anonymous functions in python
'''

-   A lambda functoin is a small anonymous function.
-   A lambda function can take any number of argumnets.
-   It can create functions in one line when possible.

'''

def add(a, b):
    return a+b

# def minus(x, y):
#     return x-y-2

minus = lambda x, y: x-y

print(minus(9, 4))

# Q2. 
'''
WAP in python to calculate the square root of a
whole number by using lambda expressoin and math.sqrt 
technique.
'''

from math import sqrt
sqrtOfaNumber = lambda x : sqrt(x)

print(sqrtOfaNumber(6))

# Map in python
'''

-   The map() function exceutes a specified function for
    each item.
-   The item is send to the function as a parameter.

'''

def myFunc(n):
    return len(n)

x = map(myFunc, ('apple', 'banana', 'cherry'))
print(list(x))

def myfunc(a, b):
    return a+b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

# Q3.
'''
WAP in python to check if the number is prime or not ?
Check multiple number at once.
'''

from math import sqrt

def PrimeOrNot(x):
    count = False
    for n in range(2, int(sqrt(x))+1):
        if x % n == 0:
            count = True
            break
    if count:
        return "It is not a Prime Number."
    else:
        return "It is a Prime Number."

x = map(PrimeOrNot, (7, 8, 13))
print(list(x)[0])