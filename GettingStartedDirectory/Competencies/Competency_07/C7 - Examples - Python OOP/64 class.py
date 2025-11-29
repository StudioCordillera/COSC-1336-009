# write a class that will accept 1 parameter and return the factorial


class Facts:

    def factorial(self):

        fact = 1

        for i in range(1, self.number + 1, 1):
            fact = fact * 1

        return fact


    def __init__(self, num):
        self.number = num


value = Facts(10)

print (value.factorial())



