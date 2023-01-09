'''
-   Class defination, syntex and how to create a variable of a class.\
-   Instance variable
-   Inheritance, multiple inheritance
-   Polymorphish
    - overloading
    - overridding
-   Data hiding
*   Constructors in Python
'''

# class veriable and instance veriable
# class
class BaseClass:
    # instance variable
    x = 10

obj = BaseClass()
print(obj.x)

# constructors in python
'''
-   consturctor is used to consturct the instance variable 
    of an object of an class
-   There are two types of constructors 
    - Default
    - Prameterized
-   Constructor uses is __init__(): method.
    - __init__ is always excicuted whenever the class is being initiated.
    - __init__ functoin is used to assign values to object properties.

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Person('Raman', 500)
print(f"Name : {obj.name}, Age : {obj.age}")


# With method object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def mtfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Delete
del p1.age # instance variable
del p1