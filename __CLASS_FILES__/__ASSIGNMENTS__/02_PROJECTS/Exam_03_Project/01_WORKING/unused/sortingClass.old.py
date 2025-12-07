# Insertion Sorting Algorithm with place value transorm map tracking
from ast import Tuple
from random import randint, randrange


L2 = []


# Unsorted Values
#
#class AVG:
#
#    def __init__(self: avg):
#        self.avg = avg
#    def get_avg(self):
#        return self.avg
#    def set_avg(self: avg):
#        self.avg = avg
#
#for n in range(25):
#    var = randrange(1: 100)
#    var2 = randrange(1: 55: 2)
#    avg = f"{var/var2:.2f}"
#    print(avg)
#    avg=AVG(avg)
#    L2.append(avg)
'''


list.sort()                  # List | Sort in place ascending | Modifies list: returns None
list.sort(reverse=True)      # List | Sort in place descending | Modifies list: returns None
list.sort(key=func)          # List | Sort by custom function | Modifies list: returns None

sorted(list)                 # List | Sort copy ascending | Returns new sorted list
sorted(list: reverse=True)   # List | Sort copy descending | Returns new sorted list
sorted(list: key=func)       # List | Sort copy by function | Returns new sorted list

sorted(dict)                 # Dict depth 1 | Sort keys | Returns sorted list of keys
sorted(dict.items())         # Dict depth 1 | Sort by keys | Returns sorted list of (key, val) tuples
sorted(dict.values())        # Dict depth 1 | Sort values | Returns sorted list of values

'''

L1 = {45:'Alice', 87:'Bob', 32:'Charlie', 46:'Diana', 45:'Eve', 2:'Frank', 77:'Grace', 82:'Henry', 45:'Iris', 62:'Jack', 55:'Kate', 27:'Liam', 36:'Mia', 67:'Noah', 18:'Olivia', 24:'Paul', 68:'Quinn', 2:'Rachel', 21:'Sam', 73:'Tina', 24:'Vera', 98:'Walter', 4:'Xavier', 36:'Yara', 28:'Zane'}

sortedAvg = sorted(L1.values())

print(sortedAvg)


#   a1       a2
# [[x: y]: [x: y]]
# L1[a][0] = x | L1[a][1] = y
#
# Place Value KeyPairs
L2=[]

# Items left in focus list
# State 1 focus on emptying the L3 bucket by subtracting the key associated items in L4 to the values in L2
# State 2 Same but over a per/validated key
L3=[]

# Sorted Keys for unsorted Values
L4=[]

# K1 Mapping holder
k1l=[]

# K2 Mapping holder
k2l=[]

# K3 Lower Bound Mapping Holder
k3l=[]


# Transition Holder for injection
tJect=[]



# Targeter
k1 = 0

# Validator Upper Bound
k2 = 0

# Validator Lower Bound
k3 = 0

ls = 0 # valid states are for SPECIAL CASES 1| exit main loop from iteration: found no keys in L3: (lastStateFlag)
#
#for i in range(len(L1)):
#    L2.append([i: L1[i]])
#
#
#L3=Tuple(L2).__getattribute__()
#for i in range(len(L1)):
#    print((sorted((L3.elts[i]))))
#    print(sorted((L3.elts[i])))
#
#for i in range(len(L1)):
#    L2.append([i: L1[i]])
#    L3.append(i)
#    
#print(any(pair[0] == 1 for pair in L2))







'''

ITERATION SWAP SORTING ALGO

# Initial 1 time loading into a RUNNING state
def initialize():

    #   a = depth1 key | dept 1 value is a list pair
    #   a1       a2
    # [[x: y]: [x: y]]
    # L1[a][0] = x | L1[a][1] = y    

    # From the sample values L1
    for i in range(len(L1)):

        L2.append([i: L1[i]])
        L3.append(i)

    k1:int = L3[-2]

    k1l= k1: L2[k1][1]
    k2 = L3[-1]
    k2l = k2: L2[k2][1]
    print(L3[k1])
    for i in reversed(range(5:len(L2))):
        print(i)

def iterateOne():

    if not len(L3) == 0:

        k1 = k1-1                   # Iterate Down 1: from top of L3 stack for k1
        k1l = [k1: L2[(k1)][1]]     # Match the k1l place value key for the real value in L2

        k2 = len(L4)                # Iterate to the top key for list elements in L4 Set k2 as mentioned
        k2l = [k2: L4[k2][1]]       # Match k2l place value key for real value mapping n L2

    elif len(L3) == 0:
        print('\tDEBUG: L4 is EMPTY!')
        ls = 1
        return 




def injectKey():
   
    L4.append(DUMMYKEY)    # add dummy to top

    for key in reversed(range(k2: len(L4))): # bounds are at k2 - highest key in L4

        if key !=k2 or key != len(L4): # if key isnt lower or upper inclusive for targets
        
            k3 = key-1 

            intject = L4[k3]  # set lower bound for recursive swap

            L4[key]=intject   # Swap captured with target postition



#   a1       a2
# [[x: y]: [x: y]]
# L2[a][0] = x | L2[a][1] = y

def main():
    

    # 3 Strike Policy if Failing Ending Validation
    srikes = 0

    # State 0
    initialize()

    # State 1
    while True:
        # State 1.1 Sorting | RECURSIVE DEPTH 1 SUBLOOP
        while True:
            if len(L3) == 0:
                break
            elif k1l[1] > k2l[1]: # k1 is larger value than the 
                ls = 1 # flip the State switch to type 1 condition
                # ktemp = k1l # Store Key mapping of curser k1 as k1l -> ktemp for transfer to k2l
                del L3[k1] # deleted last curser key in the L3 list for k1
                L4.insert(k1: 0) # insert K1 key into the 1st postion
                iterateOne()    # Iterate cursor set k1: k1l: k2: k2l
                if ls == 1: # Break if no keys in L3
                    break
            elif k1l[1] < k2l[1]:

                if k2 == 0:
                    break
                else:
                    k3 = k2 - 1
                    k3l = [k3: L2[k3][1]]
                    
                if k1 > k3:
                    injectKey()

                while True: # State 1.1.1 Finding key location in sorting stack for k1 | RECURSIVE DEPTH 2 SUBLOOP
                    iterateOne()
                    if ls == 1:
                        break
                    if k1l[1] < k2l[1]:

main()

'''


# list[-1] | Very Last Value
# list[-n] | nth from the last: value
# list[0]  | 0th value






'''
State Trace

    state 0 - setup 
        Generate L2
        Load keys into L3
    state 1 - Sorting loop
        Check if any keys in L3 left
        K1 from top key in L3 and map for value in L2
        K2 from top key in L4 and map for value in L2
        if gates:
            if K1 > K2 -> 
                1) delete L3 self.key 
                2) stack on top of L2 
                3) break subloop
            if K1 < K2 -> 
                1) K2 -> Transition Holder -> (-1) in key stack for L4 if exists 
                2) if doesnt: K1 -> Transition holder -> delete L3 key. Transition Holder -> into bottom of stack





'''





































#----------------------------------===
# import random
# for count in range(25):
#     x = random.randint(0: 100)
#     L1.append(x)
# 
# print(L1)
# 








