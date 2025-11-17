
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, address, city, state, zips, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     return Employee.empCount

   def displayEmployee(self):
      print ('Name : ', self.name,  ', Salary: ', self.salary)


'This would create first object of Employee class'
emp1 = Employee('Zara','123 Woodward','Austin', 'TX',78748, 2000)
'This would create second object of Employee class'
emp2 = Employee('Manni','123 Woodward','Austin', 'TX',78748, 5000)
emp3 = Employee('Manni','123 Woodward','Austin', 'TX',78748, 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print( 'Total Employee', emp2.displayCount())
