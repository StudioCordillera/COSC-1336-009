class Factorial:
    
    def factorial(self):
        
        if self.number < 0:
            return "No factorial"
        
        elif self.number == 0:
            return "Factorial is 1"
        
        else:
            products = 1
            
            for value in range(self.number, 1, -1):
                products = products * value
                
            return products
        
    def __init__(self, s1):
        self.number = s1
        

# Create an instance of Box.
x = Factorial(5)

# Print area.
print(x.factorial())
