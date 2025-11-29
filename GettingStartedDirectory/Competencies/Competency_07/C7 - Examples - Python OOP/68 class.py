# write a class that will accept 1 binary number convert to decimal
class binaryConversion :

    def conversion(self):
        stringNum = str(self.binary)
        sumofDigits = 0
        place = len(stringNum)

        for value in stringNum:
            place = place -1
            sumofDigits = sumofDigits + float(value) * 2**place
        
        return sumofDigits
                      
    def __init__(self,binary):
        self.binary = binary
        
value = binaryConversion(101101010101)

print(value.conversion())
        




