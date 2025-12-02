"""
ABSTRACT VISUAL PATTERNS COLLECTION
====================================
Comprehensive catalog of ASCII visual design patterns inspired by Python documentation.
All patterns use standard ASCII characters for maximum compatibility.

Author: GitHub Copilot
Purpose: Visual pattern library for documentation, UI design, and creative ASCII art
"""

# ============================================================================
# SECTION 1: HIERARCHICAL TREE STRUCTURES
# ============================================================================

"""
Classic Tree Structure (File System Style)
"""
TREE_CLASSIC = '''
root/
├── branch_1/
│   ├── leaf_1.txt
│   ├── leaf_2.txt
│   └── subbranch/
│       ├── nested_leaf_1.txt
│       └── nested_leaf_2.txt
├── branch_2/
│   └── leaf_3.txt
└── branch_3/
    ├── leaf_4.txt
    └── leaf_5.txt
'''

"""
Binary Tree Structure
"""
BINARY_TREE = '''
                    ROOT
                   /    \\
                  /      \\
                 A        B
                / \\      / \\
               C   D    E   F
              / \\       \\   / \\
             G   H       I J   K
'''

"""
Decision Tree / Flow Tree
"""
DECISION_TREE = '''
                [START]
                   |
            +------+------+
            |             |
        [Choice A]   [Choice B]
            |             |
        +---+---+     +---+---+
        |       |     |       |
      [A1]    [A2]  [B1]    [B2]
        |       |     |       |
     [END]   [END] [END]   [END]
'''

"""
Radial Tree / Star Pattern
"""
RADIAL_TREE = '''
              [N1]
               |
       [W1]---[C]---[E1]
               |
              [S1]
'''

# ============================================================================
# SECTION 2: BOX DRAWING & FRAMES
# ============================================================================

"""
Single Line Box (Basic)
"""
BOX_SINGLE = '''
+-------------------+
|   Content Here    |
+-------------------+
'''

"""
Double Line Box
"""
BOX_DOUBLE = '''
+===================+
|   Content Here    |
+===================+
'''

"""
Mixed Border Box (Heavy Top/Bottom)
"""
BOX_MIXED = '''
+===================+
|   Header Section  |
+-------------------+
|   Content Area    |
+-------------------+
|   Footer Section  |
+===================+
'''

"""
Nested Boxes (3 Levels)
"""
NESTED_BOXES = '''
+---------------------------------------+
| OUTER LAYER                           |
| +-----------------------------------+ |
| | MIDDLE LAYER                      | |
| | +-------------------------------+ | |
| | | INNER LAYER                   | | |
| | +-------------------------------+ | |
| +-----------------------------------+ |
+---------------------------------------+
'''

"""
Shadow Box (3D Effect)
"""
SHADOW_BOX = '''
  +-------------------+
  |   Content Here    |▓
  |   With Shadow     |▓
  +-------------------+▓
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
'''

"""
Corner Decoration Box
"""
DECORATED_BOX = '''
  *-------------------*
  |   Corner Stars    |
  |   Content Area    |
  *-------------------*
'''

"""
Complex Grid Box
"""
GRID_BOX = '''
+-------+-------+-------+
| A1    | B1    | C1    |
+-------+-------+-------+
| A2    | B2    | C2    |
+-------+-------+-------+
| A3    | B3    | C3    |
+-------+-------+-------+
'''

# ============================================================================
# SECTION 3: FLOWCHARTS & PROCESS DIAGRAMS
# ============================================================================

"""
Linear Process Flow
"""
LINEAR_FLOW = '''
[START] --> [STEP 1] --> [STEP 2] --> [STEP 3] --> [END]
'''

"""
Conditional Process Flow
"""
CONDITIONAL_FLOW = '''
           [START]
              |
              v
          [CHECK?]
            /   \\
          YES    NO
          /       \\
         v         v
    [ACTION A]  [ACTION B]
         \\       /
          v     v
          [MERGE]
             |
             v
           [END]
'''

"""
Loop Process Flow
"""
LOOP_FLOW = '''
    [INIT]
      |
      v
 +-> [CHECK] --NO--> [EXIT]
 |    |
 |   YES
 |    |
 |    v
 | [PROCESS]
 |    |
 +----+
'''

"""
Parallel Process Flow
"""
PARALLEL_FLOW = '''
                [START]
                   |
        +----------+----------+
        |          |          |
        v          v          v
    [TASK A]   [TASK B]   [TASK C]
        |          |          |
        +----------+----------+
                   |
                   v
                 [SYNC]
                   |
                   v
                 [END]
'''

# ============================================================================
# SECTION 4: DATA STRUCTURE VISUALIZATIONS
# ============================================================================

"""
Array / List Structure
"""
ARRAY_STRUCTURE = '''
Index:  0     1     2     3     4
      +-----+-----+-----+-----+-----+
Data: | A   | B   | C   | D   | E   |
      +-----+-----+-----+-----+-----+
'''

"""
Linked List Structure
"""
LINKED_LIST = '''
[HEAD] -> [A|*] -> [B|*] -> [C|*] -> [D|NULL]
           data     data     data     data
'''

"""
Doubly Linked List
"""
DOUBLY_LINKED = '''
[NULL] <-> [A|*|*] <-> [B|*|*] <-> [C|*|*] <-> [NULL]
            prev data next
'''

"""
Stack Structure (LIFO)
"""
STACK = '''
    TOP
     |
     v
  +-----+
  |  D  |  <-- Push/Pop here
  +-----+
  |  C  |
  +-----+
  |  B  |
  +-----+
  |  A  |
  +-----+
  BOTTOM
'''

"""
Queue Structure (FIFO)
"""
QUEUE = '''
REAR                           FRONT
  |                               |
  v                               v
+---+   +---+   +---+   +---+   +---+
| E | <-| D | <-| C | <-| B | <-| A |
+---+   +---+   +---+   +---+   +---+
Enqueue                        Dequeue
'''

"""
Hash Table Structure
"""
HASH_TABLE = '''
Bucket  Key -> Value
  0:    [empty]
  1:    k1 -> v1
  2:    k2 -> v2 --> k5 -> v5 (collision chain)
  3:    [empty]
  4:    k3 -> v3
  5:    k4 -> v4
'''

"""
Binary Search Tree
"""
BST = '''
              50
            /    \\
           /      \\
          30       70
         /  \\     /  \\
        20   40  60   80
       /
      10
'''

"""
Graph Structure (Adjacency)
"""
GRAPH = '''
    [A]----[B]
     | \\    |
     |  \\   |
     |   \\ |
    [C]---[D]
     |
    [E]
'''

# ============================================================================
# SECTION 5: TABLES & MATRICES
# ============================================================================

"""
Simple Table
"""
SIMPLE_TABLE = '''
+----------+----------+----------+
| Header 1 | Header 2 | Header 3 |
+----------+----------+----------+
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |
| Data 7   | Data 8   | Data 9   |
+----------+----------+----------+
'''

"""
Matrix Representation
"""
MATRIX = '''
        j0   j1   j2   j3
     +----+----+----+----+
  i0 | a  | b  | c  | d  |
     +----+----+----+----+
  i1 | e  | f  | g  | h  |
     +----+----+----+----+
  i2 | i  | j  | k  | l  |
     +----+----+----+----+
'''

"""
Truth Table
"""
TRUTH_TABLE = '''
+---+---+-------+-------+-------+
| A | B | A AND | A OR  | A XOR |
+===+===+=======+=======+=======+
| 0 | 0 |   0   |   0   |   0   |
+---+---+-------+-------+-------+
| 0 | 1 |   0   |   1   |   1   |
+---+---+-------+-------+-------+
| 1 | 0 |   0   |   1   |   1   |
+---+---+-------+-------+-------+
| 1 | 1 |   1   |   1   |   0   |
+---+---+-------+-------+-------+
'''

"""
Comparison Table
"""
COMPARISON_TABLE = '''
+==========+==========+==========+==========+
| Feature  | Option A | Option B | Option C |
+==========+==========+==========+==========+
| Speed    | Fast     | Medium   | Slow     |
+----------+----------+----------+----------+
| Memory   | High     | Low      | Medium   |
+----------+----------+----------+----------+
| Cost     | $$$      | $        | $$       |
+==========+==========+==========+==========+
'''

# ============================================================================
# SECTION 6: TIMELINES & SEQUENCES
# ============================================================================

"""
Horizontal Timeline
"""
HORIZONTAL_TIMELINE = '''
Event1    Event2    Event3    Event4    Event5
  |         |         |         |         |
  *---------*---------*---------*---------*
  t0       t1        t2        t3        t4
'''

"""
Vertical Timeline
"""
VERTICAL_TIMELINE = '''
    2025  *  Event 5
          |
    2024  *  Event 4
          |
    2023  *  Event 3
          |
    2022  *  Event 2
          |
    2021  *  Event 1
          |
    2020  *  Start
'''

"""
Gantt Chart Style
"""
GANTT_CHART = '''
Task A  |=====>              |
Task B  |    |=====>         |
Task C  |         |=====>    |
Task D  |              |====>|
        +----+----+----+----+
        t0   t1   t2   t3   t4
'''

"""
Sequence Diagram
"""
SEQUENCE = '''
Client      Server      Database
  |           |             |
  |--Request->|             |
  |           |---Query---->|
  |           |             |
  |           |<--Result----|
  |<-Response-|             |
  |           |             |
'''

# ============================================================================
# SECTION 7: GEOMETRIC PATTERNS
# ============================================================================

"""
Triangle Patterns
"""
TRIANGLE = '''
      *
     * *
    * * *
   * * * *
  * * * * *
'''

"""
Diamond Pattern
"""
DIAMOND = '''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

"""
Pyramid Pattern
"""
PYRAMID = '''
        #
       ###
      #####
     #######
    #########
   ###########
'''

"""
Checkerboard Pattern
"""
CHECKERBOARD = '''
# # # #
 # # # #
# # # #
 # # # #
# # # #
'''

"""
Wave Pattern
"""
WAVE = '''
  *     *     *     *
 * *   * *   * *   * *
*   * *   * *   * *   *
'''

# ============================================================================
# SECTION 8: BRACKETS & DELIMITERS
# ============================================================================

"""
Nested Brackets
"""
NESTED_BRACKETS = '''
{ [ ( < content > ) ] }
'''

"""
Block Scope Visualization
"""
SCOPE_BLOCKS = '''
{
    { outer scope
        { middle scope
            { inner scope
                statement;
            }
        }
    }
}
'''

"""
Expression Tree
"""
EXPRESSION_TREE = '''
          (+)
         /   \\
       (*)   (/)
      /  \\  /  \\
     a   b c   d
'''

# ============================================================================
# SECTION 9: ARROWS & POINTERS
# ============================================================================

"""
All Arrow Directions
"""
ARROWS = '''
       ^
       |
       |
   <---+--->
       |
       |
       v
'''

"""
Curved Connection
"""
CURVED = '''
    A
    |
    +---.
        |
        v
        B
'''

"""
Bidirectional Flow
"""
BIDIRECTIONAL = '''
    [A] <======> [B]
    
    [C] -------> [D]
        <-------
'''

"""
Pointer Chain
"""
POINTER_CHAIN = '''
[A]-->[B]-->[C]-->[D]
 |     |     |     |
 v     v     v     v
[E]   [F]   [G]   [H]
'''

# ============================================================================
# SECTION 10: MEMORY & ARCHITECTURE DIAGRAMS
# ============================================================================

"""
Memory Layout
"""
MEMORY_LAYOUT = '''
High Address
+------------------+
|      STACK       |  <- Stack grows down
|        |         |
|        v         |
+------------------+
|                  |
|    FREE SPACE    |
|                  |
+------------------+
|        ^         |
|        |         |
|      HEAP        |  <- Heap grows up
+------------------+
|      DATA        |  <- Global/Static
+------------------+
|      CODE        |  <- Program code
+------------------+
Low Address
'''

"""
Buffer Structure
"""
BUFFER = '''
+--------+--------+--------+--------+--------+
| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 |
+--------+--------+--------+--------+--------+
|  0x41  |  0x42  |  0x43  |  0x44  |  0x00  |
+--------+--------+--------+--------+--------+
    A        B        C        D       NULL
'''

"""
CPU Architecture Layers
"""
CPU_LAYERS = '''
+================================+
|         APPLICATION            |
+================================+
|      OPERATING SYSTEM          |
+================================+
|        FIRMWARE/BIOS           |
+================================+
|         HARDWARE               |
+================================+
'''

"""
Network Stack
"""
NETWORK_STACK = '''
+---------------------------+
|  Application Layer        | <- HTTP, FTP, SMTP
+---------------------------+
|  Transport Layer          | <- TCP, UDP
+---------------------------+
|  Network Layer            | <- IP
+---------------------------+
|  Data Link Layer          | <- Ethernet
+---------------------------+
|  Physical Layer           | <- Cables, Radio
+---------------------------+
'''

# ============================================================================
# SECTION 11: STATE MACHINES & AUTOMATA
# ============================================================================

"""
Finite State Machine
"""
FSM = '''
       input_a
    +----------+
    |          v
  [S0] ---> [S1]
    ^          |
    |          | input_b
    +----------+
'''

"""
State Transition Diagram
"""
STATE_TRANSITIONS = '''
              event1
    [IDLE] ----------> [ACTIVE]
      ^                   |
      |                   | event2
      |                   v
      +<------------- [WAITING]
           event3
'''

"""
DFA (Deterministic Finite Automaton)
"""
DFA = '''
    --> (S0) --0--> (S1) --0--> ((S2))
         |           |
         1           1
         |           |
         v           v
       (S3) <--0-- (S4)
        |           ^
        1           |
        +-----1-----+
'''

# ============================================================================
# SECTION 12: BAR CHARTS & HISTOGRAMS
# ============================================================================

"""
Horizontal Bar Chart
"""
HORIZONTAL_BAR = '''
Item A  |========>    (8)
Item B  |============>(12)
Item C  |=====>       (5)
Item D  |===============>(15)
Item E  |===========>  (10)
        +----+----+----+----+
        0    5    10   15   20
'''

"""
Vertical Bar Chart
"""
VERTICAL_BAR = '''
20 |
15 |     ##
10 |  ## ##  ##
 5 |  ## ##  ##  ##
 0 +--##-##--##--##--
    A   B   C   D
'''

"""
Stacked Bar Chart
"""
STACKED_BAR = '''
10 |
 9 |  ++
 8 |  ++
 7 |  ++  ++
 6 |  ++  ++
 5 |  ##  ##  ++
 4 |  ##  ##  ++
 3 |  ##  ##  ##  ++
 2 |  ##  ##  ##  ++
 1 |  ##  ##  ##  ##
 0 +--##--##--##--##--
     Q1  Q2  Q3  Q4
     
Legend: ## = Sales, ++ = Profit
'''

"""
Histogram
"""
HISTOGRAM = '''
Frequency
  30 |     ##
  25 |     ##
  20 |  ## ##
  15 |  ## ##
  10 |  ## ## ##
   5 |  ## ## ##
   0 +--##-##-##--
      10 20 30  (bins)
'''

# ============================================================================
# SECTION 13: CLASS DIAGRAMS & UML
# ============================================================================

"""
Class Structure
"""
CLASS_DIAGRAM = '''
+-------------------+
|    ClassName      |
+-------------------+
| - privateField    |
| + publicField     |
+-------------------+
| + publicMethod()  |
| - privateMethod() |
+-------------------+
'''

"""
Inheritance Hierarchy
"""
INHERITANCE = '''
      +----------+
      |  Animal  |
      +----------+
           ^
           |
    +------+------+
    |             |
+-------+     +-------+
|  Dog  |     |  Cat  |
+-------+     +-------+
'''

"""
Composition Relationship
"""
COMPOSITION = '''
+--------+       +--------+
|  Car   |<>---->| Engine |
+--------+       +--------+
  owns
'''

"""
Association Relationship
"""
ASSOCIATION = '''
+----------+            +----------+
| Teacher  |<---------->| Student  |
+----------+  teaches   +----------+
'''

# ============================================================================
# SECTION 14: PROGRESS INDICATORS & METERS
# ============================================================================

"""
Progress Bar (Empty to Full)
"""
PROGRESS_BAR = '''
  0% [                    ]
 25% [#####               ]
 50% [##########          ]
 75% [###############     ]
100% [####################]
'''

"""
Loading Animation States
"""
LOADING = '''
Frame 1: |
Frame 2: /
Frame 3: -
Frame 4: \\
Frame 5: |
'''

"""
Percentage Meter
"""
METER = '''
+----+----+----+----+----+
|////|////|////|    |    | 60%
+----+----+----+----+----+
'''

"""
Battery Level Indicator
"""
BATTERY = '''
Full:    [||||||||] 100%
High:    [||||||  ]  75%
Medium:  [||||    ]  50%
Low:     [||      ]  25%
Empty:   [        ]   0%
'''

# ============================================================================
# SECTION 15: DECORATIVE DIVIDERS & SEPARATORS
# ============================================================================

"""
Various Divider Styles
"""
DIVIDERS = '''
Simple:     ----------------------------------------

Double:     ========================================

Dashed:     - - - - - - - - - - - - - - - - - - - -

Dotted:     . . . . . . . . . . . . . . . . . . . .

Star:       * * * * * * * * * * * * * * * * * * * *

Hash:       ########################################

Equal:      ========================================

Wave:       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mixed:      -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Section:    +======================================+
'''

# ============================================================================
# SECTION 16: TEXT BANNERS & HEADERS
# ============================================================================

"""
Boxed Header
"""
BOXED_HEADER = '''
+========================================+
|                                        |
|          MAIN HEADER TEXT              |
|                                        |
+========================================+
'''

"""
Underlined Header
"""
UNDERLINED = '''
MAIN TITLE
==========

Subtitle
--------
'''

"""
Framed Title
"""
FRAMED_TITLE = '''
  ******************************************
  *                                        *
  *           IMPORTANT TITLE              *
  *                                        *
  ******************************************
'''

"""
Banner with Decorations
"""
DECORATED_BANNER = '''
  .:*~*:._.:*~*:._.:*~*:._.:*~*:.
  
       FEATURED CONTENT
       
  .:*~*:._.:*~*:._.:*~*:._.:*~*:.
'''

# ============================================================================
# SECTION 17: MATHEMATICAL NOTATIONS
# ============================================================================

"""
Set Notation
"""
SET_NOTATION = '''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A ∩ B = {4, 5}       (Intersection)
A ∪ B = {1,2,3,4,5,6,7,8} (Union)
A - B = {1, 2, 3}    (Difference)
'''

"""
Function Mapping
"""
FUNCTION_MAP = '''
f: X -> Y

X = {a, b, c}    Y = {1, 2, 3}

a |---> 1
b |---> 2
c |---> 3
'''

"""
Matrix Operations
"""
MATRIX_OPS = '''
        [a b]       [e f]       [a+e b+f]
A + B = [c d]   +   [g h]   =   [c+g d+h]
'''

# ============================================================================
# SECTION 18: CALENDAR & SCHEDULE LAYOUTS
# ============================================================================

"""
Monthly Calendar Grid
"""
CALENDAR = '''
      November 2025
+---+---+---+---+---+---+---+
|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
+---+---+---+---+---+---+---+
|   |   |   |   |   |   | 1 |
+---+---+---+---+---+---+---+
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |
+---+---+---+---+---+---+---+
| 9 |10 |11 |12 |13 |14 |15 |
+---+---+---+---+---+---+---+
|16 |17 |18 |19 |20 |21 |22 |
+---+---+---+---+---+---+---+
|23 |24 |25 |26 |27 |28 |29 |
+---+---+---+---+---+---+---+
|30 |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
'''

"""
Daily Schedule
"""
DAILY_SCHEDULE = '''
Time    | Activity
--------+-----------------
08:00   | Morning Meeting
09:00   | Work Block 1
10:30   | Break
11:00   | Work Block 2
12:30   | Lunch
13:30   | Work Block 3
15:00   | Break
15:30   | Work Block 4
17:00   | End of Day
'''

# ============================================================================
# SECTION 19: MOLECULAR & CHEMICAL STRUCTURES
# ============================================================================

"""
Chemical Bonds
"""
CHEMICAL = '''
    H
    |
H - C - H
    |
    H

Methane (CH4)
'''

"""
Molecular Structure
"""
MOLECULE = '''
      O
     / \\
    /   \\
   H     H

Water (H2O)
'''

"""
Benzene Ring
"""
BENZENE = '''
      C
     / \\
    /   \\
   C     C
   ||    |
   |     |
   C     C
    \\   /
     \\ /
      C
'''

# ============================================================================
# SECTION 20: GAME BOARDS & GRIDS
# ============================================================================

"""
Chess Board
"""
CHESS = '''
  +---+---+---+---+---+---+---+---+
8 | R | N | B | Q | K | B | N | R |
  +---+---+---+---+---+---+---+---+
7 | P | P | P | P | P | P | P | P |
  +---+---+---+---+---+---+---+---+
6 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
5 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
4 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
3 |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
2 | p | p | p | p | p | p | p | p |
  +---+---+---+---+---+---+---+---+
1 | r | n | b | q | k | b | n | r |
  +---+---+---+---+---+---+---+---+
    a   b   c   d   e   f   g   h
'''

"""
Tic-Tac-Toe
"""
TIC_TAC_TOE = '''
  X | O | X
 ---+---+---
  O | X | O
 ---+---+---
  X |   | O
'''

"""
Sudoku Grid
"""
SUDOKU = '''
+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+
'''

# ============================================================================
# SECTION 21: WAVEFORMS & SIGNALS
# ============================================================================

"""
Square Wave
"""
SQUARE_WAVE = '''
  +--+  +--+  +--+  +--+
  |  |  |  |  |  |  |  |
--+  +--+  +--+  +--+  +--
'''

"""
Sine Wave Approximation
"""
SINE_WAVE = '''
    *           *
  *   *       *   *
 *     *     *     *
*       *   *       *
         * *
'''

"""
Pulse Train
"""
PULSE_TRAIN = '''
  +  +  +  +  +  +  +  +
  |  |  |  |  |  |  |  |
--+--+--+--+--+--+--+--+--
'''

"""
Amplitude Modulation
"""
AM_SIGNAL = '''
     *   *   *
   *  * *  * *  *
  *    *    *    *
 *              *
*                *
'''

# ============================================================================
# SECTION 22: CIRCUIT DIAGRAMS
# ============================================================================

"""
Simple Circuit
"""
CIRCUIT = '''
    +----[R]----+
    |           |
  [BAT]       [LED]
    |           |
    +-----------+
'''

"""
Logic Gates
"""
LOGIC_GATES = '''
AND:    A ----\\
              &----- Y
        B ----/

OR:     A ----\\
              >=1--- Y
        B ----/

NOT:    A -----O----- Y
'''

# ============================================================================
# SECTION 23: COORDINATE SYSTEMS & GRAPHS
# ============================================================================

"""
Cartesian Coordinate System
"""
CARTESIAN = '''
      Y
      |
    4 +     *
    3 |
    2 |   *
    1 | *
    0 +----------- X
   -1 |     0 1 2 3 4
      |
'''

"""
Plot with Data Points
"""
SCATTER_PLOT = '''
Y |
10|           *
 9|       *
 8|   *
 7| *       *
 6|   *
 5|       *
 4| *
 3|   *
 2|
 1| *
 0+---+---+---+---+---+ X
  0   2   4   6   8  10
'''

"""
Function Graph
"""
FUNCTION_GRAPH = '''
  y = x^2
  
  |     *
  |    * *
  |   *   *
  |  *     *
  | *       *
  +-------------
     Origin
'''

# ============================================================================
# SECTION 24: ORGANIZATIONAL CHARTS
# ============================================================================

"""
Company Hierarchy
"""
ORG_CHART = '''
              [CEO]
                |
        +-------+-------+
        |               |
      [CTO]           [CFO]
        |               |
    +---+---+       +---+---+
    |       |       |       |
  [Dev]  [Ops]   [Acc]  [Fin]
'''

"""
Project Structure
"""
PROJECT_STRUCTURE = '''
        [PROJECT]
            |
    +-------+-------+
    |       |       |
 [Team A][Team B][Team C]
    |       |       |
  [T1]   [T2]    [T3]
  [T4]   [T5]    [T6]
'''

# ============================================================================
# SECTION 25: VENN DIAGRAMS
# ============================================================================

"""
Two-Set Venn Diagram
"""
VENN_2 = '''
     .--.      .--.
   .'    '.  .'    '.
  (   A    )(    B   )
   '. .--.  '--. .'
     '    AB    '
'''

"""
Three-Set Venn Diagram
"""
VENN_3 = '''
        .--.
      .'  A '.
     (        )
      '.    .'
    .--'.--'.--. 
  .'  B  ABC  C '.
 (              )
  '.          .'
    '--....--'
'''

# ============================================================================
# SECTION 26: MUSICAL NOTATION (ASCII Style)
# ============================================================================

"""
Staff Lines
"""
STAFF = '''
  ===========================
  ===========================
  ===========================
  ===========================
  ===========================
'''

"""
Piano Keys Pattern
"""
PIANO = '''
 | | | | | | | | | | | | |
 | | | | | | | | | | | | |
 |_| |_| |_| |_| |_| |_| |
|   |   |   |   |   |   |
| C | D | E | F | G | A | B
|___|___|___|___|___|___|
'''

# ============================================================================
# SECTION 27: LAYERED ARCHITECTURES
# ============================================================================

"""
Three-Tier Architecture
"""
THREE_TIER = '''
+================================+
|     PRESENTATION LAYER         |  <- UI/Frontend
+================================+
|     BUSINESS LOGIC LAYER       |  <- Application
+================================+
|     DATA ACCESS LAYER          |  <- Database
+================================+
'''

"""
MVC Architecture
"""
MVC = '''
    +-------+
    | Model |
    +---+---+
        |
  +-----+-----+
  |           |
+---+---+ +---+---+
| View  | |Control|
+-------+ +-------+
'''

"""
Microservices Architecture
"""
MICROSERVICES = '''
[Client]
    |
    v
[API Gateway]
    |
    +---+---+---+
    |   |   |   |
    v   v   v   v
   [A] [B] [C] [D]  <- Services
    |   |   |   |
    +---+---+---+
        |
    [Database]
'''

# ============================================================================
# SECTION 28: ERROR & WARNING INDICATORS
# ============================================================================

"""
Alert Levels
"""
ALERTS = '''
[!] CRITICAL: System failure
[X] ERROR:    Operation failed
[*] WARNING:  Check configuration
[i] INFO:     Process started
[+] SUCCESS:  Task completed
[-] DEBUG:    Variable value = 42
'''

"""
Status Icons
"""
STATUS = '''
[✓] Completed
[✗] Failed
[~] In Progress
[?] Unknown
[!] Attention Required
'''

# ============================================================================
# SECTION 29: FILE TREE WITH ICONS
# ============================================================================

"""
Detailed File Tree
"""
FILE_TREE_ICONS = '''
project/
├─ 📁 src/
│  ├─ 📄 main.py
│  ├─ 📄 utils.py
│  └─ 📁 modules/
│     ├─ 📄 auth.py
│     └─ 📄 db.py
├─ 📁 tests/
│  ├─ 📄 test_main.py
│  └─ 📄 test_utils.py
├─ 📄 README.md
└─ 📄 requirements.txt
'''

# ============================================================================
# SECTION 30: COMPLEX COMBINED PATTERNS
# ============================================================================

"""
Dashboard Layout
"""
DASHBOARD = '''
+=====================================+
|            HEADER                   |
+========+============================+
|        |                            |
| MENU   |      CONTENT AREA          |
|        |                            |
| - Home |  +----------------------+  |
| - Data |  | Graph/Chart          |  |
| - Help |  +----------------------+  |
|        |                            |
|        |  +----------+----------+   |
|        |  | Card 1   | Card 2   |   |
|        |  +----------+----------+   |
+========+============================+
|            FOOTER                   |
+=====================================+
'''

"""
Form Layout
"""
FORM_LAYOUT = '''
+-----------------------------------+
|  USER REGISTRATION FORM           |
+-----------------------------------+
|  Name:     [__________________]   |
|  Email:    [__________________]   |
|  Password: [__________________]   |
|  Confirm:  [__________________]   |
|                                   |
|  [ ] I agree to terms             |
|                                   |
|  [Submit]  [Cancel]               |
+-----------------------------------+
'''

"""
Multi-Panel Interface
"""
MULTI_PANEL = '''
+-------+-------+-------+
| Panel | Panel | Panel |
|   1   |   2   |   3   |
|       |       |       |
| ###   | @@@   | ***   |
| ###   | @@@   | ***   |
| ###   | @@@   | ***   |
+-------+-------+-------+
| Panel 4 - Full Width  |
|                       |
| ##################### |
+-------+-------+-------+
'''

"""
Terminal/Console Layout
"""
TERMINAL = '''
+--------------------------------------+
| $ command --option value             |
| Processing...                        |
| [====================] 100%          |
| Success: Task completed              |
| Output saved to: /path/to/file       |
| $ _                                  |
+--------------------------------------+
'''

"""
Nested Data Structure
"""
NESTED_DATA = '''
{
  "user": {
    "id": 123,
    "name": "John",
    "address": {
      "street": "Main St",
      "city": "NYC",
      "coords": {
        "lat": 40.7,
        "lon": -74.0
      }
    },
    "contacts": [
      {"type": "email", "value": "john@example.com"},
      {"type": "phone", "value": "555-1234"}
    ]
  }
}
'''

# ============================================================================
# SECTION 31: ABSTRACT ART PATTERNS
# ============================================================================

"""
Maze Pattern
"""
MAZE = '''
+---+---+---+---+---+
|       |   |       |
+   +---+   +---+   +
|   |       |       |
+---+   +---+   +---+
|       |       |   |
+   +---+---+---+   +
|   |               |
+---+---+---+---+---+
'''

"""
Labyrinth
"""
LABYRINTH = '''
   +-+-+-+-+-+-+-+
   |     |     | |
   + +-+ + +-+ + +
   | |   | |   | |
   + + +-+-+ +-+ +
   |   |     |   |
   +-+-+-+-+-+-+-+
'''

"""
Spiral Pattern
"""
SPIRAL = '''
        *
      * * *
    * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

"""
Concentric Squares
"""
CONCENTRIC = '''
  +-----------+
  | +-------+ |
  | | +---+ | |
  | | | * | | |
  | | +---+ | |
  | +-------+ |
  +-----------+
'''

"""
Cross Hatch Pattern
"""
CROSS_HATCH = '''
  / / / / / /
 / / / / / /
/ / / / / /
\ \ \ \ \ \
 \ \ \ \ \ \
  \ \ \ \ \ \
'''

"""
Mosaic Pattern
"""
MOSAIC = '''
  + - + - + - +
  | # | @ | # |
  + - + - + - +
  | @ | # | @ |
  + - + - + - +
  | # | @ | # |
  + - + - + - +
'''

# ============================================================================
# SECTION 32: SPECIAL DECORATIVE ELEMENTS
# ============================================================================

"""
Corner Brackets
"""
CORNERS = '''
  /===============\\
  |               |
  |    CONTENT    |
  |               |
  \\===============/
'''

"""
Fancy Box
"""
FANCY_BOX = '''
  .==========================================.
  |                                          |
  |     +------------------------------+     |
  |     |     INNER CONTENT AREA       |     |
  |     +------------------------------+     |
  |                                          |
  '=========================================='
'''

"""
Scroll Design
"""
SCROLL = '''
    ___________________________
   /                           \\
  |  +-----------------------+  |
  |  |                       |  |
  |  |   SCROLL CONTENT      |  |
  |  |                       |  |
  |  +-----------------------+  |
   \\___________________________/
'''

"""
Badge Design
"""
BADGE = '''
     .-----------.
    /             \\
   |    * * *      |
   |   PREMIUM     |
   |    * * *      |
    \\             /
     '-----------'
'''

# ============================================================================
# SECTION 33: BLOCK SHADING PATTERNS
# ============================================================================

"""
Gradient Effect (Using Characters)
"""
GRADIENT = '''
  ||||||||||||||||||||
  ||||||||||||||||||||
  MMMMMMMMMMMMMMMMMMMM
  MMMMMMMMMMMMMMMMMMMM
  ::::::::::::::::::::
  ::::::::::::::::::::
  ....................
  ....................
'''

"""
Dithering Pattern
"""
DITHER = '''
  # . # . # . # . # .
  . # . # . # . # . #
  # . # . # . # . # .
  . # . # . # . # . #
  # . # . # . # . # .
'''

"""
Fill Patterns
"""
FILLS = '''
Solid:    ████████████
Light:    ░░░░░░░░░░░░
Medium:   ▒▒▒▒▒▒▒▒▒▒▒▒
Heavy:    ▓▓▓▓▓▓▓▓▓▓▓▓
Dots:     ............
Hash:     ############
'''

# ============================================================================
# SECTION 34: ICONIC REPRESENTATIONS
# ============================================================================

"""
Simple Icons
"""
ICONS = '''
Folder:  [+]
File:    [-]
Link:    @->
Locked:  [#]
Star:    (*)
Heart:   <3
Cloud:   (::)
Home:    /^\\
Mail:    [@]
'''

"""
Emoji-Style ASCII
"""
EMOJI_ASCII = '''
Happy:   :)  or  :-)  or  ^_^
Sad:     :(  or  :-(  or  T_T
Wink:    ;)  or  ;-)  or  ^_~
Cool:    8)  or  B-)  or  (^_^)
Love:    <3  or  ♥    or  (*.*)
Laugh:   :D  or  XD   or  ^O^
'''

# ============================================================================
# SECTION 35: ALIGNMENT & POSITIONING GUIDES
# ============================================================================

"""
Alignment Grid
"""
ALIGNMENT_GRID = '''
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | X |   |   |   |   |  <- Center
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
'''

"""
Margin Guide
"""
MARGIN_GUIDE = '''
|<-- Margin
|  +--------------------------------+
|  |  Content Area                  |
|  |                                |
|  |  All content stays within      |
|  |  these boundaries              |
|  |                                |
|  +--------------------------------+
|<-- Margin
'''

"""
Column Layout
"""
COLUMNS = '''
+----------+----------+----------+
|          |          |          |
| Column 1 | Column 2 | Column 3 |
|          |          |          |
| Content  | Content  | Content  |
| goes     | goes     | goes     |
| here     | here     | here     |
|          |          |          |
+----------+----------+----------+
'''

# ============================================================================
# SECTION 36: COMPARISON VISUALIZATIONS
# ============================================================================

"""
Before/After Comparison
"""
BEFORE_AFTER = '''
+----------+          +----------+
| BEFORE   |          | AFTER    |
+----------+          +----------+
| * Issue  |   ===>   | * Fixed  |
| * Problem|          | * Solved |
| * Error  |          | * Clean  |
+----------+          +----------+
'''

"""
Side-by-Side Comparison
"""
SIDE_BY_SIDE = '''
  Option A              Option B
+-----------+        +-----------+
| Feature 1 |   VS   | Feature 1 |
| ✓         |        | ✗         |
+-----------+        +-----------+
| Feature 2 |        | Feature 2 |
| ✗         |        | ✓         |
+-----------+        +-----------+
| Feature 3 |        | Feature 3 |
| ✓         |        | ✓         |
+-----------+        +-----------+
'''

"""
Version Comparison
"""
VERSION_COMPARE = '''
v1.0              v2.0              v3.0
+------+          +------+          +------+
| Old  |  --->    | Mid  |  --->    | New  |
+------+          +------+          +------+
Features:         Features:         Features:
- Basic           - Basic           - Basic
                  - Enhanced        - Enhanced
                                    - Advanced
                                    - Premium
'''

# ============================================================================
# SECTION 37: PATHWAY & JOURNEY MAPS
# ============================================================================

"""
Customer Journey
"""
JOURNEY = '''
Awareness -> Interest -> Decision -> Action -> Loyalty
    |          |           |          |         |
  [AD]      [DEMO]      [QUOTE]    [BUY]    [SUPPORT]
'''

"""
Process Pipeline
"""
PIPELINE = '''
[INPUT] --> [FILTER] --> [TRANSFORM] --> [VALIDATE] --> [OUTPUT]
              |              |              |
            [LOG]          [LOG]          [LOG]
'''

"""
User Flow
"""
USER_FLOW = '''
    [LANDING]
        |
    [SIGN UP?]
      /    \\
    YES    NO
    /        \\
[REGISTER] [BROWSE]
    |         |
    +----+----+
         |
    [DASHBOARD]
'''

# ============================================================================
# SECTION 38: LAYERED DIAGRAMS
# ============================================================================

"""
Geological Layers
"""
LAYERS_GEO = '''
==================== Surface
~~~~~~~~~~~~~~~~~~~~  Soil
--------------------  Rock Layer 1
====================  Rock Layer 2
^^^^^^^^^^^^^^^^^^^^  Mineral Layer
####################  Core
'''

"""
Data Layers
"""
DATA_LAYERS = '''
[User Interface Layer]
        |
[Business Logic Layer]
        |
[Data Access Layer]
        |
[Database Layer]
        |
[Storage Layer]
'''

"""
Security Layers
"""
SECURITY_LAYERS = '''
+------------------------+
| Firewall              | <- Layer 7
+------------------------+
| Encryption            | <- Layer 6
+------------------------+
| Authentication        | <- Layer 5
+------------------------+
| Authorization         | <- Layer 4
+------------------------+
| Audit                 | <- Layer 3
+------------------------+
| Monitoring            | <- Layer 2
+------------------------+
| Physical Security     | <- Layer 1
+------------------------+
'''

# ============================================================================
# SECTION 39: TRANSFORMATION SEQUENCES
# ============================================================================

"""
Data Transformation
"""
TRANSFORM = '''
RAW DATA          CLEAN DATA         ENRICHED DATA
+------+          +------+           +------+
| #### |  Clean   | #### |  Enrich   | #### |
| #### |  ----->  | **** |  ------>  | $$$$ |
| #### |          | **** |           | $$$$ |
+------+          +------+           +------+
'''

"""
State Transformation
"""
STATE_TRANSFORM = '''
[SOLID]  --Heat-->   [LIQUID]  --Heat-->   [GAS]
  ICE      +100°C      WATER      +100°C    STEAM
  |||                  ~~~                   ...
  |||                  ~~~                   ...
  |||                  ~~~                   ...
'''

"""
Evolution Sequence
"""
EVOLUTION = '''
[v1.0]      [v2.0]      [v3.0]      [v4.0]
  *    -->   **   -->    ***  -->    ****
Simple     Enhanced    Advanced    Complete
'''

# ============================================================================
# SECTION 40: FINAL SUMMARY - MASTER INDEX
# ============================================================================

"""
Complete Pattern Categories Index
"""
MASTER_INDEX = '''
+=============================================================+
|         ABSTRACT VISUAL PATTERNS - MASTER INDEX             |
+=============================================================+
| 01. Hierarchical Trees          | 21. Waveforms & Signals  |
| 02. Box Drawing & Frames        | 22. Circuit Diagrams     |
| 03. Flowcharts & Processes      | 23. Coordinate Systems   |
| 04. Data Structures             | 24. Org Charts           |
| 05. Tables & Matrices           | 25. Venn Diagrams        |
| 06. Timelines & Sequences       | 26. Musical Notation     |
| 07. Geometric Patterns          | 27. Layered Architecture |
| 08. Brackets & Delimiters       | 28. Error Indicators     |
| 09. Arrows & Pointers           | 29. File Trees w/Icons   |
| 10. Memory & Architecture       | 30. Combined Patterns    |
| 11. State Machines              | 31. Abstract Art         |
| 12. Bar Charts & Histograms     | 32. Decorative Elements  |
| 13. Class Diagrams & UML        | 33. Block Shading        |
| 14. Progress Indicators         | 34. Iconic Reps          |
| 15. Dividers & Separators       | 35. Alignment Guides     |
| 16. Text Banners                | 36. Comparisons          |
| 17. Mathematical Notations      | 37. Journey Maps         |
| 18. Calendar Layouts            | 38. Layered Diagrams     |
| 19. Molecular Structures        | 39. Transformations      |
| 20. Game Boards                 | 40. Master Index         |
+=============================================================+
|  Total Patterns: 100+  |  ASCII Only  |  Python 3.x       |
+=============================================================+
'''

# ============================================================================
# END OF ABSTRACT VISUAL PATTERNS COLLECTION
# ============================================================================

"""
USAGE EXAMPLES:

# Print a specific pattern
print(TREE_CLASSIC)

# Use in documentation
def document_structure():
    '''
    Project Structure:
    ''' + FILE_TREE_ICONS

# Create custom variations
my_flow = CONDITIONAL_FLOW.replace('[CHECK?]', '[VALIDATE?]')

# Combine patterns
dashboard = BOXED_HEADER + "\\n" + DASHBOARD + "\\n" + DIVIDERS

# Template for new patterns
def create_custom_box(content, width=40):
    border = '+' + '-' * (width - 2) + '+'
    padding = '|' + ' ' * (width - 2) + '|'
    text_line = f'| {content.center(width - 4)} |'
    return f"{border}\\n{padding}\\n{text_line}\\n{padding}\\n{border}"

"""

# ============================================================================
# METADATA
# ============================================================================

__version__ = "1.0.0"
__author__ = "GitHub Copilot"
__created__ = "2025-11-30"
__patterns_count__ = 100
__categories__ = 40
__license__ = "MIT"
