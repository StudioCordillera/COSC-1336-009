class tutorials :
    name = 'Classes in Python'
    difficulty= 'easy'
    
    def yourname(self,names):
        self.name = names
        
    def hello(self):
        print('Hello ',self.name,' ****')
        
#### Function call ####
obj1 = tutorials()	# objt1 is an object of Class tutorials
obj2 = tutorials()	# same here

obj1.yourname('Oscar')	
obj2.yourname('kim')# same here

obj1.hello()

obj2.hello()

