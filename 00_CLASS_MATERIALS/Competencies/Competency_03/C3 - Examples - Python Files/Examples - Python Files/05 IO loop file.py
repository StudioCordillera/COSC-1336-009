# Name      Ally Baba
# Date      February 7 2020
# Program   IO
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
#Loop through a file

def main():
      fileRead = open('test1.txt','r')

      myList = []

      for line in fileRead:
            myLine = line.strip('\n')
            myValue = int(myLine)
            myList.append(myValue)

      print('Value:', len(myList))
      fileRead.close()


main()
print('\nEnd of Project')
