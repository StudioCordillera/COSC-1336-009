

"""
Nested Box Demo - Using Refactored Responsive Display System

Goal:
+----------------------------------------------+
|  OUTER BOX                                   |
|  +---------------------------------------+   |
|  |  INNER BOX                            |   |
|  |  +--------------------------------+   |   |
|  |  |  NESTED BOX                    |   |   |
|  |  +--------------------------------+   |   |
|  +---------------------------------------+   |
+----------------------------------------------+
"""

from responsiveDisplay import createFrame, Box, AdaptiveDimensionCalculator
from renderHelpers import drawBox, clearScreen, hideCursor, showCursor
import os
import time


# Create components
frame = createFrame(margins=10)

dimCalc = AdaptiveDimensionCalculator()
outerBox = Box(frame, dimCalc, topMargin=5, bottomMargin=5, leftMargin=5, rightMargin=5, label="OUTER BOX")
innerBox = Box(outerBox, dimCalc, topMargin=5, bottomMargin=5, leftMargin=5, rightMargin=5, label="INNER BOX")
nestedBox = Box(innerBox, dimCalc, topMargin=5, bottomMargin=5, leftMargin=5, rightMargin=5, label="NESTED BOX")


def render():
    """Refresh and draw all boxes"""
    frame.refresh()
    outerBox.refresh()
    innerBox.refresh()
    nestedBox.refresh()
    
    clearScreen()
    drawBox(outerBox.x, outerBox.y, outerBox.xRange, outerBox.yRange, outerBox.label)
    drawBox(innerBox.x, innerBox.y, innerBox.xRange, innerBox.yRange, innerBox.label)
    drawBox(nestedBox.x, nestedBox.y, nestedBox.xRange, nestedBox.yRange, nestedBox.label)
    
    print(f"\n\nTerminal: {frame.cols}x{frame.rows} | Resize to see nested boxes adapt (Ctrl+C to quit)")


def main():
    hideCursor()
    prevSize = None
    
    try:
        while True:
            currSize = os.get_terminal_size()
            if currSize != prevSize:
                render()
                prevSize = currSize
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        showCursor()
        print("\n")


if __name__ == "__main__":
    main()


