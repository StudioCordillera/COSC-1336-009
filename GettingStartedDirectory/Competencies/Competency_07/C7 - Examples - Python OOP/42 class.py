# write a class that will accept 3 perameters and find the roots
#of the quadratic function
class quadratic :

    def maha(self):
       if self.a== 0 or self.b*self.b - 4*self.a*self.c<0:
           return "no solution"
        else:
            dt = self.b**2-4*self.a*self.c
            x1= (-self.b + dt**.5)/ (2*self.a)
            x2=(-self.b - dt**.5)/ (2*self.a)
           return  str(x1)+str(x2)
            
            
        


    def __init__(self, n1, n2, n3):
        self.a = n1
        self.b = n2
        self.c = n3
        
value = ( 1,2,3)
print (value. maha())
        




