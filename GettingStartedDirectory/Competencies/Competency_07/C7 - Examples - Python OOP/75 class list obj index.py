class Student:  
    def __init__(self, name):  
        self.name = name  

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name

   
# creating list        
list = []  
  
# appending instances to list  
list.append( Student('Akash') ) 
list.append( Student('Deependra') ) 
list.append( Student('Reaper') ) 
  
for obj in list: 
    print( obj.getName() )

print(list.Student())
  

