###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   October 29, 2025    |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  PROJECT 01 | 4-Exam Grade Average Calculator              |
|_____________________________________________________________|
|                                                             |
|  INPUT:                                                     |
|    - Exam 1 grade (float)                                   |
|    - Exam 2 grade (float)                                   |
|    - Exam 3 grade (float)                                   |
|    - Exam 4 grade (float)                                   |
|_____________________________________________________________|
|                                                             |
|  PROCESSING:                                                |
|    - Calculate average of 4 exam grades                     |
|    - Format average to 2 decimal places                     |
|_____________________________________________________________|
|                                                             |
|  OUTPUT:                                                    |
|    - Display individual exam grades                         |
|    - Display calculated average                             |
|_____________________________________________________________|
|                                                             |
|  FUNCTIONS                                                  |
|_____________________________________________________________|
|                                                             |
|    REQUIRED:                                                |
|        - getFloat(prompt)     | Get float input from user   |
|        - getCalcAvg()         | Calculate 4-exam average    |
|        - displaySummary()     | Print formatted results     |
|        - main()               | ORCHESTRATES                |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
###############################################################
##                      START - MY CODE                      ##
###############################################################

#   SOPB
#  ------------------------------------------------------------------------
def projectStart():
    print(' ' * 4, '-'* 80)
    print(' ' * 4, 'Start of Project 1')
    print(' ' * 5, 'Written by: Matthew Ochoa')
    print(' ' * 5,'Date: October 29, 2025')
    print(' ' * 4,'-' * 80)
    print('\t  4-Exam Grade Average Calculator')
    print(' ' * 4,'-' * 80, '\n')

#   EOPB
#  ------------------------------------------------------------------------
def projectEnd():
    print('\n', ' ' * 4,'-' * 80)
    print(' ' * 5, 'End of Project 1')
    print(' ' * 4,'-' * 80)

#   Get Float Input
#  ------------------------------------------------------------------------
def getFloat(prompt):
    value=float(input(prompt))  # Get user input as float
    return value                # Return validated value >

#   Calculate Average
#  ------------------------------------------------------------------------
def getCalcAvg(exam1, exam2, exam3, exam4):
    average=(exam1 + exam2 + exam3 + exam4) / 4  # Sum all exams / 4
    return average                                # Return calculated avg >

#   Display Summary
#  ------------------------------------------------------------------------
def displaySummary(exam1, exam2, exam3, exam4, examAverage):
    print('\n' + '-' * 30)
    print('\n\tSummary of Exam Grades')
    print('\t' + '-' * 30)
    print('\t  Exam 1: ', exam1)           # Display exam 1
    print('\t  Exam 2: ', exam2)           # Display exam 2
    print('\t  Exam 3: ', exam3)           # Display exam 3
    print('\t  Exam 4: ', exam4)           # Display exam 4
    print('\t' + '-' * 30)
    print('\tExam Average: ', examAverage)  # Display calculated average
    print('\t' + '-' * 30)

###############################################################
##    MAIN FUNCTION                                          ##
###############################################################
def main(): 
    # SOPB
    projectStart()

    # Get grades from user | Input collection
    exam1=getFloat('\tEnter your Exam 1 grade: ')
    exam2=getFloat('\tEnter your Exam 2 grade: ')
    exam3=getFloat('\tEnter your Exam 3 grade: ')
    exam4=getFloat('\tEnter your Exam 4 grade: ')

    # Calculate average | Process data
    examAverage = format(getCalcAvg(exam1, exam2, exam3, exam4), '.2f')
   
    # Display summary | Output results
    displaySummary(exam1, exam2, exam3, exam4, examAverage)
   
    # EOPB
    projectEnd()
      
main() #<= | Call Main