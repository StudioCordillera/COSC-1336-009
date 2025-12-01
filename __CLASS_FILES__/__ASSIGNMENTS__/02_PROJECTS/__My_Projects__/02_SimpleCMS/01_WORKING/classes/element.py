## Element Class
from dataclasses import dataclass

@dataclass
class Employee:

    name = str




def main():

    e1 = Employee()
    e1.name = 'Bob'

    print(e1.__dict__)
    
    for k, v in e1.__dict__.items():
        print(k)
        print(v)

#main()