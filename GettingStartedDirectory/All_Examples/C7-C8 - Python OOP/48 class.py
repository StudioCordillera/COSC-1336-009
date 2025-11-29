
class Quadratic:
    
    def quadratic(self):
        if self.side1 == 0 or self.side2 * self.side2 - 4 * self.side1 * self.side3 < 0:
            return "no real roots." 
        elif self.side2 * self.side2 - 4 * self.side1 * self.side3 == 0:
            return - self.side2 / (2 * self.side1) 
        else: 
            det = (self.side2 * self.side2 - 4 * self.side1 * self.side3) ** (1/2)
            x1 = ( - self.side2 + det) / (2 * self.side1)
            x2 = ( - self.side2 - det) / (2 * self.side1)
            return str(x1) + " and " + str(x2)   
        
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c

# Create an instance of Box.
x = Quadratic(1, -5 , 6)

# Print area.
print(x.quadratic())
