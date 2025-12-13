###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
from MyClasses import displayLabels
from Hospital import patientsClass
Project10=displayLabels.Context(10, '12/08/2025', 'HospitalCalc', 'Patient Fee Calculations')
END, START = Project10.END, Project10.START
PatientAccount=patientsClass.PatientAccount
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - Patient Account Management                               |
|        - Enter patient name                                 |
|        - Track length of hospital stay ($1000/day)          |
|        - Select surgery from menu                           |
|        - Select pharmacy items from menu                    |
|    - Display Billing Summary                                |
|        - Patient name                                       |
|        - Days stayed and daily charges                      |
|        - Surgery performed and cost                         |
|        - Medications and cost                               |
|        - Total charges                                      |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - main()               | Orchestrates                |
|                                                             |
|    IMPORTED                                                 |
|        - patientsClass        | PatientAccount Class        |
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

    # Initialize Patient Account
    Account=PatientAccount()

    # Calls function to display the end of project
    END()
      
main() # calling the function main()
