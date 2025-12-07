import typeValidation
import displayLabels
import studentClass

# user input and student data mobilization orchestration
def getStudents(studentsRng):
    
    # custom styling for grammatical context
  for input in range():
    if input == 0:
      ref = 'first students\'s'
    else:
      ref = 'next student\'s'

  # initialize placeholders
  unsortedPerformers:dict[int,str] = {}
  studentDirectory = {}

  # Get user input per student
  studentName = typeValidation.validateInput(str, f'\tEnter the {ref} name: ')
  exam1 = typeValidation.validateInput(float, f'\tEnter the {ref} exam1 score: ')
  exam2 = typeValidation.validateInput(float, f'\tEnter the {ref} exam2 score: ')
  exam3 = typeValidation.validateInput(float, f'\tEnter the {ref} exam3 score: ')

  # Initialize Student Instance
  studentName = studentClass.Student(studentName, exam1, exam2, exam3)
  
  # Call for & store exam average from instance method calc
  examavg = studentName.examAvg()
  
  # Format exam floats as to the hundreths place value }| e.g 0.00
  examavg,exam1,exam2,exam3 = f"{examavg:.2f}", f"{exam1:.2f}", f"{exam2:.2f}", f"{exam3:.2f}"
  
  # Sorted exam everage deliverable
  unsortedPerformers[examavg]=studentName
  
  # Formal Detailed Registry
  studentDirectory[studentName]={'exams average':examavg, 'exam1':exam1, 'exam2': exam2, 'exam3':exam3}

  # Return Unsorted Performers, and Student Directory when finished
  return unsortedPerformers, studentDirectory


def displaySummary(sortedPerformers):
    
  print(sortedPerformers)




def main(): 
    
  # SOPB
  displayLabels.START()

  # pass user input for max students range into get students func
  # Get the unsorted list back
  unsortedPerformers, SD = getStudents(typeValidation.validateInput(int, '\tEnter the number of students: '))

  # Get sorted list from unsorted one | by values
  # Pass in SD as Student Directory
  sortedPerformers = sorted(unsortedPerformers.values())

  displaySummary(sortedPerformers)





  # EOPB
  displayLabels.END()
      
main() # ENTRYPOINT






