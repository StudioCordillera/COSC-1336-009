# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# fromkrys

seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("New Dictionary : %s" %  str(dict))

dict = dict.fromkeys(seq, 10)
print ("New Dictionary : %s" %  str(dict))
