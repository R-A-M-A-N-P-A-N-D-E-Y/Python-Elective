# List
'''

Data Structures: List
-   Basic List Operations
     - Creating a list
     - Insertion
     - Replacing
     - Removing an element
     - Searching
     - Sorting
-   Methods of List objects
-   Nested List
-   Using list as Stack and Queues
-   How efficient list are when used as stack or queue

'''

# 1. What is list in Python ?
'''

- List is a Python's in-built data Structure.
- List can store different types of elements whereas array can store only single type of elements
  [int arr[3] = {1,2,3}; ]
- [], square brackets are used to create a list

'''

# 1.1 Empty list example
from tokenize import Number


listSample = []
print(listSample)

# 2. Create a list!
Participants = ['John', 'Rakesh', 'Amit', 'Suresh', 123, 123.5, 'A']
print(Participants)

print(Participants[1])

print(Participants[2])

print(Participants[-1])

print(Participants[-2])

# 3. Updating a list element
Participants[3] = 'Maria'
print(Participants)

# 4. Delete an element from the list
del Participants[2]
#del Participants[1:3]
print(Participants)
print(Participants[2])

# 5. Add new elements into a list
Participants.append("Raman")
Participants.append("123")
Participants.append(123)
Participants.append("A")
Participants.append(123.4)
print(Participants)

# 6. Replace Values in a List using indexing
l = ['Hardik', 'Rohit', 'Rahul', 'Virat', 'Pant']
l[0] = 'Raman'
print(l)

# 7. List Slicing

'''

list[index]
list[start, stop]
list[start, stop, step]
stop element would be excluded from the end result

'''

Participants = ['Suresh', "John", 'Maria', 'Amit', 'Sumit', 'Cat', 123]

print(Participants)

print(Participants[1:3])

print(Participants[:2])

print(Participants[4:])

print(Participants[-2:])

print(Participants[-2::-1])

# 8. Finding index of an element of the list
Maria_index = Participants.index("Maria")
print(Maria_index)

# ValueError: 'Maria123' is not in list
index = Participants.index("Maria123")
print(index)

# 9. Search an element in the list
x = [1, 2, 3, 4, 5]
print(2 in x)      # True
print(7 not in x)  # True

Participants = ['Suresh', 'John', 'Maria', 'Amit', 'Sumit', 'Cat', 123]


x = [1, 2, 3, 4, 5]
if (2 in x):
  a = x.index(2)
  print(a)
else:
  print("Element not found in the list..!")

# 10. Sort a list
Participants.sort()
print(Participants)

# 10.1 Sort in reverse order
Participants.sort(reverse=True)
# The change will take place in the original string only
print(Participants)

Numbers = [2, 3, 4, 5, 1]
Numbers.sort()
print(Numbers)

Numbers.sort(reverse=True)
print(Numbers)

# 11. Creating a list using range function
lst = range(1, 9, 2)
for i in lst:
  print(i)

# print(list[0])

# 12. Concat two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)   # It will create a list of combined elements


# 13. Nested list as matrics [Nested list]

Participants = ['Suresh', 'John', 'Maria', 'Amit', 'Sumit', 'Cat', 123]

Newcomers = ['Joshua', 'Barittany']
print(Newcomers)

print("__Bigger_List__")
Bigger_List = [Participants, Newcomers]

print(Bigger_List)
print(Bigger_List[0])
print(Bigger_List[1])

print(Bigger_List[0][0])
print(Bigger_List[1][0])

# 14. Find max and min from a list
Numbers = [1, 2, 3, 4, 5]
print(max(Numbers))
print(min(Numbers))


# 15. Extra Methods of list Objects
n = [1, 2, 3, 4, 5]
print(len(n))
n.append(6)
n.append(6)
print(n)

print(n.count(6))

n.remove(6)
print(n)

n.reverse()
print(n)

n.clear()
print(n)

# 16. List Comprehensions
'''

List comprehension represents creation of new lists from an itrable object like range, set, tuple and so on

'''
s = []
for i in range(1,9):
  s.append(i)

print(s)

lst = range(1, 9 ,2)
for i in lst:
  print(i)

# yet to explore: set, tuple, dictionary -> list

# 17. Using list as Stacks
# stack using list
'''LIFO Order'''

stack = ['Amar', 'Akbar', 'Anthony']
stack.append('Ram')
stack.append('Iqbal')
print(stack)

# Remove the last item
print(stack.pop())
print(stack)

# Removes the last item
print(stack.pop())
print(stack)

# 18. Using list as queue
# Initializing a queue
'''First in first out [FIFO]'''
queue = []

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# How efficient lists are when used as stack or queue ?
# As Stack
'''
The bigger issue is that it can run into speed issues  as it grows.
The items in the list are stored next to each other in memory,
if the stack grows bigger then the block of memory that currently holds it,
then Python needs to do some memory allocations. This can lead to some append()
calls taking much longer then the other one.
'''

# As Queue
'''
However, lists are quite slow for this purpose because inserting or deleting an elemsnt at the
beiginning requires shifting all of the other elements by one, requiring O(n) time.
'''