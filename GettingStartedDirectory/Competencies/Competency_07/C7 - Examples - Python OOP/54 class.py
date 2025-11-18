class Triangle:
    
    def check(self):
        if side1 == side2 == side3:
            return "It is"
        else:
            return "It is Not"
        
    def __init__(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

# Create an instance of Box.
x = Triangle(10, 2,5)

# Print area.
print(x.check())
