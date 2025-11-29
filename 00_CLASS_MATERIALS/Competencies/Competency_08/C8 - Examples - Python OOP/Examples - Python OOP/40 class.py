# write a class that will accept 3 values and return the largest


class greatest:

    def check(self):
        largest = self.num1
        if self.num2 > largest:
            largest = self.num2
        if self.num3 > largest:
            largest = self.num3
        return largest
        


    def __init__(self, n1, n2, n3):
        self.num1 = n1
        self.num2 = n2
        self.num3 = n3
    
        
value = greatest(1, 2, 3)

print(value.check())





