#@Author Prathamesh More


class ConstructorDemo:

    name = ""

    def __init__(self, name):

        print("Printing from Constructor")
        ConstructorDemo.name = name
        print(name)



c = ConstructorDemo('Prathamesh More')