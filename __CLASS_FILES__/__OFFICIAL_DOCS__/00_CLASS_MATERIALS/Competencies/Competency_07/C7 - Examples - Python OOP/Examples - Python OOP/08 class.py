class MyClass:
     
    def __init__(self):
        self.attribute = 0 
     
    def MyMethod(self):
        self.attribute += 1 #Modifies object's attribute by +1.
     
MyObject1 = MyClass()
MyObject2 = MyClass()
print(MyObject1.attribute)
print(MyObject2.attribute)

MyObject2.MyMethod()
print(MyObject2.attribute)

MyObject2.MyMethod()
print(MyObject2.attribute)
print(MyObject1.attribute)

MyObject3 = MyClass()
print(MyObject3.attribute)

MyObject4 = MyObject2
print(MyObject4.attribute)


