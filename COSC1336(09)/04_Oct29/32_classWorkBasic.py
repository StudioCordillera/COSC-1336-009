########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Classwork N. 32                 #####
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
def displaySummary(studentName, averageGrade):
    print('\n')
    print('\tGrade Summary')
    print('-' *60)
    print('\tStudent name: ', studentName)
    print('\tStudent Exam Average: ', averageGrade)
    

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
    displaySummary(studentName, averageGrade)


    # Display end of project
    projectEnd()



          
main()

# Trace: 2
