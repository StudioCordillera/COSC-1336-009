########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 33                 #####
## --------------------------------#####
## Project Objectives              #####
##   Learning the basics of Python #####
########################################

# This function will display the start of project
def projectStart():
    print("-" * 60)
    print("\tStart of Project")
    print("\tWritten By Matthew Ochoa")
    print("\tLearning Functions")
    print("-" * 60)

# This fucntion will display the end of project
def projectEnd():
    print('\n')
    print('-' * 60)
    print('\tEnd of project')

# This function will get user entry for an integer
def getIntData(prompt):
        value = int(input(prompt))

        # Send to main Integer data
        return value

# This function gets user entry for float
def getFloatData(prompt):
        value = float(input(prompt))

        # Send to main float value
        return value

# This function gets user string input
def getStringData(prompt):
        value = input(prompt)

        # Send to main string value
        return value

# This function Displays a summary of the average grades and student name
def displaySummary(studentName, examOne, examTwo, examThree, examFour, averageGrade):
    print('\n')
    print('\tGrade Summary')
    print('-' *60)
    print('\tStudent name: ', studentName)
    print('\tExam 1: ', format(examOne, '.2f'))
    print('\tExam 2: ', format(examTwo, '.2f'))
    print('\tExam 3: ', format(examThree, '.2f'))
    print('\tExam 4: ', format(examFour, '.2f'))
    print('\tStudent Exam Average: ', format(averageGrade, '.2f'))
    

def main():
    # Display start of project
    projectStart()

    # Assign variable
    print('\tUser entry')
    studentName = getStringData('\tEnter name of student: ')
    examOne = getFloatData('\tEnter the grade for Exam 1: ')
    examTwo = getFloatData('\tEnter the grade for Exam 2: ')
    examThree = getFloatData('\tEnter the grade for Exam 3: ')
    examFour = getFloatData('\tEnter the grade for Exam 4: ')
    
    
    # Average Grades
    averageGrade = (examOne + examTwo + examThree + examFour) / 4


    # Call Summary
    displaySummary(studentName, examOne, examTwo, examThree, examFour, averageGrade)


    # Display end of project
    projectEnd()



          
main()

# Trace: 2
