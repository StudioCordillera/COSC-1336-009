import os
import time
import sys
from responsiveMath 

if sys.platform == 'win32':
    import ctypes
    ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)



# ESCAPE CODES CODEX

e='\033'       # Escape character
ef='\033['     # Function call starter



# csf = Construct Sequence Function
def csf(function:str, a=None, b=None, c=None):  # function = letter (like 'm') where m(), (a,b,c) = arguments
    function=function.capitalize().strip()
    
    if a is None:
        return f"{ef}{function}"
    elif b is None:
        return f"{ef}{a}{function}"
    elif c is None:
        return f"{ef}{a};{b}{function}"
    else:
        return f"{ef}{a};{b};{c}{function}"
    
def pcsf(function, a=None, b=None, c=None):
    es=csf(function,a,b,c)
    print(es, end='', flush=True)


''' |    CODES INDEX: CURSOR
    |
    |   #   |   A   |   (l)     Move l  Lines up
    |   #   |   B   |   (l)     Move l  Lines down
    |   #   |   C   |   (c)     Move c  Columns right 
    |   #   |   D   |   (c)     Move c  Columns Left
    | MOVET |   H   |   (r, c)  Move to: r row, c column  
    | CFULL |   J   |   (*)     CLEAR *2 is for full screen
    | CLINE |   K   |   (*)     CLEAR *2 is for full line
    |   #   |   S   |   (None)  SAVE Cursor Position
    |   #   |   U   |   (None)  RESTORE Cursor Position
'''

def getString(*args):
    result = []
    for i in args:
        try:
            result.append(str(i))
        except Exception as e:
            print(f"\t{e}")
    return result

    
# cf = Cursor Functions
def cf(option:int):
    options = ['?25l', '?25h']
    return f"{ef}{options[option-1]}"

''' |   CURSOR FUNC CODEX
    |      1   |   HIDE |   ?251
    |      2   |   SHOW |   ?25h
'''

# CLIP = CLI Print (by: row) (user responsible for managing row content |   ! function will not handle overides)
def clip(column, row, item):
    move=csf('h',row,column)
    print(f"{move}{item}", end='', flush=True)


def pclip(height, width, item, debug=False):
    # height = % down (0-100), width = % across (0-100)
    col, row = Dynamic('Convert', width, height)
    if debug:
        clip(1, 6, f"pclip debug: width%={width}, height%={height} -> col={col}, row={row}     ")
    move=csf('h',row,col)
    print(f"{move}{item}", end='', flush=True)
    


def start():
    os.system('cls')
    debug(True)

    

def printScreenSize():
    cols, rows = os.get_terminal_size()
    cols, rows = getString(cols, rows)
    item = f"{cols}x{rows}"
    clip(1,1,item)



def showScaled():
    '''Builds a square boundry for the full screen bounds'''
    
    # Dynamic('Convert', width%, height%) returns (col, row)
    # Top or Bottom | Left or Right | Column or Row

    padding=5
    
    tlc,tlr,trc,trr,blc,blr,brc,brr=setScaleCorners(padding)
    
    
    

    # clip(column, row, item)
    clip(tlc, tlr, '+')           # Top-left corner
    clip(trc, trr, '+')         # Top-right corner
    clip(blc, blr, '+')     # Bottom-left corner
    clip(brc, brr, '+')
    #   
    #   for row in range(rows):
    #
    #       clip(w,row,'-')
    #       clip(cols,row,'-')
    #
    #   for column in range(cols):
    #       clip(column, 2, '|')
    #       clip(column, rows, '|')



'''

# Screen size (1-10000)
screen_size = 76

# Calculate the 1/100 fractional unit size
unit_size = screen_size / 100

# Verify: how many units fit in the screen (should be 100)
number_of_units = screen_size / unit_size

'''



def debug(cond):
    print(cf(1), end='', flush=True)  # Hide cursor
    prev_size = None
    while cond:
        curr_size = os.get_terminal_size()
        
        # Only clear if screen size changed
        if curr_size != prev_size:
            print(csf('H') + csf('J', 2), end='', flush=True)
            prev_size = curr_size
        
        # Display debug info
        h, w = Dynamic('Debug')
        clip(1, 2, h)
        clip(1, 3, w)
        
        printScreenSize()
        showScaled()
        pclip(50, 50, 'Test')
        time.sleep(0.1)












def main():
    start()
main()
