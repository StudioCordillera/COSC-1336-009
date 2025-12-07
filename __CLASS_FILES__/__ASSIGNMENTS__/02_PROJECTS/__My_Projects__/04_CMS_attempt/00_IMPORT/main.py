
from Registry import BaseRegisteredClass
from Registry import RegisteredEmployee
from EmployeeClass import Employee

def main():
    
    EmpClass = BaseRegisteredClass.REGISTRY['RegisteredEmployee']
    e1= EmpClass()

    e2= EmpClass()
    e2.setVars('Howards')
    
    
    print(e1)

main()










