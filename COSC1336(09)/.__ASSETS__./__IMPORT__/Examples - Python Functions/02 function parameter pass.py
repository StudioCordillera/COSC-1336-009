# Name      Ally Baba
# Date      February 7 2020
# Program   Function
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# -------------
# Function used a passing parameters - Pass By Value

def sums(a,b):
   b = a + b
   
def main():
   a = 10
   b = 20
   sums(a,b)
   print("The value of b is after sums function is called = ", b)

main()


