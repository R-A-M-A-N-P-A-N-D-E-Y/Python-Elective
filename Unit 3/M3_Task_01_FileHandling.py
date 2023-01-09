# Working of open() function
'''

file = open(filename with path, mode)

'''
import os
path = os.path.dirname(__file__)
path = path + '/'
# path = "C:\Users\Dell\Python Work Space\Unit-3"
file = open(path + '/abc.txt', 'r')

for i in file:
    print(i)


'''

r    : open an existing file for a read operation
w    : open an existing file for a write operation. If the file contains some data then it will be overridden but if the file does not exist then it will a new fine with the given name.
w+   : Read + Write -> Overridden
a    : open an existing file for append operation. It won't override existing data.
a+   : Read + Append -> Not Overridden
r+   : To read and write data into the file. The previous data will be overriden.

'''

file = open(path + 'abc.txt', 'r')
print(file.read())

file = open(path + 'abc.txt', 'r')
print(file.read(5))

# Write into a file (w)
file = open(path + "abc.txt", 'w')
file.write("This is write command. ")
file.write("It allows us to write in a particular way!")
file.close()
file = open(path + 'abc.txt', 'r')
print(file.read())

# Write into a file (w+)
file = open(path + "abc.txt", 'w')
file.write("This is write command. ")
file.write("It allows us to write in a particular way!")
file.seek(0)
print(file.read())

# Append Mode (a)
file = open(path + "abc.txt", 'a')
file.write("Hello ")
file.write("There..!")
file.close()
file = open(path + 'abc.txt', 'r')
print(file.read())

# Append Mode (a+)
file = open(path + "abc.txt", 'a+')
file.write("Hello ")
file.write("There..!")
file.seek(0)
print(file.read())

# split() lines
'''

-  We can also split lines using file handing in Python.
   It splits the file data when space us encountered.
-  You can also split using any characters as you wish

'''

# file = open(path + 'abc.txt', 'r)
with open(path + 'abc.txt', 'r') as file:
    data = file.readlines()
    for lines in data:
        word = lines.split()  # line.split('a')
        print(word)

# Renaming a file 
# Case insenstive
import os
os.rename(path + "ABC.txt", path + 'abc.txt')

# Deleting a file
# Case insenstive
os.remove(path + 'ABC.txt')