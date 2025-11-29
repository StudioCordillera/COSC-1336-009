class Counter:
   __Count = 0
  
   def getCount(self):
      return self.__Count

   def setCount(self, value):
       self.__Count = value

counter = Counter()
counter.setCount(5)
print (counter.getCount())
