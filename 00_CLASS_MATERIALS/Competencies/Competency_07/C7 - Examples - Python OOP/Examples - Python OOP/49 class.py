
class Calculator:
    
    def add(self):
        return self.number1 + self.number2
        
    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2
        
    def __init__(self, a, b):
        self.number1 = a
        self.number2 = b

# Create an instance of Box.
x = Calculator(1, -5)

# Print area.
print("Sum is " + str(x.add()))
print("Difference is " + str(x.subtract()))
print("Product " + str(x.multiply()))
print("Quotient " + str(x.divide()))
