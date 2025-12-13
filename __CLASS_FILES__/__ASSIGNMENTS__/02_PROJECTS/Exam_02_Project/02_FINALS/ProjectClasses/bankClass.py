###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Bank Account Class                                |
|_____________________________________________________________|
|                                                             |
|   - BankAccount Class                                       |
|        - Manages account state (Name, Balance)              |
|        - Handles transactions (Deposit, Withdraw)           |
|        - Tracks transaction history                         |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__all__ = ['BankAccount']

import sys
import os
# Add parent directory to path if running from ProjectClasses folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph, longBar = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph, displayLabels.longBar
ExamTwo=displayLabels.Context(2, '12/12/2025','AllyBaba Bank', 'Account Management System')
START=ExamTwo.START
v=V=typeValidation.validateInput

class BankAccount:

    def __init__(self):

        self.balance:float = 0.0
        self.serviceCharges:float = 0.0
        self.accountNumber:str = "123456"
        self.date:str = "12/12/2025"

        self.setupAccount()
        self.runTransactions()
        self.printSummary()


    def setupAccount(self):
        print(f"{tab}AllyBaba Transaction Statement")
        print(f"{tab}{longBar}")
        print(f"{tab}Today's Date: {self.date}")
        print(f"{tab}Account Number: {self.accountNumber}")
        
        while True:
            self.balance = float(v(int, f"{nL+tab}Enter the beginning balance: "))
            if self.balance < 0:
                print(f"{tab}Balance cannot be negative!")
            else:
                break


    def runTransactions(self):
        while True:
            print(f"{tab}{longBar}")
            print(f"{tab}Transaction Menu")
            print(f"{tab}{longBar}")
            print(f"{tab}W     Process a check")
            print(f"{tab}D      Process a deposit")
            print(f"{tab}E      Exit")
            print(f"{tab}{longBar}")

            transactionType = v(str, f"{nL+tab}Enter transaction type: ").strip().upper()

            if transactionType not in ['W', 'D', 'E']:
                print(f"Invalid transaction type! Please enter W, D, or E")
                continue
                
            if transactionType == 'E':
                print(f"Processing end of Transaction")
                break
                    
            elif transactionType == 'W':
                self.processCheck()
                
            elif transactionType == 'D':
                self.processDeposit()


    def processCheck(self):
        while True:
            amount = float(v(int, f"Enter Check amount: "))
            if amount <= 0:
                print(f"Amount must be greater than $0!")
            else:
                break
        
        print(f"Processing Check for ${amount:.2f}{nL}")
        
        if amount > self.balance:
            print(f"Cannot Process Check of ${amount:.2f}")
            print(f"Over Draft: Insufficient Balance")
            print(f"Current Balance: ${self.balance:,.2f}{nL}")
            print(f"Service charge: $40.25 for writing a check")
            self.serviceCharges += 40.25
        else:
            self.balance -= amount
            print(f"Processed Check for ${amount:.2f}")
            print(f"Current Balance: ${self.balance:,.2f}{nL}")
            print(f"Service charge: $.25 for writing a check")
            self.serviceCharges += 0.25
        
        print(f"Accrued service charges: ${self.serviceCharges:.2f}")


    def processDeposit(self):
        while True:
            amount = float(v(int, f"Enter transaction amount: "))
            if amount <= 0:
                print(f"Amount must be greater than $0!")
            else:
                break
        
        print(f"Processing Deposit of ${amount:.2f}{nL}")
        self.balance += amount
        print(f"Processed Deposit of ${amount:.2f}")
        print(f"Current Balance: ${self.balance:,.2f}{nL}")
        print(f"Accrued service charges: ${self.serviceCharges:.2f}")


    def printSummary(self):
        finalBalance = self.balance - self.serviceCharges
        
        print(f"{nL+tab}{longBar}")
        print(f"{tab}Summary: End of Daily Transaction")
        print(f"{tab}{longBar}")
        print(f"{tab}Today's Date: {self.date}")
        print(f"{tab}Account Number: {self.accountNumber}{nL}")
        print(f"{tab}Current Balance:{tab+tab+tab}${self.balance:,.2f}")
        print(f"{tab}Accrued service charges:{tab+tab}${self.serviceCharges:.2f}")
        print(f"{tab}End of Transaction balance:{tab}${finalBalance:,.2f}")
