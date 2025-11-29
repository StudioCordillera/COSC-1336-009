
def main():
   value = getData('Enter a number ')

def getData(prompt):
   while True:
      try:
         value = int(input('Enter an integer '))
         return value
      except ValueError:
         print('Not a number, enter a number')

main()
