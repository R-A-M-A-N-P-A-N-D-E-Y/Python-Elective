from math import sqrt


def sqrt1(x):
    i=1
    j=1
    while(j <= x):
        j = i*i
        i += 1

    return i-1

def PrimeOrNot(x):
    count = False
    for n in range(2, int(sqrt(x))+1):
        if x % n == 0:
            count = True
    if count:
        print("\nIt is not a Prime Number.")
    else:
        print("\nIt is a Prime Number.")


def primeOrNot(x):
    count = False
    for n in range(2, x):
        if x % n == 0:
            count = True
    if count:
        print("\nIt is not a Prime Number.")
    else:
        print("\nIt is a Prime Number.")

def primeOrnot(x):
    count = False
    for n in range(2, int(x/2)):
        if x % n == 0:
            count = True
    if count:
        print("\nIt is not a Prime Number.")
    else:
        print("\nIt is a Prime Number.")



num = int(input("Enter the Number: "))
PrimeOrNot(num)
primeOrNot(num)
primeOrnot(num)