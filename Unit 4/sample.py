import re

txt = "I 20.20.20221 Hey Hy Hay this is amit Chauhan, Software Engineer, amit.chauhan@gmail.com akash 12.12.2022 12122012"

# . and \ ReGex
# result = re.search("@.", txt)
# print(result)
# print(result.group())

# @. * RegEx [+: one or more, *: zero or more]
# result = re.search("@.*", txt)
# print(result.group())
# print(result.group().split())
# print(result.group().split()[0])/

# [0-9]{2}\.[0-9]{2}\.[0-9]{4}
# result = re.search("[0-9]{2}\.[0-9]{2}\.[0-9]{4}\s", txt)
# print(result.group())

# print(re.findall("\\b[aeiouAEIOU]\S*", txt))

# print(re.findall("He?y", txt)) # ? -> optional

# print(re.findall("\d\d\.", txt))    # \d -> checks for digits only, \D -> chceks for everything except digits.

# print(re.findall("\AY", txt))   # \A -> perticular charactor in the string.

# print(re.findall("[^\d]", txt))     # [^] -> not, ^[0-9] -> must start from

# \\b -> muat start with
# (....)\l -> looks for replicated words.

# print(re.findall("\w", txt))    # \w -> [a-zA-Z0-9]