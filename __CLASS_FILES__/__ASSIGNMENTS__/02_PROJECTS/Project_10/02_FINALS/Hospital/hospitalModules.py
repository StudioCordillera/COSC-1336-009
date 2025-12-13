__all__ = ['Surgery', 'Pharmacy']
import sys
import os
# Add parent directory to path if running from ProjectClasses folder
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from MyClasses import displayLabels, typeValidation
nL, tab, tab1, lineGraph, shortBar, medBar = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar
v=V=typeValidation.validateInput



def Menu(choices, key, value):

    for count in range(len(choices)):
        print(f"{tab}{choices[count+1][key]}: ${choices[count+1][value]}")

    while True:

        userChoice = v(int, f"{tab}Enter an option: ")

        if userChoice not in choices:
            print(f"{tab}Not an option!")

        else:
            return str(choices[userChoice][key]), int(choices[userChoice][value])
        

def Surgery():
    options = []
    choices = {}
    num=0

    with open('./Hospital/surgery.txt', 'r') as file:
        
        for lines in file:
            options.append(lines.strip().split(', '))

    for x,y in options:
        num+=1
        choices[num]={'Surgery':x, 'Cost':y}

    return Menu(choices, 'Surgery', 'Cost')
    



def Pharmacy():

    options = []
    choices = {}
    num=0

    with open('./Hospital/medicine.txt', 'r') as file:
        
        for lines in file:
            options.append(lines.strip().split(', '))

    for x,y in options:

        num+=1
        choices[num]={'Medicine':x, 'Cost':y}

    return Menu(choices, 'Medicine', 'Cost')
    




