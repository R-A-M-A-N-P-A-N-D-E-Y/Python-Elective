def add(x,y):
    '''This function adds two variables a and b and 
    returns the sum of a and b
    '''

    return x+y

def sub(x,y):
    '''This function substracts two variables a and b
    and returns the substraction of a and b
    '''

    return x-y

print("Hello world 1")

def main():
    '''This function is testing all the functionalities
    '''
    if add(1,2) == 3:
        print("Add functionality is working fine..!")
    if sub(3,2) == 1:
        print("sub functionality is working fine..!")

# print(__name__)

# if __name__ == "M1_OtherFunctions":
#     main()

if __name__ == "__main__":
    main()

print("Hello world 3")
