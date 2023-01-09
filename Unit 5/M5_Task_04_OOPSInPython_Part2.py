# Inheritance and Multiple Inheritance in Python

class Class1:
    def display(self):
        print("In Class1")

class Class2(Class1):
    def display(self):
        print("In Class2")

class Class3(Class1):
    def display(self):
        print("In Class3")

class Class4(Class3, Class2):
    pass

obj = Class4()
obj.display()


# Polymorphism
'''
- The word polymorphism means having many forms.
- In programming, polymorphism means the same function name
  (but different signatures) being used for different types.
- The key difference is the data types and number of 
  arguments used in function.

1. Inbuilt polymorphism function
    print(len("Raman"))
    print(len[10, 20, 30])

2. User-defined polymorphism functions
    def add(x, y, z = 0):
        return x + y + z

    print(add(2, 3))
    print(add(2, 3, 4))
'''

class India:
    def capital(self, a):
        print("New Delhi is the capital of India: ", a)

    def capital(self):
        print("New Delhi is the capital of India.")
        
    def language(self):
        print("Hindi is most widely spoken language of India.")

obj_ind = India()
obj_ind.capital("India")

obj_ind = India()
obj_ind.capital()

# Method Overloading
####################
def add(datatype, *args):
    if datatype == 'int':
        answer = 0

    if datatype == 'str':
        answer = ''

    for x in args:
        answer = answer + x

    print(answer)

# Integer
add('int', 5, 6)

# String
add('str', "Hi", "Geeks")

# Method Overriding
###################
class A:
    def fun1(self):
        print('fun1 of class A')
    
    def fun2(self):
        print('fun2 of class A')
