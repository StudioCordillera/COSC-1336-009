###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   November 26, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - reads                                                    |
|        - data.txt | (integer value list)                    |
|    - Lines contain single integer ( seperation by >\n< )    | 
|    - stores data in lines                                   |
|        - in list                                            |
|    - Calculate                                              |
|        - statistics                                         |
|    - print stats with summary                               |
|_____________________________________________________________|
|                                                             |
|   DISPLAY                                                   |
|_____________________________________________________________|
|                                                             |
|    REQUIRED:                                                |
|        Display following for list values:                   |
|            - average (place val = 0.00)                     |
|            - all numbers                                    |
|            - count                                          |
|            - sum                                            |
|            - maximum                                        |
|            - minimum                                        |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - readData()           | Extract Var < data.txt      |
|        - main()               | ORCHESTRATES                |
|                                                             |
|    OPTIONAL                                                 |
|        - storeVars():         | Store variables             |
|        - storeVars():         | Processng for vars          |
|        - displaySummary():    | Print summary               |
|                                                             |
|_____________________________________________________________|
|                                                             |
|   STATIC VARIABLES                                          |
|_____________________________________________________________|
|                      |                                      |
|      - dataLines     |   integer list FROM data.txt         |
|      - lineCount     |   elements count for dataLines       |
|      - lineVarSum    |   sum of the numbers in dataLines    |
|      - averageLines  |   avg values in dataLines            |
|      - maxNum        |   Maximum value in dataLines         |
|      - minNum        |   Minimum value in dataLines         |
|                                                             |
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
###############################################################
##                    PROVIDED FUNCTIONS                     ##
###############################################################
import os
from dataclasses import dataclass
import Bank_Class 
from Utils_Class import Utils

# TODO  add string validation in utils class

###############################################################
##                      START - MY CODE                      ##
###############################################################        

def main():
    # Display start of project
    projectStart()

    # Get Bank instance as b1
    b1 = Bank(1000)

    b1.set_name('b1')

    print(displayBalance(b1))

    print(b1.__dict__)

    
    # Display end of project
    projectEnd()
   
main()


'''

manage one-time bank transactions customer AllyBaba


INPUT 
    - initial account balance   
    - process
        - series of financial transactions
    - keep track of
        - deposits
        - withdrawals
        - applicable service charges. 

Functionality Overview 
The program should: 
    1. Prompt the user to enter an initial balance. 
    2. Allow the user to enter a series of transactions, one time. 

        Valid Transaction Types 
            Code Description 
                - W Withdraw Money 
                - D Deposit Checks 
                - E End Transaction
                    - deduct the total

        Service Charges 
            - $0.25 service charge for each withdrawal. 
            - $40 overdraft charge if a withdrawal exceeds the current balance. 
            - Withdrawals that would result in a negative balance are not processed. 
            - Service and overdraft charges are accumulated and deducted at the end of the session, not immediately. 

        Transaction Processing 
            After each transaction, display the following: 
                • The transaction command and amount 
                • The resulting account balance 
                • The total service charges accrued so far 

    3. Each transaction must include a transaction type, followed by a transaction amount (when applicable). 



service/overdraft charges from the balance and display: 
    - Final balance 
    - Total service charges 

Input Validation Requirements 
    - If the transaction type is invalid (i.e., not W, D, or E), display an informative error message, ignore the transaction, and prompt the user again. 
    - The transaction amount must be a positive number greater than zero. If not, display an error and prompt again. 
    - The program should not allow overdraft withdrawals—these should be rejected, and a message should be shown. 

Additional Requirements 
    - Use functions to structure your program logic (e.g., getTransaction(), processTransaction(), displaySummary()). 
    - No global variables: all variables should be passed as parameters or returned by functions. 
    - All monetary values must be displayed with 2 decimal places


'''







