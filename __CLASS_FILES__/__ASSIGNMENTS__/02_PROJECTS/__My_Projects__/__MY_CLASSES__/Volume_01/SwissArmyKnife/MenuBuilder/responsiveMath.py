import os
class Frame:

    def __init__(self, topM, bottomM, leftM, rightM):

        self.cols, self.rows = os.get_terminal_size()

        self.topM = topM
        self.bottomM = bottomM
        self.leftM = leftM
        self.rightM = rightM
    
        # Now calculate margins and ranges
        self.getScreen()
        self.get_coord()

        self.x:int
        self.y:int
        self.xRange:int
        self.yRange:int
        self.xUnit:int
        self.yUnit:int

    def getScreen(self):
        # Adaptive margin scaling: prioritize content, shrink margins aggressively
        minContentCols = 40  # Need space for nested boxes
        minContentRows = 15  # Need space for nested boxes
        
        # Calculate desired margins
        leftCols = max(0, round((self.leftM / 100) * self.cols))
        rightCols = max(0, round((self.rightM / 100) * self.cols))
        topRows = max(0, round((self.topM / 100) * self.rows))
        bottomRows = max(0, round((self.bottomM / 100) * self.rows))
        
        # Aggressively cap margins to prioritize content
        availableCols = self.cols
        availableRows = self.rows
        
        # If we can't fit minimum content with margins, reduce margins to 1 or 0
        if availableCols - leftCols - rightCols < minContentCols:
            totalMarginNeeded = availableCols - minContentCols
            if totalMarginNeeded < 2:
                leftCols = 0
                rightCols = 0
            else:
                # Split remaining margin space
                leftCols = min(1, totalMarginNeeded // 2)
                rightCols = min(1, totalMarginNeeded - leftCols)
        
        if availableRows - topRows - bottomRows < minContentRows:
            totalMarginNeeded = availableRows - minContentRows
            if totalMarginNeeded < 2:
                topRows = 0
                bottomRows = 0
            else:
                topRows = min(1, totalMarginNeeded // 2)
                bottomRows = min(1, totalMarginNeeded - topRows)
        
        self.xRange = max(minContentCols, self.cols - leftCols - rightCols)
        self.yRange = max(minContentRows, self.rows - topRows - bottomRows)
        self.xUnit=self.getUnitNum(self.xRange)
        self.yUnit=self.getUnitNum(self.yRange)

    def get_coord(self):

        self.x = max(1, round((self.leftM / 100) * self.cols))
        self.y = max(1, round((self.topM / 100) * self.rows))

    def getUnitNum(self, range):
        baseNum = range / 100
        return baseNum

    def setXScale(self, percent):
        xScale = max(1, round(percent * self.getUnitNum(self.xRange)))
        return xScale
    
    def setYScale(self, percent):
        yScale = max(1, round(percent * self.getUnitNum(self.yRange)))
        return yScale
    
    def refresh(self):
        self.cols, self.rows = os.get_terminal_size()
        self.getScreen()
        self.get_coord()

class Box:

    def __init__(self, parentFrame: 'Frame | Box', topM, bottomM, leftM, rightM, content="", size_mode='percentage', flex_grow=0, flex_shrink=1):
        self.parent = parentFrame
        self.topM = topM
        self.bottomM = bottomM
        self.leftM = leftM
        self.rightM = rightM
        self.content = content
        self.size_mode = size_mode
        self.flex_grow = flex_grow
        self.flex_shrink = flex_shrink
        
        # Calculate minimum sizes based on content
        self.minWidth = len(content) + 4 if content else 5
        self.minHeight = 3
        
        # Scrolling support
        self.scrollOffset = 0
        self.contentHeight = self.minHeight  # Virtual height (can exceed yRange)
        self.maxScroll = 0
        
        self.x:int
        self.y:int
        self.xRange:int
        self.yRange:int
        self.xUnit:int
        self.yUnit:int
        
        self.getScreen()
        self.get_coord()

    def getScreen(self):
        # Box uses parent Frame's dimensions instead of terminal size
        # Adaptive margin scaling for nested boxes - prioritize content
        minContentCols = 5
        minContentRows = 3
        
        leftCols = max(0, round((self.leftM / 100) * self.parent.xRange))
        rightCols = max(0, round((self.rightM / 100) * self.parent.xRange))
        topRows = max(0, round((self.topM / 100) * self.parent.yRange))
        bottomRows = max(0, round((self.bottomM / 100) * self.parent.yRange))
        
        # If content doesn't fit, reduce margins to zero
        if self.parent.xRange - leftCols - rightCols < minContentCols:
            remaining = self.parent.xRange - minContentCols
            if remaining < 1:
                leftCols = 0
                rightCols = 0
            else:
                leftCols = remaining // 2
                rightCols = remaining - leftCols
        
        if self.parent.yRange - topRows - bottomRows < minContentRows:
            remaining = self.parent.yRange - minContentRows
            if remaining < 1:
                topRows = 0
                bottomRows = 0
            else:
                topRows = remaining // 2
                bottomRows = remaining - topRows
        
        self.xRange = max(minContentCols, self.parent.xRange - leftCols - rightCols)
        self.yRange = max(minContentRows, self.parent.yRange - topRows - bottomRows)
        self.xUnit = self.getUnitNum(self.xRange)
        self.yUnit = self.getUnitNum(self.yRange)
    
    def get_coord(self):
        # Calculate margin offsets from parent's top-left
        leftOffset = max(0, round((self.leftM / 100) * self.parent.xRange))
        topOffset = max(0, round((self.topM / 100) * self.parent.yRange))
        
        # Position is parent's position + margin offset
        self.x = self.parent.x + leftOffset
        self.y = self.parent.y + topOffset
    
    def getUnitNum(self, range):
        baseNum = range / 100
        return baseNum

    def setXScale(self, percent):
        xScale = max(1, round(percent * self.getUnitNum(self.xRange)))
        return xScale
    
    def setYScale(self, percent):
        yScale = max(1, round(percent * self.getUnitNum(self.yRange)))
        return yScale
    
    def refresh(self):
        self.getScreen()
        self.get_coord()
        self.updateScroll()
    
    def updateScroll(self):
        # Update max scroll based on content vs viewport
        self.maxScroll = max(0, self.contentHeight - self.yRange)
        self.scrollOffset = max(0, min(self.scrollOffset, self.maxScroll))
    
    def scroll(self, delta):
        # Scroll by delta lines (positive = down, negative = up)
        self.scrollOffset = max(0, min(self.scrollOffset + delta, self.maxScroll))
    
    def getVisibleY(self):
        # Get the actual Y coordinate adjusted for scroll
        return self.y - self.scrollOffset

class TextBox(Box):
    
    def __init__(self, parent, content, topM=0, bottomM=0, leftM=0, rightM=0, flex_grow=0, flex_shrink=1, h_align='left', v_align='top'):
        self.h_align = h_align  # 'left', 'center', 'right'
        self.v_align = v_align  # 'top', 'center', 'bottom'
        super().__init__(parent, topM, bottomM, leftM, rightM, content, 'content', flex_grow, flex_shrink)
    
    def getScreen(self):
        # TextBox sizes itself based on content, not percentages
        self.xRange = self.minWidth
        self.yRange = self.minHeight
        self.xUnit = self.getUnitNum(self.xRange)
        self.yUnit = self.getUnitNum(self.yRange)
    
    def getTextPosition(self):
        """Calculate text position based on alignment within the box"""
        contentWidth = len(self.content)
        availableWidth = self.xRange - 4  # Subtract borders and padding
        availableHeight = self.yRange - 2  # Subtract top and bottom borders
        
        # Horizontal alignment
        if self.h_align == 'left':
            text_x = self.x + 2  # Left padding
        elif self.h_align == 'center':
            text_x = self.x + 2 + (availableWidth - contentWidth) // 2
        elif self.h_align == 'right':
            text_x = self.x + 2 + (availableWidth - contentWidth)
        else:
            text_x = self.x + 2
        
        # Vertical alignment
        if self.v_align == 'top':
            text_y = self.y + 1
        elif self.v_align == 'center':
            text_y = self.y + 1 + availableHeight // 2
        elif self.v_align == 'bottom':
            text_y = self.y + self.yRange - 2
        else:
            text_y = self.y + 1
        
        return text_x, text_y

class FlexBox:

    def __init__(self, parent: 'Frame | Box', direction='row', justify='start', gap=0):
        self.parent = parent
        self.direction = direction
        self.justify = justify
        self.gap = gap
        self.children = []
        
        # Initialize from parent using getattr to avoid linting issues
        self.x: int = getattr(parent, 'x')
        self.y: int = getattr(parent, 'y')
        self.xRange: int = getattr(parent, 'xRange')
        self.yRange: int = getattr(parent, 'yRange')

    def add(self, box):
        self.children.append(box)
        self.layout()

    def layout(self):
        if not self.children:
            return
            
        totalGap = self.gap * (len(self.children) - 1)
        
        if self.direction == 'row':
            availableSpace = self.xRange - totalGap
            
            # Pass 1: Calculate minimum space needed
            minTotalSize = sum(getattr(c, 'minWidth', c.xRange) for c in self.children)
            
            # Pass 2: Distribute space
            if availableSpace >= minTotalSize:
                # Extra space - distribute to flex_grow boxes
                totalGrow = sum(getattr(c, 'flex_grow', 0) for c in self.children)
                extraSpace = availableSpace - minTotalSize
                
                for child in self.children:
                    minW = getattr(child, 'minWidth', child.xRange)
                    grow = getattr(child, 'flex_grow', 0)
                    if totalGrow > 0 and grow > 0:
                        child.xRange = minW + int((grow / totalGrow) * extraSpace)
                    else:
                        child.xRange = minW
            else:
                # Tight space - use minimums
                for child in self.children:
                    child.xRange = getattr(child, 'minWidth', child.xRange)
            
            # Position children
            childSizes = [c.xRange for c in self.children]
            totalSize = sum(childSizes)
            
            if self.justify == 'start':
                offset = 0
            elif self.justify == 'center':
                offset = max(0, (availableSpace - totalSize) // 2)
            elif self.justify == 'end':
                offset = max(0, availableSpace - totalSize)
            elif self.justify == 'space-between':
                offset = 0
                if len(self.children) > 1 and totalSize < availableSpace:
                    self.gap = (availableSpace - totalSize) // (len(self.children) - 1)
            
            x = self.x + offset
            for child in self.children:
                child.x = x
                child.y = self.y
                x += child.xRange + self.gap
                
        else:  # column
            availableSpace = self.yRange - totalGap
            
            # Pass 1: Calculate minimum space needed
            minTotalSize = sum(getattr(c, 'minHeight', c.yRange) for c in self.children)
            
            # Pass 2: Distribute space
            if availableSpace >= minTotalSize:
                # Extra space - distribute to flex_grow boxes
                totalGrow = sum(getattr(c, 'flex_grow', 0) for c in self.children)
                extraSpace = availableSpace - minTotalSize
                
                for child in self.children:
                    minH = getattr(child, 'minHeight', child.yRange)
                    grow = getattr(child, 'flex_grow', 0)
                    if totalGrow > 0 and grow > 0:
                        child.yRange = minH + int((grow / totalGrow) * extraSpace)
                    else:
                        child.yRange = minH
            else:
                # Tight space - use minimums
                for child in self.children:
                    child.yRange = getattr(child, 'minHeight', child.yRange)
            
            # Position children
            childSizes = [c.yRange for c in self.children]
            totalSize = sum(childSizes)
            
            if self.justify == 'start':
                offset = 0
            elif self.justify == 'center':
                offset = max(0, (availableSpace - totalSize) // 2)
            elif self.justify == 'end':
                offset = max(0, availableSpace - totalSize)
            elif self.justify == 'space-between':
                offset = 0
                if len(self.children) > 1 and totalSize < availableSpace:
                    self.gap = (availableSpace - totalSize) // (len(self.children) - 1)
            
            y = self.y + offset
            for child in self.children:
                child.x = self.x
                child.y = y
                y += child.yRange + self.gap
    
    def refresh(self):
        self.x = self.parent.x
        self.y = self.parent.y
        self.xRange = self.parent.xRange
        self.yRange = self.parent.yRange
        self.layout()
    
    def setContentHeight(self, height):
        # Allow FlexBox to have virtual height larger than viewport
        if hasattr(self, 'parent') and hasattr(self.parent, 'contentHeight'):
            self.parent.contentHeight = height
            self.parent.updateScroll()

class RowBox(Box):
    """Box that layouts children horizontally in a row"""
    
    def __init__(self, parent: 'Frame | Box', topM=0, bottomM=0, leftM=0, rightM=0, gap=1):
        super().__init__(parent, topM, bottomM, leftM, rightM)
        self.children = []
        self.gap = gap
    
    def add(self, child):
        self.children.append(child)
        self.layout()
    
    def layout(self):
        if not self.children:
            return
        
        # Calculate available width
        totalGap = self.gap * (len(self.children) - 1)
        availableWidth = self.xRange - totalGap
        widthPerChild = availableWidth // len(self.children)
        
        # Position children horizontally
        x = self.x
        for child in self.children:
            child.x = x
            child.y = self.y
            child.xRange = widthPerChild
            child.yRange = self.yRange
            x += widthPerChild + self.gap
    
    def refresh(self):
        super().refresh()
        self.layout()

class ColumnBox(Box):
    """Box that layouts children vertically in a column"""
    
    def __init__(self, parent: 'Frame | Box', topM=0, bottomM=0, leftM=0, rightM=0, gap=1):
        super().__init__(parent, topM, bottomM, leftM, rightM)
        self.children = []
        self.gap = gap
    
    def add(self, child):
        self.children.append(child)
        self.layout()
    
    def layout(self):
        if not self.children:
            return
        
        # Calculate available height
        totalGap = self.gap * (len(self.children) - 1)
        availableHeight = self.yRange - totalGap
        heightPerChild = availableHeight // len(self.children)
        
        # Position children vertically
        y = self.y
        for child in self.children:
            child.x = self.x
            child.y = y
            child.xRange = self.xRange
            child.yRange = heightPerChild
            y += heightPerChild + self.gap
    
    def refresh(self):
        super().refresh()
        self.layout()
