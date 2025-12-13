import os
import sys
from turtle import width
if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from MyClasses import displayLabels
nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph, longBar = displayLabels.nL, displayLabels.tab, displayLabels.tab1, displayLabels.lineGraph, displayLabels.shortBar, displayLabels.medBar, displayLabels.dashGraph, displayLabels.longBar
Project10=displayLabels.Context(10, '12/08/2025', 'HostpitalCalc', 'Patient Fee Calculations')

HEADERS = ['SUMMARY', 'ITEM', 'COST', 'TOTAL']
'''
nL: str = '\n'
tab: str = '    '  # 4 spaces
tab1: str = '     '  # 5 spaces
longBar: str = '--------------------------------------------------------------------------------'  # 80 dashes
medBar: str = '--------------------------------------------------'  # 50 dashes
shortBar: str = '------------'  # 12 dashes
dashGraph: str = '------------------------------------------------------------'  # 60 dashes
lineGraph: str = '____________________________________________________________'  # 60 underscores

f"{var:spec}"                # Variable + spec | Apply format spec | Returns formatted string
f"{var:width}"               # Variable + int | Minimum field width | Returns padded string
f"{var:<width}"              # Variable | Left align in width | Returns left-aligned string
f"{var:>width}"              # Variable | Right align in width | Returns right-aligned string
f"{var:^width}"              # Variable | Center in width | Returns centered string
f"{var:=width}"              # Number | Padding after sign | Returns sign + padding + number
f"{var:0width}"              # Number | Zero-padding | Returns zero-padded number
f"{var:+}"                   # Number | Force sign display | Returns +/- prefixed number
f"{var:-}"                   # Number | Sign only for negative | Returns number with - if negative
f"{var: }"                   # Number | Space for positive | Returns space/- prefixed number
'''
# nL, tab, tab1, lineGraph, shortBar, medBar, dashGraph
def printSummary():
    cols, rows = os.get_terminal_size()
    n=4
    rs = int(cols/(n+2))
    name, days, dayFees, medicine, medicineCost, procedure, procedureCost, totalCost=  'NAME', 9, 10000, 'MEDICINE', 1000, 'PROCEDURE', 1000, 100000
    print(cols, rows)
    print(f"{'-':->{cols}}")
    print(f"{' ': >{int(rs/n)}}{HEADERS[0]:>{int(rs/2)}}{'|':>{int(rs/2)}}{HEADERS[1]:^{rs}}{'|':^{int(rs/4)}}{HEADERS[2]:^{rs}}{'|':^{int(rs/4)}}{HEADERS[3]:^{rs}}")
    print(f"{'-':->{cols}}")
    print(f"{' ': >{int(rs/n)}}{'Days':>{int(rs/2)}}{'|':>{int(rs/2)}}{days:^{rs}}{'|':^{int(rs/4)}}{dayFees:^{rs}}{'|':^{int(rs/4)}}{dayFees:^{rs}}")
    print(f"{' ': >{int(rs/n)}}{'Medicine':>{int(rs/2)}}{'|':>{int(rs/2)}}{medicine:^{rs}}{'|':^{int(rs/4)}}{medicineCost:^{rs}}{'|':^{int(rs/4)}}{dayFees+medicineCost:^{rs}}")
    print(f"{' ': >{int(rs/n)}}{'Procedure':>{int(rs/2)}}{'|':>{int(rs/2)}}{procedure:^{rs}}{'|':^{int(rs/4)}}{procedureCost:^{rs}}{'|':^{int(rs/4)}}{dayFees+medicineCost+procedureCost:^{rs}}")
    print(f"{'-':->{cols}}{nL}{' ': >{int(rs/n)}}{'Days':>{int(rs/2)}}{'|':>{int(rs/2)}}{('Total:' + (' '*(int(rs/12))) + str(totalCost)):^{rs}}")

printSummary()


