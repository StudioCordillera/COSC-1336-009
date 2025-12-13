###############################################################
##:::::|   Matthew Ochoa       |-----------------------|:::::##
##:::::|   December 12, 2025   |   Status: COMPLETE    |:::::##
##:::::|   Class: COSC 1336    |-----------------------|:::::##
###############################################################
import studentClass
from MyClasses import displayLabels, typeValidation
ExamThree=displayLabels.Context(3, '12/12/2025','AllyBaba Grades', 'Student Performance Tracker')
END, START = ExamThree.END, ExamThree.START
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph
v=V=typeValidation.validateInput
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
______________________________________________________________
|                                                             |
|   REQUIREMENTS - EXAM #3 PROJECT (Student Grades)           |
|_____________________________________________________________|
|                                                             |
|  OBJECTIVE:                                                 |
|    - Track student performance based on three exam scores   |
|    - Display sorted results with letter grades              |
|                                                             |
|  INPUT:                                                     |
|    - Number of students                                     |
|    - For each student:                                      |
|        - Name (string)                                      |
|        - Exam 1, 2, 3 scores (floats, 0-105 with bonus)    |
|                                                             |
|  PROCESSING:                                                |
|    - Calculate average for each student                     |
|    - Determine letter grade (A: 90-105, B: 80-89, etc.)     |
|    - Sort students by average (descending for display)      |
|                                                             |
|  OUTPUT:                                                    |
|    - Table with: Name, Scores (sorted), Average, Grade      |
|_____________________________________________________________|
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def getLetterGrade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def getStudents(numStudents):
    students = []
    
    for i in range(numStudents):
        print(f"{nL}Student #{i+1}")
        
        name = v(str, f'Enter the name ').strip()
        
        while True:
            exam1 = v(float, f'Enter grade for Exam 1: ')
            if 0 <= exam1 <= 105:
                break
            print(f"Score must be between 0 and 105!")
        
        while True:
            exam2 = v(float, f'Enter grade for Exam 2: ')
            if 0 <= exam2 <= 105:
                break
            print(f"Score must be between 0 and 105!")
        
        while True:
            exam3 = v(float, f'Enter grade for Exam 3: ')
            if 0 <= exam3 <= 105:
                break
            print(f"Score must be between 0 and 105!")
        
        student = studentClass.Student(name, exam1, exam2, exam3)
        students.append(student)
    
    return students

def sortStudents(students):
    return sorted(students, key=lambda s: s.examAvg(), reverse=True)

def displayResults(students, courseName):
    print(f"{nL}Summary: Student Grades")
    print(f"{tab}Total Number of Students: {len(students)}")
    
    # Calculate overall statistics
    totalAvg = 0
    gradeCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    
    # Display header
    print(f"{'Name':<15} {'Scores':<20} {'Average':>10} {'Letter Grade':>12}")
    
    # Display each student
    for student in students:
        avg = student.examAvg()
        grade = getLetterGrade(avg)
        scores = sorted([student.exam1, student.exam2, student.exam3])
        scores_str = f"{int(scores[0])}, {int(scores[1])}, {int(scores[2])}"
        
        print(f"{student.name:<15} {scores_str:<20} {avg:>10.2f}  {grade:>12}")
        
        totalAvg += avg
        gradeCount[grade] += 1
    
    # Calculate overall average
    overallAvg = totalAvg / len(students) if students else 0
    
    print(medBar)
    print(f"Course Summary")
    print(f" Name of the Course: {courseName}")
    print(f" Average Grade of all students  {overallAvg:.2f}")
    print(f"Number of A's{tab1}{gradeCount['A']}")
    print(f"Number of B's{tab1}{gradeCount['B']}")
    print(f"Number of C's{tab1}{gradeCount['C']}")
    print(f"Number of D's{tab1}{gradeCount['D']}")
    print(f"Number of F's{tab1}{gradeCount['F']}")
    print(lineGraph)

def main(): 
    START()
    
    print(f"Instructor's Entry")
    courseName = v(str, f'Name of the course:  ').strip()
    
    while True:
        numStudents = v(int, f'How many students:  ')
        if numStudents > 0:
            break
        print(f"Must have at least 1 student!")
    
    students = getStudents(numStudents)
    sortedStudents = sortStudents(students)
    displayResults(sortedStudents, courseName)
    
    END()
      
main()






