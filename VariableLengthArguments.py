#@Author Prathamesh More

#You may need to process a function for more arguments than you specified while defining
#the function. These arguments are called variable-length arguments and are not named in
#the function definition, unlike required and default arguments.

def funcname(arg, *vars):
    print("Output with single variable : ",arg)

    for var in vars:
        print("Varible length : ",var)


funcname("Prathamesh",10,20,30)