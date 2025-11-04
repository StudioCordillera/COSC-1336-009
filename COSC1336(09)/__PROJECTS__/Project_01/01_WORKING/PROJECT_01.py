########################################
## Matthew Ochoa                   #####
## October 29, 2025                #####
## Project: 01                     #####
## Status: IN PROGRESS             #####
## Class: COSC 1336                #####
## --------------------------------#####
## Project 1 Objectives            #####
##   4-Exams grade average program #####
########################################

# Get float value from user given prompt
def getFloat(prompt):
    value=float(input(prompt))

    return value    


# Calc average for 4 exams
def getCalcAvg(exam1, exam2, exam3, exam4):
    average=(exam1 + exam2 + exam3 + exam4) / 4

    return average

# Display summary of all vars
def displaySummary(exam1, exam2, exam3, exam4, examAverage):

    print('\n' + '-' * 30)
    print('\n\tSummary of Exam Grades')
    print('\t' + '-' * 30)
    print('\t  Exam 1: ', exam1)
    print('\t  Exam 2: ', exam2)
    print('\t  Exam 3: ', exam3)
    print('\t  Exam 4: ', exam4)
    print('\t' + '-' * 30)
    print('\tExam Average: ', examAverage)
    print('\t' + '-' * 30)


def main(): 
    # Project start
    print('\n'+'-' * 30)
    print('\tStart of Project 1')
    print('\tBy: Matthew Ochoa')
    
    print('-' * 30 + '\n')

    # Get grades from user
    exam1=getFloat('\tEnter your Exam 1 grade: ')
    exam2=getFloat('\tEnter your Exam 2 grade: ')
    exam3=getFloat('\tEnter your Exam 3 grade: ')
    exam4=getFloat('\tEnter your Exam 4 grade: ')


    # Call get calculate Average
    examAverage = format(getCalcAvg(exam1, exam2, exam3, exam4), '.2f')
   
   
   # Call display summary
    displaySummary(exam1, exam2, exam3, exam4, examAverage)
   
    # project end
    print('\n' + '-' * 30)
    print('\n\tEnd of Project 1')
    print('\n' + '-' * 30)
      
main() # calling the function main()