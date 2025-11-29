def calc(value):
    product = 1

    for i in range (1, value+1):
        product = product * i

    return product

def main():

    while True:
        try:
            value = int(input("Please enter a number: "))
            break   

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    if value <= 0:
        print('rule does not apply')

    else:
        print(calc(value))


main ()
