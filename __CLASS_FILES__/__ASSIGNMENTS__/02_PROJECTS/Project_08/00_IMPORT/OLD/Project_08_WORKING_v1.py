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
|  - prompt                                                   |
|        - initiial account balance                           |
|                                                             |
|  - Keep track of transactions                               | 
|    - valid transactions:                                    |
|        - Withdraw, Deposit, End Transaction                 |
|        - Deposit                                            |
|        - End Transaction | Deduct the Total                 |
|    - Service Charges & Policy                               |
|        - $0.25 per withdraw                                 |
|        - $40 overdraft charge | Purchase > balance          |
|        - Withdraws > balance  | refused                     |
|        - Service & Overdraft deducted @ end of session      |
|                                                             |
|  - Display | Transaction Processing                         |
|        - After every Transaction, Display:                  |
|            - Transaction Code & $ Amount                    |
|            - Ending account balance                         |
|            - Total accrued service charges                  |
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


from collections import ChainMap
import time
from typeValidation import ValidateUI
from Utils_Class import projectEnd, projectStart
V = ValidateUI.validateInput

dataPath = ('data.txt')
    


# TODO  add string validation in utils class


###############################################################
##                      START - MY CODE                      ##
###############################################################        


    with open(dataPath, 'r') as file:
        for line, row in enumerate(file):
            row = row.strip().strip('\n').split(', ')


def main():

    # Display start of project
    projectStart()


    firstRun()

 

    
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
                - P Purchases 
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










