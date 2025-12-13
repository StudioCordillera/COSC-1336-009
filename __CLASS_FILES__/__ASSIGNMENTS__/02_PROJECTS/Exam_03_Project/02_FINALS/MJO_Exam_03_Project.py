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
        
        name = input(f'{tab}Enter the name: ').strip().title()
        
        while True:
            exam1 = float(v(int, f'{tab}Enter grade for Exam 1: '))
            if 0 <= exam1 <= 105:
                break
            print(f"{tab}Score must be between 0 and 105!")
        
        while True:
            exam2 = float(v(int, f'{tab}Enter grade for Exam 2: '))
            if 0 <= exam2 <= 105:
                break
            print(f"{tab}Score must be between 0 and 105!")
        
        while True:
            exam3 = float(v(int, f'{tab}Enter grade for Exam 3: '))
            if 0 <= exam3 <= 105:
                break
            print(f"{tab}Score must be between 0 and 105!")
        
        student = studentClass.Student(name, exam1, exam2, exam3)
        students.append(student)
    
    return students

def sortStudents(students):
    return sorted(students, key=lambda s: s.examAvg(), reverse=True)

def displayResults(students, courseName):
    print(f"{nL+tab}Summary: Student Grades{nL}")
    print(f"{tab}   Total Number of Students: {len(students)}{nL}")
    
    print(f"{tab}Name{tab+tab+tab+tab+tab}Scores{tab+tab+tab+tab}Average{tab}Letter Grade")
    for student in students:
        avg = student.examAvg()
        grade = getLetterGrade(avg)
        scores = sorted([student.exam1, student.exam2, student.exam3], reverse=True)
        scores_str = f"{int(scores[0])}, {int(scores[1])}, {int(scores[2])}"
        
        print(f"{tab}{student.name}{tab+tab+tab+tab}{scores_str}{tab+tab+tab}{avg:.2f}{tab}{grade}")
    
    print(f"{nL+tab}-----------------------------------------------------------------------")
    print(f"{tab}Course Summary{nL}")
    
    totalAvg = sum(s.examAvg() for s in students) / len(students)
    gradeCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for student in students:
        gradeCount[getLetterGrade(student.examAvg())] += 1
    
    print(f"{tab}Name of the Course:{tab+tab+tab+tab}{courseName}")
    print(f"{tab}Average Grade of all students{tab+tab}{totalAvg:.2f}")
    print(f"{tab}Number of A's{tab+tab+tab+tab}{gradeCount['A']}")
    print(f"{tab}Number of B's{tab+tab+tab+tab}{gradeCount['B']}")
    print(f"{tab}Number of C's{tab+tab+tab+tab}{gradeCount['C']}")
    print(f"{tab}Number of D's{tab+tab+tab+tab}{gradeCount['D']}")
    print(f"{tab}Number of F's{tab+tab+tab+tab}{gradeCount['F']}")

def main(): 
    START()
    
    print(f"{tab}Instructor's Entry")
    courseName = v(str, f'{tab}Name of the course: ').strip()
    
    while True:
        numStudents = v(int, f'{tab}How many students: ')
        if numStudents > 0:
            break
        print(f"{tab}Must have at least 1 student!")
    
    students = getStudents(numStudents)
    sortedStudents = sortStudents(students)
    displayResults(sortedStudents, courseName)
    
    END()
      
main()






