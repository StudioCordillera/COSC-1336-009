## Element Collection Class
import os
from dataclasses import dataclass
from element import Employee

@dataclass
class Collection:

    Employee = Employee()
    state = {}
    stateFile = './state.txt'

    def updateEntry(self):
        self.state[self.Employee.name]=self.Employee.__dict__
        

    def set_employee_name(self, name):
        print(name)
        self.Employee.name = name
        self.updateEntry()

    def saveState(self):
        with open('./state.txt', 'w') as file:
            for key, value in self.state.items():
                file.write(f"{key}:{value}\n")



def main():

    
    c1.set_employee_name('Dave')
    print(c1.Employee.__dict__)

    c1.saveState()


#main()