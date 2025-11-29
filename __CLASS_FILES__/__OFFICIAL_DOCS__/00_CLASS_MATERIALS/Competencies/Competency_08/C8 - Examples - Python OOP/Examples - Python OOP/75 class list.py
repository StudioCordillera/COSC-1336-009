class Student:  
    def __init__(self, name):  
        self.name = name  

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name

def main():
    # creating list        
    list = []  
      
    # appending instances to list  
    list.append( Student('Akash') ) 
    list.append( Student('Deependra') ) 
    list.append( Student('Reaper') ) 
      
    for obj in list: 
        print( obj.getName() ) 
      
    for number in range(len(list)):
        print(list[number].getName())


main()
