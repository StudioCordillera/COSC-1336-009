###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 10, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
from MyClasses import displayLabels
from ProjectClasses import vehiclesClass
Project9=displayLabels.Context(9, '12/08/2025','VROOM', 'Drive a Chosen Car!')
END, START = Project9.END, Project9.START
Car=vehiclesClass.Car
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - Car Selection                                            |
|        - Load cars from data.txt                            |
|        - User selects a car from menu                       |
|    - Simulation                                             |
|        - User inputs acceleration count                     |
|        - User inputs brake count                            |
|        - Display speed changes (+5 mph / -5 mph)            |
|    - Display                                                |
|        - Car Information (Year, Make, Model)                |
|        - Acceleration Log                                   |
|        - Braking Log                                        |
|        - Final Speed                                        |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - main()               | Orchestrates                |
|                                                             |
|    IMPORTED                                                 |
|        - vehiclesClass        | Car & CarMenu Classes       |
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

    # Initialize Car
    Vroom=Car()

    # Calls function to display the start of project
    END()
      
main() # calling the function main()

1
