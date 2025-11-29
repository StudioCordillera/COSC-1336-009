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
def displaySummary(studentName, examOne, examTwo, examThree, examFour, averageGrade):
    print('\n')
    print('\tGrade Summary')
    print('-' * 60)
    print('\tStudent name: ', studentName)
    print('\tExam 1: ', format(examOne, '.2f'))
    print('\tExam 2: ', format(examTwo, '.2f'))
    print('\tExam 3: ', format(examThree, '.2f'))
    print('\tExam 4: ', format(examFour, '.2f'))
    print('\tAverage: ', format(averageGrade, '.2f'))

# This function will calculate the average
def findAverage(examOne, examTwo, examThree, examFour):
    value = (examOne + examTwo + examThree + examFour) / 4

    return value

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
    averageGrade = findAverage(examOne, examTwo, examThree, examFour)
    
    # display summary
    displaySummary(studentName, examOne, examTwo, examThree, examFour, averageGrade)
    
    # Display end of project
    projectEnd()
   
main()

# Trace: 2
