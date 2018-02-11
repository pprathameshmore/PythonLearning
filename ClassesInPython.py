#@Author Prathamesh More

"""
Class: A user-defined prototype for an object that defines a set of attributes that
characterize any object of the class. The attributes are data members (class
variables and instance variables) and methods, accessed via dot notation.
 Class variable: A variable that is shared by all instances of a class. Class variables
are defined within a class but outside any of the class's methods. Class variables
are not used as frequently as instance variables are.
 Data member: A class variable or instance variable that holds data associated with
a class and its objects.
"""

class Additon:

    result = 0
    number_one = 0
    number_two = 0

    def __init__(self, one, two):

        Additon.number_one = one
        Additon.number_two = two


    def performAddition(self):

        Additon.result = Additon.number_one + Additon.number_two

    def showResult(self):

        print('Addition is ', Additon.result)


add1 = Additon(10,20)
add2 = Additon(20,30)
add1.performAddition()
add1.showResult()
add2.performAddition()
add2.showResult()