# write a class that will accept 1 parameter and return the factorial


class Triangle:

    def check(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2
                and self.side2 + self.side3 > self.side1:
            return True
        else:
            return False


    def __init__(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

test = Triangle(2,3,5)

print ( test.check() )








