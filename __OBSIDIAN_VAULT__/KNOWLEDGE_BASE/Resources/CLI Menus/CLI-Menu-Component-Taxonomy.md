# CLI Menu Component Taxonomy

> **Comprehensive classification of menu system components by deployment complexity, architectural layer, and implementation difficulty**

---

## Table of Contents

1. [Taxonomy Overview](#taxonomy-overview)
2. [Component Classification Matrix](#component-classification-matrix)
3. [Deployment Complexity Layers (0-9)](#deployment-complexity-layers-0-9)
4. [Component Categories](#component-categories)
5. [Inheritance & Composition Chains](#inheritance--composition-chains)
6. [Implementation Difficulty Reference](#implementation-difficulty-reference)

---

## Taxonomy Overview

### Classification Dimensions

Each component is evaluated across multiple dimensions:

| Dimension | Description | Weight Factor |
|-----------|-------------|---------------|
| **Deployment Depth** | Lines of code + dependencies to instantiate | 1x - 10x |
| **Visual Real Estate** | Screen space consumed (characters/lines) | Low/Med/High |
| **State Complexity** | Number of internal state variables | 0 - 20+ |
| **Inheritance Chain** | Number of parent classes/interfaces | 0 - 5+ |
| **Composition Depth** | Number of child components | 0 - 50+ |
| **Event Handlers** | Number of input/event callbacks required | 0 - 20+ |
| **Rendering Logic** | Complexity of draw/update operations | Trivial - Complex |
| **Data Binding** | Integration with external data sources | None - Bidirectional |

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

---

## Component Classification Matrix

### By Type & Purpose

| Type | Purpose | Examples |
|------|---------|----------|
| **Primitive** | Atomic visual units | Character, Symbol, Color |
| **Styled Element** | Decorated primitives | Bold text, Colored background |
| **Input Control** | User interaction points | Button, Checkbox, TextBox |
| **Container** | Groups other components | List, Panel, Frame |
| **Layout** | Spatial arrangement | Grid, Stack, Flow |
| **View** | Data presentation | Table, Tree, Chart |
| **Navigation** | User flow control | Menu, Wizard, Router |
| **Animation** | Temporal effects | Spinner, Progress, Transition |
| **Composite** | Multi-component systems | Dialog, Form, Dashboard |
| **Application** | Top-level orchestrators | App, Widget, Window |

---

## Deployment Complexity Layers (0-9)

### Layer 0: Terminal Primitives
**Complexity: 1-5 | LOC: 1-5 | State: 0**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Character | Primitive | `char: str` | None | ⭐ Trivial |
| Symbol | Primitive | `unicode: int, fallback: str` | None | ⭐ Trivial |
| Color Code | Primitive | `ansi_code: int` | None | ⭐ Trivial |
| Coordinate | Primitive | `x: int, y: int` | None | ⭐ Trivial |
| Dimension | Primitive | `width: int, height: int` | None | ⭐ Trivial |

#### Behaviors
- Direct output to terminal
- No state management
- No event handling
- Immediate rendering

---

### Layer 1: Styled Primitives
**Complexity: 5-15 | LOC: 5-20 | State: 0-2**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Styled Character | Element | `char, fg, bg, attrs` | Layer 0 | ⭐ Trivial |
| Text Span | Element | `text: str, style: Style` | Layer 0 | ⭐ Trivial |
| Background Fill | Element | `color, width, height` | Layer 0 | ⭐ Trivial |
| Border Character | Element | `position: str, style: BorderStyle` | Layer 0 | ⭐⭐ Easy |
| Gradient Segment | Element | `start_color, end_color, position` | Layer 0 | ⭐⭐ Easy |

#### Behaviors
- Applies styling to primitives
- Immutable configuration
- No interaction
- Single-pass rendering

---

### Layer 2: Basic Interactive Elements
**Complexity: 15-50 | LOC: 20-80 | State: 2-5**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Label | Display | `text, align, style` | Layer 1 | ⭐ Trivial |
| Divider | Display | `length, char, orientation` | Layer 1 | ⭐ Trivial |
| Icon | Display | `symbol, color, size` | Layer 1 | ⭐ Trivial |
| Button | Input | `label, enabled, focused, callback` | Layer 1 | ⭐⭐ Easy |
| Checkbox | Input | `label, checked, enabled, callback` | Layer 1 | ⭐⭐ Easy |
| Radio Button | Input | `label, selected, group, callback` | Layer 1 | ⭐⭐ Easy |
| TextBox (Static) | Input | `text, width, cursor_pos` | Layer 1 | ⭐⭐⭐ Medium |
| Toggle Switch | Input | `state, labels, callback` | Layer 1 | ⭐⭐ Easy |
| Hotkey | Behavior | `key, modifier, action` | Layer 0 | ⭐⭐ Easy |

#### Behaviors
- Single-element state (checked, focused, text)
- Basic event handling (click, key press)
- Self-contained rendering
- No child components

#### State Variables
```python
class Button:
    text: str
    enabled: bool
    focused: bool
    hovered: bool
    pressed: bool
```

---

### Layer 3: Container Components
**Complexity: 50-120 | LOC: 80-200 | State: 5-12**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| List (Homogeneous) | Container | `items: List[str], selected` | Layer 2 | ⭐⭐ Easy |
| Panel | Container | `children, border, padding` | Layer 1-2 | ⭐⭐ Easy |
| Frame | Container | `title, children, size` | Layer 1-2 | ⭐⭐ Easy |
| Menu Bar | Container | `items: List[MenuItem]` | Layer 2 | ⭐⭐⭐ Medium |
| Toolbar | Container | `buttons: List[Button]` | Layer 2 | ⭐⭐ Easy |
| Status Bar | Container | `segments: List[Label]` | Layer 2 | ⭐⭐ Easy |
| Card | Container | `header, body, footer` | Layer 2 | ⭐⭐ Easy |
| Wrapper Graphic | Container | `child, decoration` | Layer 1 | ⭐⭐ Easy |

#### Behaviors
- Manages collection of child components
- Layout calculation (position children)
- Event delegation to children
- Scroll state management
- Focus management

#### State Variables
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

---

### Layer 4: Complex Interactive Components
**Complexity: 120-250 | LOC: 200-500 | State: 12-20**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| TextBox (Editable) | Input | `text, cursor, selection, validation` | Layer 2 | ⭐⭐⭐ Medium |
| Dropdown | Input | `items, selected, expanded` | Layer 3 | ⭐⭐⭐ Medium |
| Slider | Input | `value, min, max, step` | Layer 2 | ⭐⭐⭐ Medium |
| Progress Bar | Display | `value, max, style, label` | Layer 1 | ⭐⭐ Easy |
| Spinner | Animation | `frames, speed, active` | Layer 1 | ⭐⭐ Easy |
| Menu (Vertical) | Navigation | `items, selected, actions` | Layer 3 | ⭐⭐⭐ Medium |
| Tab Bar | Navigation | `tabs, active, content` | Layer 3 | ⭐⭐⭐ Medium |
| Accordion | Container | `sections, expanded` | Layer 3 | ⭐⭐⭐ Medium |
| Pagination | Navigation | `page, total, size` | Layer 2 | ⭐⭐ Easy |

#### Behaviors
- Complex internal state machines
- Multi-step interactions
- Validation logic
- Keyboard navigation
- Mouse interaction zones

#### State Variables
```python
class TextBox:
    text: str
    cursor_position: int
    selection_start: int
    selection_end: int
    scroll_offset: int
    max_length: int
    validator: Callable
    valid: bool
    focused: bool
    modified: bool
    placeholder: str
```

---

### Layer 5: Composite Views & Data Displays
**Complexity: 250-500 | LOC: 500-1000 | State: 20-40**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Dialog Box | Composite | `title, content, buttons, result` | Layer 3-4 | ⭐⭐⭐ Medium |
| Message Box | Composite | `message, type, buttons` | Layer 4 | ⭐⭐⭐ Medium |
| Form | Composite | `fields: List[Input], validation` | Layer 3-4 | ⭐⭐⭐⭐ Hard |
| Table (Simple) | View | `headers, rows, selection` | Layer 3 | ⭐⭐⭐ Medium |
| List (Objects) | View | `objects, renderer, selection` | Layer 3 | ⭐⭐⭐ Medium |
| Context Menu | Navigation | `items, position, parent` | Layer 4 | ⭐⭐⭐ Medium |
| Tooltip | Display | `text, target, delay, position` | Layer 2 | ⭐⭐ Easy |
| Notification | Display | `message, type, timeout, action` | Layer 3 | ⭐⭐⭐ Medium |
| Loader Animation | Animation | `type, message, cancellable` | Layer 4 | ⭐⭐⭐ Medium |
| Modal | Container | `content, backdrop, closeable` | Layer 4 | ⭐⭐⭐⭐ Hard |

#### Behaviors
- Orchestrates multiple components
- Modal/focus management
- Result callbacks
- Complex event flow
- Lifecycle management (open, close, validate)

#### State Variables
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

---

### Layer 6: Advanced Data Views
**Complexity: 500-1000 | LOC: 1000-2000 | State: 40-60**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Table (Spreadsheet) | View | `data, columns, sort, filter, edit` | Layer 5 | ⭐⭐⭐⭐⭐ Very Hard |
| Data Grid | View | `data_source, columns, virtualization` | Layer 5 | ⭐⭐⭐⭐⭐ Very Hard |
| Tree View (Simple) | View | `nodes, expanded, selected` | Layer 3-4 | ⭐⭐⭐⭐ Hard |
| File Browser | View | `path, files, selection, actions` | Layer 5 | ⭐⭐⭐⭐ Hard |
| Calendar | View | `date, events, selection` | Layer 4 | ⭐⭐⭐⭐ Hard |
| Chart (Bar/Line) | View | `data, axes, labels, legend` | Layer 4 | ⭐⭐⭐⭐ Hard |
| Split Panel | Layout | `children, orientation, ratio, resizable` | Layer 3 | ⭐⭐⭐ Medium |
| Linear Flow | Navigation | `steps, current, validation, navigation` | Layer 5 | ⭐⭐⭐⭐ Hard |

#### Behaviors
- Large dataset handling
- Virtual scrolling
- Sorting/filtering/searching
- In-place editing
- Cell navigation (2D)
- Data binding/synchronization

#### State Variables
```python
class DataGrid:
    data_source: List[Dict]
    columns: List[Column]
    visible_rows: List[int]  # Virtualization
    scroll_position: Tuple[int, int]
    selected_cells: Set[Tuple[int, int]]
    edited_cells: Dict[Tuple[int, int], Any]
    sort_column: Optional[int]
    sort_direction: str
    filters: Dict[int, Filter]
    cell_renderers: Dict[int, Callable]
    cell_editors: Dict[int, Component]
    active_editor: Optional[Tuple[int, int]]
    column_widths: List[int]
    frozen_columns: int
    frozen_rows: int
    total_width: int
    total_height: int
```

---

### Layer 7: Navigation & Flow Systems
**Complexity: 1000-2000 | LOC: 2000-4000 | State: 60-100**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Wizard | Navigation | `steps, validation, state, branching` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Multi-Step Form | Navigation | `pages, progress, state, validation` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Nested Flow | Navigation | `routes, stack, transition, guards` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Router | Navigation | `routes, history, params, guards` | Layer 5 | ⭐⭐⭐⭐⭐ Very Hard |
| Slideshow | View | `slides, navigation, transitions` | Layer 5 | ⭐⭐⭐⭐ Hard |
| Carousel | View | `items, index, loop, auto_play` | Layer 5 | ⭐⭐⭐⭐ Hard |
| Tree (Hierarchical) | View | `root, nodes, lazy_load, actions` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Breadcrumb | Navigation | `path, clickable, overflow` | Layer 3 | ⭐⭐⭐ Medium |

#### Behaviors
- Route management
- History stack
- State preservation across navigation
- Conditional rendering based on route
- Transition animations
- Guard functions (canActivate, canDeactivate)
- Deep linking

#### State Variables
```python
class Router:
    routes: Dict[str, Route]
    current_route: str
    history_stack: List[str]
    history_index: int
    route_params: Dict[str, Any]
    query_params: Dict[str, str]
    state: Dict[str, Any]
    guards: List[Callable]
    interceptors: List[Callable]
    transitions: Dict[Tuple[str, str], Transition]
    loading: bool
    error: Optional[Exception]
    default_route: str
    not_found_route: str
```

---

### Layer 8: Graph & Spatial Navigation
**Complexity: 2000-4000 | LOC: 4000-8000 | State: 100-150**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| 2D Navigation Map | Navigation | `grid, nodes, edges, pathfinding` | Layer 7 | ⭐⭐⭐⭐⭐ Very Hard |
| Mind Map | View | `nodes, connections, layout, zoom` | Layer 7 | ⭐⭐⭐⭐⭐ Very Hard |
| Network Graph | View | `nodes, edges, layout, physics` | Layer 7 | ⭐⭐⭐⭐⭐ Very Hard |
| Gantt Chart | View | `tasks, dependencies, timeline` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Kanban Board | View | `columns, cards, drag_drop, state` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Spatial Browser | Navigation | `items, positions, zoom, pan` | Layer 7 | ⭐⭐⭐⭐⭐ Very Hard |
| Hierarchical Tree | View | `data, renderer, collapsible, search` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |

#### Behaviors
- 2D coordinate management
- Pathfinding algorithms
- Collision detection
- Spatial queries (nearest, within bounds)
- Viewport management (pan, zoom)
- Interactive node editing
- Edge routing
- Layout algorithms (force-directed, hierarchical)

#### State Variables
```python
class NavigationMap:
    nodes: Dict[str, Node]
    edges: List[Edge]
    grid: Grid2D
    current_position: Tuple[int, int]
    viewport: Rect
    zoom_level: float
    selected_nodes: Set[str]
    hovered_node: Optional[str]
    path: List[Tuple[int, int]]
    obstacles: Set[Tuple[int, int]]
    traversable: Set[Tuple[int, int]]
    layout_algorithm: LayoutAlgorithm
    physics_enabled: bool
    collision_detection: bool
    node_renderers: Dict[str, Callable]
    edge_renderers: Dict[str, Callable]
    interaction_mode: str  # view, edit, navigate
    undo_stack: List[Action]
    redo_stack: List[Action]
```

---

### Layer 9: Application-Level Widgets
**Complexity: 4000+ | LOC: 8000+ | State: 150+**

#### Elements
| Element | Type | Attributes | Dependencies | Difficulty |
|---------|------|------------|--------------|------------|
| Dashboard | Application | `widgets, layout, state, data_sources` | Layer 6-8 | ⭐⭐⭐⭐⭐ Very Hard |
| IDE Panel | Application | `editor, explorer, terminal, debug` | Layer 7-8 | ⭐⭐⭐⭐⭐ Very Hard |
| Terminal Emulator | Application | `buffer, cursor, escape_handler` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Text Editor | Application | `buffer, syntax, undo, search, cursor` | Layer 6-7 | ⭐⭐⭐⭐⭐ Very Hard |
| File Manager | Application | `tree, preview, operations, state` | Layer 7 | ⭐⭐⭐⭐⭐ Very Hard |
| Music Player | Application | `playlist, controls, visualization` | Layer 6 | ⭐⭐⭐⭐⭐ Very Hard |
| Chat Interface | Application | `messages, input, users, rooms` | Layer 6-7 | ⭐⭐⭐⭐⭐ Very Hard |
| Game Board | Application | `state, rules, rendering, AI` | Layer 7-8 | ⭐⭐⭐⭐⭐ Very Hard |

#### Behaviors
- Entire application lifecycle
- Multiple coordinated subsystems
- Complex state management (Redux-like)
- Plugin architecture
- Configuration management
- Persistence layer
- Inter-widget communication
- Theme system
- Keyboard shortcuts registry

#### State Variables
```python
class Dashboard:
    widgets: List[Widget]
    layout: Layout
    data_sources: Dict[str, DataSource]
    global_state: State
    event_bus: EventBus
    config: Config
    theme: Theme
    shortcuts: Dict[str, Action]
    active_widget: Optional[str]
    widget_states: Dict[str, Any]
    refresh_intervals: Dict[str, int]
    connections: List[Connection]
    filters: Dict[str, Filter]
    transformations: Dict[str, Transform]
    alerts: List[Alert]
    history: CircularBuffer
    undo_manager: UndoManager
    plugin_manager: PluginManager
    persistence_layer: Storage
```

---

## Component Categories

### By Element Type

#### 1. PRIMITIVES (Difficulty: ⭐)
**Atomic building blocks with zero logic**

| Component | LOC | State Vars | Dependencies | Rendering | Difficulty |
|-----------|-----|------------|--------------|-----------|------------|
| Character | 1 | 0 | None | Direct | ⭐ |
| Symbol | 1 | 0 | None | Direct | ⭐ |
| Color | 1 | 0 | None | Modifier | ⭐ |
| Coordinate | 2 | 0 | None | N/A | ⭐ |
| Dimension | 2 | 0 | None | N/A | ⭐ |

---

#### 2. ATTRIBUTES (Difficulty: ⭐ - ⭐⭐)
**Styling and decoration modifiers**

| Component | LOC | State Vars | Dependencies | Rendering | Difficulty |
|-----------|-----|------------|--------------|-----------|------------|
| Bold | 5 | 0 | Color | Modifier | ⭐ |
| Italic | 5 | 0 | Color | Modifier | ⭐ |
| Underline | 5 | 0 | Color | Modifier | ⭐ |
| Strikethrough | 5 | 0 | Color | Modifier | ⭐ |
| Blink | 5 | 0 | Color | Modifier | ⭐ |
| Reverse | 5 | 0 | Color | Modifier | ⭐ |
| Foreground Color | 8 | 0 | Color | Modifier | ⭐ |
| Background Color | 8 | 0 | Color | Modifier | ⭐ |
| Gradient | 25 | 0 | Color | Complex | ⭐⭐ |
| Border Style | 15 | 0 | Character | Pattern | ⭐⭐ |
| Padding | 10 | 0 | Dimension | Layout | ⭐ |
| Margin | 10 | 0 | Dimension | Layout | ⭐ |
| Alignment | 15 | 0 | None | Layout | ⭐⭐ |

---

#### 3. DISPLAY ELEMENTS (Difficulty: ⭐ - ⭐⭐)
**Static or simple output components**

| Component | LOC | State Vars | Dependencies | Rendering | Difficulty |
|-----------|-----|------------|--------------|-----------|------------|
| Label | 20 | 1 | Styled Text | Single | ⭐ |
| Icon | 15 | 1 | Symbol | Single | ⭐ |
| Image (ASCII) | 50 | 1 | None | Multi-line | ⭐⭐ |
| Logo | 40 | 1 | Image | Multi-line | ⭐⭐ |
| Badge | 25 | 2 | Label | Single | ⭐⭐ |
| Tag | 25 | 2 | Label | Single | ⭐⭐ |
| Divider (H) | 20 | 1 | Character | Single | ⭐ |
| Divider (V) | 20 | 1 | Character | Single | ⭐ |
| Spacer | 15 | 1 | Dimension | None | ⭐ |
| Rule | 30 | 2 | Border | Single | ⭐⭐ |

---

#### 4. INPUT CONTROLS (Difficulty: ⭐⭐ - ⭐⭐⭐⭐)
**Interactive user input components**

| Component | LOC | State Vars | Dependencies | Event Handlers | Difficulty |
|-----------|-----|------------|--------------|----------------|------------|
| Button | 60 | 5 | Label | 3 (click, hover, key) | ⭐⭐ |
| Checkbox | 70 | 4 | Label, Icon | 2 (click, key) | ⭐⭐ |
| Radio Button | 80 | 5 | Label, Icon | 2 (click, key) | ⭐⭐ |
| Toggle | 75 | 4 | Label | 2 (click, key) | ⭐⭐ |
| TextBox (Static) | 100 | 6 | Label | 1 (key) | ⭐⭐⭐ |
| TextBox (Editable) | 350 | 12 | Label, Cursor | 8 (key, mouse, focus) | ⭐⭐⭐⭐ |
| TextArea | 450 | 15 | TextBox | 10 (key, mouse, scroll) | ⭐⭐⭐⭐ |
| Slider | 200 | 8 | Label | 5 (drag, click, key) | ⭐⭐⭐ |
| Spinner (Numeric) | 180 | 7 | TextBox, Button | 4 (click, key, wheel) | ⭐⭐⭐ |
| DatePicker | 400 | 20 | Calendar, TextBox | 12 | ⭐⭐⭐⭐⭐ |
| TimePicker | 300 | 15 | TextBox, Dropdown | 8 | ⭐⭐⭐⭐ |
| ColorPicker | 500 | 18 | Grid, Slider | 10 | ⭐⭐⭐⭐⭐ |

---

#### 5. CONTAINERS (Difficulty: ⭐⭐ - ⭐⭐⭐⭐)
**Components that hold and organize other components**

| Component | LOC | State Vars | Child Components | Layout Logic | Difficulty |
|-----------|-----|------------|------------------|--------------|------------|
| Panel | 80 | 5 | 0-20 | Simple | ⭐⭐ |
| Frame | 100 | 6 | 0-20 | Simple | ⭐⭐ |
| Box | 90 | 5 | 0-20 | Simple | ⭐⭐ |
| Card | 120 | 7 | 3-10 | Sectioned | ⭐⭐⭐ |
| Group | 70 | 4 | 0-20 | Stack | ⭐⭐ |
| Fieldset | 110 | 6 | 0-20 | Stack | ⭐⭐ |
| Stack (V) | 150 | 8 | 0-50 | Linear | ⭐⭐⭐ |
| Stack (H) | 150 | 8 | 0-50 | Linear | ⭐⭐⭐ |
| Grid | 300 | 15 | 0-100 | 2D Matrix | ⭐⭐⭐⭐ |
| Flex Container | 350 | 18 | 0-100 | Dynamic | ⭐⭐⭐⭐ |
| Scrollable | 250 | 12 | 1 | Viewport | ⭐⭐⭐⭐ |
| Split Panel | 280 | 14 | 2 | Resizable | ⭐⭐⭐⭐ |
| Tabs Container | 200 | 10 | 2-20 | Switched | ⭐⭐⭐ |
| Accordion | 220 | 12 | 2-20 | Collapsible | ⭐⭐⭐ |

---

#### 6. LISTS & COLLECTIONS (Difficulty: ⭐⭐ - ⭐⭐⭐⭐⭐)
**Components displaying multiple items**

| Component | LOC | State Vars | Item Types | Features | Difficulty |
|-----------|-----|------------|------------|----------|------------|
| List (Simple) | 120 | 8 | String | Selection, scroll | ⭐⭐ |
| List (Objects) | 250 | 15 | Object | Render fn, scroll | ⭐⭐⭐ |
| CheckList | 180 | 12 | String | Multi-select | ⭐⭐⭐ |
| Tree (2-level) | 300 | 18 | Node | Expand/collapse | ⭐⭐⭐⭐ |
| Tree (N-level) | 600 | 35 | Node | Recursive, lazy | ⭐⭐⭐⭐⭐ |
| Table (Static) | 200 | 12 | Row | Headers, scroll | ⭐⭐⭐ |
| Table (Sortable) | 350 | 20 | Row | Sort, scroll | ⭐⭐⭐⭐ |
| Data Grid | 1200 | 55 | Cell | Edit, filter, virtual | ⭐⭐⭐⭐⭐ |
| Gallery | 280 | 16 | Item | Grid layout, select | ⭐⭐⭐⭐ |
| Carousel | 320 | 18 | Slide | Navigation, loop | ⭐⭐⭐⭐ |

---

#### 7. NAVIGATION (Difficulty: ⭐⭐⭐ - ⭐⭐⭐⭐⭐)
**Components controlling application flow**

| Component | LOC | State Vars | Routes/Items | Navigation Logic | Difficulty |
|-----------|-----|------------|--------------|------------------|------------|
| Menu (Vertical) | 180 | 10 | 2-20 | Selection | ⭐⭐⭐ |
| Menu (Horizontal) | 180 | 10 | 2-20 | Selection | ⭐⭐⭐ |
| Context Menu | 220 | 12 | 2-20 | Popup, position | ⭐⭐⭐ |
| Menu Bar | 200 | 12 | 2-10 | Dropdown | ⭐⭐⭐ |
| Breadcrumb | 150 | 8 | 1-10 | Path display | ⭐⭐⭐ |
| Pagination | 180 | 9 | N/A | Page control | ⭐⭐⭐ |
| Stepper | 200 | 11 | 2-10 | Step tracking | ⭐⭐⭐ |
| Wizard | 800 | 45 | 2-10 | Multi-step, validation | ⭐⭐⭐⭐⭐ |
| Router | 1000 | 50 | 2-50 | History, guards | ⭐⭐⭐⭐⭐ |
| Tab Bar | 160 | 9 | 2-10 | Tab switching | ⭐⭐⭐ |

---

#### 8. FEEDBACK COMPONENTS (Difficulty: ⭐⭐ - ⭐⭐⭐⭐)
**Visual feedback and status indicators**

| Component | LOC | State Vars | Animation | Timing | Difficulty |
|-----------|-----|------------|-----------|--------|------------|
| Progress Bar | 100 | 6 | No | N/A | ⭐⭐ |
| Progress Circle | 150 | 7 | No | N/A | ⭐⭐⭐ |
| Spinner (Loading) | 80 | 5 | Yes | Frame-based | ⭐⭐ |
| Throbber | 70 | 4 | Yes | Frame-based | ⭐⭐ |
| Skeleton | 120 | 6 | Yes | Shimmer | ⭐⭐⭐ |
| Toast | 180 | 10 | Yes | Timeout | ⭐⭐⭐ |
| Notification | 200 | 12 | Yes | Timeout, dismiss | ⭐⭐⭐ |
| Snackbar | 190 | 11 | Yes | Slide, timeout | ⭐⭐⭐ |
| Alert | 160 | 9 | No | N/A | ⭐⭐⭐ |
| Badge (Counter) | 60 | 3 | No | N/A | ⭐⭐ |
| Status Indicator | 50 | 3 | Optional | Pulse | ⭐⭐ |
| Tooltip | 140 | 8 | Yes | Delay, position | ⭐⭐⭐ |

---

#### 9. DIALOGS & MODALS (Difficulty: ⭐⭐⭐ - ⭐⭐⭐⭐⭐)
**Modal/overlay interaction components**

| Component | LOC | State Vars | Components | Features | Difficulty |
|-----------|-----|------------|------------|----------|------------|
| Alert Dialog | 150 | 8 | 2 | Message, button | ⭐⭐⭐ |
| Confirm Dialog | 180 | 10 | 3 | Message, yes/no | ⭐⭐⭐ |
| Prompt Dialog | 250 | 14 | 4 | Message, input | ⭐⭐⭐⭐ |
| Dialog (Custom) | 300 | 18 | Variable | Full custom | ⭐⭐⭐⭐ |
| Modal | 280 | 16 | Variable | Backdrop, focus trap | ⭐⭐⭐⭐ |
| Drawer | 320 | 18 | Variable | Slide, position | ⭐⭐⭐⭐ |
| Bottom Sheet | 300 | 17 | Variable | Slide up | ⭐⭐⭐⭐ |
| Popover | 260 | 15 | Variable | Position, arrow | ⭐⭐⭐⭐ |
| Form Dialog | 600 | 35 | 5-20 | Validation, submit | ⭐⭐⭐⭐⭐ |

---

#### 10. ANIMATIONS & TRANSITIONS (Difficulty: ⭐⭐ - ⭐⭐⭐⭐)
**Temporal effects and motion**

| Component | LOC | State Vars | Frames | Timing Function | Difficulty |
|-----------|-----|------------|--------|-----------------|------------|
| Fade In/Out | 60 | 4 | N/A | Linear | ⭐⭐ |
| Slide In/Out | 80 | 5 | N/A | Linear | ⭐⭐ |
| Spin | 50 | 3 | 4-8 | Cyclic | ⭐⭐ |
| Pulse | 60 | 4 | N/A | Oscillate | ⭐⭐ |
| Bounce | 90 | 6 | N/A | Easing | ⭐⭐⭐ |
| Shake | 80 | 5 | N/A | Damped | ⭐⭐⭐ |
| Typewriter | 100 | 6 | Character | Sequential | ⭐⭐⭐ |
| Marquee | 120 | 7 | N/A | Continuous | ⭐⭐⭐ |
| Ripple | 150 | 9 | N/A | Radial expand | ⭐⭐⭐⭐ |
| Particle System | 400 | 25 | N/A | Physics | ⭐⭐⭐⭐⭐ |

---

#### 11. SPECIALIZED VIEWS (Difficulty: ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐)
**Domain-specific complex components**

| Component | LOC | State Vars | Sub-Components | Domain Logic | Difficulty |
|-----------|-----|------------|----------------|--------------|------------|
| Calendar | 500 | 28 | 5 | Date math | ⭐⭐⭐⭐ |
| File Browser | 700 | 38 | 8 | FS operations | ⭐⭐⭐⭐⭐ |
| Color Palette | 400 | 22 | 6 | Color theory | ⭐⭐⭐⭐ |
| Chart (Bar) | 350 | 20 | 4 | Scaling | ⭐⭐⭐⭐ |
| Chart (Line) | 380 | 22 | 5 | Interpolation | ⭐⭐⭐⭐ |
| Chart (Pie) | 320 | 18 | 4 | Angle math | ⭐⭐⭐⭐ |
| Gantt Chart | 900 | 50 | 10 | Timeline, deps | ⭐⭐⭐⭐⭐ |
| Kanban Board | 850 | 48 | 12 | Drag-drop, state | ⭐⭐⭐⭐⭐ |
| Mind Map | 1200 | 65 | 8 | Graph layout | ⭐⭐⭐⭐⭐ |
| Code Editor | 2000 | 90 | 15 | Syntax, undo | ⭐⭐⭐⭐⭐ |
| Terminal | 1800 | 80 | 10 | ANSI parsing | ⭐⭐⭐⭐⭐ |

---

## Inheritance & Composition Chains

### Common Inheritance Hierarchies

#### 1. Display Component Chain
```
Component (Base)
├─ Element
│  ├─ Primitive
│  │  ├─ Character
│  │  ├─ Symbol
│  │  └─ Color
│  └─ Styled
│     ├─ StyledText
│     ├─ StyledBackground
│     └─ Border
├─ DisplayComponent
│  ├─ Label
│  ├─ Icon
│  ├─ Image
│  └─ Divider
└─ InteractiveComponent
   └─ (See Input Hierarchy)
```

**Inheritance Depth**: 0-4 levels
**Complexity Impact**: +10 per level

---

#### 2. Input Component Chain
```
InteractiveComponent
├─ InputControl
│  ├─ Button
│  ├─ Checkbox
│  ├─ Radio
│  ├─ Toggle
│  └─ TextInput
│     ├─ TextBox
│     ├─ TextArea
│     └─ MaskedInput
├─ SelectControl
│  ├─ Dropdown
│  ├─ Combobox
│  └─ Autocomplete
└─ RangeControl
   ├─ Slider
   ├─ ProgressBar
   └─ Spinner
```

**Inheritance Depth**: 2-4 levels
**Complexity Impact**: +15 per level (more event handling)

---

#### 3. Container Component Chain
```
Component
└─ Container
   ├─ SimpleContainer
   │  ├─ Panel
   │  ├─ Frame
   │  └─ Box
   ├─ LayoutContainer
   │  ├─ Stack
   │  ├─ Grid
   │  ├─ Flex
   │  └─ SplitPanel
   └─ ScrollableContainer
      ├─ Scrollable
      ├─ VirtualScroll
      └─ InfiniteScroll
```

**Inheritance Depth**: 2-4 levels
**Complexity Impact**: +20 per level (layout calculations)

---

#### 4. List/Collection Component Chain
```
Container
└─ Collection
   ├─ List
   │  ├─ SimpleList
   │  ├─ ObjectList
   │  └─ CheckList
   ├─ Tree
   │  ├─ SimpleTree
   │  └─ LazyTree
   └─ Table
      ├─ StaticTable
      ├─ SortableTable
      └─ DataGrid
```

**Inheritance Depth**: 2-4 levels
**Complexity Impact**: +25 per level (data management)

---

#### 5. Navigation Component Chain
```
InteractiveComponent
└─ NavigationComponent
   ├─ Menu
   │  ├─ VerticalMenu
   │  ├─ HorizontalMenu
   │  └─ ContextMenu
   ├─ Navigator
   │  ├─ Tabs
   │  ├─ Breadcrumb
   │  └─ Pagination
   └─ FlowController
      ├─ Router
      ├─ Wizard
      └─ Stepper
```

**Inheritance Depth**: 2-4 levels
**Complexity Impact**: +30 per level (state routing)

---

#### 6. Dialog Component Chain
```
Container
└─ Overlay
   ├─ Modal
   │  ├─ Dialog
   │  │  ├─ AlertDialog
   │  │  ├─ ConfirmDialog
   │  │  └─ PromptDialog
   │  └─ CustomModal
   ├─ Drawer
   └─ Popover
      ├─ Tooltip
      └─ ContextMenu
```

**Inheritance Depth**: 2-5 levels
**Complexity Impact**: +35 per level (focus management)

---

### Composition Patterns

#### Pattern 1: Simple Composition (1-3 children)
```python
class Button:
    """Button = Label + Border + EventHandler"""
    def __init__(self):
        self.label = Label()
        self.border = Border()
        self.events = EventHandler()
```

**Complexity**: Low (⭐⭐)
**LOC**: 50-100

---

#### Pattern 2: Collection Composition (3-10 children)
```python
class Form:
    """Form = Title + Fields[] + Buttons[] + Validation"""
    def __init__(self):
        self.title = Label()
        self.fields = []  # List of InputControls
        self.buttons = []  # List of Buttons
        self.validator = Validator()
```

**Complexity**: Medium (⭐⭐⭐)
**LOC**: 200-400

---

#### Pattern 3: Deep Composition (10-50 children)
```python
class DataGrid:
    """Complex multi-level composition"""
    def __init__(self):
        self.header = Header([Column()])
        self.body = Body([Row([Cell()])])
        self.footer = Footer([StatusBar(), Pagination()])
        self.scrollbar_v = Scrollbar()
        self.scrollbar_h = Scrollbar()
        self.context_menu = ContextMenu()
        self.editor = CellEditor()
```

**Complexity**: High (⭐⭐⭐⭐⭐)
**LOC**: 1000-2000

---

#### Pattern 4: Recursive Composition (Tree-like)
```python
class TreeNode:
    """Recursive structure"""
    def __init__(self):
        self.label = Label()
        self.icon = Icon()
        self.children = []  # List of TreeNode
        self.expander = Button()
```

**Complexity**: Very High (⭐⭐⭐⭐⭐)
**LOC**: 600-1200
**Special**: Infinite depth potential

---

## Implementation Difficulty Reference

### Difficulty Calculation Formula

```python
def calculate_difficulty(component):
    base_score = (
        component.lines_of_code * 0.1 +
        component.state_variables * 2 +
        component.inheritance_depth * 5 +
        component.child_components * 0.5 +
        component.event_handlers * 3 +
        component.rendering_passes * 4
    )
    
    multipliers = {
        'has_animation': 1.5,
        'has_validation': 1.3,
        'has_virtualization': 2.0,
        'has_drag_drop': 1.8,
        'has_data_binding': 1.6,
        'has_async_ops': 1.4,
        'has_recursive_logic': 2.5
    }
    
    for feature, multiplier in multipliers.items():
        if getattr(component, feature, False):
            base_score *= multiplier
    
    return base_score
```

### Difficulty Tiers

| Tier | Score Range | Stars | Examples | Time to Implement |
|------|-------------|-------|----------|-------------------|
| **Trivial** | 0-10 | ⭐ | Character, Color, Symbol | 5-15 min |
| **Easy** | 10-50 | ⭐⭐ | Label, Button, Divider | 30 min - 2 hrs |
| **Medium** | 50-150 | ⭐⭐⭐ | TextBox, Menu, List | 2-8 hrs |
| **Hard** | 150-500 | ⭐⭐⭐⭐ | Form, Table, Tree | 1-3 days |
| **Very Hard** | 500+ | ⭐⭐⭐⭐⭐ | DataGrid, Router, Dashboard | 3-14 days |

---

### Component Readiness Matrix

Quick reference for determining implementation order:

| Component | Prerequisites | Difficulty | Priority | Notes |
|-----------|---------------|------------|----------|-------|
| **Character** | None | ⭐ | 1 | Start here |
| **Label** | Character, Style | ⭐ | 1 | Foundation |
| **Button** | Label, Events | ⭐⭐ | 2 | Core interaction |
| **List** | Label, Scrolling | ⭐⭐⭐ | 3 | Common pattern |
| **Menu** | List, Navigation | ⭐⭐⭐ | 3 | User navigation |
| **Dialog** | Container, Button | ⭐⭐⭐ | 4 | Modal flows |
| **Form** | Inputs, Validation | ⭐⭐⭐⭐ | 5 | Data collection |
| **Table** | List, Headers | ⭐⭐⭐⭐ | 5 | Data display |
| **DataGrid** | Table, Editing | ⭐⭐⭐⭐⭐ | 7 | Advanced data |
| **Router** | Navigation, State | ⭐⭐⭐⭐⭐ | 8 | App architecture |
| **Dashboard** | All above | ⭐⭐⭐⭐⭐ | 9 | Final integration |

---

## Summary

### Total Component Count by Layer

| Layer | Components | Avg Difficulty | Total LOC Range |
|-------|------------|----------------|-----------------|
| 0 | 5 | ⭐ | 1-5 |
| 1 | 5 | ⭐ | 5-20 |
| 2 | 9 | ⭐⭐ | 20-80 |
| 3 | 8 | ⭐⭐ | 80-200 |
| 4 | 9 | ⭐⭐⭐ | 200-500 |
| 5 | 10 | ⭐⭐⭐⭐ | 500-1000 |
| 6 | 8 | ⭐⭐⭐⭐ | 1000-2000 |
| 7 | 8 | ⭐⭐⭐⭐⭐ | 2000-4000 |
| 8 | 7 | ⭐⭐⭐⭐⭐ | 4000-8000 |
| 9 | 8 | ⭐⭐⭐⭐⭐ | 8000+ |

**Total Components**: 77+

### Component Categories Summary

| Category | Count | Difficulty Range |
|----------|-------|------------------|
| Primitives | 5 | ⭐ |
| Attributes | 13 | ⭐ - ⭐⭐ |
| Display | 10 | ⭐ - ⭐⭐ |
| Input Controls | 12 | ⭐⭐ - ⭐⭐⭐⭐⭐ |
| Containers | 14 | ⭐⭐ - ⭐⭐⭐⭐ |
| Lists & Collections | 10 | ⭐⭐ - ⭐⭐⭐⭐⭐ |
| Navigation | 10 | ⭐⭐⭐ - ⭐⭐⭐⭐⭐ |
| Feedback | 12 | ⭐⭐ - ⭐⭐⭐⭐ |
| Dialogs & Modals | 9 | ⭐⭐⭐ - ⭐⭐⭐⭐⭐ |
| Animations | 10 | ⭐⭐ - ⭐⭐⭐⭐⭐ |
| Specialized Views | 11 | ⭐⭐⭐⭐ - ⭐⭐⭐⭐⭐ |

---

## Menu Component Construction Guide

### Menu Scope Items by Difficulty

#### 1. Simple Menu (Difficulty: ⭐⭐⭐)

**Component:** Vertical Menu with keyboard navigation

**Dependencies (-1 Depth - Atomics):**
- `Character` - Individual characters for text and borders
- `Color` - ANSI color codes for styling
- `Coordinate` - Position tracking (x, y)
- `Styled Character` - Characters with applied colors/attributes

**Derivatives (+1 Level - Built from this):**
- `Context Menu` - Menu with popup positioning
- `Dropdown Menu` - Menu with expand/collapse state
- `Menu Bar` - Horizontal menu container
- `Hierarchical Menu` - Menu with submenus

**Constructor Code:**

```python
class SimpleMenu:
    """Basic vertical menu with keyboard navigation"""
    
    def __init__(self, items: List[str], title: str = "Menu"):
        # Core state (-1 atomics)
        self.items = items                    # List of menu item strings
        self.title = title                    # Menu title
        self.selected_index = 0               # Currently selected item
        self.position = (0, 0)               # Screen coordinates (Coordinate)
        
        # Visual properties (styled atomics)
        self.fg_normal = '\033[37m'          # Normal text color (Color)
        self.fg_selected = '\033[30m'        # Selected text color (Color)
        self.bg_selected = '\033[47m'        # Selected background (Color)
        self.border_char = '─'               # Border character (Character)
        
        # State tracking
        self.visible = True
        self.focused = True
    
    def render(self) -> List[str]:
        """Generate menu display lines"""
        output = []
        
        # Title with border
        width = max(len(self.title), max(len(item) for item in self.items)) + 4
        output.append(f"╭{'─' * (width - 2)}╮")
        output.append(f"│ {self.title.center(width - 4)} │")
        output.append(f"├{'─' * (width - 2)}┤")
        
        # Menu items
        for i, item in enumerate(self.items):
            if i == self.selected_index:
                # Selected item (Styled Character composition)
                output.append(f"│{self.bg_selected}{self.fg_selected}▶ {item.ljust(width - 4)}\033[0m│")
            else:
                # Normal item
                output.append(f"│{self.fg_normal}  {item.ljust(width - 4)}\033[0m│")
        
        # Bottom border
        output.append(f"╰{'─' * (width - 2)}╯")
        
        return output
    
    def handle_input(self, key: str) -> Optional[int]:
        """Handle keyboard input, return selected index if enter pressed"""
        if key == 'up' and self.selected_index > 0:
            self.selected_index -= 1
        elif key == 'down' and self.selected_index < len(self.items) - 1:
            self.selected_index += 1
        elif key == 'enter':
            return self.selected_index
        return None
```

---

#### 2. Interactive List (Difficulty: ⭐⭐⭐)

**Component:** Scrollable list with selection

**Dependencies (-1 Depth - Atomics):**
- `Character` - List item text
- `Color` - Selection highlighting
- `Coordinate` - Scroll offset, cursor position
- `Dimension` - Viewport size (width, height)

**Derivatives (+1 Level - Built from this):**
- `CheckList` - List with checkbox per item
- `Tree View` - Hierarchical list with expand/collapse
- `File Browser` - List specialized for file system
- `Search Results List` - List with filtering

**Constructor Code:**

```python
class InteractiveList:
    """Scrollable list with keyboard/mouse selection"""
    
    def __init__(self, items: List[str], height: int = 10):
        # Core state (-1 atomics)
        self.items = items                    # All list items
        self.selected_index = 0               # Current selection
        self.scroll_offset = 0                # Top visible item index
        self.viewport_height = height         # Dimension (height)
        self.position = (0, 0)               # Coordinate (x, y)
        
        # Visual properties
        self.width = 40                       # Dimension (width)
        self.show_scrollbar = True
        self.show_indices = True
        
        # Selection colors (Color atomics)
        self.color_normal = '\033[0m'
        self.color_selected = '\033[7m'       # Reverse video
        self.color_scrollbar = '\033[90m'     # Dim gray
    
    def get_visible_items(self) -> List[Tuple[int, str]]:
        """Get items currently in viewport"""
        start = self.scroll_offset
        end = min(start + self.viewport_height, len(self.items))
        return [(i, self.items[i]) for i in range(start, end)]
    
    def render(self) -> List[str]:
        """Generate list display lines"""
        output = []
        visible = self.get_visible_items()
        
        for idx, item in visible:
            # Build line with index and item
            if self.show_indices:
                prefix = f"{idx + 1:3}. "
            else:
                prefix = "  "
            
            # Truncate item to fit width
            display_item = item[:self.width - len(prefix) - 3]
            line = f"{prefix}{display_item.ljust(self.width - len(prefix) - 1)}"
            
            # Apply selection highlight
            if idx == self.selected_index:
                line = f"{self.color_selected}{line}\033[0m"
            else:
                line = f"{self.color_normal}{line}"
            
            # Add scrollbar indicator
            if self.show_scrollbar:
                if len(self.items) > self.viewport_height:
                    scroll_pos = idx - self.scroll_offset
                    scroll_size = len(self.items)
                    scroll_ratio = scroll_pos / scroll_size
                    
                    # Simple scrollbar: █ for current area, │ for track
                    if self.scroll_offset <= idx < self.scroll_offset + self.viewport_height:
                        bar = f"{self.color_scrollbar}█\033[0m"
                    else:
                        bar = f"{self.color_scrollbar}│\033[0m"
                    
                    line += bar
            
            output.append(line)
        
        return output
    
    def handle_input(self, key: str) -> Optional[str]:
        """Handle navigation input"""
        if key == 'up':
            if self.selected_index > 0:
                self.selected_index -= 1
                # Scroll up if needed
                if self.selected_index < self.scroll_offset:
                    self.scroll_offset = self.selected_index
        
        elif key == 'down':
            if self.selected_index < len(self.items) - 1:
                self.selected_index += 1
                # Scroll down if needed
                if self.selected_index >= self.scroll_offset + self.viewport_height:
                    self.scroll_offset = self.selected_index - self.viewport_height + 1
        
        elif key == 'page_up':
            self.selected_index = max(0, self.selected_index - self.viewport_height)
            self.scroll_offset = max(0, self.scroll_offset - self.viewport_height)
        
        elif key == 'page_down':
            self.selected_index = min(len(self.items) - 1, 
                                     self.selected_index + self.viewport_height)
            self.scroll_offset = min(len(self.items) - self.viewport_height,
                                    self.scroll_offset + self.viewport_height)
        
        elif key == 'home':
            self.selected_index = 0
            self.scroll_offset = 0
        
        elif key == 'end':
            self.selected_index = len(self.items) - 1
            self.scroll_offset = max(0, len(self.items) - self.viewport_height)
        
        elif key == 'enter':
            return self.items[self.selected_index]
        
        return None
```

---

#### 3. Button (Difficulty: ⭐⭐)

**Component:** Interactive button with click/hover states

**Dependencies (-1 Depth - Atomics):**
- `Character` - Button text and border
- `Color` - State-based colors
- `Styled Character` - Text with attributes (bold, underline)
- `Coordinate` - Button position

**Derivatives (+1 Level - Built from this):**
- `Toggle Button` - Button with on/off states
- `Button Group` - Multiple buttons in container
- `Icon Button` - Button with symbol instead of text
- `Split Button` - Button with dropdown menu

**Constructor Code:**

```python
class Button:
    """Interactive button with multiple states"""
    
    def __init__(self, label: str, callback: Callable = None):
        # Core state (-1 atomics)
        self.label = label                    # Button text (Character sequence)
        self.callback = callback              # Action on click
        self.position = (0, 0)               # Coordinate (x, y)
        
        # State machine
        self.enabled = True
        self.focused = False
        self.hovered = False
        self.pressed = False
        
        # Visual properties (Color atomics)
        self.color_normal = '\033[37m'        # White text
        self.color_focused = '\033[36m'       # Cyan when focused
        self.color_disabled = '\033[90m'      # Gray when disabled
        self.bg_normal = '\033[44m'           # Blue background
        self.bg_hover = '\033[46m'            # Cyan background on hover
        self.bg_pressed = '\033[45m'          # Magenta when pressed
        
        # Border characters (Character atomics)
        self.border_style = {
            'normal': ['[', ']'],
            'focused': ['<', '>'],
            'pressed': ['{', '}']
        }
        
        # Padding
        self.padding = 1
    
    def get_width(self) -> int:
        """Calculate button width (Dimension)"""
        return len(self.label) + 2 * self.padding + 2  # +2 for borders
    
    def render(self) -> str:
        """Generate button display string"""
        # Determine current style based on state
        if not self.enabled:
            fg_color = self.color_disabled
            bg_color = ''
            borders = ['[', ']']
        elif self.pressed:
            fg_color = self.color_normal
            bg_color = self.bg_pressed
            borders = self.border_style['pressed']
        elif self.hovered:
            fg_color = self.color_normal
            bg_color = self.bg_hover
            borders = self.border_style['normal']
        elif self.focused:
            fg_color = self.color_focused
            bg_color = self.bg_normal
            borders = self.border_style['focused']
        else:
            fg_color = self.color_normal
            bg_color = self.bg_normal
            borders = self.border_style['normal']
        
        # Build padded label
        padded_label = f"{' ' * self.padding}{self.label}{' ' * self.padding}"
        
        # Compose styled button (Styled Character composition)
        button_text = f"{bg_color}{fg_color}{borders[0]}{padded_label}{borders[1]}\033[0m"
        
        return button_text
    
    def handle_click(self) -> bool:
        """Handle button click, return True if action executed"""
        if self.enabled and self.callback:
            self.callback()
            return True
        return False
    
    def handle_input(self, key: str) -> bool:
        """Handle keyboard input (space/enter activates)"""
        if key in ('enter', 'space') and self.enabled:
            return self.handle_click()
        return False
```

---

#### 4. Dialog Box (Difficulty: ⭐⭐⭐⭐)

**Component:** Modal dialog with title, content, and buttons

**Dependencies (-1 Depth - Atomics):**
- `Character` - Text and borders
- `Color` - Title, content, button colors
- `Coordinate` - Dialog position, centered
- `Dimension` - Dialog width and height
- `Button` - Action buttons (Layer 2 component)
- `Label` - Title and message text (Layer 2 component)

**Derivatives (+1 Level - Built from this):**
- `Confirm Dialog` - Dialog with Yes/No buttons
- `Alert Dialog` - Dialog with OK button only
- `Prompt Dialog` - Dialog with text input field
- `Form Dialog` - Dialog with multiple input fields

**Constructor Code:**

```python
class DialogBox:
    """Modal dialog with customizable content and buttons"""
    
    def __init__(self, title: str, message: str, buttons: List[str] = None):
        # Core state (-1 atomics combined in Layer 2 components)
        self.title = title                    # Title text
        self.message = message                # Message text
        self.buttons = buttons or ["OK"]      # Button labels
        
        # Position and size (Coordinate, Dimension atomics)
        self.width = 50
        self.height = 10
        self.position = None                  # None = centered
        
        # State management
        self.visible = False
        self.result = None
        self.focused_button = 0
        
        # Visual properties (Color atomics)
        self.color_title = '\033[1m\033[36m'  # Bold cyan
        self.color_message = '\033[37m'       # White
        self.color_border = '\033[90m'        # Dim
        self.bg_dialog = '\033[40m'           # Black background
        self.bg_backdrop = '\033[0;40m'       # Dim backdrop
        
        # Border style (Character atomics)
        self.border_chars = {
            'tl': '╭', 'tr': '╮', 'bl': '╰', 'br': '╯',
            'h': '─', 'v': '│'
        }
        
        # Button components (Layer 2 components - derivatives of atomics)
        self.button_components = [
            Button(label, callback=lambda i=i: self._on_button_click(i))
            for i, label in enumerate(self.buttons)
        ]
    
    def center_position(self, screen_width: int, screen_height: int):
        """Calculate centered position (Coordinate calculation)"""
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.position = (x, y)
    
    def render(self) -> List[str]:
        """Generate dialog display lines"""
        output = []
        
        # Top border
        top_line = (f"{self.color_border}{self.border_chars['tl']}"
                   f"{self.border_chars['h'] * (self.width - 2)}"
                   f"{self.border_chars['tr']}\033[0m")
        output.append(top_line)
        
        # Title line
        title_text = self.title.center(self.width - 4)
        title_line = (f"{self.color_border}{self.border_chars['v']}\033[0m"
                     f"{self.bg_dialog}{self.color_title} {title_text} \033[0m"
                     f"{self.color_border}{self.border_chars['v']}\033[0m")
        output.append(title_line)
        
        # Separator
        sep_line = (f"{self.color_border}{self.border_chars['v']}"
                   f"{self.border_chars['h'] * (self.width - 2)}"
                   f"{self.border_chars['v']}\033[0m")
        output.append(sep_line)
        
        # Message lines (word-wrapped)
        message_lines = self._wrap_text(self.message, self.width - 6)
        for msg_line in message_lines:
            padded = msg_line.ljust(self.width - 4)
            content_line = (f"{self.color_border}{self.border_chars['v']}\033[0m"
                          f"{self.bg_dialog}{self.color_message} {padded} \033[0m"
                          f"{self.color_border}{self.border_chars['v']}\033[0m")
            output.append(content_line)
        
        # Empty line before buttons
        empty_line = (f"{self.color_border}{self.border_chars['v']}\033[0m"
                     f"{self.bg_dialog}{' ' * (self.width - 2)}\033[0m"
                     f"{self.color_border}{self.border_chars['v']}\033[0m")
        output.append(empty_line)
        
        # Buttons line (centered)
        button_texts = []
        for i, btn in enumerate(self.button_components):
            btn.focused = (i == self.focused_button)
            button_texts.append(btn.render())
        
        buttons_combined = "  ".join(button_texts)
        button_padding = (self.width - len(self._strip_ansi(buttons_combined)) - 4) // 2
        button_line = (f"{self.color_border}{self.border_chars['v']}\033[0m"
                      f"{self.bg_dialog}{' ' * button_padding}{buttons_combined}"
                      f"{' ' * button_padding}\033[0m"
                      f"{self.color_border}{self.border_chars['v']}\033[0m")
        output.append(button_line)
        
        # Bottom border
        bottom_line = (f"{self.color_border}{self.border_chars['bl']}"
                      f"{self.border_chars['h'] * (self.width - 2)}"
                      f"{self.border_chars['br']}\033[0m")
        output.append(bottom_line)
        
        return output
    
    def _wrap_text(self, text: str, width: int) -> List[str]:
        """Word-wrap text to fit width"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) <= width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(" ".join(current_line))
        
        return lines
    
    def _strip_ansi(self, text: str) -> str:
        """Remove ANSI codes for length calculation"""
        import re
        return re.sub(r'\033\[[0-9;]*m', '', text)
    
    def _on_button_click(self, button_index: int):
        """Handle button click"""
        self.result = button_index
        self.visible = False
    
    def handle_input(self, key: str) -> Optional[int]:
        """Handle keyboard navigation"""
        if key == 'left':
            self.focused_button = max(0, self.focused_button - 1)
        elif key == 'right':
            self.focused_button = min(len(self.buttons) - 1, self.focused_button + 1)
        elif key == 'enter':
            self._on_button_click(self.focused_button)
            return self.result
        elif key == 'escape':
            self.visible = False
            return None
        
        return None
    
    def show(self) -> int:
        """Display dialog and return selected button index"""
        self.visible = True
        self.result = None
        # (Main loop would handle rendering and input until visible=False)
        return self.result
```

---

#### 5. Progress Bar (Difficulty: ⭐⭐)

**Component:** Visual progress indicator

**Dependencies (-1 Depth - Atomics):**
- `Character` - Bar fill characters (█, ░)
- `Color` - Bar colors (complete vs remaining)
- `Dimension` - Bar width
- `Coordinate` - Bar position

**Derivatives (+1 Level - Built from this):**
- `Progress Ring` - Circular progress indicator
- `Multi-Progress` - Multiple stacked progress bars
- `Indeterminate Progress` - Animated loading bar
- `Segmented Progress` - Progress with step markers

**Constructor Code:**

```python
class ProgressBar:
    """Visual progress indicator with percentage display"""
    
    def __init__(self, total: int = 100, width: int = 40):
        # Core state
        self.value = 0                        # Current progress
        self.total = total                    # Maximum value
        self.width = width                    # Dimension (bar width in chars)
        self.position = (0, 0)               # Coordinate (x, y)
        
        # Visual properties (Character atomics)
        self.char_filled = '█'               # Completed portion
        self.char_empty = '░'                # Remaining portion
        self.char_partial = '▌'              # Fractional completion
        
        # Colors (Color atomics)
        self.color_filled = '\033[32m'       # Green for complete
        self.color_empty = '\033[90m'        # Dim for remaining
        self.color_text = '\033[37m'         # White for percentage
        self.color_border = '\033[90m'       # Dim for border
        
        # Display options
        self.show_percentage = True
        self.show_value = True
        self.show_border = True
        
        # Label
        self.label = ""
    
    def set_value(self, value: int):
        """Update progress value"""
        self.value = min(max(0, value), self.total)
    
    def increment(self, amount: int = 1):
        """Increment progress"""
        self.set_value(self.value + amount)
    
    def get_percentage(self) -> float:
        """Calculate completion percentage"""
        if self.total == 0:
            return 100.0
        return (self.value / self.total) * 100.0
    
    def render(self) -> str:
        """Generate progress bar display"""
        percentage = self.get_percentage()
        
        # Calculate filled characters
        bar_width = self.width - 2 if self.show_border else self.width
        filled_width = int((percentage / 100.0) * bar_width)
        empty_width = bar_width - filled_width
        
        # Build bar segments (Character composition)
        filled_segment = self.char_filled * filled_width
        empty_segment = self.char_empty * empty_width
        
        # Apply colors (Styled Character composition)
        colored_filled = f"{self.color_filled}{filled_segment}\033[0m"
        colored_empty = f"{self.color_empty}{empty_segment}\033[0m"
        
        # Build complete bar
        if self.show_border:
            bar = f"{self.color_border}[{colored_filled}{colored_empty}]{self.color_border}\033[0m"
        else:
            bar = f"{colored_filled}{colored_empty}"
        
        # Add percentage text
        if self.show_percentage:
            pct_text = f"{self.color_text} {percentage:5.1f}%\033[0m"
            bar += pct_text
        
        # Add value text
        if self.show_value:
            val_text = f"{self.color_text} ({self.value}/{self.total})\033[0m"
            bar += val_text
        
        # Add label prefix
        if self.label:
            bar = f"{self.color_text}{self.label}: \033[0m{bar}"
        
        return bar
    
    def render_multiline(self) -> List[str]:
        """Generate multi-line display with label above bar"""
        output = []
        
        if self.label:
            output.append(f"{self.color_text}{self.label}\033[0m")
        
        output.append(self.render())
        
        return output
```

---

#### 6. Text Input Box (Difficulty: ⭐⭐⭐⭐)

**Component:** Editable text field with cursor

**Dependencies (-1 Depth - Atomics):**
- `Character` - Input text, cursor character
- `Color` - Text color, border color, cursor color
- `Coordinate` - Cursor position, scroll offset
- `Dimension` - Input width, max length

**Derivatives (+1 Level - Built from this):**
- `Password Input` - Masked text input (shows ***)
- `Number Input` - Numeric-only input with validation
- `Search Box` - Input with search icon and clear button
- `Auto-complete Input` - Input with suggestion dropdown

**Constructor Code:**

```python
class TextInputBox:
    """Editable single-line text input with cursor"""
    
    def __init__(self, width: int = 30, max_length: int = 100):
        # Core state
        self.text = ""                        # Current input text
        self.cursor_position = 0              # Cursor index in text
        self.scroll_offset = 0                # Horizontal scroll for long text
        
        # Dimensions (Dimension atomics)
        self.width = width                    # Visible width
        self.max_length = max_length          # Maximum input length
        
        # Position (Coordinate atomic)
        self.position = (0, 0)
        
        # State flags
        self.focused = False
        self.enabled = True
        self.modified = False
        
        # Visual properties (Color atomics)
        self.color_text = '\033[37m'          # White text
        self.color_cursor = '\033[7m'         # Reverse video cursor
        self.color_border = '\033[90m'        # Dim border
        self.color_focused = '\033[36m'       # Cyan when focused
        self.color_disabled = '\033[90m'      # Gray when disabled
        
        # Border characters (Character atomics)
        self.border_style = ['[', ']']
        self.cursor_char = '█'
        
        # Placeholder
        self.placeholder = ""
        self.color_placeholder = '\033[90m'
        
        # Validation
        self.validator = None                 # Optional validation function
        self.valid = True
    
    def insert_char(self, char: str):
        """Insert character at cursor position"""
        if not self.enabled:
            return
        
        if len(self.text) < self.max_length and char.isprintable():
            self.text = (self.text[:self.cursor_position] + 
                        char + 
                        self.text[self.cursor_position:])
            self.cursor_position += 1
            self.modified = True
            self._validate()
            self._adjust_scroll()
    
    def delete_char(self):
        """Delete character before cursor (backspace)"""
        if not self.enabled or self.cursor_position == 0:
            return
        
        self.text = (self.text[:self.cursor_position - 1] + 
                    self.text[self.cursor_position:])
        self.cursor_position -= 1
        self.modified = True
        self._validate()
        self._adjust_scroll()
    
    def delete_forward(self):
        """Delete character at cursor (delete)"""
        if not self.enabled or self.cursor_position >= len(self.text):
            return
        
        self.text = (self.text[:self.cursor_position] + 
                    self.text[self.cursor_position + 1:])
        self.modified = True
        self._validate()
    
    def move_cursor(self, direction: str):
        """Move cursor left or right"""
        if direction == 'left':
            self.cursor_position = max(0, self.cursor_position - 1)
        elif direction == 'right':
            self.cursor_position = min(len(self.text), self.cursor_position + 1)
        elif direction == 'home':
            self.cursor_position = 0
        elif direction == 'end':
            self.cursor_position = len(self.text)
        
        self._adjust_scroll()
    
    def _adjust_scroll(self):
        """Adjust horizontal scroll to keep cursor visible"""
        # Scroll right if cursor beyond visible area
        if self.cursor_position >= self.scroll_offset + self.width - 2:
            self.scroll_offset = self.cursor_position - self.width + 3
        
        # Scroll left if cursor before visible area
        if self.cursor_position < self.scroll_offset:
            self.scroll_offset = self.cursor_position
        
        # Keep scroll offset in bounds
        self.scroll_offset = max(0, self.scroll_offset)
    
    def _validate(self):
        """Run validation if validator provided"""
        if self.validator:
            self.valid = self.validator(self.text)
        else:
            self.valid = True
    
    def render(self) -> str:
        """Generate input box display"""
        # Determine colors based on state
        if not self.enabled:
            text_color = self.color_disabled
            border_color = self.color_disabled
        elif not self.valid:
            text_color = '\033[31m'  # Red for invalid
            border_color = '\033[31m'
        elif self.focused:
            text_color = self.color_text
            border_color = self.color_focused
        else:
            text_color = self.color_text
            border_color = self.color_border
        
        # Get visible portion of text
        visible_text = self.text[self.scroll_offset:self.scroll_offset + self.width - 2]
        
        # Show placeholder if empty
        if not visible_text and not self.focused and self.placeholder:
            visible_text = self.placeholder[:self.width - 2]
            text_color = self.color_placeholder
        
        # Build text with cursor (Character and Styled Character composition)
        if self.focused:
            cursor_pos_in_view = self.cursor_position - self.scroll_offset
            
            # Insert cursor at position
            text_before = visible_text[:cursor_pos_in_view]
            cursor = self.cursor_char if cursor_pos_in_view < len(visible_text) else ' '
            text_after = visible_text[cursor_pos_in_view + 1:]
            
            # Apply cursor highlighting
            display_text = (f"{text_color}{text_before}"
                          f"{self.color_cursor}{cursor}\033[0m"
                          f"{text_color}{text_after}\033[0m")
        else:
            display_text = f"{text_color}{visible_text}\033[0m"
        
        # Pad to width
        padding_needed = self.width - 2 - len(visible_text)
        if padding_needed > 0:
            display_text += f"{text_color}{' ' * padding_needed}\033[0m"
        
        # Add border
        input_box = (f"{border_color}{self.border_style[0]}\033[0m"
                    f"{display_text}"
                    f"{border_color}{self.border_style[1]}\033[0m")
        
        return input_box
    
    def handle_input(self, key: str, char: str = None) -> bool:
        """
        Handle keyboard input
        key: special key name ('backspace', 'delete', 'left', etc.)
        char: printable character if any
        Returns True if input was handled
        """
        if not self.enabled:
            return False
        
        if key == 'backspace':
            self.delete_char()
            return True
        elif key == 'delete':
            self.delete_forward()
            return True
        elif key == 'left':
            self.move_cursor('left')
            return True
        elif key == 'right':
            self.move_cursor('right')
            return True
        elif key == 'home':
            self.move_cursor('home')
            return True
        elif key == 'end':
            self.move_cursor('end')
            return True
        elif char and char.isprintable():
            self.insert_char(char)
            return True
        
        return False
    
    def get_value(self) -> str:
        """Get current input value"""
        return self.text
    
    def set_value(self, value: str):
        """Set input value programmatically"""
        self.text = value[:self.max_length]
        self.cursor_position = len(self.text)
        self.modified = False
        self._validate()
        self._adjust_scroll()
    
    def clear(self):
        """Clear input"""
        self.text = ""
        self.cursor_position = 0
        self.scroll_offset = 0
        self.modified = False
        self.valid = True
```

---

### Quick Reference: Component Hierarchy

```
Atomics (Layer -1)          Component (Layer 0)              Derivatives (Layer +1)
─────────────────────────── ──────────────────────────────── ────────────────────────────────
Character, Color,           SimpleMenu                       ContextMenu, DropdownMenu,
Coordinate, Styled Char  →  (⭐⭐⭐)                        →  MenuBar, HierarchicalMenu

Character, Color,           InteractiveList                  CheckList, TreeView,
Coordinate, Dimension    →  (⭐⭐⭐)                        →  FileBrowser, SearchResults

Character, Color,           Button                           ToggleButton, ButtonGroup,
Styled Char, Coordinate  →  (⭐⭐)                          →  IconButton, SplitButton

Character, Color,           ProgressBar                      ProgressRing, MultiProgress,
Dimension, Coordinate    →  (⭐⭐)                          →  IndeterminateProgress

Character, Color,           TextInputBox                     PasswordInput, NumberInput,
Coordinate, Dimension    →  (⭐⭐⭐⭐)                      →  SearchBox, AutoComplete

Button, Label, Character,   DialogBox                        ConfirmDialog, AlertDialog,
Color, Coordinate        →  (⭐⭐⭐⭐)                      →  PromptDialog, FormDialog
```
