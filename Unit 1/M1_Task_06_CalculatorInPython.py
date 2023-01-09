def Add(a, b):
    return(a+b)

def Sub(a, b):
    return(a-b)

def Multi(a, b):
    return(a*b)

def Div(a, b):
    return(a/b)

def Power(a, b):
    return(a**b)

def FloorDiv(a, b):
    return(a//b)

def Remain(a, b):
    return(a%b)

def main():

    if Add(5, 10) == 15:
        print("Add Function is working fine..!")

    if Sub(5, 10) == -5:
        print("Sub Function is working fine..!")

    if Multi(5, 10) == 50:
        print("Multi Function is working fine..!")

    if Div(10, 5) == 2:
        print("Div Function is working fine..!")

    if Power(5, 2) == 25:
        print("Power Function is working fine..!")

    if FloorDiv(50, 10) == 5:
        print("FloorDiv Function is working fine..!")
    
    if Remain(50, 10) == 0:
        print("Remain Function is working fine..!")

if __name__ == "__main__":
    main()

