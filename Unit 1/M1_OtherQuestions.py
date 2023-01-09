# Convert H2O using maketrans and translate method of string.
str = "H2O"
subscript = str.maketrans("0123456789", "")
print(str.translate(subscript))

# Q2.

marks = int(input("Enter the marks of the student: "))

if marks == 75:
    print()