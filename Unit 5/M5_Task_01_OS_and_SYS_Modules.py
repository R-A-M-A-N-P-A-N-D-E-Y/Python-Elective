# OS and SYS Modeuls

import os
import sys

# Get the current working directory (CWD)
cwd = os.getcwd()
print("Current working directory:", cwd)

#  Changing the current working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

current_path()
# Changing the CWD
os.chdir('../')
# Printing CWD after change

parent_dir = os.getcwd()
# path = os.path.join(parent_dir, directory)
# os.make

##### SYS MODULE #####
'''

The SYS module in Python provides various functoins and variables that are used
to manipulate different parts of the Python runtime environment.

-   sys.version is used which returns a string containing the version of Python Interpreter with some additional information.
-   This shows how the sys module interacts with the interpreter.

'''

import sys
print(sys.version)

# Input and Output using sys
'''

# stdin:
-   It can be used to get input from the command
    line directly.
-   It, also, automatically adds '\n' after each
    sentence.

'''
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

'''

# stdout:
-   A built-in file object that is analogous 
    to the interpreter's.
-   stdout is used to display out directly to the screen
    console.

'''

print("####stdout####")
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')

# print function
print("####print function####")
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')
sys.stdout.write('Raman Pandey')

# sys.argv:
'''

# sys.argv: command line arguments:
-   Command-line arguments are those which are passed 
    during the calling of the program along with the 
    calling statement.

'''

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# arguments passed
print("\nName of Python script: ", sys.argv[0])

print("\nArguments passed: ", end="")
for i in range(1, n):
    print(sys.argv[i], end=" ")

#  Addition of numbers
Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\nResult: ", Sum)

# end = " "
'''

By default, the print functoin ends with a newline.
Passing the whitespace to the end parameter (end=" ")
indicates that the end charactor has to be identified by
whitespace and not a newline.

'''

# Q1.
'''
Write a python program to check if the entered number is 
prime or not command using line argumnet tachnique.

Also use square root technique to check if it is prime 
or not!
'''
# Ans1:
from math import sqrt

def PrimeOrNot(x):
    count = False
    for n in range(2, int(sqrt(x))+1):
        if x % n == 0:
            count = True
    if count:
        print("\nIt is not a Prime Number.")
    else:
        print("\nIt is a Prime Number.")

PrimeOrNot(sys.argv[1])