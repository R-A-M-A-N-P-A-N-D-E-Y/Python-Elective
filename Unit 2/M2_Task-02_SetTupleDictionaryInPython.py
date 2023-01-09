'''

1. Tuple
2. Sets
3. Difference between list and tuple
4. DIctionary
   - adding and removing keys
   - accessing values
   - Replacing vlaues
   - Traversing Dictionaries

'''

# 1. Tuple in Python
'''

    - Unchangable [Imutable]
    - Tuple items are ordered*
    - Allows duplicate values.
    - Use () to create tuple instade of []

'''

# Empty Tuple

from ast import List


t1 = ()

# Multiple types of data
t1 = (1, 2, 3, 4, 5, 'Akash', 'A', 123.4)
print(t1)

t1 = 1, 2, 3, 4, 5, 6, 6


# Accesing the tuple elements
t1 = 1, 2, 3, 4, 5, 6
print(t1[3])
print(t1[:])

# list -> tuple
list1 = [1, 2, 3, 4, 5]
t2 = (list1)
print(t2)

t3 = tuple(list1)
print(t3)

# Functions to process tuple:
t1 = (1, 2, 3, 4, 5, 6, 6)

print(len(t1))
print(min(t1))
print(max(t1))
print(t1.count(6))
print(t1.index(2))
print(sorted(t1, reverse = True))
print(t1)

'''

We can not perform operations in tuples like:
    - append()
    - extend()
    - insert()
    - clear()
over tuple as tuples are immutable in python

'''
#2. Set
'''

    - {} for set
    - set is a collection which is unordered*
    - unchangable [Immutable]
    - No duplicate members
      [Will automatically be deleted from the set]
'''
setV = {'apple', 'cherry', 'apple', 123, 123}
print(setV)

print("__SET__")
t1 = (2, 1, 3, 4, 5, 6, 6)
print(t1)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1, reverse = True))
print(t1)
#print(t1.count(6))
#print(t1.index(2))

'''

We can not perform operations in set like:
    - append()
    - extend()
    - insert()
    - clear()
As sets are immutable in python

'''

# 4. Dictonary

'''

    - It is a key value pair
    - Dictonary is a collection which is ordered**
    - changeable
    - No duplicate members

'''

# Dictonary Operations
'''

     - adding and removing keys
     - accessing values
     - Replacing values
     - Traversing Dictionaries

'''

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    123: 123.4,
    'A': 12,
    'A': 13
}

print(thisdict)

# Length of the dictionary
print(len(thisdict))

# Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    123: 123.4,
    'A': 12,
    'A': 13
}

# Access Dictionary Items:
print(thisdict["brand"])
print(thisdict[123])
print(thisdict["A"])

# Ordered or Unordered ?
'''

- When we say that dictionaries are oredered, it means that the item have a defined order,
  and that order will not change
- Unordered means that the items does not have a defined order, you cannot refer to an item by 
  using an index
- As of Python version 3.7, dictionaries are ordered.
  In Python 3.6 and earlier, dictionaries are unordered

'''

# Changeable or add an new element into a dictionaries
'''

Dictionaries are changeable, meaning that we can change add or remove items after
the dictionary has been created.

'''

# Dictionary items
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x) # before the change

car["color"] = "white" # new value
car["brand"] = "Ford123" # update value

x = car.keys()
print(x) # after the change

y = car.values()
print(y)

# Removing Keys
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

thisdict.popitem() # Will remove the last item
print(thisdict)

# Traversing Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

for x in thisdict.keys():
    print(thisdict[x])


letters = 'abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRESTWXYZ'

string_letters = str(letters)
list_letters = list(letters)
tuples_letters = tuple(letters)
sets_letters = set(letters)

print("String: ", string_letters)
print() # For new line
print("Lists: ", list_letters)
print() # For new line
print("Touples: ", tuples_letters)
print() # For new line
print("Sets: ", sets_letters)