
def adding(number):
    stringNum = str(number)
    sumOfDigits = 0

    for value in stringNum:
        sumOfDigits = sumOfDigits + int(value)
    
    return sumOfDigits

