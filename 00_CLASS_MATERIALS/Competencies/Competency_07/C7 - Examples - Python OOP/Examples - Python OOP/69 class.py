# Define a class (Conversion) that will accept seconds & write a module (convert)
# that will return values in hours

class Conversion:
    def __init__(self, seconds):
        self.second = seconds

    def convert(self):
        return self.second/3600

myNic = Conversion(5400)

print(myNic.convert())






