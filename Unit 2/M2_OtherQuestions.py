from curses.ascii import isdigit


# Q1. 
num = [1,2,3,4,5,6,"a"]
sum_num = 0
for x in num:
    if type(x) == int:
        sum_num += x
print(sum_num)

# Q2. Extracting words starting with K in string list
test_list = ['Gfg is best', 'Gfg is for geeks', "I love G4G"]

K = "g"

print("The original list is : " + str(test_list))

res = []
for sub in test_list:

    temp = sub.split()
    print(temp)
    for ele in temp:

        if ele[0].lower() == K.lower():
            res.append(ele)

            print("The Filtered elements : " + str(ele))

# Q3. 
test_list = ['Gfg is best', 'Gfg is for geeks', "I love G4G"]

K = " "

print("The original list is : " + str(test_list))

res = []
for sub in test_list:

    temp = sub.split(K)
    print(temp)
    for ele in temp:
        res.append(ele)

print(str(ele))


# Q4. 
strg = "However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfecthuman being, and the very incarnation of saumya rasa, harmonious equilibrium."

s = strg.split(" ")

print(s.count("Ram"))

# Q5.

strg = strg.replace("Ram", "Shree Ram")
print(strg)

# Q6.

lst = strg.split(" ")

lst = lst.sort(reverse=True)

s =""
for i in lst:
     s= s + i + " "

print(s)
print(str(lst))

# Q7. 
lst = [1,2,3,4,5,7,6]

lst1 = lst.sort()

if lst == lst1:
    print("Sorted")
else:
    print("Not Sorted")