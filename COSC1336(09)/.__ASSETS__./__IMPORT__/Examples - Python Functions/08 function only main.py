# Name      AllyBaba
# Date      February 11 2017
# Program   Project 3
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# This assignment will calculate the total sales amount where sames amount
# and tax rate is entered

def main():
    # input section
    salesAmount = float(input('Enter your sales amount '))
    taxRate = float(input('Enter your tax rate in decimals '))

    #calculation section
    tax = salesAmount * taxRate
    totalSales = salesAmount + tax

    #print section
    print('The sales amount is ', salesAmount)
    print('The tax is ', tax)
    print('The total sales is ', totalSales)



main()



