###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Patient Account Class                             |
|_____________________________________________________________|
|                                                             |
|   - PatientAccount Class                                    |
|        - Manages patient billing (Name, Stay, Charges)      |
|        - Handles menu-driven data entry                     |
|        - Displays billing summary                           |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__all__ = ['PatientAccount']

import sys
import os
# Add parent directory to path if running from Hospital folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
from Hospital.hospitalModules import Surgery, Pharmacy
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph
Project10=displayLabels.Context(10, '12/08/2025', 'HospitalCalc', 'Patient Fee Calculations')
START=Project10.START
v=V=typeValidation.validateInput

class PatientAccount:

    def __init__(self):

        self.patientName:str = ''
        self.daysInHospital:int = 0
        self.dailyFees:int = 0
        self.procedure:str = ''
        self.medicine:str = ''
        self.procedureCost:int = 0
        self.medicineCost:int = 0
        self.totalCharges:float = 0.0

        self.Start()
        self.MainMenu()
        self.printSummary()


    def Start(self):
        print(f"{nL+tab}Press Enter to begin...")
        input()

        while True:
            userInput = v(str, f"{tab}Are you ready to enter Patient Information? (Y/N) ").upper().strip()
            if userInput == 'Y' or userInput == 'YES':
                break
            elif userInput == 'N' or userInput == 'NO':
                print(f"{tab}Take your time...")
            else:
                print(f"{tab}Not an option! Please enter Y or N")


    def MainMenu(self):
        
        self.patientName = v(str, f"{nL+tab}Name of Patient: ").strip().title()

        RED = '\033[91m'
        GREEN = '\033[92m'
        RESET = '\033[0m'

        OPTIONS = {
            'L': {'PROMPT': 'Enter length of stay', 'COMPLETED': False},
            'S': {'PROMPT': 'Enter surgery menu', 'COMPLETED': False},
            'P': {'PROMPT': 'Enter pharmacy menu', 'COMPLETED': False}
        }
        
        while True:
            all_completed = all(opt['COMPLETED'] for opt in OPTIONS.values())
            
            print(f"{nL+tab+medBar}")
            print(f"{tab}Hospital Patient Check-out")
            print(f"{tab+medBar}")
            
            for key in OPTIONS:
                color = GREEN if OPTIONS[key]['COMPLETED'] else RED
                print(f"{tab}{color}{key} ..... {OPTIONS[key]['PROMPT']}{RESET}")
            
            x_color = GREEN if all_completed else RED
            print(f"{tab}{x_color}X ..... exit program and view bill summary{RESET}")
            print(f"{tab+medBar}")

            userInput = v(str, f"{nL+tab}Enter your selection: ").strip().upper()

            if userInput not in ['L', 'S', 'P', 'X']:
                print(f"{tab}NOT AN OPTION!")
                continue
                
            if userInput == 'X':
                if not all_completed:
                    print(f"{tab}{RED}Please complete all options first (L, S, P)...{RESET}")
                else:
                    self.totalCharges = self.dailyFees + self.procedureCost + self.medicineCost
                    break
                    
            elif userInput == 'L':
                if OPTIONS['L']['COMPLETED']:
                    print(f"{tab}{RED}Length of stay already entered!{RESET}")
                else:
                    self.stayLengthMenu()
                    OPTIONS['L']['COMPLETED'] = True
                
            elif userInput == 'S':
                if OPTIONS['S']['COMPLETED']:
                    print(f"{tab}{RED}Surgery already selected!{RESET}")
                else:
                    self.procedure, self.procedureCost = Surgery()
                    print(f"{tab}Surgery selected: {self.procedure} - ${self.procedureCost}")
                    OPTIONS['S']['COMPLETED'] = True
                
            elif userInput == 'P':
                if OPTIONS['P']['COMPLETED']:
                    print(f"{tab}{RED}Pharmacy already selected!{RESET}")
                else:
                    self.medicine, self.medicineCost = Pharmacy()
                    print(f"{tab}Medicine selected: {self.medicine} - ${self.medicineCost}")
                    OPTIONS['P']['COMPLETED'] = True


    def stayLengthMenu(self):
        while True:
            stayLength = v(int, f"{tab}Enter number of days stayed: ")
            if stayLength <= 0:
                print(f"{tab}Days must be greater than 0!")
            else:
                self.daysInHospital = stayLength
                self.dailyFees = stayLength * 1000
                print(f"{tab}Added {stayLength} days (@ $1000/day) = ${self.dailyFees}")
                break


    def printSummary(self):
        print(f"{nL+dashGraph}")
        print(f"BILLING SUMMARY")
        print(f"{dashGraph+nL}")
        print(f"Patient Name:{tab+tab+tab+tab+tab}{self.patientName}")
        print(f"{shortBar}")
        print(f"Hospital Stay:{tab+tab+tab+tab}{self.daysInHospital} days @ $1000/day")
        print(f"Daily Charges:{tab+tab+tab+tab}${self.dailyFees:.2f}")
        print(f"{shortBar}")
        print(f"Surgery:{tab+tab+tab+tab+tab+tab}{self.procedure}")
        print(f"Surgery Cost:{tab+tab+tab+tab}${self.procedureCost:.2f}")
        print(f"{shortBar}")
        print(f"Medication:{tab+tab+tab+tab+tab}{self.medicine}")
        print(f"Medication Cost:{tab+tab+tab}${self.medicineCost:.2f}")
        print(f"{shortBar}")
        print(f"TOTAL CHARGES:{tab+tab+tab+tab}${self.totalCharges:.2f}")
        print(f"{dashGraph}")


    # Getter methods for compatibility
    def getName(self):
        return self.patientName
    
    def getDailyFees(self):
        return self.dailyFees, self.daysInHospital
    
    def getProcedure(self):
        return self.procedure, self.procedureCost
    
    def getMedicine(self):
        return self.medicine, self.medicineCost
    
    def getTotalCharges(self):
        return self.totalCharges
