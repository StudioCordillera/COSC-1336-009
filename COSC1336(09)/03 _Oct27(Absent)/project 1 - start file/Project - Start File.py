# ---------------------------------------------
# Name: Class of People
# Date: , 10/27/2025
# Project: Project 1
# Status: WIP
# Class: COSC 1336
# ---------------------------------------------
# Project Objectives
#   Calculates the average grade based on four exams
#   average = exams 1-4 added, / 4
# ---------------------------------------------

def main(): 
    # Project start
    print('Start of Project 1')
    print('-' * 30 + '\n')

    # User Entry
    name = input("\tGimme your name: ")
    examOne = float(input("\tEnter Exam 1 score: "))
    examTwo = float(input("\tEnter Exam 2 score: "))
    examThree = float(input("\tEnter Exam 3 score: "))
    examFour = float(input("\tEnter Exam 4 score: "))
    print('-' * 30 + '\n')

    # Finding the average
    averageGrade = (examOne + examTwo + examThree + examFour) / 4

    # Displaying Result
    print("Grade Summary")
    print('-' * 30 + '\n')
    print("\t", name, end = "")
    print("'s average grade is:", format(averageGrade,".2f"))
    
    
    # project end
    print('\n' + '-' * 30)
    print('\nEnd of Project 1')
      
main() # calling the function main()


