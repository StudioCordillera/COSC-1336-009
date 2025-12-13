###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   MODULE: Bank Transaction Manager                          |
|_____________________________________________________________|
|                                                             |
|   - BankAccount Class                                       |
|        - Processes withdrawals (checks) with $0.25 fee      |
|        - Processes deposits                                 |
|        - $40 overdraft charge for insufficient funds        |
|        - Tracks accrued service charges                     |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

__all__ = ['BankAccount']

import sys
import os
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels, typeValidation
from datetime import datetime
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph
v=V=typeValidation.validateInput

class BankAccount:

    def __init__(self):
        self.balance = 0.0
        self.serviceCharges = 0.0
        self.accountNumber = '123456'
        self.date = datetime.now().strftime('%m/%d/%Y')
        
        self.setupAccount()
        self.runTransactions()
        self.displaySummary()


    def setupAccount(self):
        print(f"AllyBaba Transaction Statement")
        print(lineGraph)
        print(f"Today's Date: {self.date}")
        print(f"Account Number: {self.accountNumber}")
        print()
        
        while True:
            self.balance = v(float, f"Enter the beginning balance: ")
            if self.balance >= 0:
                break
            print("Balance cannot be negative!")


    def showMenu(self):
        print(lineGraph)
        print("Transaction Menu")
        print(lineGraph)
        print("W     Process a check")
        print("D      Process a deposit")
        print("E      Exit")
        print(lineGraph)


    def runTransactions(self):
        while True:
            self.showMenu()
            
            choice = v(str, "Enter transaction type: ").strip().upper()
            
            if choice == 'W':
                self.processWithdrawal()
            elif choice == 'D':
                self.processDeposit()
            elif choice == 'E':
                print("Processing end of Transaction")
                break
            else:
                print("\t\tERROR Message: Wrong selection")


    def processWithdrawal(self):
        while True:
            amount = v(float, "Enter Check amount: ")
            if amount > 0:
                break
            print("Amount must be greater than zero!")
        
        print(f"Processing Check for ${amount:.2f}")
        print()
        
        # Check if withdrawal would cause overdraft
        if amount > self.balance:
            print(f"Cannot Process Check of ${amount:.2f}")
            print("Over Draft: Insufficient Balance")
            print(f"Current Balance: ${self.balance:.2f}")
            print()
            
            # Add overdraft charge ($40) + withdrawal fee ($0.25)
            self.serviceCharges += 40.25
            print(f"Service charge: $40.25 for writing a check")
            print(f"Accrued service charges: ${self.serviceCharges:.2f}")
        else:
            # Process the withdrawal
            self.balance -= amount
            print(f"Processed Check for ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")
            print()
            
            # Add withdrawal fee ($0.25)
            self.serviceCharges += 0.25
            print(f"Service charge: $.25 for writing a check")
            print(f"Accrued service charges: ${self.serviceCharges:.2f}")
        
        print()


    def processDeposit(self):
        while True:
            amount = v(float, "Enter transaction amount: ")
            if amount > 0:
                break
            print("Amount must be greater than zero!")
        
        print(f"Processing Deposit of ${amount:.2f}")
        print()
        
        self.balance += amount
        print(f"Processed Deposit of ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")
        print()
        print(f"Accrued service charges: ${self.serviceCharges:.2f}")
        print()


    def displaySummary(self):
        print()
        print(lineGraph)
        print("Summary: End of Daily Transaction")
        print(lineGraph)
        print(f"Today's Date: {self.date}")
        print(f"Account Number: {self.accountNumber}")
        print()
        print(f"Current Balance:{tab1*3}${self.balance:.2f}")
        print(f"Accrued service charges:{tab1*2}${self.serviceCharges:.2f}")
        
        finalBalance = self.balance - self.serviceCharges
        print(f"End of Transaction balance:{tab1*2}${finalBalance:.2f}")
