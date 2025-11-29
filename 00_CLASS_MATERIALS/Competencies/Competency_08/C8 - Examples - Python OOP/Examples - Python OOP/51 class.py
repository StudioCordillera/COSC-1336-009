#write a class that will accept 2 parameters and return the area of the triangle


class Triangle:
    def area(self):
        return self.base * self.height * .5

    def __init__(self, base, height):
        self.base = base
        self.height = height


