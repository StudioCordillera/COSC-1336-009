# Grid Layout System

## Overview
The `GridLayout` class provides a responsive grid-based positioning system for terminal UI components, similar to CSS Grid.

## Class: GridLayout

### Constructor
```python
GridLayout(rows, cols, margin=2, padding=2)
```

**Parameters:**
- `rows` (int): Number of grid rows
- `cols` (int): Number of grid columns
- `margin` (int): Space from terminal edges (default: 2)
- `padding` (int): Space between grid cells (default: 2)

**Terminal Dimensions:**
- Total Width: 78 characters
- Total Height: 35 rows

### Methods

#### `get_cell(row, col)`
Returns the absolute position and size of a grid cell.

**Returns:** `(y, x, width, height)`
- `y`: Absolute row position
- `x`: Absolute column position
- `width`: Cell width in characters
- `height`: Cell height in rows

**Example:**
```python
grid = GridLayout(rows=3, cols=2)
y, x, w, h = grid.get_cell(0, 0)  # Top-left cell
```

#### `get_inner_bounds(row, col, margin=1)`
Returns the inner bounds of a cell with margin applied.

**Returns:** `(y, x, width, height)`
- Inner area excludes margin space for cleaner component placement

**Example:**
```python
grid = GridLayout(rows=3, cols=2)
y, x, w, h = grid.get_inner_bounds(0, 0)  # Top-left cell with 1-char margin
```

#### `draw_grid()`
Draws the entire grid structure with boxes around each cell.

**Example:**
```python
grid = GridLayout(rows=3, cols=2)
grid.draw_grid()  # Visualizes the grid structure
```

## Grid Layouts by Demo

### Container Components (3x2)
```
+--------+--------+
| [0,0]  | [0,1]  |  Row 0: Wrapper, Panel
+--------+--------+
| [1,0]  | [1,1]  |  Row 1: Frame, Section
+--------+--------+
| [2,0]  | [2,1]  |  Row 2: Menu, Dialogue
+--------+--------+
```

### Display Components (4x2)
```
+--------+--------+
| [0,0]  | [0,1]  |  Row 0: Header (spans 2 cols)
+--------+--------+
| [1,0]  | [1,1]  |  Row 1: Labels/Prompt, Messages
+--------+--------+
| [2,0]  | [2,1]  |  Row 2: List, Tree
+--------+--------+
| [3,0]  | [3,1]  |  Row 3: Preview (spans 2 cols)
+--------+--------+
```

### Input Components (5x2)
```
+--------+--------+
| [0,0]  | [0,1]  |  Row 0: Input Fields, Buttons
+--------+--------+
| [1,0]  | [1,1]  |  Row 1: Text Fields, Dropdown
+--------+--------+
| [2,0]  | [2,1]  |  Row 2: Text Area, Selector
+--------+--------+
| [3,0]  | [3,1]  |  Row 3: Checkboxes, Toggles
+--------+--------+
| [4,0]  | [4,1]  |  Row 4: Disabled Button (spans 2 cols)
+--------+--------+
```

### Navigation Components (4x1)
```
+----------------+
| [0,0]          |  Row 0: Breadcrumb
+----------------+
| [1,0]          |  Row 1: Nav Controls & Buttons
+----------------+
| [2,0]          |  Row 2: Pagination
+----------------+
| [3,0]          |  Row 3: Tabs
+----------------+
```

### Specialized Components (4x2)
```
+--------+--------+
| [0,0]  | [0,1]  |  Row 0: Choice Objects, Param Fields
+--------+--------+
| [1,0]  | [1,1]  |  Row 1: Checkbox List, Directory Tree
+--------+--------+
| [2,0]  | [2,1]  |  Row 2: Status Bar (spans 2 cols)
+--------+--------+
| [3,0]  | [3,1]  |  Row 3: Info text (spans 2 cols)
+--------+--------+
```

## Usage Patterns

### Basic Grid Layout
```python
from Menus.terminal import draw_box
from ui_components import Component

# Create grid
grid = GridLayout(rows=2, cols=2)
grid.draw_grid()

# Place component in cell [0,0]
y, x, w, h = grid.get_inner_bounds(0, 0)
component = Component(y, x, w, h)
component.render()
```

### Spanning Multiple Columns
```python
# Get cell positions for columns 0 and 1
y, x, w, h = grid.get_cell(0, 0)
_, x2, w2, _ = grid.get_cell(0, 1)

# Calculate full width across both cells
full_width = (x2 + w2) - x

# Create component spanning both columns
component = Component(y, x, full_width, h)
component.render()
```

### Spanning Multiple Rows
```python
# Get cell positions for rows 0 and 1
y, x, w, h = grid.get_cell(0, 0)
y2, _, _, h2 = grid.get_cell(1, 0)

# Calculate full height across both rows
full_height = (y2 + h2) - y

# Create component spanning both rows
component = Component(y, x, w, full_height)
component.render()
```

## Cell Calculations

### Cell Dimensions
For a grid with `rows=3, cols=2, margin=2, padding=2`:

**Cell Width:**
```
cell_width = (78 - (2 * 2) - (2 - 1) * 2) / 2
           = (78 - 4 - 2) / 2
           = 72 / 2
           = 36 characters
```

**Cell Height:**
```
cell_height = (35 - (2 * 2) - (3 - 1) * 2) / 3
            = (35 - 4 - 4) / 3
            = 27 / 3
            = 9 rows
```

### Cell Positions
Cell [row, col] position:
```python
x = margin + col * (cell_width + padding)
y = margin + row * (cell_height + padding)
```

Example for [1, 1] (second row, second column):
```python
x = 2 + 1 * (36 + 2) = 2 + 38 = 40
y = 2 + 1 * (9 + 2) = 2 + 11 = 13
```

## Benefits

1. **Consistent Layouts**: All components follow grid structure
2. **Responsive**: Automatic calculation of cell dimensions
3. **Visual Clarity**: Grid boundaries make layout obvious
4. **Flexible**: Supports spanning multiple cells
5. **Easy to Use**: Simple API for positioning components

## Best Practices

1. **Use `get_inner_bounds()`** for component placement to add margin
2. **Draw grid first** with `draw_grid()` before rendering components
3. **Label cells** with descriptive headers for better organization
4. **Span strategically** - use column/row spanning for important components
5. **Test different grids** - try various row/column combinations for optimal layout

## Examples

### 2x2 Grid (Quad Layout)
```python
grid = GridLayout(rows=2, cols=2, margin=2, padding=2)
grid.draw_grid()
write(1, 3, "=== 2x2 QUAD LAYOUT ===")
```

### 3x1 Grid (Vertical Stack)
```python
grid = GridLayout(rows=3, cols=1, margin=2, padding=2)
grid.draw_grid()
write(1, 3, "=== 3x1 VERTICAL STACK ===")
```

### 1x3 Grid (Horizontal Strip)
```python
grid = GridLayout(rows=1, cols=3, margin=2, padding=2)
grid.draw_grid()
write(1, 3, "=== 1x3 HORIZONTAL STRIP ===")
```

### 4x4 Grid (Dense Layout)
```python
grid = GridLayout(rows=4, cols=4, margin=1, padding=1)
grid.draw_grid()
write(1, 3, "=== 4x4 DENSE GRID ===")
```

## Integration with Components

All UI components support grid-based positioning:

```python
# Example: Button in grid cell
grid = GridLayout(rows=3, cols=2)
y, x, w, h = grid.get_inner_bounds(1, 0)

button = Button(y+1, x+2, w-4, "Click Me")
button.render()
```

The `get_inner_bounds()` provides margins, and then you can add additional offsets for precise positioning within the cell.
