###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 10, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Vehicles Class                                    |
|_____________________________________________________________|
|                                                             |
|   - Car Class                                               |
|        - Manages car state (Year, Make, Speed)              |
|        - Handles driving simulation (Accelerate, Brake)     |
|   - CarMenu Class                                           |
|        - Loads car data from file                           |
|        - Provides selection menu                            |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__all__ = ['Car']

import sys
import os
# Add parent directory to path if running from ProjectClasses folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar
Project9=displayLabels.Context(9, '12/08/2025','VROOM', 'Drive a Chosen Car!')
START=Project9.START
v=V=typeValidation.validateInput

class Car:

    def __init__(self, year:int = 1000, make:str = 'make', speed:int = 0):

        self.year = year
        self.make = make
        self.speed = speed

        GetCar=CarMenu()
        self.car=GetCar.Start()
        # car = [2024, 'Honda', 'Civic Type R']
        self.Constructor(self.car)
        self.Driving(self.make, self.year, self.speed)


    def Constructor(self, car):
        self.year= car[0]
        self.make= f"{car[1]}, {car[2]}"
        return self.year, self.make
    
        
    def printCarInfo(self, make, year):
        os.system('cls')
        START()
        print(f"{tab+tab}My Car Information{nL+tab+tab+medBar}")
        print(f"{tab+tab}Car Make: {make}")
        print(f"{tab+tab}Car Year: {year}")


    def Driving(self, year, make, speed):

        # | 'nL' | 'tab' | 'tab1' | 'longBar' | 'medBar' |
        # | 'shortBar' | 'dashGraph' | 'lineGraph'
        
        self.printCarInfo(year, make)

        while True:
            accelerated:int = v(int,f"{nL+tab+tab}How many times did you accelerate? ")
            if accelerated <0:
                os.system('cls')
                print('\tCan you do that in real life???')
                input()
                os.system('cls')
                START()
                self.printCarInfo(year, make)
            elif accelerated == 0:
                os.system('cls')
                print('\tYOU JUST WANT TO SIT STILL??')
                input()
                os.system('cls')
                START()
                self.printCarInfo(year, make)
                print(f"{tab+tab}How many times did you accelerate? {accelerated}")  
            elif accelerated >0:
                break


        while True:
            braked:int = v(int, f"{tab+tab}How many times did you brake? ")
            if braked <0:
                os.system('cls')
                print('\tYou can\'t break less than 1 times man...')
                input()
                os.system('cls')
                START()
                self.printCarInfo(year, make)
                print(f"{tab+tab}How many times did you accelerate? {accelerated}")
            elif braked > accelerated:
                os.system('cls')
                print(f"\tYou can\'t break less than the times you accelerated: {accelerated}.")
                input()
                os.system('cls')
                START()
                self.printCarInfo(year, make)
                print(f"{tab+tab}How many times did you accelerate? {accelerated}")  
            elif braked >=0:
                break

        print(f"{tab+tab+lineGraph+nL+nL+tab+tab1}Car Travel Information{nL+tab+tab+lineGraph}")
        print(f"{tab+tab}Acceleration applied:{nL+tab+tab+shortBar}")

        for count in range(accelerated):
            speed=self.Accelerator(speed)
            print(f"{tab+tab1}Accelerate #{count+1}:{tab}Increase by 5 mph{tab}Current speed: {speed}mpg")

        print(f"{nL+tab+tab}Brake Appled{nL+tab+tab+shortBar}")

        for count in range(braked):
            speed=self.Brake(speed)
            print(f"{tab+tab1}Brake #{count+1}:{tab}Decrease by 5 mph{tab}Current speed: {speed}mpg")

        print(f"{tab+tab+lineGraph+nL+tab+tab}Chevy Final Speed:{tab}{speed}mpg")

    def Accelerator(self, speed):
        self.speed = speed + 5
        return self.speed
    
    def Brake(self, speed):
        if speed <5 or speed == 0:
            speed = 0
        else:
            self.speed = speed - 5
        return self.speed



class CarMenu():


    def __init__(self):

        self.carMakeYear:list
        self.choices:list
        self.choice:int


    def set_carMakeYear(self, carMakeYear):
        self.carMakeYear = carMakeYear
    def get_carMakeYear(self):
        return self.carMakeYear
    
    def set_choices(self, choices):
        self.choices = choices
    def get_choices(self):
        return self.choices
    def set_choice(self, choice):
        self.choice = choice
    def get_choice(self):
        return self.choice
    


    def Start(self):

        carMakeYear = []
        choices = {}

        with open('data.txt', 'r') as file:
            carList:dict = (eval(str(file.read())))

        for car in carList:
            carMakeYear.append([carList[car]['year'], carList[car]['make'], car])
        carMakeYear.sort()

        for index, car in enumerate(carMakeYear, start=1):
            choices[index] = car

        self.set_choices(choices)
        return self.Provide()
        
    def Provide(self):

        choices = self.get_choices()

        while True:
            
            print('\n\tPlease choose an option:\n')

            for num in choices:
                year = choices[num][0]
                make = choices[num][1]
                model = choices[num][2]
                print(f"\t{num}) {year} {make}: {model}")


            try:
                choice = int(input('\n\tEnter the number associated: '))
            except ValueError:
                os.system('cls')
                print('\tPlease only enter numbers for a choice', flush=True)
                input('\n\tPress Enter to continue...')
                os.system('cls')
                continue
            
            if choice not in choices:
                os.system('cls')
                print('\tNot an option', flush=True)
                input('\n\tPress Enter to continue...')
                os.system('cls')
                continue
            
            year = choices[choice][0]
            make = choices[choice][1]
            model = choices[choice][2]
            os.system('cls')
            print(f"\n\tYou chose: {year} {make} {model}", flush=True)
            input('\n\tPress Enter to continue...')
            self.set_choice(choice)
            return choices[choice]
    









