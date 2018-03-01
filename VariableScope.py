#@Author Prathamesh More

"""
All variables in a program may not be accessible at all locations in that program. This
depends on where you have declared a variable.
The scope of a variable determines the portion of the program where you can access a
particular identifier. There are two basic scopes of variables in Python-
 Global variables
 Local variables

Variables that are defined inside a function body have a local scope, and those defined
outside have a global scope.

"""

total = 0

def additionTwoNumbers(num1, num2, num3):
    
    total = num1 + num2 + num3
    print("Total inside in Function : ", total)


additionTwoNumbers(10,20,30)

print("Total outside of function : ",total)