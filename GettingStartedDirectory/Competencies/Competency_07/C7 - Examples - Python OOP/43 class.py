class BinaryConversion :

    def conversion(self):
        stringNum = str(self.binary)
        sumofDigits = 0
        place = len(stringNum)

        for value in stringNum:
            place = place -1
            sumofDigits = sumofDigits+float(value)*2**place
        
        return sumofDigits
                      
    def __init__(self,binary):
        self.binary = binary
        
value = BinaryConversion(1011)

print(value.conversion())
        




