# Name      Ally Baba
# Date      February 7 2020
# Program   dictionary
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# Delete Dictionary Elements

word = {'a': '1', 'b': '2', 'c': '3'}

sentence = 'abc'

answer = ""

for ctr in sentence:
    answer = answer + word[ctr]

print(answer)

