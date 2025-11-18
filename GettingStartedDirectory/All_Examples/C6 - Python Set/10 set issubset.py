# Name      Ally Baba
# Date      February 7 2020
# Program   dey
# Class     COSC 1336 Programming Language 1
# ----------------------------------------------------------------
# Description
# set - issubset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))

# Returns False
print(A.issubset(C))

# Returns True
print(C.issubset(B))
