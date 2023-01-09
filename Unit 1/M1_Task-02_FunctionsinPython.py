# Function
from calendar import c


def my_function():
    print("Hello from function")

my_function()

# Function with parameter
def my_function(fname):
    print(f"{fname} Reference")

my_function("Email")
my_function("Password")
my_function(123)

def my_function(fname, lname):
    print(f"{fname}  {lname}")

my_function("Email", "Password")
my_function(123, 123.5)

# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Ravi", "Sumit", "Amit")
my_function("Ravi", "Sumit", "Amit", "Ankush")

# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emi", child2="Amit", child3="Ravi")

# Default value of function parameter
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweeden")
my_function("India")
my_function()
my_function("Brazil")

# Passing list as an Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["Apple", "Banana", "Cherry"]

my_function(fruits)

# Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9.2))

# Pass Function
def my_function():
    pass

my_function()
