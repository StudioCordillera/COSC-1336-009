class Product:
    def product(self):
        return self.number1 * self.number2

    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

# Create an instance of Box.
x = Product(10, 2)

# Print area.
print(x.product())
