#@Author Prathamesh More
"""
You can always override your parent class methods. One reason for overriding parent's
methods is that you may want special or different functionality in your subclass.

"""


class Parent:
    def myMethod(self):

        print("This is Parent")


class Child(Parent):
    def myMethod(self):

        print("This is child")


c = Child()
c.myMethod()
p = Parent()
p.myMethod()