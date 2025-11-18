# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# for loop
def main():
    stocks = {
        'IBM': 146.48,
        'MSFT':44.11,
        'CSCO':25.54
    }

    #print out all the keys
    for c in stocks:
        print(c)

    #print key n values
    for k, v in stocks.items():
        print("Code : {0}, Value : {1}".format(k, v))

main()
