#@Author Prathamesh More

#A function is a block of organized, reusable code that is used to perform a single, related
#action. Functions provide better modularity for your application and a high degree of code
#reusing.
#As you already know, Python gives you many built-in functions like print(), etc. but you
#can also create your own functions. These functions are called user-defined functions.


#Simple Function which prints the string on console

def printData(str):
    
    print(str)


printData("This is simple fuction")
printData("Hello there")

#Pass byReferencevsValue
#All parameters (arguments) in the Python language are passed by reference. It means if
#you change what a parameter refers to within a function, the change also reflects back in
#the calling function. For example


# Function definition is here
def changeme( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function before change: ", mylist)
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
    return


# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)