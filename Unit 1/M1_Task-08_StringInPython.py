# s1 = "hello"
# s2 = "hello"

# if s1 == s2:
#     print("A")
# if s1 <= s2:
#     print("B")
# else:
#     print("C")

# s1 = "Hello"

# print(s1.upper())
# print(s1.lower())
# print(s1) # Strings are inmutable.

'''If an object is inmutable that means the content of that object will always be intackt'''

from turtle import st


s1 = "One"
s2 = "Two"
s1 = s2
print(s1)

# String Slicing

'''
Syntex:
    s[index]
    s[start, stop]
    s[start, stop, step]
'''

string = "STRING IN PYTHON"

string[0]
string[2::]
string[::2]
string[:4:]

string[-4:-1]
string[-1:-4:-1] #ASTRING

# Reapeating a string
print((string + "\n") * 10) # repeats the string 10 times
print(123 * 10) # Calculates them

# String length
string = 'Hello'
print(len(string)) # includes spaces also

# removing space from the string
name = " Raman Pandey "
print(name.rstrip()) # Removes space from right side
print(name.lstrip()) # Removes space from left side
print(name.strip())  # Removes space from both side
print(name)

# Find a substring
str = input("Enter main string: ")
subStr = input("Enter sub string: ")

n = str.find(subStr, 0,len(str))

if n==-1:
    print("Substring not found")
else:
    print("Substring found at position ", n)

# str.maketrans(exp, change)  .translate()
