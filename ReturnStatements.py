#@Author Prathamesh More

"""
The statement return [expression] exits a function, optionally passing back an expression
to the caller. A return statement with no arguments is the same as return None.

"""


def sum(arg1, arg2):

    total = arg1 + arg2
    print("Total inside function : ", total)
    return total


total = sum (10,20)

print("Total outside function : ", total)