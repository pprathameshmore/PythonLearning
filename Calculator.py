#@Author Prathamesh More

class Calculator:

    result = 0
    number_one = 0
    number_two = 0


    def __init__(self, number_one, number_two):

        Calculator.number_one = number_one
        Calculator.number_two = number_two


    def performAdditon(self):

        Calculator.result = Calculator.number_one + Calculator.number_two
        print('Addition is ', Calculator.result)

    def performSubstraction(self):

        Calculator.result = Calculator.number_one - Calculator.number_two
        print('Substraction is ', Calculator.result)

    def performMultiplication(self):

        Calculator.result = Calculator.number_one * Calculator.number_two
        print('Multiplication is ', Calculator.result)

    def performDivision(self):

        Calculator.result = Calculator.number_one / Calculator.number_two
        print('Division is ', Calculator.result)

cal = Calculator(10,20)
cal.performAdditon()
cal.performSubstraction()
cal.performMultiplication()
cal.performDivision()


c = Calculator(50,30)
cal.performAdditon()
cal.performSubstraction()
cal.performMultiplication()
cal.performDivision