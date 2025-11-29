# Ally Baba
# October 29, 2025
# Classwork #27
# ----------------------------
# Project Objectives
# --------------------------------

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By King AllyBaba")
    print("\tLearning Functions")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get the user's entry for a float
def getFloatData(prompt):
    value = float(input(prompt))

    return value

# This fucntion will get the user's entry for an integer
def getIntegerData(prompt):
    value = int(input(prompt))

    return value

# This function will get the user's entry of string
def getStringData(prompt):
    value = input(prompt)

    return value

# This function will display the summary
def displaySummary(studentName):
    print('\n')
    print('\tGrade Summary')
    print('-' * 60)
    print('\tStudent name: ', studentName)

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    studentName = getStringData('\tEnter the name of the student: ')
    examOne = getFloatData('\tEnter the grade for Exam 1: ')
    examTwo = getFloatData('\tEnter the grade for Exam 2: ')
    examThree = getFloatData('\tEnter the grade for Exam 3: ')
    examFour = getFloatData('\tEnter the grade for Exam 4: ')
    
    # Multiplying hours worked
    averageGrade = (examOne + examTwo + examThree + examFour) / 4
    
    # display summary
    displaySummary(studentName)

    
    # Display end of project
    projectEnd()

   
main()

# Trace: 2
