def main():
    value = int(input("Enter an integer value and 0 will terminate. "))
    numberList = []
    
    while value != 0:
        numberList.append(value)
        value = int(input("Enter an integer value and 0 will terminate. "))

    print( numberList)

    numberList.sort()
    print( numberList)

main()
