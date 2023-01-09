# else if









# For statements [The range() Function]
for i in range(1, 5):
    print(i)

x = 5

# While loop statement [Values in reverse order]
while(x >= 1):
    print(x)
    x = x-1

# Break and Continue Statements, and else Cla

n = 7
count = 0
for x in range(2, n+1):
    if n % x == 0:
        print("Not a Prime")
        break
    else:
        # loop fell through without finding a
        count = count + 1
        continue
if count == 0:
    print("It is a Prime Number")

# The match statement evaluates the variable's value
match cpuModel:
    case "celeron": # We test for the different values and print different messages
        print("Forget about ")



# Lazy 
'''
    Python can sometime skip to evaluate when one operand is enough to provide the answer.
'''
