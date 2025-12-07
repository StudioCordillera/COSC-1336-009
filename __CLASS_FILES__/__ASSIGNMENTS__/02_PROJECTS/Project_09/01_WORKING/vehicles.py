import ast

class Car:

    def __init__(self, name, make, year, speed):

        self.name = name
        self.make = make
        self.year = year
        self.speed = speed

    def Accelerator(self, speed):
        self.speed = 5 + speed
        return speed
    
    def Brake(self, speed):
        self.speed = 5 - speed
        return speed



def main():

    carList = []

    with open('data.txt', 'r') as file:
        cars:dict=(eval(file.read()))
        # print(cars)
        
        for item in cars:
            carList.append(cars[item])


    for car in range(len(carList)):
        obj = carList[car]['type']
        name = carList[car]['type']
        year = carList[car]['year']
        make = carList[car]['make']
        speed = carList[car]['speed']

        obj = Car(name, make, year, speed)

        print(obj.name)
        
    

            
            
            
                
            

main()




