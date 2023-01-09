# Note 
'''

-   A RegEx, or Regular Ecpression, is a sequence of charactors that forms a search pattern.
-   RegEx can be used to check if a string contains the specified search pattern.
-   Python has a built-in package called "re", which can be used to work with Regular Expression.

'''

txt = "The rain in Spain"
x = txt.find("ai")
print(x)

x = txt.find("ai", 7)
print(x)

# Import re Module
import re

x = re.findall(r"ai", txt) # findall returns all the instances of the substring as a list that you are tring to find.
print(x)

x = txt.find("aiI", 7)
print(x)

x = re.findall(r"aiI", txt)
print(x)

# Search for the first white-space character or even a word in the 
x = re.search(r"\s", txt)
y = re.search(r"rain", txt)
print(x)
print(y)
print(type(y))

# Split a statement, based on a singlr space
txt = "The rain in Sapin"
x = re.split("\s", txt)     # this will return a list of eords
print(x)

# control the number of occurrences by specifying the maxsplit parameter
txt = "The rain in Sapin"
x = re.split("\s", txt, 1)
print(x)

# The sub() function replaces the matches with the text of your choice
txt = "The rain in Sapin"
x = re.sub("\s", "_", txt)
print(x)

# control the number of replacements by specifying the count paprameters
txt = "The rain in Sapin"
x = re.sub("\s", "_", txt, 2)
print(x)

# Match Objext
'''

-   A MatchObject is an object containing information about the search and the result.
-   If there is no match, the value None will be returned, insted of the Match Object.

'''

# Match Object in RegEx
txt = "The rain in Sapin"
x = re.search("ai", txt)        # this will return an object Match
print(x)
print(type(x))

print(x.group())
print(x.span())
print(x.start())
print(x.end())

# Q1. Find host or domain name from text provided

# 1. First Apporoch (String function) :
data = "From akash.chauhan@gmail.com 12-12-22 09:14:16"

eloc = data.find("@")
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)

# 2. Search approch (RegEx Functions) :
data = 'From akash.chauhan@gmail.com 12-12-2022 02:14:16'
# x = re.search('@.*', data)
# print(x)
# x = x.group()
# print(x)
# x = x.split()[0]
# print(x)

x = re.search('@.*', data).grop().split()[0]
print(x)

# Extract Date from a string
txt = "I have submitted my report to the department on 12-12-2022"
x = re.search(r"([0-9]{2}\-[0-9]{2}\-[0-9]{4})", txt)
print(x.group())

# Split a string with multiple de
txt = "I have submitted my report to the department on 12-12-2022"
print(re.split("\s|,|\.", txt))

# Find words start with vowels
txt = "I have submitted my report to the department on 12-12-2022"
print(re.findall("\\b[aeiouAEIOU]\S*", txt))
