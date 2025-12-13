###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
from MyClasses import displayLabels
from ProjectClasses import bankClass
ExamTwo=displayLabels.Context(2, '12/12/2025','AllyBaba Bank', 'Account Management System')
END, START = ExamTwo.END, ExamTwo.START
BankAccount=bankClass.BankAccount
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - Bank Account Management                                  |
|        - Create account with starting balance               |
|        - Deposit funds                                      |
|        - Withdraw funds                                     |
|        - Check balance                                      |
|        - View transaction history                           |
|    - Display                                                |
|        - Account holder name                                |
|        - Current balance                                    |
|        - Transaction log                                    |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - main()               | Orchestrates                |
|                                                             |
|    IMPORTED                                                 |
|        - bankClass            | BankAccount Class           |
|        - displayLabels        | UI Banners                  |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    # Calls function to display the start of project
    START()

    # Initialize Bank Account
    Account=BankAccount()

    # Calls function to display the end of project
    END()
      
main() # calling the function main()
