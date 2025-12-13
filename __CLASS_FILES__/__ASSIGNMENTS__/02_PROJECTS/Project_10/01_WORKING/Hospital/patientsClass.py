###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Patient Account Management                        |
|_____________________________________________________________|
|                                                             |
|   - PatientAccount Class                                    |
|        - Manages patient billing for hospital stay          |
|        - Tracks: Length of stay ($1000/day)                 |
|        - Tracks: Surgery charges from file                  |
|        - Tracks: Pharmacy charges from file                 |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__all__ = ['PatientAccount']

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph
v=V=typeValidation.validateInput

class PatientAccount:

    def __init__(self):
        self.patientName = ''
        self.daysInHospital = 0
        self.totalCharges = 0.0
        self.hospitalStayCharges = 0.0
        self.surgeryCharges = 0.0
        self.pharmacyCharges = 0.0
        
        # Load surgery and pharmacy data from files
        self.surgeryData = self.loadFile('surgery.txt')
        self.pharmacyData = self.loadFile('medicine.txt')
        
        self.setupPatient()
        self.runMenu()
        self.displayBill()


    def loadFile(self, filename):
        """Load surgery or pharmacy data from file"""
        data = []
        try:
            # Try relative path from Hospital folder
            filepath = os.path.join(os.path.dirname(__file__), '..', '00_IMPORT', filename)
            with open(filepath, 'r') as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split(',')
                        data.append(parts)
        except FileNotFoundError:
            print(f"Warning: Could not find {filename}")
        return data


    def setupPatient(self):
        print(f"{nL}This program computes the total charges for a hospital stay.  Users can select")
        print("medicines and surgeries and days sent in the hospital.")
        print(lineGraph)
        print("Welcome to AllyBaba Patient Management System")
        print(lineGraph)
        print()
        
        ready = v(str, "Are you ready to enter Patient Information? (Y/N) ").strip().upper()
        
        if ready == 'Y':
            print()
            print(lineGraph)
            print("Hospital Patient Check-out")
            print()
            self.patientName = v(str, "Name of Patient: ").strip()


    def showMenu(self):
        print()
        print(lineGraph)
        print("Hospital Patient Check-out")
        print(lineGraph)
        print("L ..... enter length of stay")
        print("S ..... enter surgery menu")
        print("P ..... enter pharmacy menu")
        print("X ..... exit program and view bill summary")
        print(lineGraph)


    def runMenu(self):
        while True:
            self.showMenu()
            
            choice = v(str, f"{nL}Enter your selection: ").strip().upper()
            
            if choice == 'L':
                self.enterLengthOfStay()
            elif choice == 'S':
                self.enterSurgery()
            elif choice == 'P':
                self.enterPharmacy()
            elif choice == 'X':
                break
            else:
                print("Invalid selection!")


    def enterLengthOfStay(self):
        while True:
            days = v(int, "Enter the length of stay: ")
            if days > 0:
                break
            print("Must enter a positive number of days!")
        
        self.daysInHospital = days
        charge = days * 1000
        self.hospitalStayCharges = charge
        self.totalCharges += charge
        
        print(f"Adding  {days} days (at $1,000/day to patient bill)")
        print(f"Total amount for Hospital Stay: ${self.hospitalStayCharges}")


    def enterSurgery(self):
        print()
        print(dashGraph[:64])
        print("Surgery Menu")
        print(dashGraph[:64])
        
        for idx, surgery in enumerate(self.surgeryData, start=1):
            print(f"{idx:<5} {surgery}")
        
        print(lineGraph)
        print()
        
        while True:
            choice = v(int, "Enter a surgery: ")
            if 1 <= choice <= len(self.surgeryData):
                break
            print(f"Invalid choice! Select 1-{len(self.surgeryData)}")
        
        selected = self.surgeryData[choice - 1]
        cost = float(selected[1].strip())
        
        self.surgeryCharges += cost
        self.totalCharges += cost
        
        print(f"Adding  {selected} to patient bill.")
        print(f"Surgery Bill: ${int(self.surgeryCharges)}")


    def enterPharmacy(self):
        print(dashGraph[:64])
        print("Pharmacy Menu")
        print(dashGraph[:64])
        
        for idx, medicine in enumerate(self.pharmacyData, start=1):
            print(f"{idx:<5} {medicine}")
        
        print(lineGraph)
        print()
        
        while True:
            choice = v(int, "Enter a medicine: ")
            if 1 <= choice <= len(self.pharmacyData):
                break
            print(f"Invalid choice! Select 1-{len(self.pharmacyData)}")
        
        selected = self.pharmacyData[choice - 1]
        cost = float(selected[1].strip())
        
        self.pharmacyCharges += cost
        self.totalCharges += cost
        
        print(f"Adding  {selected} to patient bill.")
        print(f"Medicine Bill: ${int(self.pharmacyCharges)}")


    def displayBill(self):
        print()
        print(dashGraph[:64])
        print("Summary: Patient Bill")
        print(dashGraph[:64])
        print(f"Name: {self.patientName}")
        print(f"Total Bill: owes: ${self.totalCharges:,.2f}")
        print(dashGraph[:64])
        print()
        
        another = v(str, "Do you like to process another Patient? (Y/N) ").strip().upper()
