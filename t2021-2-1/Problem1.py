class Calculator:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def getResults(self, a, b, operator):
        if operator == "+":
            print(a + b)
        elif operator == "-":
            print(a - b)
        elif operator == "*":
            print(a * b)
        elif operator == "/":
            print(a / b)
        else:
            print("Invalid operator")


operator = input("Enter the operator")
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
obj = Calculator(a, b, operator)
obj.getResults(a, b, operator)
