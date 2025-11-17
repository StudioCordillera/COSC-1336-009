class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount = Employee.empCount + 1
   
   def displayCount(self):
     print ("Total Employee", Employee.empCount)

   def setName(self, value):
      self.name = value

   def setSalary(self, value):
      self.salary = value

def main():
   employee1 = Employee("AllyBaba", 34)
   employee2 = Employee("HollyBaba", 39)
   employee3 = Employee("HHllyBaba", 34)

   employee1.displayCount()
            
   

main()
            
