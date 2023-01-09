# Exception Handling 
'''

Exception, Error, Compilation Issues
1. Comploation Issues :
    - Syntex Issues, or issues in the code catch by the python compiler.
2. Exception :
    - Issues in your code, catch by the PVM [Python Virtual Machine].
    - Run time issues, Handle by [PVM].
    - Handling is possible by using try and except.
    - Exception are always handled by the programmer.
3. Error :
    - Can not be handled.
    - Happen at run time.
    - Even PVM can not catch them.
    - System Design should be robust and efficient.

'''

# 1. try, except, finally
import os
path = os.path.dirname(__file__)
path = path + '/'

try:
    #Write suspicious code here!
    f = open(path + 'abc.txt', 'w')
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a/b
    f.write("Write $d into my file" %c)

except ZeroDivisionError:
    #This block of code only runs when exception is happened in the code
    print("Division by zero happened, so don't enter zero as a input.")

finally:
    #This block of code will always run
    f.close()
    print("File is closed now.")