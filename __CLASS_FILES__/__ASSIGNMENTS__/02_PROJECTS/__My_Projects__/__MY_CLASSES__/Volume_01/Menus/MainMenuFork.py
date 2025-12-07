
titleMain = 'MAIN MENU'
headingMain = 'Content Management System'

corner = '+'
vert = '|'
horiz = '-'


def fstring(centered, filler, width, height):
  
    
    
fstring(vert, vert, 3, 5)
 
cls 


def borderBuilder(paddingh, paddingl, columns, label, pillar, wall, corner):


    


 


    # build walls




        




def main():
    
    borderBuilder(None, None, 3, titleMain, horiz, vert, corner)

    



main()

'''


str.strip()                     Remove leading/trailing whitespace | Returns new stripped string
str.strip(chars)                Remove specified chars from ends | Returns new stripped string
str.removeprefix(prefix)        Remove prefix if exists | Returns string without prefix
str.removesuffix(suffix)        Remove suffix if exists | Returns string without suffix


str.split()                     Split on whitespace | Returns list of substrings
str.split(sep)                  Split on separator | Returns list of substrings
str.split(sep, maxsplit)        Split with max splits | Returns list with max parts
str.rsplit()                    Split from right on whitespace | Returns list of substrings
str.rsplit(sep, maxsplit)       Split from right with max | Returns list with max parts
str.splitlines()                Split on line breaks | Returns list of lines
str.splitlines(keepends=True)   Split keeping line breaks | Returns list with newlines
str.partition(sep)              Split on first separator | Returns (before, sep, after) tuple
str.rpartition(sep)             Split on last separator | Returns (before, sep, after) tuple
sep.join(iterable)              Join items with separator | Returns joined string


str.find(sub)                   Find first occurrence | Returns index or -1 if not found
str.find(sub, start)            Find from start position | Returns index or -1
str.find(sub, start, end)       Find in range | Returns index or -1
str.rfind(sub)                  Find last occurrence | Returns index or -1
str.rfind(sub, start, end)      Find last in range | Returns index or -1
str.index(sub)                  Find first occurrence   | Returns index or ValueError
str.index(sub, start, end)      Find in range           | Returns index or ValueError


str.replace(old, new)           Replace all occurrences | Returns new string with replacements
str.replace(old, new, count)    Replace first count occurrences | Returns new string with replacements

str.center(width)            Center in width            | Returns centered string with spaces
str.center(width, fillchar)  Center with fill char      | Returns centered string with fillchar
str.ljust(width)             Left-justify in width      | Returns left-aligned string
str.ljust(width, fillchar)   Left-justify with fill     | Returns left-aligned string
str.rjust(width)             Right-justify in width     | Returns right-aligned string
str.rjust(width, fillchar)   Right-justify with fill    | Returns right-aligned string
str.zfill(width)             Pad with zeros on left     | Returns zero-padded string
str.expandtabs()             Expand tabs to spaces      | Returns string with spaces
str.expandtabs(tabsize)      Expand tabs custom size    | Returns string with custom spacing



+==============================================================================+
|                            CMS MAIN MENU                                     |
+==============================================================================+

    Please select an option:

    +----------------------------------------------------------------------+
    |  1. REGISTER NEW ITEM                                                |
    |  2. VIEW COLLECTION                                                  |
    |  3. SETTINGS                                                         |
    |  4. EXIT                                                             |
    +----------------------------------------------------------------------+

    Enter your choice: 


    Component Breakdown:

        menu_wrapper → Heavy border box 
        title → Centered text in header box
        choice_menu_wrapper → Light border box 
        prompt → Plain text above choices
        choices_wrapper → List container
        choice_object → Numbered item with description



TYPE: FORK

    1   REGISTER NEW ITEM         → Flow
    2   VIEW COLLECTION            → Stati
    3   SETTINGS                   → Fork
    4   EXIT                       → Termi

    [ON HOLD: CHOOSE NEW COLLECTION]


DESIGN:
    MENU WRAPPER
        HEADER|TITLE
        CHOICES MENU WRAPPER
            PROMPT
            CHOICES WRAPPER
                CHOICE

STATES:
    DISPLAY
    WAITING ON INPUT
    SELECTION LOOP
    CHOICE SELECTED
    CHOICE CONFIRMED


{main_menu:{
    fork:{

        1: item_registration,
        2: view_collection, 
        3: settings,
        4: exit_app


    },
    states:{
    
        1: DISPLAY
        2: WAITING ON INPUT,
        3: SELECTION LOOP,
        4: CHOICE SELECTED,
        5: CHOICE CONFIRMED
    
    },
    design:{
    
        1: menu+_wrapper:{
        
            1.1: title,
            1.2: choice_menu_wrapper{
                1.2.1: prompt,
                1.2.2: choices_wrapper{

                    1.2.2.1: choice_object
                
                }
            }
        }
    }
}



'''

























