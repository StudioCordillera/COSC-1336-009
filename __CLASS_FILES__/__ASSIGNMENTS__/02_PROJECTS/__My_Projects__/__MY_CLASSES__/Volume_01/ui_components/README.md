# UI Components Library
**MenuNav Standard Phase 1 Implementation**

Complete set of 31+ terminal UI components with responsive layout and robust rendering.

---

## ✅ Features

- **Responsive Layout** - All components support percentages (0.0-1.0) or absolute positioning
- **State Management** - Components track IDLE, ACTIVE, FOCUSED, and DISABLED states
- **Robust Rendering** - Handles terminal resize, minimum widths, and content clipping
- **Modular Design** - Composable components with parent-child relationships
- **Clean Formatting** - Consistent box drawing using Python doc-style ASCII

---

## 📦 Package Structure

```
ui_components/
├── __init__.py          # Package exports
├── base.py              # Component base class
├── containers.py        # Wrapper, Panel, Frame, Section, Dialogue, Menu
├── display.py           # Header, Title, Label, Prompt, Message, List, Tree, Preview
├── input.py             # InputField, TextField, TextArea, Button, Checkbox, Toggle, Dropdown, Selector
├── navigation.py        # Breadcrumb, NavigationControls, NavigationButtons, Pagination, Tabs
├── specialized.py       # ChoiceObject, ParamField, CheckboxList, DirectoryTree, StatusBar
├── demo.py              # Interactive demo of all components
└── example_main_menu.py # MenuNav Standard catalog example #1
```

---

## 🚀 Quick Start

### Run the Demo
```bash
python -m ui_components.demo
```

### Run Main Menu Example
```bash
python -m ui_components.example_main_menu
```

### Basic Usage
```python
from ui_components import Panel, Button, Label

# Create components with responsive positioning
panel = Panel(0.2, 0.2, 0.6, 0.5, title="My Panel")
panel.render()

button = Button(0.5, 0.4, 20, "Click Me")
button.set_state(button.STATE_ACTIVE)
button.render()

label = Label(10, 20, 40, "Hello World", align="center")
label.render()
```

---

## 📚 Component Reference

### Container Components (6)
| Component | Purpose | Key Features |
|-----------|---------|-------------|
| **Wrapper** | Generic container | Optional padding and border |
| **Panel** | Bordered container | Optional title on border |
| **Frame** | Decorative container | Title, subtitle, decorative border |
| **Section** | Logical grouping | Label and separator line |
| **Dialogue** | Modal container | Auto-centered, titled |
| **Menu** | Navigation container | Title, prompt, choice list |

### Display Components (8)
| Component | Purpose | Key Features |
|-----------|---------|-------------|
| **Header** | Section heading | Optional underline |
| **Title** | Primary label | Large text, centered option |
| **Label** | Text display | Left/center/right alignment |
| **Prompt** | User instruction | Icon/marker prefix |
| **Message** | Notification | Info/warning/error/success styles |
| **List** | Ordered items | Numbered or bulleted |
| **Tree** | Hierarchical display | Indent levels |
| **Preview** | Content area | Bordered preview box |

### Input Components (8)
| Component | Purpose | Key Features |
|-----------|---------|-------------|
| **InputField** | Single-line input | Placeholder support |
| **TextField** | Validated input | Label, required flag, validation |
| **TextArea** | Multi-line input | Bordered, scrollable |
| **Button** | Action trigger | State-based styling |
| **Checkbox** | Boolean toggle | Checked/unchecked visual |
| **Toggle** | Binary switch | ON/OFF display |
| **Dropdown** | List selector | Collapsed/expanded states |
| **Selector** | Choice picker | Arrow navigation |

### Navigation Components (5)
| Component | Purpose | Key Features |
|-----------|---------|-------------|
| **Breadcrumb** | Path display | Customizable separator |
| **NavigationControls** | Movement buttons | Back/forward/up controls |
| **NavigationButtons** | Action button set | Multiple buttons, selection |
| **Pagination** | Page control | Prev/next, page numbers |
| **Tabs** | View switcher | Active tab indicator |

### Specialized Components (5)
| Component | Purpose | Key Features |
|-----------|---------|-------------|
| **ChoiceObject** | Menu item | Number, text, arrow |
| **ParamField** | Labeled input | Label + input pair |
| **CheckboxList** | Multi-select list | Checkboxes with focus |
| **DirectoryTree** | File browser | Hierarchical file display |
| **StatusBar** | Info bar | Bottom-aligned status text |

---

## 💡 Examples

### Responsive Layout
```python
from Menus.terminal import margin, clear
from ui_components import Panel, Button

clear()

# Use margin helper for responsive layout
row, col, width, height = margin(0.1, 0.1, 0.1, 0.1)

panel = Panel(row, col, width, height, title="Application")
panel.render()

# Centered button
button = Button(0.5, 0.4, 20, "OK")
button.render()
```

### State Management
```python
from ui_components import Button, Component

button = Button(10, 20, 20, "Submit")

# Change states
button.set_state(Component.STATE_ACTIVE)    # Highlighted
button.set_state(Component.STATE_FOCUSED)   # With cursor
button.set_state(Component.STATE_DISABLED)  # Grayed out
button.set_state(Component.STATE_IDLE)      # Normal

button.render()
```

### Form Layout
```python
from ui_components import Frame, TextField, Button, Label

frame = Frame(5, 10, 50, 15, title="Login Form")
frame.render()

label1 = Label(7, 12, 46, "Enter your credentials:")
label1.render()

username = TextField(9, 12, 46, label="Username", required=True)
username.render()

password = TextField(11, 12, 46, label="Password", required=True)
password.render()

btn_submit = Button(13, 20, 15, "Login")
btn_submit.set_state(Component.STATE_ACTIVE)
btn_submit.render()
```

---

## 🎨 Component States

All components support these states:
- `STATE_IDLE` - Normal display (default)
- `STATE_ACTIVE` - Highlighted/selected
- `STATE_FOCUSED` - Has focus, ready for input
- `STATE_DISABLED` - Grayed out, no interaction

---

## 📏 Positioning

Components accept both absolute and percentage positioning:

```python
# Absolute positioning
component = Panel(10, 20, 60, 15)  # row=10, col=20, width=60, height=15

# Percentage positioning (responsive)
component = Panel(0.2, 0.3, 0.5, 0.4)  # 20% from top, 30% from left, etc.

# Mixed
component = Panel(0.5, 20, 0.6, 10)  # Centered vertically, fixed horizontal
```

---

## ✅ Success Criteria Met

### Phase 1A: Foundation ✓
- [x] Component base class with responsive positioning
- [x] 6 container components implemented
- [x] 6 display components implemented
- [x] All handle percentages and absolute values

### Phase 1B: Interaction ✓
- [x] 8 input components with state management
- [x] 5 navigation components
- [x] State changes reflect visually
- [x] Focus and disabled states working

### Phase 1C: Specialization ✓
- [x] 5 specialized components for complex use cases
- [x] Directory tree with indentation
- [x] Checkbox list with multi-select
- [x] Status bar with bottom alignment

### Testing & Validation ✓
- [x] demo.py showcases all 31 components
- [x] Main menu example from catalog working
- [x] Responsive layout verified
- [x] Content clipping handles edge cases
- [x] All components render cleanly

---

## 🛠️ Dependencies

- Python 3.6+
- `terminal.py` module (MenuNav terminal control library)

---

## 📝 License

Part of MenuNav Standard implementation for COSC 1336-09 coursework.

---

## 🎯 Next Steps (Phase 2)

- [ ] Color/style support using ANSI codes
- [ ] Animation and transitions
- [ ] Keyboard input handling
- [ ] Event system for interactions
- [ ] Layout manager for auto-positioning
- [ ] Theme system

---

**Status**: Phase 1 Complete ✅  
**Components**: 31+ working components  
**Demo**: Interactive demo available  
**Examples**: MenuNav catalog implementations
