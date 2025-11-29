def main():
    value = int(input("Enter an integer value and 0 will terminate."))
    numberList = []
    
    while value != 0:
        numberList.append(value)
        value = int(input("Enter an integer value and 0 will terminate."))

    numberList.sort()
    print(numberList)
    maxNumber = max(numberList)
    print(maxNumber)
    minNumber = min(numberList)
    print(minNumber)
    product = maxNumber * minNumber
    print(product)
    product2 = numberList[0] * numberList[-1]
    print(product2)
main()
