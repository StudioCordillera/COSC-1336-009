# Unified Catalog - Complete CLI Menu System Reference

> **Version 1.0 | Single Comprehensive Integration of MenuNav, Taxonomy, and Visual Standards | 2025-12-06**

---

## Table of Contents

1. [Quick Start Guide](#quick-start-guide)
2. [Complete Component Catalog](#complete-component-catalog)
3. [Implementation Cookbook](#implementation-cookbook)
4. [Design Patterns Library](#design-patterns-library)
5. [Navigation Index](#navigation-index)
6. [Usage Examples](#usage-examples)
7. [Reference Tables](#reference-tables)
8. [Troubleshooting Guide](#troubleshooting-guide)

---

## Quick Start Guide

### For First-Time Users

**1. I need to build a menu** → See [Menu Components](#menu-components) (p. 15)

**2. I need to display data** → See [Data View Components](#data-view-components) (p. 28)

**3. I need user input** → See [Input Components](#input-components) (p. 22)

**4. I need to show a form** → See [Form Components](#form-components) (p. 35)

**5. I need to visualize something** → See [Visual Patterns Quick Reference](#visual-patterns-quick-reference) (p. 50)

### The Three Pillars

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   STRUCTURE     │────►│ CLASSIFICATION  │────►│  VISUALIZATION  │
│   (MenuNav)     │     │   (Taxonomy)    │     │    (Visual)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
  What to build         How complex it is       How it looks
```

**MenuNav Standard** (01): Defines WHAT components exist and HOW they're structured
**Taxonomy Standard** (02): Classifies components by complexity and difficulty
**Visual Patterns** (03): Shows HOW components appear in the terminal

### 5-Second Decision Tree

```
What do I need?
│
├─ Navigation/Menu? ────► Endpoint: FORK ────► Layer 3-7 ────► Box + List pattern
│
├─ Sequential Process? ─► Endpoint: FLOW ────► Layer 5-7 ────► Form + Step pattern
│
├─ Data Display? ───────► Endpoint: STATION ──► Layer 5-6 ────► Table/Grid pattern
│
└─ Final Action? ───────► Endpoint: TERMINAL ─► Layer 5 ──────► Dialog pattern
```

---

## Complete Component Catalog

### Catalog Organization

Components are organized by:
1. **MenuNav Classification** - Endpoint type and component vocabulary
2. **Taxonomy Classification** - Layer (0-9) and difficulty (⭐-⭐⭐⭐⭐⭐)
3. **Visual Specification** - Character tier and pattern type

---

### Display Components

#### 1. Label / Text

**MenuNav**: `title`, `header`, `label`, `text`

**Taxonomy**: Layer 2 - Display - Label
- **Difficulty**: ⭐ (Trivial)
- **LOC**: 5-20
- **State vars**: 0-2
- **Complexity Score**: 5-15

**Visual Patterns**:

Tier 1 (ASCII):
```
Simple Text
HEADER TEXT
```

Tier 3 (Unicode):
```
═══════════════════════════════════════
            CENTERED HEADER
═══════════════════════════════════════
```

**Usage**: Headers, titles, static text displays

**States**: N/A (static) or {VISIBLE, HIDDEN}

**Example Code Pattern**:
```python
{title: {
    type: "label",
    text: "Main Menu",
    states: {VISIBLE}
}}
```

---

#### 2. Divider / Separator

**MenuNav**: `divider`, `separator`, `line`

**Taxonomy**: Layer 2 - Display - Divider
- **Difficulty**: ⭐ (Trivial)
- **LOC**: 1-10
- **State vars**: 0-1
- **Complexity Score**: 2-8

**Visual Patterns**:

Tier 1:
```
----------------------------------------
========================================
```

Tier 3:
```
────────────────────────────────────────
════════════════════════════════════════
```

**Usage**: Section separators, visual breaks

**States**: N/A (static)

---

#### 3. Badge / Icon / Marker

**MenuNav**: `badge`, `icon`, `marker`, `indicator`

**Taxonomy**: Layer 2 - Display - Icon/Badge
- **Difficulty**: ⭐ (Trivial)
- **LOC**: 5-15
- **State vars**: 0-2
- **Complexity Score**: 5-12

**Visual Patterns**:
```
✓ Success
✗ Error
⚠ Warning
ℹ Info
● Active
○ Inactive
[NEW]
[!]
```

**Usage**: Status indicators, visual markers

**States**: {ACTIVE, INACTIVE} or context-specific

---

### Input Components

#### 4. Button

**MenuNav**: `button`, `ok_button`, `cancel_button`, `confirm_button`, `action_button`

**Taxonomy**: Layer 2 - Input - Button
- **Difficulty**: ⭐⭐ (Easy)
- **LOC**: 10-30
- **State vars**: 2-5
- **Complexity Score**: 15-40

**Visual Patterns**:

Tier 1:
```
[OK]  [Cancel]  [Submit]  [Apply]
```

Tier 3 with states:
```
IDLE:     [Submit]
HOVER:    [>Submit<]  or  [Submit]*
PRESSED:  [SUBMIT]
DISABLED: [Submit]  (grayed)
```

**Usage**: Action triggers, form submission, navigation

**States**: {IDLE, HOVER, PRESSED, DISABLED}

**Example**:
```python
{submit_button: {
    type: "button",
    label: "Submit",
    states: {IDLE, HOVER, PRESSED, DISABLED},
    actions: {
        on_click: submit_form,
        on_hover: highlight
    }
}}
```

---

#### 5. Checkbox

**MenuNav**: `checkbox`, `toggle`, `switch`

**Taxonomy**: Layer 2 - Input - Checkbox
- **Difficulty**: ⭐⭐ (Easy)
- **LOC**: 10-25
- **State vars**: 2-4
- **Complexity Score**: 15-35

**Visual Patterns**:
```
[ ] Unchecked
[X] Checked
[*] Checked (alternative)

( ) Radio unselected
(*) Radio selected
```

**Usage**: Binary selections, options, settings

**States**: {UNCHECKED, CHECKED} or {SELECTED, UNSELECTED}

---

#### 6. TextBox / Input Field

**MenuNav**: `input_field`, `text_input`, `text_box`, `field`

**Taxonomy**: Layer 4 - Input - TextBox Editable
- **Difficulty**: ⭐⭐⭐⭐ (Hard)
- **LOC**: 150-400
- **State vars**: 10-25
- **Complexity Score**: 180-450

**Visual Patterns**:

Single-line:
```
Name: [John Doe_____________________________]
```

Multi-line:
```
Description: [First line of text                ]
             [Second line of text               ]
             [Third line with cursor|           ]
```

With validation:
```
Email: [user@example.com] ✓ Valid
Price: [abc] ✗ Invalid - must be number
```

**Usage**: Text entry, form fields, user input

**States**: {EMPTY, EDITING, VALID, INVALID, DISABLED}

**Features**: Cursor position, max length, validation, placeholder

---

#### 7. Dropdown / Select

**MenuNav**: `dropdown`, `select`, `filter_options`, `combobox`

**Taxonomy**: Layer 4 - Input - Dropdown
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 100-300
- **State vars**: 8-20
- **Complexity Score**: 120-350

**Visual Patterns**:

Collapsed:
```
Category: [Electronics      ▼]
```

Expanded:
```
Category: [Electronics      ▲]
          ┌──────────────────┐
          │ Electronics      │ ← Selected
          │ Books            │
          │ Clothing         │
          │ Food             │
          └──────────────────┘
```

**Usage**: Selection from predefined list, filtering

**States**: {COLLAPSED, EXPANDED, SELECTED, DISABLED}

---

#### 8. Slider / Range

**MenuNav**: `slider`, `range`, `progress_control`

**Taxonomy**: Layer 4 - Input - Slider
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 80-200
- **State vars**: 5-15
- **Complexity Score**: 100-280

**Visual Patterns**:
```
Volume: [----●----------] 40%
        0              100

Brightness: [████████░░░░░░░░] 50%
```

**Usage**: Numeric input, range selection, adjustable values

**States**: {IDLE, DRAGGING, DISABLED}

---

### Container Components

#### 9. Panel / Frame

**MenuNav**: `wrapper`, `panel`, `frame`, `container`

**Taxonomy**: Layer 3 - Container - Panel/Frame
- **Difficulty**: ⭐⭐ (Easy) to ⭐⭐⭐ (Moderate)
- **LOC**: 50-150
- **State vars**: 3-8
- **Complexity Score**: 50-180

**Visual Patterns**:

Simple Panel (Tier 3):
```
┌────────────────────────────┐
│  Content goes here         │
│  More content              │
└────────────────────────────┘
```

Frame with Header (Tier 4):
```
╔════════════════════════════╗
║       FRAME TITLE          ║
╠════════════════════════════╣
║  Content area              ║
║                            ║
╚════════════════════════════╝
```

**Usage**: Content grouping, visual boundaries, sections

**States**: {VISIBLE, HIDDEN, COLLAPSED, EXPANDED}

---

#### 10. Card

**MenuNav**: `card`, `panel_sectioned`

**Taxonomy**: Layer 3 - Container - Card
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 80-200
- **State vars**: 5-12
- **Complexity Score**: 90-240

**Visual Pattern**:
```
┌─────────────────────────────┐
│ HEADER                      │
├─────────────────────────────┤
│ Body content                │
│ More body content           │
├─────────────────────────────┤
│ Footer: [Actions]           │
└─────────────────────────────┘
```

**Usage**: Grouped information with sections, data cards

**States**: {VISIBLE, HIDDEN, SELECTED, HOVER}

---

#### 11. List (Simple)

**MenuNav**: `list`, `choices_wrapper`, `items_container`

**Taxonomy**: Layer 3 - Container - List Homogeneous
- **Difficulty**: ⭐⭐ (Easy)
- **LOC**: 60-180
- **State vars**: 5-15
- **Complexity Score**: 70-210

**Visual Pattern**:
```
┌─────────────────────────┐
│ • Item 1                │
│   Item 2                │
│ • Item 3                │
│   Item 4                │
└─────────────────────────┘

Or numbered:
1. First item
2. Second item
3. Third item
```

**Usage**: Simple item lists, menu choices

**States**: {VISIBLE, HIDDEN}, per-item {SELECTED, UNSELECTED}

---

### Menu Components

#### 12. Menu (Vertical)

**MenuNav**: `main_menu`, `choice_menu`, `navigation_menu`

**Taxonomy**: Layer 4 - Navigation - Menu Vertical
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 100-300
- **State vars**: 8-20
- **Complexity Score**: 120-350

**Visual Pattern**:
```
╔═══════════════════════════════════════╗
║           MAIN MENU                   ║
╚═══════════════════════════════════════╝

    ┌──────────────────────────────┐
    │ > 1. Register New Item       │
    │   2. View Collection         │
    │   3. Settings                │
    │   4. Exit                    │
    └──────────────────────────────┘

    Enter choice: [____]
```

**Usage**: Main navigation, option selection

**States**: {IDLE, ITEM_SELECTED, WAITING_ON_INPUT}

**MenuNav Type**: FORK (branching navigation)

---

#### 13. Breadcrumb Navigation

**MenuNav**: `breadcrumb`, `path_display`, `navigation_path`

**Taxonomy**: Layer 7 - Navigation - Breadcrumb
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 100-250
- **State vars**: 8-20
- **Complexity Score**: 120-320

**Visual Pattern**:
```
Home > Settings > User Profile > Edit

C:\ > Users > Documents > Projects
```

**Usage**: Show current location, hierarchical navigation

**States**: {CURRENT_PATH, PATH_UPDATED}

---

### Composite Components

#### 14. Dialog / Modal

**MenuNav**: `dialogue_wrapper`, `modal`, `popup`, `alert`

**Taxonomy**: Layer 5 - Composite - Dialog
- **Difficulty**: ⭐⭐⭐ (Moderate) to ⭐⭐⭐⭐ (Hard)
- **LOC**: 200-500
- **State vars**: 15-35
- **Complexity Score**: 250-600

**Visual Pattern**:
```
╔═══════════════════════════════════════╗
║         CONFIRM ACTION                ║
╚═══════════════════════════════════════╝

  Are you sure you want to delete this item?
  This action cannot be undone.

  Item: Gaming Laptop

  [Delete]  [Cancel]
```

**Usage**: Confirmations, alerts, forms, popups

**States**: {HIDDEN, VISIBLE, WAITING_ON_INPUT, CLOSING}

**MenuNav Type**: Often TERMINAL (final action)

---

#### 15. Form

**MenuNav**: `form`, `dialogue_wrapper` (multi-field), `registration_form`

**Taxonomy**: Layer 5 - Composite - Form
- **Difficulty**: ⭐⭐⭐⭐ (Hard)
- **LOC**: 300-700
- **State vars**: 20-50
- **Complexity Score**: 350-800

**Visual Pattern**:
```
╔═══════════════════════════════════════╗
║       REGISTER NEW ITEM               ║
╚═══════════════════════════════════════╝

  Item Name:    [_________________________]

  Category:     [Electronics      ▼]

  Description:  [_________________________]
                [_________________________]

  Quantity:     [_________________________]

  Price:        [_________________________]


  [Submit]  [Cancel]
```

**Usage**: Multi-field data entry, registration

**States**: {EMPTY, EDITING, VALIDATING, VALID, INVALID, SUBMITTING}

**MenuNav Type**: FLOW (sequential process)

---

#### 16. Notification / Alert

**MenuNav**: `notification`, `alert`, `message`, `toast`

**Taxonomy**: Layer 5 - Composite - Notification
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 150-350
- **State vars**: 8-20
- **Complexity Score**: 180-420

**Visual Patterns**:
```
┌─── ✓ SUCCESS ───────────────────────┐
│  Changes saved successfully.        │
└─────────────────────────────────────┘

┌─── ⚠ WARNING ───────────────────────┐
│  This action cannot be undone.      │
└─────────────────────────────────────┘

┌─── ✗ ERROR ─────────────────────────┐
│  An error occurred. Try again.      │
└─────────────────────────────────────┘
```

**Usage**: User feedback, status messages, errors

**States**: {HIDDEN, VISIBLE, FADING, DISMISSED}

---

#### 17. Table (Simple)

**MenuNav**: `table`, `params_list` (key-value), `simple_grid`

**Taxonomy**: Layer 5 - Composite - Table
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 200-500
- **State vars**: 12-30
- **Complexity Score**: 240-580

**Visual Pattern**:
```
┌──────┬──────────────┬────────┬─────────┐
│  ID  │     Name     │  Qty   │  Price  │
├──────┼──────────────┼────────┼─────────┤
│  001 │ Laptop       │   5    │ $1299   │
│  002 │ Mouse        │  15    │ $29     │
│  003 │ Keyboard     │   8    │ $89     │
└──────┴──────────────┴────────┴─────────┘
```

**Usage**: Structured data display, comparisons

**States**: {VISIBLE, HIDDEN, LOADING}

---

#### 18. Progress Bar

**MenuNav**: `progress_bar`, `loading_indicator`, `status_bar`

**Taxonomy**: Layer 4 - Feedback - Progress Bar
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 80-200
- **State vars**: 5-15
- **Complexity Score**: 100-270

**Visual Patterns**:
```
Loading... [████████░░░░░░░░] 50%

Upload: [████████████████░░] 80% (4.0 MB / 5.0 MB)

Processing: [▰▰▰▰▰▰▱▱▱▱] 60%
```

**Usage**: Show progress, loading states

**States**: {IDLE, ACTIVE, COMPLETE, ERROR}

---

### Data View Components

#### 19. Data Grid (Advanced)

**MenuNav**: `collection_list`, `data_grid`, `table_advanced`

**Taxonomy**: Layer 6 - View - Data Grid
- **Difficulty**: ⭐⭐⭐⭐⭐ (Very Hard)
- **LOC**: 800-2000
- **State vars**: 40-80
- **Complexity Score**: 1000-2400

**Visual Pattern**:
```
╔═══════════════════════════════════════════════════════════════╗
║               VIEW COLLECTION - Page 1 of 3                   ║
╚═══════════════════════════════════════════════════════════════╝

┌─── FILTERS ───────────────────────────────────────────────────┐
│ Category: [All ▼]  Price: [Any ▼]  [Apply] [Clear]          │
└───────────────────────────────────────────────────────────────┘

┌─────┬───────────────┬──────────┬─────┬────────┬──────┐
│ [☑] │ Name ↑        │ Category │ Qty │ Price  │ Edit │
├─────┼───────────────┼──────────┼─────┼────────┼──────┤
│ [ ] │ Laptop        │ Electron │  5  │ $1299  │ [*]  │
│ [X] │ Mouse         │ Electron │ 15  │ $29    │ [*]  │
│ [ ] │ Keyboard      │ Electron │  8  │ $89    │ [*]  │
└─────┴───────────────┴──────────┴─────┴────────┴──────┘

                [< Previous]  [Next >]  [Select Action]

Selected: 1 item
```

**Usage**: Large dataset display, sorting, filtering, pagination

**States**: {LOADING, READY, FILTERING, SORTING, ERROR}

**Features**: Row selection, column sorting, filtering, pagination, inline editing

**MenuNav Type**: STATION (data workspace)

---

#### 20. Tree View

**MenuNav**: `directory_tree`, `tree_view`, `hierarchy_view`

**Taxonomy**: Layer 6 - View - Tree N-level
- **Difficulty**: ⭐⭐⭐⭐⭐ (Very Hard)
- **LOC**: 800-2000
- **State vars**: 40-80
- **Complexity Score**: 1000-2400

**Visual Pattern**:
```
📁 Project Root
├── 📁 src
│   ├── 📄 main.py
│   ├── 📄 utils.py
│   └── 📁 components
│       ├── 📄 button.py
│       └── 📄 panel.py
├── 📁 tests
│   └── 📄 test_main.py
└── 📄 README.md

Tier 1 (ASCII):
C:\
+-- Users
    +-- Documents
        +-- Collections
            +-- Electronics
            +-- Books
```

**Usage**: File browsers, hierarchical data, folder structures

**States**: {COLLAPSED, EXPANDED, SELECTED, LOADING}

**Features**: Expand/collapse, node selection, multi-level navigation

---

#### 21. File Browser

**MenuNav**: `browser_panel`, `file_picker`, `directory_browser`

**Taxonomy**: Layer 6 - View - File Browser
- **Difficulty**: ⭐⭐⭐⭐ (Hard)
- **LOC**: 600-1500
- **State vars**: 30-60
- **Complexity Score**: 750-1800

**Visual Pattern**:
```
╔═══════════════════════════════════════════════════════════════╗
║           FILE BROWSER - CHOOSE COLLECTION                    ║
╚═══════════════════════════════════════════════════════════════╝

Current Path: C:\ > Users > Documents > Collections

┌───────────────────────────────────────────────────────────────┐
│ 📁 C:\                                                        │
│   📁 Users                                                    │
│     📁 Documents                                              │
│       📁 Collections         <-- Current Location             │
│         📁 Electronics                                        │
│         📁 Books                                              │
│         📁 Tools                                              │
└───────────────────────────────────────────────────────────────┘

Target: [___________________________]  (*) Dir  ( ) File

[↑ Up]  [Create New]  [Select]  [Cancel]
```

**Usage**: File/folder selection, navigation

**States**: {BROWSING, SELECTED, CREATING, ERROR}

**MenuNav Type**: FLOW (navigation process)

---

### Navigation Components

#### 22. Wizard / Stepper

**MenuNav**: `wizard`, `stepper`, `multi_step_form`

**Taxonomy**: Layer 7 - Navigation - Wizard
- **Difficulty**: ⭐⭐⭐⭐ (Hard)
- **LOC**: 400-1000
- **State vars**: 20-50
- **Complexity Score**: 500-1200

**Visual Pattern**:
```
╔═══════════════════════════════════════════════════════════════╗
║              SETUP WIZARD - Step 2 of 4                       ║
╚═══════════════════════════════════════════════════════════════╝

Progress: [████████░░░░░░░░] 50%

┌─ Step 1: Welcome       [✓] Complete
├─ Step 2: Configuration [●] Current ← You are here
├─ Step 3: Review        [ ] Pending
└─ Step 4: Complete      [ ] Pending

───────────────────────────────────────────────────────────────

  Configuration Options:

  [ ] Enable feature A
  [X] Enable feature B
  [ ] Enable feature C

───────────────────────────────────────────────────────────────

  [< Back]  [Next >]  [Cancel]
```

**Usage**: Multi-step processes, setup flows, tutorials

**States**: {STEP_1, STEP_2, STEP_N, COMPLETE, CANCELLED}

**MenuNav Type**: FLOW (sequential process)

---

#### 23. Router / Navigator

**MenuNav**: `router`, `navigator`, `state_manager`

**Taxonomy**: Layer 7 - Navigation - Router
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 300-800
- **State vars**: 15-40
- **Complexity Score**: 400-960

**Conceptual Visualization**:
```
Current Route: /dashboard/settings/profile

History Stack:
  / (Home)
  /dashboard
  /dashboard/settings
→ /dashboard/settings/profile ← Current

Navigation:
[Home] > [Dashboard] > [Settings] > [Profile]
```

**Usage**: State management, screen navigation, routing

**States**: {NAVIGATING, ROUTE_CHANGED, ERROR}

---

#### 24. Tab Bar / Tab Container

**MenuNav**: `tabs`, `tab_bar`, `tabbed_container`

**Taxonomy**: Layer 4 - Navigation - Tabs
- **Difficulty**: ⭐⭐⭐ (Moderate)
- **LOC**: 150-400
- **State vars**: 10-25
- **Complexity Score**: 180-480

**Visual Pattern**:
```
┌─ Tab 1 ─┬─ Tab 2 ─┬─ Tab 3 ─┐
│                              │
│  Content for Tab 1           │
│                              │
│                              │
└──────────────────────────────┘

Or:
[● General] [Settings] [Advanced]

  Content for General tab...
```

**Usage**: Multiple views, settings panels, organized content

**States**: {TAB_1_ACTIVE, TAB_2_ACTIVE, TAB_N_ACTIVE}

---

### Application-Level Components

#### 25. Dashboard

**MenuNav**: `dashboard`, `main_screen`, `control_panel`

**Taxonomy**: Layer 9 - Application - Dashboard
- **Difficulty**: ⭐⭐⭐⭐⭐ (Very Hard)
- **LOC**: 2000-8000+
- **State vars**: 150+
- **Complexity Score**: 2500+

**Visual Pattern**:
```
╔═══════════════════════════════════════════════════════════════╗
║                    SYSTEM DASHBOARD                           ║
╚═══════════════════════════════════════════════════════════════╝

┌─ SYSTEM STATUS ───┬─ ACTIVE USERS ──┬─ PERFORMANCE ─────┐
│ CPU:  [████░] 45% │ Online:  127    │ Response: 45ms    │
│ RAM:  [██████] 78%│ Active:   89    │ Uptime: 45d 3h    │
│ Disk: [███░] 34%  │ Idle:     38    │ Errors: 3         │
└───────────────────┴─────────────────┴───────────────────┘

┌─ RECENT ACTIVITY ─────────────────────────────────────────┐
│ 14:32  User 'admin' logged in                            │
│ 14:31  Backup completed                                  │
│ 14:29  New user registered                               │
└───────────────────────────────────────────────────────────┘

┌─ QUICK ACTIONS ───────────────────────────────────────────┐
│ [Restart] [Logs] [Users] [Settings]                      │
└───────────────────────────────────────────────────────────┘
```

**Usage**: Overview screens, monitoring, control centers

**States**: Complex multi-component state management

**MenuNav Type**: Combination of multiple endpoint types

---

## Implementation Cookbook

### Recipe 1: Building a Simple Menu

**Ingredients**:
- 1× menu_wrapper (Layer 3)
- 1× title (Layer 2)
- 4× choice_object (Layer 2)
- 1× input_field (Layer 4)

**Steps**:
1. Create outer frame using heavy Unicode (╔═╗)
2. Add centered title
3. Create inner box with light Unicode (┌─┐)
4. Add numbered menu items
5. Add input prompt

**Result**: Complete FORK-type menu

**Code Structure**:
```python
main_menu = {
    wrapper: frame(width=80, style="heavy"),
    title: label("MAIN MENU", align="center"),
    choices: [
        choice("1. Register New Item"),
        choice("2. View Collection"),
        choice("3. Settings"),
        choice("4. Exit")
    ],
    input: textbox("Enter choice: ", width=10)
}
```

---

### Recipe 2: Building a Data Entry Form

**Ingredients**:
- 1× dialogue_wrapper (Layer 5)
- 5× input_field (Layer 4)
- 1× dropdown (Layer 4)
- 2× button (Layer 2)

**Steps**:
1. Create dialog box with title
2. Add field labels
3. Add input fields with validation
4. Add dropdown for categories
5. Add Submit/Cancel buttons

**Result**: Complete FLOW-type form

**Validation States**:
- EMPTY → Show placeholder
- EDITING → Show cursor
- VALID → Show ✓
- INVALID → Show ✗ with error message

---

### Recipe 3: Building a Data Grid

**Ingredients**:
- 1× collection_list (Layer 6)
- 1× filter_panel (Layer 4)
- 1× table structure
- Navigation controls

**Steps**:
1. Create header with title and pagination
2. Add filter panel
3. Build table with headers
4. Add data rows with selection
5. Add navigation buttons

**Result**: Complete STATION-type data view

**Features**:
- Row selection (checkboxes)
- Column sorting (↑↓ indicators)
- Filtering (dropdown filters)
- Pagination (Previous/Next)

---

### Recipe 4: Building a Multi-Step Wizard

**Ingredients**:
- 1× wizard (Layer 7)
- N× form panels (one per step)
- 1× progress bar (Layer 4)
- Navigation buttons

**Steps**:
1. Create wizard container
2. Add progress indicator
3. Create step indicators
4. Add current step content
5. Add Back/Next/Cancel buttons

**Result**: Complete FLOW-type wizard

**State Management**:
```
Steps: [COMPLETE, COMPLETE, CURRENT, PENDING, PENDING]
Current: Step 3 of 5
Progress: 60%
```

---

## Design Patterns Library

### Pattern: Master-Detail

**Structure**:
```
┌─────────────┬──────────────────────────────┐
│  List       │  Details                     │
│             │                              │
│ > Item 1    │  Item 1 Details:             │
│   Item 2    │  Name: Widget A              │
│   Item 3    │  Price: $29.99               │
│   Item 4    │  Description: ...            │
│             │                              │
│             │  [Edit] [Delete]             │
└─────────────┴──────────────────────────────┘
```

**Components**: List (Layer 3) + Detail Panel (Layer 5)

**Usage**: Show list with detailed view of selected item

---

### Pattern: Filter + Grid

**Structure**:
```
┌─ FILTERS ──────────────────────────────────┐
│ Category: [All ▼]  Price: [Any ▼]  [Apply]│
└────────────────────────────────────────────┘
┌────────────────────────────────────────────┐
│  Filtered Results Grid                     │
│  +────+──────────+─────+──────+            │
│  | ID | Name     | Qty | Price|            │
│  +────+──────────+─────+──────+            │
└────────────────────────────────────────────┘
```

**Components**: Filter Panel (Layer 4) + Data Grid (Layer 6)

**Usage**: Filter large datasets

---

### Pattern: Wizard Flow

**Structure**:
```
Step 1: Input    →    Step 2: Review    →    Step 3: Confirm
[Form]                [Summary]               [Dialog]
```

**Components**: Multiple Forms (Layer 5) + Progress (Layer 4)

**Usage**: Multi-step processes, setup, registration

---

### Pattern: Tree + Detail

**Structure**:
```
┌─────────────┬──────────────────────────────┐
│  Tree       │  Selected Item Details       │
│  📁 Root    │                              │
│  ├─📁 Docs  │  Path: /Root/Docs/file.txt   │
│  │ └─📄 file│  Size: 1.2 MB                │
│  └─📁 Pics  │  Modified: 2025-12-06        │
└─────────────┴──────────────────────────────┘
```

**Components**: Tree View (Layer 6) + Detail Panel (Layer 5)

**Usage**: File browsers, hierarchical data exploration

---

## Navigation Index

### By Complexity (Taxonomy Layer)

**Layer 0-1**: Foundation (not user-facing)
**Layer 2**: [Label](#1-label--text), [Divider](#2-divider--separator), [Badge](#3-badge--icon--marker), [Button](#4-button), [Checkbox](#5-checkbox)
**Layer 3**: [Panel](#9-panel--frame), [Card](#10-card), [List](#11-list-simple)
**Layer 4**: [TextBox](#6-textbox--input-field), [Dropdown](#7-dropdown--select), [Slider](#8-slider--range), [Menu](#12-menu-vertical), [Progress Bar](#18-progress-bar), [Tabs](#24-tab-bar--tab-container)
**Layer 5**: [Dialog](#14-dialog--modal), [Form](#15-form), [Notification](#16-notification--alert), [Table](#17-table-simple)
**Layer 6**: [Data Grid](#19-data-grid-advanced), [Tree View](#20-tree-view), [File Browser](#21-file-browser)
**Layer 7**: [Breadcrumb](#13-breadcrumb-navigation), [Wizard](#22-wizard--stepper), [Router](#23-router--navigator)
**Layer 8**: (Advanced - not in base catalog)
**Layer 9**: [Dashboard](#25-dashboard)

### By Difficulty

**⭐ Trivial**: Label, Divider, Badge
**⭐⭐ Easy**: Button, Checkbox, Panel
**⭐⭐⭐ Moderate**: Card, List, Dropdown, Slider, Menu, Breadcrumb, Router, Notification, Table, Tabs
**⭐⭐⭐⭐ Hard**: TextBox, Dialog, Form, File Browser, Wizard
**⭐⭐⭐⭐⭐ Very Hard**: Data Grid, Tree View, Dashboard

### By MenuNav Endpoint Type

**FORK** (Branching): [Menu](#12-menu-vertical), [Tabs](#24-tab-bar--tab-container)
**FLOW** (Sequential): [Form](#15-form), [Wizard](#22-wizard--stepper), [File Browser](#21-file-browser)
**STATION** (Workspace): [Data Grid](#19-data-grid-advanced), [Tree View](#20-tree-view)
**TERMINAL** (Final Action): [Dialog](#14-dialog--modal), [Notification](#16-notification--alert)

### By Visual Tier

**Tier 1** (Pure ASCII): All components have ASCII fallback
**Tier 2** (Extended ASCII): Progress bars, special markers
**Tier 3** (Light Unicode): Recommended for most components
**Tier 4** (Heavy Unicode): Headers, emphasis, formal dialogs

---

## Usage Examples

### Example 1: Complete CMS Main Menu

**Scenario**: Content Management System entry point

**Components Used**:
- menu_wrapper (Layer 3, ⭐⭐)
- title (Layer 2, ⭐)
- choice_menu_wrapper (Layer 3, ⭐⭐)
- choice_object × 4 (Layer 2, ⭐⭐)
- input_field (Layer 4, ⭐⭐⭐⭐)

**Implementation**:
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                            CMS MAIN MENU                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

    Please select an option:

    ┌──────────────────────────────────────────────────────────────────────┐
    │  1. REGISTER NEW ITEM                                                │
    │  2. VIEW COLLECTION                                                  │
    │  3. SETTINGS                                                         │
    │  4. EXIT                                                             │
    └──────────────────────────────────────────────────────────────────────┘

    Enter your choice: [____]
```

**Endpoint Type**: FORK
**Total Complexity**: ~250 (moderate)
**States**: {WAITING_ON_INPUT, ITEM_SELECTED, NAVIGATING}

---

### Example 2: Item Registration Flow

**Step 1 - Data Entry** (FLOW 1.1):
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        REGISTER NEW ITEM                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

    Item Name:        [Gaming Laptop_____________________________________]

    Category:         [Electronics      ▼]

    Description:      [High-performance laptop with RTX graphics_________]
                      [________________________________________________]

    Quantity:         [5_______________________________________________]

    Price:            [1299.99_________________________________________]


    [Submit]  [Cancel]
```

**Step 2 - Review** (FLOW 1.2):
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        REGISTRATION SUMMARY                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─── ITEM DETAILS ──────────────────────────────────────────────────────────────┐
│                                                                               │
│   Item Name:         Gaming Laptop                                           │
│   Category:          Electronics                                             │
│   Description:       High-performance laptop with RTX graphics               │
│   Quantity:          5                                                       │
│   Price:             $1,299.99                                               │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘

    [Confirm]  [Revise]  [Cancel]
```

**Step 3 - Confirmation** (TERMINAL):
```
╔═══════════════════════════════════════════════════════════════════╗
║                    ✓ SUCCESS                                      ║
╚═══════════════════════════════════════════════════════════════════╝

  Item registered successfully!

  Item ID: #001
  Name: Gaming Laptop

  [View Collection]  [Add Another]  [Return to Menu]
```

**Endpoint Type**: FLOW → TERMINAL
**Total Complexity**: ~1200 (complex workflow)

---

### Example 3: Collection View (Data Grid)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    VIEW COLLECTION - Electronics                             ║
║                         Page 1 of 3 (Total: 127 items)                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─── FILTERS ───────────────────────────────────────────────────────────────────┐
│  Category: [Electronics ▼]  Price: [Any ▼]  Stock: [In Stock ▼]  [Apply]    │
└───────────────────────────────────────────────────────────────────────────────┘

+----------+---------------------------+------------+----------+--------+-------+
|   [☑]    |       Name ↑              |  Category  | Quantity | Price  | Edit  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Gaming Laptop             | Electronics|    5     |$1299.99|  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [X]    | Wireless Mouse            | Electronics|   15     | $29.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Mechanical Keyboard       | Electronics|    8     | $89.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | USB-C Hub                 | Electronics|   12     | $49.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Monitor 27"               | Electronics|    3     |$399.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+

                    [< Previous]  [Next >]  [Select Action ▼]

Selected: 1 item | Showing: 1-5 of 127
```

**Components**:
- Frame (Layer 3)
- Filter Panel (Layer 4)
- Data Grid (Layer 6)
- Pagination (Layer 4)
- Checkboxes (Layer 2)
- Dropdowns (Layer 4)

**Endpoint Type**: STATION
**Total Complexity**: ~1800 (very complex)

---

## Reference Tables

### Complete Component Quick Reference

| Component | Layer | Difficulty | LOC | Visual Pattern | Endpoint |
|-----------|-------|------------|-----|----------------|----------|
| Label | 2 | ⭐ | 5-20 | Text | N/A |
| Divider | 2 | ⭐ | 1-10 | `───` or `===` | N/A |
| Badge | 2 | ⭐ | 5-15 | `✓ ✗ [!]` | N/A |
| Button | 2 | ⭐⭐ | 10-30 | `[OK]` | Any |
| Checkbox | 2 | ⭐⭐ | 10-25 | `[X] [ ]` | Any |
| TextBox | 4 | ⭐⭐⭐⭐ | 150-400 | `[____]` | FLOW |
| Dropdown | 4 | ⭐⭐⭐ | 100-300 | `[Item ▼]` | Any |
| Slider | 4 | ⭐⭐⭐ | 80-200 | `[──●──]` | Any |
| Panel | 3 | ⭐⭐ | 50-150 | `┌──┐` | Any |
| Card | 3 | ⭐⭐⭐ | 80-200 | Sectioned box | Any |
| List | 3 | ⭐⭐ | 60-180 | Numbered/bulleted | Any |
| Menu | 4 | ⭐⭐⭐ | 100-300 | Choice list | FORK |
| Breadcrumb | 7 | ⭐⭐⭐ | 100-250 | `A > B > C` | FLOW |
| Dialog | 5 | ⭐⭐⭐⭐ | 200-500 | Modal box | TERMINAL |
| Form | 5 | ⭐⭐⭐⭐ | 300-700 | Multi-field | FLOW |
| Notification | 5 | ⭐⭐⭐ | 150-350 | Alert box | TERMINAL |
| Table | 5 | ⭐⭐⭐ | 200-500 | Grid | STATION |
| Progress Bar | 4 | ⭐⭐⭐ | 80-200 | `[████░░]` | Any |
| Data Grid | 6 | ⭐⭐⭐⭐⭐ | 800-2000 | Advanced table | STATION |
| Tree View | 6 | ⭐⭐⭐⭐⭐ | 800-2000 | `├──└──` | STATION |
| File Browser | 6 | ⭐⭐⭐⭐ | 600-1500 | Tree + controls | FLOW |
| Wizard | 7 | ⭐⭐⭐⭐ | 400-1000 | Steps | FLOW |
| Router | 7 | ⭐⭐⭐ | 300-800 | State mgmt | Any |
| Tabs | 4 | ⭐⭐⭐ | 150-400 | Tab bar | FORK |
| Dashboard | 9 | ⭐⭐⭐⭐⭐ | 2000+ | Full UI | Mixed |

### Visual Patterns by Character Tier

| Tier | Characters | Usage | Compatibility |
|------|-----------|--------|---------------|
| 1 | `+ - | = # < > ^ v / \` | Maximum compatibility | 100% |
| 2 | `[ ] / \ * · °` | Decorative | 95% |
| 3 | `┌ ─ │ └ ├ ┤ ┬ ┴ ┼` | Clean, modern | 90% |
| 4 | `╔ ═ ║ ╚ ╠ ╣ ╦ ╩ ╬` | Emphasis | 90% |

### State Complexity Guide

| Pattern | State Vars | Components | Visual Feedback |
|---------|-----------|------------|-----------------|
| Minimal | 0-2 | Label, Divider | None/static |
| Simple | 3-8 | Button, Checkbox, Panel | Hover, focus |
| Moderate | 10-25 | TextBox, Dropdown, Form | Multiple states |
| High | 40-80 | Data Grid, Tree View | Status indicators |
| Very High | 150+ | Dashboard, App | Full tracking |

---

## Troubleshooting Guide

### Problem: Components Don't Align

**Symptoms**: Inconsistent spacing, misaligned borders

**Diagnosis**:
1. Check character width consistency (some Unicode chars are double-width)
2. Verify all rows use same border characters
3. Check for mixing Tier 1 and Tier 3 characters

**Solution**:
- Use consistent tier throughout component
- Pad text to exact widths
- Use monospace font

---

### Problem: Visual Corruption

**Symptoms**: Broken boxes, missing characters, weird symbols

**Diagnosis**:
1. Terminal doesn't support Unicode → Use Tier 1 (ASCII)
2. Encoding issues → Check UTF-8 support
3. Font doesn't include characters → Use compatible font

**Solution**:
- Fallback to Tier 1 for maximum compatibility
- Test in target environment
- Provide tier selection option

---

### Problem: Poor Performance

**Symptoms**: Slow rendering, lag with large data

**Diagnosis**:
1. Too many components → Reduce complexity
2. No pagination → Add pagination to data views
3. Inefficient rendering → Optimize redraw logic

**Solution**:
- Use Layer 6 Data Grid for large datasets
- Implement virtual scrolling
- Only render visible items

---

### Problem: State Management Issues

**Symptoms**: States not updating, inconsistent behavior

**Diagnosis**:
1. State vars not tracked → Add proper state variables
2. Missing state transitions → Define all transitions
3. No validation → Add state validation

**Solution**:
- Review Taxonomy layer requirements for state vars
- Implement state machine pattern
- Add state change logging

---

## Version History

### Version 1.0 (2025-12-06)
- Complete unified catalog integrating all three standards
- 25 components fully documented with specifications
- Quick start guide and decision trees
- Implementation cookbook with 4 recipes
- Design patterns library with 4 patterns
- Complete navigation index (by complexity, difficulty, endpoint, tier)
- 3 comprehensive usage examples
- Reference tables (component quick reference, visual tiers, state complexity)
- Troubleshooting guide with 4 common problems

---

**END OF UNIFIED CATALOG**
