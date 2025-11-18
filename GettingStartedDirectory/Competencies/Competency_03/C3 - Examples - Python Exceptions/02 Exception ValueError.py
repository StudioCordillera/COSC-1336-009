while True:
    try:
        value = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

factorial = 1

if value == 0:
    print('Factorial is 1')
elif  value < 0:
    print('Factorial is not posisble')
else:
    for x in range(1, value+1):
        factorial = factorial * x
    print('Factorial is ', factorial)
    
