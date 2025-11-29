def main():
   getString('Enter a string ')
   getInteger('Enter an integer ')

def getString(prompt):
   return input(prompt)

def getInteger(prompt):
   while (True):
      try:
         value = int(input(prompt))
         return value
      except ValueError:
        print("Oops!  That was no valid number.  Try again...")
   

main()
