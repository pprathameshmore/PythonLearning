#@Author Prathamesh More

class DestructorDemo:

    def __init__(self, x = 10, y = 10):

        self.x = x
        self.y = y

        print("Printing from Constructor")

    def __del__(self):

        print("Printing from Destructor")
        class_name = self.__class__ .__name__
        print(class_name, "Destroyed")

d1 = DestructorDemo()

d2 = d1

print(id(d1), id(d2))
