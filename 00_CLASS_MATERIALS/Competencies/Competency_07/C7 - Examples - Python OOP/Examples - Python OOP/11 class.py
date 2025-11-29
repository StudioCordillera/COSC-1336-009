class Box:
    count = 0
    
    def area(self):
        print(self.count)
        return self.width * self.height

    
    def __init__(self, width, height):
        self.count = self.count + 1
        self.width = width
        self.height = height
        

    def change(self, value):
        self.width = value

# Create an instance of Box.
x = Box(10, 2)
y = Box(1, 3)
x.change(3)

# Print area.
print(x.area())
print(y.area())
