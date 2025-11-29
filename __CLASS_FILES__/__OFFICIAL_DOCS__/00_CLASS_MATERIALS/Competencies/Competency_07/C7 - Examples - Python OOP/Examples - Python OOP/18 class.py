#Example #1 Class
 
class VMname:
    def createVM(self, name):
        self.name=name
    def stateVM(self):
        print('Printing from the 1st Class Example ' + self.name)
        print() #Adding Whitespace  
 
#Explicitly initializing the Class
example1 = VMname()
example1.createVM('classEx.foo.org')
example1.stateVM()
 
#Example #3 What the heck is this __init__?
class VMname1:
    def __init__(self, name):
        self.name=name
    def stateVM1(self):
        print('Printing from the 2nd Class Example ' + self.name)
        print() #Adding Whitespace
 
#__init__ initializes the Class
example2 = VMname1('constructorEx.foo.org')
example2.stateVM1()
 
#Example #3 Predefined Data
class VMname2:
    def __init__(self, name='predefinedvarsEx.foo.org'):
        self.name=name
    def stateVM2(self):
        print('Printing from the 3rd Class Example ' + self.name)
        print() #Adding Whitespace
 
#__init__ initializes the Class and a predefined value for name
example3 = VMname2()
example3.stateVM2()
