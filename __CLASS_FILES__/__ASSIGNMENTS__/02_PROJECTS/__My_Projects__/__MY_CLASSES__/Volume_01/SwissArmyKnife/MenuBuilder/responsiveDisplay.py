"""
Responsive CLI Display System - Refactored with Design Patterns

Design Patterns Used:
- Composite: Component base class for Frame/Box hierarchy
- Strategy: Layout algorithms (Horizontal, Vertical, Flex)
- Builder: Fluent interface for box construction
- Template Method: Shared rendering pipeline
- Dependency Injection: All dependencies injected through constructors
"""

import os
from abc import ABC, abstractmethod
from typing import Optional, List, Tuple, Protocol


# ============================================================================
# DEPENDENCY INJECTION - Interfaces (Protocols)
# ============================================================================

class TerminalProvider(Protocol):
    """Interface for terminal size providers (DI)"""
    def getSize(self) -> Tuple[int, int]:
        """Returns (columns, rows)"""
        ...


class DimensionCalculator(Protocol):
    """Interface for dimension calculation strategies (DI)"""
    def calculateDimensions(self, totalSize: int, marginPercent: float, 
                           minContent: int) -> Tuple[int, int]:
        """
        Calculate actual margin and content size
        Returns (marginSize, contentSize)
        """
        ...


# ============================================================================
# CONCRETE IMPLEMENTATIONS - Injectable Dependencies
# ============================================================================

class OsTerminalProvider:
    """Default terminal provider using os module"""
    def getSize(self) -> Tuple[int, int]:
        return os.get_terminal_size()


class AdaptiveDimensionCalculator:
    """Adaptive dimension calculator that prioritizes content"""
    def calculateDimensions(self, totalSize: int, marginPercent: float, 
                           minContent: int) -> Tuple[int, int]:
        # Calculate desired margin
        margin = max(0, round((marginPercent / 100) * totalSize))
        
        # If content won't fit, reduce margin
        if totalSize - margin < minContent:
            margin = max(0, totalSize - minContent)
        
        content = max(minContent, totalSize - margin)
        return margin, content


# ============================================================================
# COMPOSITE PATTERN - Component Base
# ============================================================================

class Component(ABC):
    """Base component for all display elements (Composite Pattern)"""
    
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.xRange: int = 0
        self.yRange: int = 0
        self.parent: Optional['Component'] = None
    
    @abstractmethod
    def calculateDimensions(self):
        """Calculate width and height based on constraints"""
        pass
    
    @abstractmethod
    def calculatePosition(self):
        """Calculate x,y position based on parent"""
        pass
    
    def refresh(self):
        """Template Method: Standard refresh pipeline"""
        self.calculateDimensions()
        self.calculatePosition()
        self.postRefreshHook()
    
    def postRefreshHook(self):
        """Hook for subclasses to add custom refresh behavior"""
        pass
    
    def getUnitValue(self, rangeVal: int) -> float:
        """Convert range to unit value for percentage calculations"""
        return rangeVal / 100


# ============================================================================
# ROOT CONTAINER - Frame
# ============================================================================

class Frame(Component):
    """Root container tied to terminal dimensions (with DI)"""
    
    def __init__(self, 
                 terminalProvider: TerminalProvider,
                 dimensionCalculator: DimensionCalculator,
                 topMargin: float = 0, 
                 bottomMargin: float = 0, 
                 leftMargin: float = 0, 
                 rightMargin: float = 0):
        super().__init__()
        
        # INJECTED DEPENDENCIES
        self.terminalProvider = terminalProvider
        self.dimensionCalculator = dimensionCalculator
        
        self.topMargin = topMargin
        self.bottomMargin = bottomMargin
        self.leftMargin = leftMargin
        self.rightMargin = rightMargin
        
        self.cols: int = 0
        self.rows: int = 0
        
        self.refresh()
    
    def calculateDimensions(self):
        """Calculate frame size using injected terminal provider and calculator"""
        # Use injected terminal provider
        self.cols, self.rows = self.terminalProvider.getSize()
        
        minContentWidth = 40
        minContentHeight = 15
        
        # Use injected dimension calculator for both margins
        leftMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            self.cols, self.leftMargin, minContentWidth
        )
        rightMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            self.cols, self.rightMargin, minContentWidth
        )
        
        # Ensure total margins don't exceed available space
        totalHMargin = leftMarginSize + rightMarginSize
        if self.cols - totalHMargin < minContentWidth:
            remaining = self.cols - minContentWidth
            leftMarginSize = remaining // 2
            rightMarginSize = remaining - leftMarginSize
        
        topMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            self.rows, self.topMargin, minContentHeight
        )
        bottomMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            self.rows, self.bottomMargin, minContentHeight
        )
        
        # Ensure total margins don't exceed available space
        totalVMargin = topMarginSize + bottomMarginSize
        if self.rows - totalVMargin < minContentHeight:
            remaining = self.rows - minContentHeight
            topMarginSize = remaining // 2
            bottomMarginSize = remaining - topMarginSize
        
        self.xRange = max(minContentWidth, self.cols - leftMarginSize - rightMarginSize)
        self.yRange = max(minContentHeight, self.rows - topMarginSize - bottomMarginSize)
    
    def calculatePosition(self):
        """Frame position is based on margins from terminal origin"""
        self.x = max(0, round((self.leftMargin / 100) * self.cols))
        self.y = max(0, round((self.topMargin / 100) * self.rows))


# ============================================================================
# STRATEGY PATTERN - Layout Strategies
# ============================================================================

class LayoutStrategy(ABC):
    """Strategy interface for different layout algorithms"""
    
    @abstractmethod
    def layout(self, children: List[Component], bounds: tuple, gap: int):
        """
        Position and size children within bounds
        Args:
            children: List of components to layout
            bounds: (x, y, width, height) available space
            gap: spacing between children
        """
        pass


class HorizontalLayout(LayoutStrategy):
    """Layout children in a row with equal widths"""
    
    def layout(self, children: List[Component], bounds: tuple, gap: int):
        if not children:
            return
        
        x, y, width, height = bounds
        totalGap = gap * (len(children) - 1)
        availableWidth = width - totalGap
        widthPerChild = availableWidth // len(children)
        
        currentX = x
        for child in children:
            child.x = currentX
            child.y = y
            child.xRange = widthPerChild
            child.yRange = height
            currentX += widthPerChild + gap


class VerticalLayout(LayoutStrategy):
    """Layout children in a column with equal heights"""
    
    def layout(self, children: List[Component], bounds: tuple, gap: int):
        if not children:
            return
        
        x, y, width, height = bounds
        totalGap = gap * (len(children) - 1)
        availableHeight = height - totalGap
        heightPerChild = availableHeight // len(children)
        
        currentY = y
        for child in children:
            child.x = x
            child.y = currentY
            child.xRange = width
            child.yRange = heightPerChild
            currentY += heightPerChild + gap


# ============================================================================
# COMPOSITE - Box (Leaf and Container)
# ============================================================================

class Box(Component):
    """Box component that can be nested (Composite Pattern with DI)"""
    
    def __init__(self, 
                 parent: Component,
                 dimensionCalculator: DimensionCalculator,
                 topMargin: float = 0, 
                 bottomMargin: float = 0,
                 leftMargin: float = 0, 
                 rightMargin: float = 0,
                 label: str = ""):
        super().__init__()
        self.parent = parent
        
        # INJECTED DEPENDENCY
        self.dimensionCalculator = dimensionCalculator
        
        self.topMargin = topMargin
        self.bottomMargin = bottomMargin
        self.leftMargin = leftMargin
        self.rightMargin = rightMargin
        self.label = label
        
        # Optional layout strategy for container boxes
        self.layoutStrategy: Optional[LayoutStrategy] = None
        self.children: List[Component] = []
        self.gap: int = 1
        
        self.refresh()
    
    def calculateDimensions(self):
        """Calculate box size using injected dimension calculator"""
        parentWidth = getattr(self.parent, 'xRange', 0)
        parentHeight = getattr(self.parent, 'yRange', 0)
        
        minWidth = 5
        minHeight = 3
        
        # Use injected dimension calculator
        leftMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            parentWidth, self.leftMargin, minWidth
        )
        rightMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            parentWidth, self.rightMargin, minWidth
        )
        
        # Ensure total margins don't exceed parent width
        totalHMargin = leftMarginSize + rightMarginSize
        if parentWidth - totalHMargin < minWidth:
            remaining = parentWidth - minWidth
            leftMarginSize = remaining // 2
            rightMarginSize = remaining - leftMarginSize
        
        topMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            parentHeight, self.topMargin, minHeight
        )
        bottomMarginSize, _ = self.dimensionCalculator.calculateDimensions(
            parentHeight, self.bottomMargin, minHeight
        )
        
        # Ensure total margins don't exceed parent height
        totalVMargin = topMarginSize + bottomMarginSize
        if parentHeight - totalVMargin < minHeight:
            remaining = parentHeight - minHeight
            topMarginSize = remaining // 2
            bottomMarginSize = remaining - topMarginSize
        
        self.xRange = max(minWidth, parentWidth - leftMarginSize - rightMarginSize)
        self.yRange = max(minHeight, parentHeight - topMarginSize - bottomMarginSize)
    
    def calculatePosition(self):
        """Calculate position relative to parent"""
        parentX = getattr(self.parent, 'x', 0)
        parentY = getattr(self.parent, 'y', 0)
        parentWidth = getattr(self.parent, 'xRange', 0)
        parentHeight = getattr(self.parent, 'yRange', 0)
        
        leftOffset = max(0, round((self.leftMargin / 100) * parentWidth))
        topOffset = max(0, round((self.topMargin / 100) * parentHeight))
        
        self.x = parentX + leftOffset
        self.y = parentY + topOffset
    
    def postRefreshHook(self):
        """After refreshing self, layout children if we have a strategy"""
        if self.layoutStrategy and self.children:
            bounds = (self.x, self.y, self.xRange, self.yRange)
            self.layoutStrategy.layout(self.children, bounds, self.gap)
            
            # Refresh children after layout
            for child in self.children:
                child.refresh()
    
    def addChild(self, child: Component):
        """Add a child component (for container boxes)"""
        self.children.append(child)
        child.parent = self
        if self.layoutStrategy:
            self.postRefreshHook()
    
    def setLayout(self, strategy: LayoutStrategy, gap: int = 1):
        """Set the layout strategy for this container"""
        self.layoutStrategy = strategy
        self.gap = gap


# ============================================================================
# BUILDER PATTERN - Fluent Box Construction
# ============================================================================

class BoxBuilder:
    """Builder for creating boxes with fluent interface (with DI)"""
    
    def __init__(self, parent: Component, dimensionCalculator: DimensionCalculator):
        self.parentComponent = parent
        self.dimensionCalc = dimensionCalculator
        self.topValue = 0.0
        self.bottomValue = 0.0
        self.leftValue = 0.0
        self.rightValue = 0.0
        self.layoutStrat = None
        self.gapValue = 1
        self.labelValue = ""
    
    def margins(self, allSides: float) -> 'BoxBuilder':
        """Set all margins to same value"""
        self.topValue = self.bottomValue = self.leftValue = self.rightValue = allSides
        return self
    
    def marginTop(self, value: float) -> 'BoxBuilder':
        self.topValue = value
        return self
    
    def marginBottom(self, value: float) -> 'BoxBuilder':
        self.bottomValue = value
        return self
    
    def marginLeft(self, value: float) -> 'BoxBuilder':
        self.leftValue = value
        return self
    
    def marginRight(self, value: float) -> 'BoxBuilder':
        self.rightValue = value
        return self
    
    def label(self, text: str) -> 'BoxBuilder':
        self.labelValue = text
        return self
    
    def horizontalLayout(self, gap: int = 1) -> 'BoxBuilder':
        """Set horizontal (row) layout"""
        self.layoutStrat = HorizontalLayout()
        self.gapValue = gap
        return self
    
    def verticalLayout(self, gap: int = 1) -> 'BoxBuilder':
        """Set vertical (column) layout"""
        self.layoutStrat = VerticalLayout()
        self.gapValue = gap
        return self
    
    def build(self) -> Box:
        """Create the box with injected dependencies"""
        box = Box(
            self.parentComponent, 
            self.dimensionCalc,
            self.topValue, 
            self.bottomValue, 
            self.leftValue, 
            self.rightValue,
            self.labelValue
        )
        if self.layoutStrat:
            box.setLayout(self.layoutStrat, self.gapValue)
        return box


# ============================================================================
# CONVENIENCE FUNCTIONS (with default DI)
# ============================================================================

def createFrame(margins: float = 10, 
                terminalProvider: Optional[TerminalProvider] = None,
                dimensionCalculator: Optional[DimensionCalculator] = None) -> Frame:
    """Create a frame with equal margins on all sides (injects default dependencies)"""
    if terminalProvider is None:
        terminalProvider = OsTerminalProvider()
    if dimensionCalculator is None:
        dimensionCalculator = AdaptiveDimensionCalculator()
    
    return Frame(terminalProvider, dimensionCalculator, margins, margins, margins, margins)


def createRowBox(parent: Component, 
                  margins: float = 5, 
                  gap: int = 1,
                  dimensionCalculator: Optional[DimensionCalculator] = None) -> Box:
    """Create a box with horizontal layout"""
    if dimensionCalculator is None:
        dimensionCalculator = AdaptiveDimensionCalculator()
    
    return BoxBuilder(parent, dimensionCalculator).margins(margins).horizontalLayout(gap).build()


def createColumnBox(parent: Component, 
                     margins: float = 5, 
                     gap: int = 1,
                     dimensionCalculator: Optional[DimensionCalculator] = None) -> Box:
    """Create a box with vertical layout"""
    if dimensionCalculator is None:
        dimensionCalculator = AdaptiveDimensionCalculator()
    
    return BoxBuilder(parent, dimensionCalculator).margins(margins).verticalLayout(gap).build()
