# processing list

def main():
    numberList = [1,2,4,56,67,89,90]
    sum = 0
    
    for x in numberList:
        sum = sum + x

    average = sum / len(numberList)
    print('The average is : %8.2f' % average)
main()
