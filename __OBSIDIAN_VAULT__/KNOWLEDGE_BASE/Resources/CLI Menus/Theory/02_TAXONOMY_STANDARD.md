# Taxonomy Standard - Component Classification & Complexity System

> **Version 1.0 | Perfected from CLI-Menu-Component-Taxonomy.md | 2025-12-06**

---

## Table of Contents

1. [Overview](#overview)
2. [Classification Framework](#classification-framework)
3. [Deployment Complexity Layers](#deployment-complexity-layers)
4. [Component Type Categories](#component-type-categories)
5. [Metrics & Measurement](#metrics--measurement)
6. [Difficulty Rating System](#difficulty-rating-system)
7. [State Complexity Patterns](#state-complexity-patterns)
8. [Complete Component Catalog](#complete-component-catalog)
9. [Usage Guidelines](#usage-guidelines)

---

## Overview

### Purpose
The Taxonomy Standard provides a systematic classification framework for CLI menu system components based on:
- **Deployment Complexity** (implementation effort)
- **Architectural Layer** (dependency depth)
- **Implementation Difficulty** (skill level required)

### Scope
Applicable to:
- CLI component libraries
- Terminal UI frameworks  
- Menu system architectures
- Interactive console applications

### Design Philosophy
- **Objective Classification**: Measurable metrics over subjective assessment
- **Layered Architecture**: Clear dependency hierarchies
- **Progressive Complexity**: Predictable escalation from simple to complex
- **Practical Utility**: Real-world implementation guidance

---

## Classification Framework

### Primary Classification Dimensions

#### 1. Deployment Complexity Layers (0-9)
Hierarchical levels based on dependency depth and instantiation effort.

```
Layer 0: Terminal Primitives      (1-5 LOC, 0 state vars)
Layer 1: Styled Primitives         (5-20 LOC, 0-2 state vars)
Layer 2: Basic Interactive         (20-80 LOC, 2-5 state vars)
Layer 3: Container Components      (80-200 LOC, 5-12 state vars)
Layer 4: Complex Interactive       (200-500 LOC, 12-20 state vars)
Layer 5: Composite Views           (500-1000 LOC, 20-40 state vars)
Layer 6: Advanced Data Views       (1000-2000 LOC, 40-60 state vars)
Layer 7: Navigation & Flow Systems (2000-4000 LOC, 60-100 state vars)
Layer 8: Graph & Spatial Nav       (4000-8000 LOC, 100-150 state vars)
Layer 9: Application-Level Widgets (8000+ LOC, 150+ state vars)
```

#### 2. Component Type Categories
Functional classification by primary purpose.

| Type | Purpose | Characteristics |
|------|---------|-----------------|
| **Primitive** | Atomic visual units | No logic, direct output |
| **Styled Element** | Decorated primitives | Styling only, immutable |
| **Input Control** | User interaction | Event handling, validation |
| **Container** | Component grouping | Child management, layout |
| **Layout** | Spatial arrangement | Positioning, flow control |
| **View** | Data presentation | Rendering, virtualization |
| **Navigation** | Flow control | Routing, state preservation |
| **Animation** | Temporal effects | Frame-based, timed |
| **Composite** | Multi-component system | Orchestration, lifecycle |
| **Application** | Top-level widget | Full app functionality |

#### 3. Implementation Difficulty Rating
Skill level required for implementation.

| Rating | Description | LOC Range | State Vars | Event Handlers |
|--------|-------------|-----------|------------|----------------|
| ⭐ | Trivial | 1-20 | 0-2 | 0 |
| ⭐⭐ | Easy | 20-100 | 2-5 | 1-2 |
| ⭐⭐⭐ | Medium | 100-300 | 5-15 | 2-8 |
| ⭐⭐⭐⭐ | Hard | 300-1000 | 15-40 | 8-15 |
| ⭐⭐⭐⭐⭐ | Very Hard | 1000+ | 40+ | 15+ |

---

## Deployment Complexity Layers

### Layer 0: Terminal Primitives
**Complexity: 1-5 | LOC: 1-5 | State: 0 | Difficulty: ⭐**

Atomic building blocks with zero abstraction.

| Component | Type | Attributes | Dependencies | Behaviors |
|-----------|------|------------|--------------|-----------|
| Character | Primitive | `char: str` | None | Direct terminal output |
| Symbol | Primitive | `unicode: int, fallback: str` | None | Unicode/ASCII fallback |
| Color Code | Primitive | `ansi_code: int` | None | ANSI color escape |
| Coordinate | Primitive | `x: int, y: int` | None | Position representation |
| Dimension | Primitive | `width: int, height: int` | None | Size representation |

**Characteristics**:
- Zero state variables
- No event handling
- Direct terminal API calls
- Immutable values
- No rendering logic (pass-through)

---

### Layer 1: Styled Primitives
**Complexity: 5-15 | LOC: 5-20 | State: 0-2 | Difficulty: ⭐ - ⭐⭐**

Decorated primitives with styling attributes.

| Component | Type | Attributes | Dependencies | Behaviors |
|-----------|------|------------|--------------|-----------|
| Styled Character | Element | `char, fg, bg, attrs` | Layer 0 | Apply style codes |
| Text Span | Element | `text: str, style: Style` | Layer 0 | Styled text segment |
| Background Fill | Element | `color, width, height` | Layer 0 | Fill rectangular area |
| Border Character | Element | `position: str, style: BorderStyle` | Layer 0 | Box-drawing char selection |
| Gradient Segment | Element | `start_color, end_color, position` | Layer 0 | Color interpolation |

**Characteristics**:
- Immutable configuration
- Style application only
- No user interaction
- Single-pass rendering
- Composable (can combine styles)

---

### Layer 2: Basic Interactive Elements
**Complexity: 15-50 | LOC: 20-80 | State: 2-5 | Difficulty: ⭐ - ⭐⭐⭐**

Simple interactive components with basic state.

#### Display Components

| Component | LOC | State Vars | Dependencies | Difficulty |
|-----------|-----|------------|--------------|------------|
| Label | 20 | 1 | Layer 1 | ⭐ |
| Divider | 20 | 1 | Layer 1 | ⭐ |
| Icon | 15 | 1 | Layer 1 | ⭐ |

#### Input Components

| Component | LOC | State Vars | Dependencies | Event Handlers | Difficulty |
|-----------|-----|------------|--------------|----------------|------------|
| Button | 60 | 5 | Layer 1 | click, hover, key | ⭐⭐ |
| Checkbox | 70 | 4 | Layer 1 | click, key | ⭐⭐ |
| Radio Button | 80 | 5 | Layer 1 | click, key | ⭐⭐ |
| Toggle Switch | 75 | 4 | Layer 1 | click, key | ⭐⭐ |
| TextBox (Static) | 100 | 6 | Layer 1 | key | ⭐⭐⭐ |

**State Pattern Example**:
```python
class Button:
    text: str            # Display text
    enabled: bool        # Can be activated
    focused: bool        # Has keyboard focus
    hovered: bool        # Mouse over (if supported)
    pressed: bool        # Currently being pressed
```

**Characteristics**:
- Single-element state machine
- Basic event handling (1-3 handlers)
- Self-contained rendering
- No child components
- Simple validation (if any)

---

### Layer 3: Container Components
**Complexity: 50-120 | LOC: 80-200 | State: 5-12 | Difficulty: ⭐⭐ - ⭐⭐⭐**

Components that manage collections of children.

| Component | Type | Child Count | Layout | State Vars | Difficulty |
|-----------|------|-------------|--------|------------|------------|
| Panel | Container | 0-20 | Simple | 5 | ⭐⭐ |
| Frame | Container | 0-20 | Simple | 6 | ⭐⭐ |
| List (Homogeneous) | Container | 0-100 | Vertical | 8 | ⭐⭐ |
| Menu Bar | Container | 2-10 | Horizontal | 10 | ⭐⭐⭐ |
| Toolbar | Container | 2-20 | Horizontal | 8 | ⭐⭐ |
| Status Bar | Container | 2-10 | Horizontal | 8 | ⭐⭐ |
| Card | Container | 3-10 | Sectioned | 7 | ⭐⭐⭐ |

**State Pattern Example**:
```python
class List:
    items: List[str]             # Content items
    selected_index: int          # Currently selected
    scroll_offset: int           # Scroll position
    visible_count: int           # Items in viewport
    focused: bool                # Has focus
    multi_select: bool           # Allow multiple selection
    selected_items: Set[int]     # All selected indices
```

**Characteristics**:
- Child component management
- Layout calculation (positioning)
- Event delegation to children
- Scroll state management
- Focus management (tab order)
- Basic collision detection

---

### Layer 4: Complex Interactive Components
**Complexity: 120-250 | LOC: 200-500 | State: 12-20 | Difficulty: ⭐⭐⭐ - ⭐⭐⭐⭐**

Advanced input controls with complex state machines.

| Component | Type | State Vars | Event Handlers | Difficulty |
|-----------|------|------------|----------------|------------|
| TextBox (Editable) | Input | 12 | 8 | ⭐⭐⭐⭐ |
| Dropdown | Input | 10 | 5 | ⭐⭐⭐ |
| Slider | Input | 8 | 5 | ⭐⭐⭐ |
| Progress Bar | Display | 6 | 0 | ⭐⭐ |
| Spinner (Loading) | Animation | 5 | 0 | ⭐⭐ |
| Menu (Vertical) | Navigation | 10 | 4 | ⭐⭐⭐ |
| Tab Bar | Navigation | 9 | 3 | ⭐⭐⭐ |
| Accordion | Container | 12 | 4 | ⭐⭐⭐ |
| Pagination | Navigation | 9 | 2 | ⭐⭐⭐ |

**State Pattern Example**:
```python
class TextBox:
    text: str                    # Content
    cursor_position: int         # Caret location
    selection_start: int         # Selection begin
    selection_end: int           # Selection end
    scroll_offset: int           # Horizontal scroll
    max_length: int              # Character limit
    validator: Callable          # Validation function
    valid: bool                  # Validation state
    focused: bool                # Has focus
    modified: bool               # Dirty flag
    placeholder: str             # Empty state text
```

**Characteristics**:
- Complex state machines (5+ states)
- Multi-step interactions
- Validation logic
- Keyboard navigation (arrow keys, home/end)
- Mouse interaction zones
- Undo/redo support (some)

---

### Layer 5: Composite Views & Data Displays
**Complexity: 250-500 | LOC: 500-1000 | State: 20-40 | Difficulty: ⭐⭐⭐ - ⭐⭐⭐⭐**

Multi-component systems with orchestration.

| Component | Type | State Vars | Child Components | Difficulty |
|-----------|------|------------|------------------|------------|
| Dialog Box | Composite | 15 | 3-10 | ⭐⭐⭐ |
| Message Box | Composite | 12 | 2-5 | ⭐⭐⭐ |
| Form | Composite | 25 | 5-20 | ⭐⭐⭐⭐ |
| Table (Simple) | View | 15 | N/A | ⭐⭐⭐ |
| List (Objects) | View | 18 | N/A | ⭐⭐⭐ |
| Context Menu | Navigation | 12 | 2-20 | ⭐⭐⭐ |
| Tooltip | Display | 8 | 1 | ⭐⭐ |
| Notification | Display | 12 | 2-5 | ⭐⭐⭐ |
| Modal | Container | 14 | 1-10 | ⭐⭐⭐⭐ |

**State Pattern Example**:
```python
class Dialog:
    title: str                   # Dialog heading
    content: Component           # Body component
    buttons: List[Button]        # Action buttons
    modal: bool                  # Blocks parent?
    visible: bool                # Currently shown
    result: Optional[Any]        # Return value
    position: Tuple[int, int]    # Screen position
    size: Tuple[int, int]        # Width, height
    closeable: bool              # Can dismiss
    backdrop: bool               # Show backdrop
    focused_element: int         # Tab index
    elements: List[Component]    # All children
    validators: List[Callable]   # Validation funcs
    valid: bool                  # All valid
    submitted: bool              # Form submitted
```

**Characteristics**:
- Orchestrates multiple components
- Modal/focus management (focus trapping)
- Result callbacks
- Complex event flow (bubbling, capturing)
- Lifecycle management (open, validate, close)
- Animation states (enter, exit)

---

### Layer 6: Advanced Data Views
**Complexity: 500-1000 | LOC: 1000-2000 | State: 40-60 | Difficulty: ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐**

High-performance data display components.

| Component | Type | State Vars | Features | Difficulty |
|-----------|------|------------|----------|------------|
| Table (Spreadsheet) | View | 55 | Sort, filter, edit, virtual scroll | ⭐⭐⭐⭐⭐ |
| Data Grid | View | 55 | Edit, filter, aggregate, virtual | ⭐⭐⭐⭐⭐ |
| Tree View (Simple) | View | 25 | Expand/collapse, 2-3 levels | ⭐⭐⭐⭐ |
| Tree View (N-level) | View | 35 | Recursive, lazy load, infinite depth | ⭐⭐⭐⭐⭐ |
| File Browser | View | 30 | Navigation, preview, operations | ⭐⭐⭐⭐ |
| Calendar | View | 28 | Date selection, events, navigation | ⭐⭐⭐⭐ |
| Chart (Bar/Line) | View | 32 | Data visualization, axes, legend | ⭐⭐⭐⭐ |
| Split Panel | Layout | 14 | Resizable divider, 2 panes | ⭐⭐⭐ |
| Linear Flow | Navigation | 25 | Multi-step wizard, validation gates | ⭐⭐⭐⭐ |

**State Pattern Example**:
```python
class DataGrid:
    data_source: List[Dict]              # Row data
    columns: List[Column]                # Column defs
    visible_rows: List[int]              # Virtual scroll indices
    scroll_position: Tuple[int, int]     # X, Y scroll
    selected_cells: Set[Tuple[int, int]] # Cell selection
    edited_cells: Dict[Tuple[int, int], Any]  # Pending edits
    sort_column: Optional[int]           # Sort by column
    sort_direction: str                  # asc/desc
    filters: Dict[int, Filter]           # Active filters
    cell_renderers: Dict[int, Callable]  # Custom renderers
    cell_editors: Dict[int, Component]   # In-place editors
    active_editor: Optional[Tuple[int, int]]  # Editing cell
    column_widths: List[int]             # Width per column
    frozen_columns: int                  # Pin left columns
    frozen_rows: int                     # Pin top rows
    total_width: int                     # Content width
    total_height: int                    # Content height
```

**Characteristics**:
- Large dataset handling (1000+ items)
- Virtual scrolling/windowing
- Sorting/filtering/searching
- In-place editing
- Cell navigation (arrow keys, 2D)
- Data binding/synchronization
- Performance optimization critical

---

### Layer 7: Navigation & Flow Systems
**Complexity: 1000-2000 | LOC: 2000-4000 | State: 60-100 | Difficulty: ⭐⭐⭐⭐⭐**

Complex navigation and workflow orchestration.

| Component | Type | State Vars | Features | Difficulty |
|-----------|------|------------|----------|------------|
| Wizard | Navigation | 45 | Multi-step, branching, validation | ⭐⭐⭐⭐⭐ |
| Multi-Step Form | Navigation | 40 | Progress, state, validation | ⭐⭐⭐⭐⭐ |
| Nested Flow | Navigation | 50 | Route stack, transitions, guards | ⭐⭐⭐⭐⭐ |
| Router | Navigation | 50 | History, params, guards, deep link | ⭐⭐⭐⭐⭐ |
| Slideshow | View | 25 | Slides, navigation, transitions | ⭐⭐⭐⭐ |
| Carousel | View | 18 | Items, loop, auto-play | ⭐⭐⭐⭐ |
| Breadcrumb | Navigation | 8 | Path, clickable, overflow | ⭐⭐⭐ |

**State Pattern Example**:
```python
class Router:
    routes: Dict[str, Route]             # Route definitions
    current_route: str                   # Active route
    history_stack: List[str]             # Navigation history
    history_index: int                   # Back/forward position
    route_params: Dict[str, Any]         # URL parameters
    query_params: Dict[str, str]         # Query string
    state: Dict[str, Any]                # Persistent state
    guards: List[Callable]               # Can activate?
    interceptors: List[Callable]         # Before navigate
    transitions: Dict[Tuple[str, str], Transition]  # Animation
    loading: bool                        # Async route load
    error: Optional[Exception]           # Route error
    default_route: str                   # Fallback
    not_found_route: str                 # 404 handler
```

**Characteristics**:
- Route management (pattern matching)
- History stack (back/forward)
- State preservation across navigation
- Conditional rendering based on route
- Transition animations
- Guard functions (canActivate, canDeactivate)
- Deep linking support
- Async route loading

---

### Layer 8: Graph & Spatial Navigation
**Complexity: 2000-4000 | LOC: 4000-8000 | State: 100-150 | Difficulty: ⭐⭐⭐⭐⭐**

Advanced 2D/graph navigation systems.

| Component | Type | State Vars | Features | Difficulty |
|-----------|------|------------|----------|------------|
| 2D Navigation Map | Navigation | 120 | Grid, pathfinding, collision | ⭐⭐⭐⭐⭐ |
| Mind Map | View | 110 | Nodes, connections, layout, zoom | ⭐⭐⭐⭐⭐ |
| Network Graph | View | 115 | Physics, layout algorithms | ⭐⭐⭐⭐⭐ |
| Gantt Chart | View | 85 | Tasks, dependencies, timeline | ⭐⭐⭐⭐⭐ |
| Kanban Board | View | 75 | Columns, cards, drag-drop | ⭐⭐⭐⭐⭐ |
| Spatial Browser | Navigation | 105 | 2D space, zoom, pan | ⭐⭐⭐⭐⭐ |

**State Pattern Example**:
```python
class NavigationMap:
    nodes: Dict[str, Node]               # Graph nodes
    edges: List[Edge]                    # Connections
    grid: Grid2D                         # Spatial data structure
    current_position: Tuple[int, int]    # Player/cursor position
    viewport: Rect                       # Visible area
    zoom_level: float                    # Magnification
    selected_nodes: Set[str]             # Multi-selection
    hovered_node: Optional[str]          # Mouse over
    path: List[Tuple[int, int]]          # Computed path
    obstacles: Set[Tuple[int, int]]      # Blocked cells
    traversable: Set[Tuple[int, int]]    # Walkable cells
    layout_algorithm: LayoutAlgorithm    # Graph layout
    physics_enabled: bool                # Simulate physics
    collision_detection: bool            # Check collisions
    node_renderers: Dict[str, Callable]  # Custom render
    edge_renderers: Dict[str, Callable]  # Custom edges
    interaction_mode: str                # view/edit/navigate
    undo_stack: List[Action]             # Undo operations
    redo_stack: List[Action]             # Redo operations
```

**Characteristics**:
- 2D coordinate management
- Pathfinding algorithms (A*, Dijkstra)
- Collision detection
- Spatial queries (nearest, within bounds)
- Viewport management (pan, zoom)
- Interactive node editing
- Edge routing (avoid overlaps)
- Layout algorithms (force-directed, hierarchical)
- Physics simulation (optional)

---

### Layer 9: Application-Level Widgets
**Complexity: 4000+ | LOC: 8000+ | State: 150+ | Difficulty: ⭐⭐⭐⭐⭐**

Full-featured application components.

| Component | Type | State Vars | Features | Difficulty |
|-----------|------|------------|----------|------------|
| Dashboard | Application | 160 | Widgets, layout, data sources | ⭐⭐⭐⭐⭐ |
| IDE Panel | Application | 180 | Editor, explorer, terminal, debug | ⭐⭐⭐⭐⭐ |
| Terminal Emulator | Application | 140 | Buffer, cursor, ANSI parsing | ⭐⭐⭐⭐⭐ |
| Text Editor | Application | 170 | Buffer, syntax, undo, search | ⭐⭐⭐⭐⭐ |
| File Manager | Application | 155 | Tree, preview, operations | ⭐⭐⭐⭐⭐ |
| Music Player | Application | 130 | Playlist, controls, visualization | ⭐⭐⭐⭐⭐ |
| Chat Interface | Application | 145 | Messages, input, users, rooms | ⭐⭐⭐⭐⭐ |
| Game Board | Application | 165 | State, rules, rendering, AI | ⭐⭐⭐⭐⭐ |

**State Pattern Example**:
```python
class Dashboard:
    widgets: List[Widget]                # All widgets
    layout: Layout                       # Arrangement
    data_sources: Dict[str, DataSource]  # Data connections
    global_state: State                  # Shared state
    event_bus: EventBus                  # Event system
    config: Config                       # Settings
    theme: Theme                         # Visual theme
    shortcuts: Dict[str, Action]         # Keyboard shortcuts
    active_widget: Optional[str]         # Focused widget
    widget_states: Dict[str, Any]        # Per-widget state
    refresh_intervals: Dict[str, int]    # Auto-refresh
    connections: List[Connection]        # Network/DB
    filters: Dict[str, Filter]           # Data filters
    transformations: Dict[str, Transform]  # Data transforms
    alerts: List[Alert]                  # Notifications
    history: CircularBuffer              # Action history
    undo_manager: UndoManager            # Global undo
    plugin_manager: PluginManager        # Extensions
    persistence_layer: Storage           # State persistence
```

**Characteristics**:
- Complete application lifecycle
- Multiple coordinated subsystems
- Complex state management (Redux-like)
- Plugin/extension architecture
- Configuration management
- Persistence layer integration
- Inter-widget communication (pub/sub)
- Theme system
- Global keyboard shortcuts registry
- Performance monitoring
- Error boundary handling

---

## Component Type Categories

### By Functional Purpose

#### 1. PRIMITIVES
**Purpose**: Atomic building blocks with zero logic

| Component | LOC | State | Dependencies | Rendering | Difficulty |
|-----------|-----|-------|--------------|-----------|------------|
| Character | 1 | 0 | None | Direct | ⭐ |
| Symbol | 1 | 0 | None | Direct | ⭐ |
| Color | 1 | 0 | None | Modifier | ⭐ |
| Coordinate | 2 | 0 | None | N/A | ⭐ |
| Dimension | 2 | 0 | None | N/A | ⭐ |

**Usage**: Foundation for all other components. Never instantiated directly in application code.

---

#### 2. ATTRIBUTES
**Purpose**: Styling and decoration modifiers

| Component | LOC | State | Dependencies | Rendering | Difficulty |
|-----------|-----|-------|--------------|-----------|------------|
| Bold | 5 | 0 | Color | Modifier | ⭐ |
| Italic | 5 | 0 | Color | Modifier | ⭐ |
| Underline | 5 | 0 | Color | Modifier | ⭐ |
| Foreground Color | 8 | 0 | Color | Modifier | ⭐ |
| Background Color | 8 | 0 | Color | Modifier | ⭐ |
| Gradient | 25 | 0 | Color | Complex | ⭐⭐ |
| Border Style | 15 | 0 | Character | Pattern | ⭐⭐ |
| Padding | 10 | 0 | Dimension | Layout | ⭐ |
| Margin | 10 | 0 | Dimension | Layout | ⭐ |
| Alignment | 15 | 0 | None | Layout | ⭐⭐ |

**Usage**: Apply visual styling without altering component logic. Composable (can stack multiple).

---

#### 3. DISPLAY ELEMENTS
**Purpose**: Static or simple output components

| Component | LOC | State | Dependencies | Rendering | Difficulty |
|-----------|-----|-------|--------------|-----------|------------|
| Label | 20 | 1 | Styled Text | Single | ⭐ |
| Icon | 15 | 1 | Symbol | Single | ⭐ |
| Image (ASCII) | 50 | 1 | None | Multi-line | ⭐⭐ |
| Badge | 25 | 2 | Label | Single | ⭐⭐ |
| Divider (H) | 20 | 1 | Character | Single | ⭐ |
| Divider (V) | 20 | 1 | Character | Single | ⭐ |
| Spacer | 15 | 1 | Dimension | None | ⭐ |

**Usage**: Non-interactive display. Use for headings, separators, decorative elements.

---

#### 4. INPUT CONTROLS
**Purpose**: Interactive user input components

| Component | LOC | State | Dependencies | Event Handlers | Difficulty |
|-----------|-----|-------|--------------|----------------|------------|
| Button | 60 | 5 | Label | 3 | ⭐⭐ |
| Checkbox | 70 | 4 | Label, Icon | 2 | ⭐⭐ |
| Radio Button | 80 | 5 | Label, Icon | 2 | ⭐⭐ |
| Toggle | 75 | 4 | Label | 2 | ⭐⭐ |
| TextBox (Static) | 100 | 6 | Label | 1 | ⭐⭐⭐ |
| TextBox (Editable) | 350 | 12 | Label, Cursor | 8 | ⭐⭐⭐⭐ |
| TextArea | 450 | 15 | TextBox | 10 | ⭐⭐⭐⭐ |
| Slider | 200 | 8 | Label | 5 | ⭐⭐⭐ |
| Spinner (Numeric) | 180 | 7 | TextBox, Button | 4 | ⭐⭐⭐ |
| DatePicker | 400 | 20 | Calendar, TextBox | 12 | ⭐⭐⭐⭐⭐ |
| ColorPicker | 500 | 18 | Grid, Slider | 10 | ⭐⭐⭐⭐⭐ |

**Usage**: Forms, dialogs, interactive panels. Require event handling and validation.

---

#### 5. CONTAINERS
**Purpose**: Hold and organize child components

| Component | LOC | State | Children | Layout | Difficulty |
|-----------|-----|-------|----------|--------|------------|
| Panel | 80 | 5 | 0-20 | Simple | ⭐⭐ |
| Frame | 100 | 6 | 0-20 | Simple | ⭐⭐ |
| Card | 120 | 7 | 3-10 | Sectioned | ⭐⭐⭐ |
| Stack (V) | 150 | 8 | 0-50 | Linear | ⭐⭐⭐ |
| Stack (H) | 150 | 8 | 0-50 | Linear | ⭐⭐⭐ |
| Grid | 300 | 15 | 0-100 | 2D Matrix | ⭐⭐⭐⭐ |
| Scrollable | 250 | 12 | 1 | Viewport | ⭐⭐⭐⭐ |
| Split Panel | 280 | 14 | 2 | Resizable | ⭐⭐⭐⭐ |
| Tabs Container | 200 | 10 | 2-20 | Switched | ⭐⭐⭐ |
| Accordion | 220 | 12 | 2-20 | Collapsible | ⭐⭐⭐ |

**Usage**: Structural organization. Essential for complex layouts.

---

#### 6. LISTS & COLLECTIONS
**Purpose**: Display multiple items

| Component | LOC | State | Item Type | Features | Difficulty |
|-----------|-----|-------|-----------|----------|------------|
| List (Simple) | 120 | 8 | String | Selection, scroll | ⭐⭐ |
| List (Objects) | 250 | 15 | Object | Renderer, scroll | ⭐⭐⭐ |
| CheckList | 180 | 12 | String | Multi-select | ⭐⭐⭐ |
| Tree (2-level) | 300 | 18 | Node | Expand/collapse | ⭐⭐⭐⭐ |
| Tree (N-level) | 600 | 35 | Node | Recursive, lazy | ⭐⭐⭐⭐⭐ |
| Table (Static) | 200 | 12 | Row | Headers, scroll | ⭐⭐⭐ |
| Table (Sortable) | 350 | 20 | Row | Sort, scroll | ⭐⭐⭐⭐ |
| Data Grid | 1200 | 55 | Cell | Edit, filter, virtual | ⭐⭐⭐⭐⭐ |

**Usage**: Data presentation. Critical for database/API-driven applications.

---

#### 7. NAVIGATION
**Purpose**: Control application flow

| Component | LOC | State | Items | Logic | Difficulty |
|-----------|-----|-------|-------|-------|------------|
| Menu (Vertical) | 180 | 10 | 2-20 | Selection | ⭐⭐⭐ |
| Context Menu | 220 | 12 | 2-20 | Popup, position | ⭐⭐⭐ |
| Menu Bar | 200 | 12 | 2-10 | Dropdown | ⭐⭐⭐ |
| Breadcrumb | 150 | 8 | 1-10 | Path display | ⭐⭐⭐ |
| Pagination | 180 | 9 | N/A | Page control | ⭐⭐⭐ |
| Stepper | 200 | 11 | 2-10 | Step tracking | ⭐⭐⭐ |
| Wizard | 800 | 45 | 2-10 | Multi-step, validation | ⭐⭐⭐⭐⭐ |
| Router | 1000 | 50 | 2-50 | History, guards | ⭐⭐⭐⭐⭐ |
| Tab Bar | 160 | 9 | 2-10 | Tab switching | ⭐⭐⭐ |

**Usage**: Multi-screen applications, workflows, SPAs (Single-Page Apps).

---

#### 8. FEEDBACK COMPONENTS
**Purpose**: Visual feedback and status

| Component | LOC | State | Animation | Timing | Difficulty |
|-----------|-----|-------|-----------|--------|------------|
| Progress Bar | 100 | 6 | No | N/A | ⭐⭐ |
| Spinner (Loading) | 80 | 5 | Yes | Frame | ⭐⭐ |
| Toast | 180 | 10 | Yes | Timeout | ⭐⭐⭐ |
| Notification | 200 | 12 | Yes | Timeout, dismiss | ⭐⭐⭐ |
| Alert | 160 | 9 | No | N/A | ⭐⭐⭐ |
| Badge (Counter) | 60 | 3 | No | N/A | ⭐⭐ |
| Status Indicator | 50 | 3 | Optional | Pulse | ⭐⭐ |

**Usage**: User feedback for async operations, validation, system status.

---

## Metrics & Measurement

### Complexity Scoring Formula

```python
complexity_score = (
    (lines_of_code * 0.3) +
    (state_variables * 5) +
    (inheritance_depth * 10) +
    (child_components * 2) +
    (event_handlers * 8) +
    (rendering_complexity * 15) +
    (data_binding_complexity * 20)
)
```

### Metric Definitions

#### Lines of Code (LOC)
Count of non-comment, non-blank lines required for implementation.

**Ranges**:
- Trivial: 1-20
- Simple: 20-100
- Moderate: 100-500
- Complex: 500-2000
- Very Complex: 2000+

#### State Variables
Number of instance variables tracking component state.

**Categories**:
- Stateless: 0-2
- Simple State: 2-5
- Moderate State: 5-15
- Complex State: 15-40
- Very Complex: 40+

#### Inheritance Depth
Number of parent classes/interfaces in hierarchy.

**Guidelines**:
- Flat: 0-1 (primitive, standalone)
- Shallow: 1-2 (standard)
- Deep: 3-4 (specialized)
- Very Deep: 5+ (avoid)

#### Child Components
Number of managed child components.

**Categories**:
- Atomic: 0 (leaf node)
- Container: 1-20
- Complex Container: 20-50
- Large Container: 50-100
- Massive: 100+

#### Event Handlers
Number of distinct event callbacks.

**Categories**:
- Non-interactive: 0
- Simple: 1-2
- Interactive: 2-5
- Complex: 5-10
- Very Complex: 10+

#### Rendering Complexity
Algorithm complexity for draw operations.

**Levels**:
- Direct: Pass-through to terminal (O(1))
- Simple: Single calculation (O(n))
- Moderate: Layout calculation (O(n log n))
- Complex: Multi-pass rendering (O(n²))
- Very Complex: Graph layout, physics (O(n³))

#### Data Binding Complexity
Integration with external data sources.

**Levels**:
- None: Static data
- One-way: Read-only binding
- Two-way: Read-write binding
- Bidirectional: Sync between multiple sources
- Complex: Transformations, validation, async

---

## Difficulty Rating System

### ⭐ Trivial (LOC: 1-20, State: 0-2)

**Characteristics**:
- No logic or minimal logic
- Direct API calls
- Immutable values
- No event handling
- Single-pass rendering

**Examples**: Character, Color, Label, Divider

**Implementation Time**: < 1 hour  
**Skill Level**: Beginner

---

### ⭐⭐ Easy (LOC: 20-100, State: 2-5)

**Characteristics**:
- Simple state machine (2-3 states)
- Basic event handling (1-2 handlers)
- Self-contained logic
- No child management
- Standard patterns

**Examples**: Button, Checkbox, Panel, Progress Bar

**Implementation Time**: 1-4 hours  
**Skill Level**: Beginner to Intermediate

---

### ⭐⭐⭐ Medium (LOC: 100-300, State: 5-15)

**Characteristics**:
- Moderate state complexity
- Multiple event handlers
- Child component management
- Layout calculations
- Focus management

**Examples**: List, Menu, Tab Bar, Form, Table (simple)

**Implementation Time**: 4-16 hours  
**Skill Level**: Intermediate

---

### ⭐⭐⭐⭐ Hard (LOC: 300-1000, State: 15-40)

**Characteristics**:
- Complex state machines
- Advanced event handling
- Virtual scrolling
- Validation logic
- Data binding

**Examples**: TextBox (editable), Tree View, Data Grid, Calendar, Router

**Implementation Time**: 16-40 hours  
**Skill Level**: Advanced

---

### ⭐⭐⭐⭐⭐ Very Hard (LOC: 1000+, State: 40+)

**Characteristics**:
- Very complex state management
- Multiple coordinated subsystems
- Performance optimization required
- Advanced algorithms (pathfinding, layout)
- Plugin architecture

**Examples**: Wizard, Data Grid (full), Dashboard, IDE Panel, Router

**Implementation Time**: 40+ hours  
**Skill Level**: Expert

---

## State Complexity Patterns

### Pattern 1: Stateless (0-2 vars)
```python
class Label:
    text: str
    style: Style
```
**Use**: Display-only components

---

### Pattern 2: Simple State (2-5 vars)
```python
class Button:
    text: str
    enabled: bool
    focused: bool
    hovered: bool
    pressed: bool
```
**Use**: Basic interactive elements

---

### Pattern 3: Moderate State (5-15 vars)
```python
class List:
    items: List[str]
    selected_index: int
    scroll_offset: int
    visible_count: int
    focused: bool
    multi_select: bool
    selected_items: Set[int]
```
**Use**: Containers, collections

---

### Pattern 4: Complex State (15-40 vars)
```python
class Dialog:
    title: str
    content: Component
    buttons: List[Button]
    modal: bool
    visible: bool
    result: Optional[Any]
    position: Tuple[int, int]
    size: Tuple[int, int]
    closeable: bool
    backdrop: bool
    focused_element: int
    elements: List[Component]
    validators: List[Callable]
    valid: bool
    submitted: bool
```
**Use**: Composite components, forms

---

### Pattern 5: Very Complex State (40+ vars)
```python
class DataGrid:
    # Data (5 vars)
    data_source: List[Dict]
    columns: List[Column]
    visible_rows: List[int]
    edited_cells: Dict[Tuple[int, int], Any]
    filters: Dict[int, Filter]
    
    # Display (6 vars)
    scroll_position: Tuple[int, int]
    column_widths: List[int]
    frozen_columns: int
    frozen_rows: int
    total_width: int
    total_height: int
    
    # Selection (3 vars)
    selected_cells: Set[Tuple[int, int]]
    active_cell: Optional[Tuple[int, int]]
    active_editor: Optional[Tuple[int, int]]
    
    # Sorting (2 vars)
    sort_column: Optional[int]
    sort_direction: str
    
    # Rendering (3 vars)
    cell_renderers: Dict[int, Callable]
    cell_editors: Dict[int, Component]
    row_heights: List[int]
    
    # ... etc (20+ more)
```
**Use**: Advanced data views, applications

---

## Complete Component Catalog

### Quick Reference Table

| Layer | Complexity | LOC Range | State Range | Examples | Difficulty |
|-------|------------|-----------|-------------|----------|------------|
| 0 | 1-5 | 1-5 | 0 | Character, Symbol, Color | ⭐ |
| 1 | 5-15 | 5-20 | 0-2 | Styled Char, Text Span, Border | ⭐ - ⭐⭐ |
| 2 | 15-50 | 20-80 | 2-5 | Label, Button, Checkbox | ⭐ - ⭐⭐⭐ |
| 3 | 50-120 | 80-200 | 5-12 | Panel, List, Menu Bar | ⭐⭐ - ⭐⭐⭐ |
| 4 | 120-250 | 200-500 | 12-20 | TextBox, Dropdown, Tab Bar | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| 5 | 250-500 | 500-1000 | 20-40 | Dialog, Form, Table | ⭐⭐⭐ - ⭐⭐⭐⭐ |
| 6 | 500-1000 | 1000-2000 | 40-60 | Data Grid, Tree, File Browser | ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐ |
| 7 | 1000-2000 | 2000-4000 | 60-100 | Wizard, Router, Nested Flow | ⭐⭐⭐⭐⭐ |
| 8 | 2000-4000 | 4000-8000 | 100-150 | Nav Map, Network Graph, Kanban | ⭐⭐⭐⭐⭐ |
| 9 | 4000+ | 8000+ | 150+ | Dashboard, IDE, Terminal Emulator | ⭐⭐⭐⭐⭐ |

---

## Usage Guidelines

### Choosing the Right Component

#### 1. Identify Required Functionality
- Display only? → Use Display Elements (Layer 2)
- User input? → Use Input Controls (Layer 2-4)
- Group components? → Use Containers (Layer 3)
- Show data? → Use Views (Layer 5-6)
- Navigate? → Use Navigation (Layer 4, 7)

#### 2. Assess Complexity Requirements
- Simple static display → Layer 0-2
- Basic interaction → Layer 2-3
- Forms and data entry → Layer 4-5
- Complex data display → Layer 6
- Multi-screen flows → Layer 7
- Advanced visualization → Layer 8
- Full applications → Layer 9

#### 3. Consider Implementation Constraints
- Development time available
- Team skill level
- Performance requirements
- Maintenance burden
- Testing complexity

### Component Composition Strategies

#### Strategy 1: Bottom-Up
Start with primitives, build upward.

```
Primitives → Styled → Controls → Containers → Views → Application
```

**Best for**: New frameworks, learning, maximum control

#### Strategy 2: Top-Down
Start with high-level component, decompose.

```
Application → Views → Containers → Controls → Primitives
```

**Best for**: Rapid prototyping, existing frameworks

#### Strategy 3: Middle-Out
Start with core components, extend both directions.

```
← Primitives ← Controls → Containers → Views →
```

**Best for**: Balanced development, iterative refinement

### Performance Optimization by Layer

| Layer | Key Optimization |
|-------|------------------|
| 0-1 | Minimal abstraction, direct rendering |
| 2-3 | Event handler efficiency, avoid re-renders |
| 4-5 | Debounce input, throttle validation |
| 6 | Virtual scrolling, lazy loading |
| 7 | Route caching, state persistence |
| 8 | Spatial indexing, viewport culling |
| 9 | Worker threads, incremental updates |

---

## Version History

### Version 1.0 (2025-12-06)
- Initial perfected taxonomy from CLI-Menu-Component-Taxonomy.md
- 10-layer classification system
- Complete metrics and difficulty ratings
- State complexity patterns
- Comprehensive component catalog

---

**END OF TAXONOMY STANDARD**
