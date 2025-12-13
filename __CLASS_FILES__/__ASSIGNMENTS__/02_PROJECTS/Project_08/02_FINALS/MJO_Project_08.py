###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 10, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS                                              |
|_____________________________________________________________|
|                                                             |
|  - Reads                                                    |
|        - data.txt | (ID, Name pairs)                        |
|    - Stores data                                            |
|        - in Dictionary (ID -> Name)                         |
|    - Search                                                 |
|        - Query by Student ID                                |
|    - Display                                                |
|        - Student Name and ID if found                       |
|        - "Student not found" if missing                     |
|        - Total search count                                 |
|_____________________________________________________________|
|                                                             |
|   FUNCTIONS                                                 |
|_____________________________________________________________|
|                                                             |
|    REQUIRED                                                 |
|        - getFileData()        | Load Data                   |
|        - displayResult()      | Search & Display            |
|        - main()               | Orchestrates                |
|                                                             |
|    IMPORTED                                                 |
|        - ValidateUI           | Input Validation            |
|        - Labels               | UI Banners                  |
|                                                             |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
from re import X
from typeValidation import ValidateUI
from displayLabels import Labels
projectStart = Labels.projectStart
projectEnd = Labels.projectEnd
bannersTitle = Labels.bannersTitle
bannersQuery = Labels.bannersQuery
V=v=ValidateUI.validateInput


def getFileData():

    studentDirectory = {}
    lines = []

    with open('data.txt', 'r') as file:
        for line in file:
            lines.append(line.strip().split(', '))

    for x, y in lines: # x|IDs y|NAMES
        studentDirectory[x]=y

    return studentDirectory



def getStringData(type, prompt):
    return v(type, prompt)


def displayResult(directory):
    searches = 0
    while getStringData(bool, '\tAre you ready to search?'):
        searches=searches+1
        studentID=getStringData(str, '\tPlease enter a student ID: ')
        bannersQuery()
        if studentID in directory:
            print(f"\tStudent Found!\n\tName: {directory[studentID]}\n\tID:{studentID}")
        else:
            print('\tStudent not found')
    else:
        print(f'\tYou have searched {searches} times.')

def main(): 

    # Calls function to display the start of project
    projectStart()

    directory=getFileData()
    displayResult(directory)



    # Calls function to display the start of project
    projectEnd()
      
main() # calling the function main()



