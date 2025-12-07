# Component-Visual Mapping - Comprehensive Design Catalog

> **Version 1.0 | Integration of MenuNav, Taxonomy, and Visual Patterns | 2025-12-06**

---

## Table of Contents

1. [Overview](#overview)
2. [Mapping Methodology](#mapping-methodology)
3. [MenuNav Component Mappings](#menunav-component-mappings)
4. [Taxonomy Layer Mappings](#taxonomy-layer-mappings)
5. [Complete Visual Component Library](#complete-visual-component-library)
6. [Implementation Guidelines](#implementation-guidelines)
7. [Cross-Reference Index](#cross-reference-index)

---

## Overview

### Purpose
This document maps abstract component definitions from MenuNav and Taxonomy standards to concrete visual design patterns, providing implementation-ready visual specifications for every component type.

### Three-Way Integration

```
MenuNav Standard          Taxonomy Standard         Visual Patterns
    (Structure)    ←→     (Classification)    ←→    (Appearance)
        ↓                        ↓                        ↓
   FORK/FLOW/              Layer 0-9              Character Sets
   STATION/TERMINAL        ⭐-⭐⭐⭐⭐⭐               Box Styles
   Component Trees         State Complexity        Table Formats
                                                   Tree Structures
```

### Mapping Dimensions

Each component mapping includes:
1. **MenuNav Reference**: Endpoint type, design hierarchy position
2. **Taxonomy Reference**: Layer, difficulty, LOC/state metrics
3. **Visual Specification**: Character sets, patterns, examples
4. **Usage Context**: When to use, variations, alternatives

---

## Mapping Methodology

### Classification Matrix

| MenuNav Concept | Taxonomy Layer | Visual Pattern Type |
|-----------------|----------------|---------------------|
| menu_wrapper | Layer 3 (Container) | Box (Heavy/Double) |
| title | Layer 2 (Display) | Centered Header |
| choice_object | Layer 2 (Input) | Numbered/Bulleted Item |
| dialogue_wrapper | Layer 5 (Composite) | Form Box with Fields |
| button | Layer 2 (Input) | `[Action]` or `[OK]` |
| params_list | Layer 5 (View) | Table or List |
| filter_panel | Layer 4 (Complex) | Collapsible Section |
| navigation_controls | Layer 4 (Navigation) | Button Row |
| directory_tree | Layer 6 (View) | Tree with `├── └──` |
| router | Layer 7 (Navigation) | State Machine Diagram |

### Visual Pattern Hierarchy

```
Tier 1: Pure ASCII (+ - | = #)
  └─ Maximum compatibility, Python official standard
Tier 2: Extended ASCII ([ ] / \ *)
  └─ Widely supported, decorative enhancements
Tier 3: Light Unicode (┌ ─ │ └)
  └─ Modern terminals, clean aesthetic
Tier 4: Heavy Unicode (╔ ═ ║ ╚)
  └─ Emphasis, formal documents
```

---

## MenuNav Component Mappings

### 1. Main Menu (FORK)

#### MenuNav Definition
```python
{main_menu:{
    type: FORK,
    design:{
        1: menu_wrapper:{
            1.1: title,
            1.2: choice_menu_wrapper:{
                1.2.1: prompt,
                1.2.2: choices_wrapper:{
                    1.2.2.1: choice_object
                }
            }
        }
    }
}}
```

#### Taxonomy Classification
- **menu_wrapper**: Layer 3 (Container, Panel) - ⭐⭐
- **title**: Layer 2 (Display, Label) - ⭐
- **prompt**: Layer 2 (Display, Label) - ⭐
- **choice_object**: Layer 2 (Input, Button/MenuItem) - ⭐⭐

#### Visual Specification

**Tier 3 (Recommended)**:
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

**Tier 1 (ASCII-Only)**:
```
+==============================================================================+
|                            CMS MAIN MENU                                     |
+==============================================================================+

    Please select an option:

    +----------------------------------------------------------------------+
    |  1. REGISTER NEW ITEM                                                |
    |  2. VIEW COLLECTION                                                  |
    |  3. SETTINGS                                                         |
    |  4. EXIT                                                             |
    +----------------------------------------------------------------------+

    Enter your choice: [____]
```

**Component Breakdown**:
- `menu_wrapper` → Heavy border box (╔═╗ or +=+)
- `title` → Centered text in header box
- `choice_menu_wrapper` → Light border box (┌─┐ or +--+)
- `prompt` → Plain text above choices
- `choices_wrapper` → List container
- `choice_object` → Numbered item with description

---

### 2. Item Registration Form (FLOW - Step 1.1)

#### MenuNav Definition
```python
design:{
    1.1:{
        1: dialogue_wrapper:{
            1.1: dialogue_prompt,
            1.2: input_field,
            1.3: ok_button
        }
    }
}
```

#### Taxonomy Classification
- **dialogue_wrapper**: Layer 5 (Composite, Dialog) - ⭐⭐⭐
- **dialogue_prompt**: Layer 2 (Display, Label) - ⭐
- **input_field**: Layer 4 (Input, TextBox Editable) - ⭐⭐⭐⭐
- **ok_button**: Layer 2 (Input, Button) - ⭐⭐

#### Visual Specification

**Tier 3**:
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        REGISTER NEW ITEM                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

    Item Name:        [________________________________________________]

    Category:         [________________________________________________]

    Description:      [________________________________________________]
                      [________________________________________________]

    Quantity:         [________________________________________________]

    Price:            [________________________________________________]


    [Submit]  [Cancel]
```

**Tier 1**:
```
+==============================================================================+
|                        REGISTER NEW ITEM                                     |
+==============================================================================+

    Item Name:        [________________________________________________]

    Category:         [________________________________________________]

    Description:      [________________________________________________]
                      [________________________________________________]

    Quantity:         [________________________________________________]

    Price:            [________________________________________________]


    [Submit]  [Cancel]
```

**Component Breakdown**:
- `dialogue_wrapper` → Form box with header
- `dialogue_prompt` → Field label (left-aligned)
- `input_field` → Bracket-enclosed text area `[____]`
- `ok_button` → Bracketed action text `[Submit]`

---

### 3. Parameters Summary (FLOW - Step 1.2)

#### MenuNav Definition
```python
design:{
    1.2:{
        1: summary_wrapper:{
            1.1: header,
            1.2: params_list,
            1.3: buttons_wrapper:{
                1.3.1: confirm_button,
                1.3.2: revise_button
            }
        }
    }
}
```

#### Taxonomy Classification
- **summary_wrapper**: Layer 3 (Container, Card) - ⭐⭐⭐
- **header**: Layer 2 (Display, Label) - ⭐
- **params_list**: Layer 5 (View, List Objects) - ⭐⭐⭐
- **buttons_wrapper**: Layer 3 (Container, Toolbar) - ⭐⭐
- **confirm_button**: Layer 2 (Input, Button) - ⭐⭐
- **revise_button**: Layer 2 (Input, Button) - ⭐⭐

#### Visual Specification

**Tier 3**:
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        REGISTRATION SUMMARY                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─── ITEM DETAILS ──────────────────────────────────────────────────────────────┐
│                                                                               │
│   Item Name:         Gaming Laptop                                           │
│   Category:          Electronics                                             │
│   Description:       High-performance gaming laptop with RTX graphics        │
│   Quantity:          5                                                       │
│   Price:             $1,299.99                                               │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘

    [Confirm]  [Revise]  [Cancel]
```

**Component Breakdown**:
- `summary_wrapper` → Double-line header + light content box
- `header` → Title in header section
- `params_list` → Key-value pairs, indented and aligned
- `buttons_wrapper` → Horizontal button row
- Button format → `[Action]` with spacing

---

### 4. Collection View (STATION)

#### MenuNav Definition
```python
design:{
    2.1:{
        1: menu_wrapper:{
            1.1: header,
            1.2: collection_list,
            1.3: navigation_controls
        }
    }
}
```

#### Taxonomy Classification
- **menu_wrapper**: Layer 3 (Container, Frame) - ⭐⭐
- **header**: Layer 2 (Display, Label) - ⭐
- **collection_list**: Layer 6 (View, Data Grid) - ⭐⭐⭐⭐⭐
- **navigation_controls**: Layer 4 (Navigation, Pagination) - ⭐⭐⭐

#### Visual Specification

**Tier 1**:
```
+==============================================================================+
|                          VIEW COLLECTION                                     |
|                       Electronics Inventory (Page 1 of 3)                    |
+==============================================================================+

+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    |         Item Name         |  Category  | Quantity | Price  | Edit  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Gaming Laptop             | Electronics|    5     |$1299.99|  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Wireless Mouse            | Electronics|   15     | $29.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+
|   [ ]    | Mechanical Keyboard       | Electronics|    8     | $89.99 |  [*]  |
+----------+---------------------------+------------+----------+--------+-------+

                    [< Previous]  [Next >]  [Select Action]
```

**Component Breakdown**:
- `menu_wrapper` → Full-width frame with header
- `header` → Two-line: title + pagination info
- `collection_list` → Table with `+---+` grid structure
- `navigation_controls` → Button row at bottom

---

### 5. Filter Panel (STATION - Sub-component 2.2)

#### MenuNav Definition
```python
design:{
    2.2:{
        1: filter_panel:{
            1.1: filter_options,
            1.2: apply_button,
            1.3: clear_button
        }
    }
}
```

#### Taxonomy Classification
- **filter_panel**: Layer 4 (Container, Accordion) - ⭐⭐⭐
- **filter_options**: Layer 4 (Input, Dropdown) - ⭐⭐⭐
- **apply_button**: Layer 2 (Input, Button) - ⭐⭐
- **clear_button**: Layer 2 (Input, Button) - ⭐⭐

#### Visual Specification

**Tier 3**:
```
┌─── FILTERS ───────────────────────────────────────────────────────────────────┐
│  Category: [All    ▼]  Price: [Any ▼]  Stock: [Any ▼]  [Apply] [Clear]      │
└───────────────────────────────────────────────────────────────────────────────┘
```

**Tier 1**:
```
+--- FILTERS -------------------------------------------------------------------+
|  Category: [All    v]  Price: [Any v]  Stock: [Any v]  [Apply] [Clear]      |
+-------------------------------------------------------------------------------+
```

**Component Breakdown**:
- `filter_panel` → Single-line collapsible section
- `filter_options` → Dropdowns with `▼` or `v` indicator
- Buttons → Inline after filters

---

### 6. File Browser (FLOW - Ambitious Feature)

#### MenuNav Definition
```python
design:{
    3.1:{
        1: browser_panel:{
            1.1: directory_tree,
            1.2: path_breadcrumbs,
            1.3: navigation_buttons
        }
    }
}
```

#### Taxonomy Classification
- **browser_panel**: Layer 6 (View, File Browser) - ⭐⭐⭐⭐
- **directory_tree**: Layer 6 (View, Tree N-level) - ⭐⭐⭐⭐⭐
- **path_breadcrumbs**: Layer 7 (Navigation, Breadcrumb) - ⭐⭐⭐
- **navigation_buttons**: Layer 3 (Container, Toolbar) - ⭐⭐

#### Visual Specification

**Tier 3**:
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        FILE BROWSER - CHOOSE COLLECTION                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

Current Path: C:\ > Users > Documents > Collections

┌──────────────────────────────────────────────────────────────────────────────┐
│ Directory Tree                                                               │
├──────────────────────────────────────────────────────────────────────────────┤
│  📁 C:\                                                                      │
│    📁 Users                                                                  │
│      📁 Documents                                                            │
│        📁 Collections                     <-- Current Location               │
│          📁 Electronics                                                      │
│          📁 Books                                                            │
│          📁 Tools                                                            │
│        📁 Projects                                                           │
│        📁 Archive                                                            │
└──────────────────────────────────────────────────────────────────────────────┘

Target Name:  [______________________________________________]  ( ) File  (*) Dir

[↑ Up]  [Create New]  [Select]  [Cancel]
```

**Tier 1** (Tree notation):
```
+==============================================================================+
|                        FILE BROWSER - CHOOSE COLLECTION                      |
+==============================================================================+

Current Path: C:\ > Users > Documents > Collections

+------------------------------------------------------------------------------+
| Directory Tree                                                               |
+------------------------------------------------------------------------------+
|  C:\                                                                         |
|  +-- Users                                                                   |
|      +-- Documents                                                           |
|          +-- Collections                     <-- Current Location            |
|              +-- Electronics                                                 |
|              +-- Books                                                       |
|              +-- Tools                                                       |
|          +-- Projects                                                        |
|          +-- Archive                                                         |
+------------------------------------------------------------------------------+

Target Name:  [______________________________________________]  ( ) File  (*) Dir

[^ Up]  [Create New]  [Select]  [Cancel]
```

**Component Breakdown**:
- `browser_panel` → Full-screen frame
- `directory_tree` → Tree structure with `├── └──` (Tier 3) or `+--` (Tier 1)
- `path_breadcrumbs` → `>` separated path components
- `navigation_buttons` → Action button row

---

### 7. Settings Menu (FORK)

#### MenuNav Definition
```python
design:{
    4.1:{
        1: settings_panel:{
            1.1: fields_list,
            1.2: add_field_button,
            1.3: remove_field_button,
            1.4: save_button
        }
    }
}
```

#### Taxonomy Classification
- **settings_panel**: Layer 5 (Composite, Form) - ⭐⭐⭐⭐
- **fields_list**: Layer 5 (View, List Objects) - ⭐⭐⭐
- **add_field_button**: Layer 2 (Input, Button) - ⭐⭐
- **remove_field_button**: Layer 2 (Input, Button) - ⭐⭐
- **save_button**: Layer 2 (Input, Button) - ⭐⭐

#### Visual Specification

**Tier 1**:
```
+==============================================================================+
|                        MANAGE ITEM FIELDS                                    |
+==============================================================================+
|                                                                              |
|  Current Fields:                                                             |
|                                                                              |
|  +------------------------------------------------------------------------+  |
|  |  [X] Item Name          (Text)                      [^] [v] [*] [-]   |  |
|  |  [X] Category           (Text)                      [^] [v] [*] [-]   |  |
|  |  [X] Description        (Text Area)                 [^] [v] [*] [-]   |  |
|  |  [X] Quantity           (Integer)                   [^] [v] [*] [-]   |  |
|  |  [X] Price              (Currency)                  [^] [v] [*] [-]   |  |
|  |  [ ] Date Added         (Date)                      [^] [v] [*] [-]   |  |
|  +------------------------------------------------------------------------+  |
|                                                                              |
|  [+ Add Field]  [Save Changes]  [Restore Defaults]  [Cancel]                |
+==============================================================================+
```

**Component Breakdown**:
- `settings_panel` → Form box with nested list
- `fields_list` → Table-like structure with action icons
- Action buttons → `[^]` up, `[v]` down, `[*]` edit, `[-]` remove
- Bottom buttons → Standard action row

---

## Taxonomy Layer Mappings

### Layer 0: Terminal Primitives

**Components**: Character, Symbol, Color, Coordinate, Dimension

**Visual Representation**: N/A (not directly visible, foundational)

**Usage**: Building blocks for all other components

---

### Layer 1: Styled Primitives

**Components**: Styled Character, Text Span, Border Character

**Visual Examples**:

**Bold/Emphasis**:
```
**BOLD TEXT**
```

**Border Characters**:
```
┌ ┐ └ ┘ ─ │ ├ ┤ ┬ ┴ ┼    (Light)
╔ ╗ ╚ ╝ ═ ║ ╠ ╣ ╦ ╩ ╬    (Heavy)
+ - | =                  (ASCII)
```

---

### Layer 2: Basic Interactive Elements

#### Labels
```
Simple Label
**Bold Label**
[Bracketed Label]
```

#### Buttons
```
[OK]  [Cancel]  [Submit]  [Apply]
[✓ Confirm]  [✗ Decline]
```

#### Checkboxes
```
[ ] Unchecked
[X] Checked
[*] Checked (alternative)
```

#### Radio Buttons
```
( ) Unselected
(*) Selected
```

#### Dividers
```
─────────────────────────────────────────    (Light)
═════════════════════════════════════════    (Heavy)
-----------------------------------------    (ASCII)
```

---

### Layer 3: Container Components

#### Panel (Simple)
```
┌─────────────────┐
│   Content       │
│   More content  │
└─────────────────┘
```

#### Frame (With Title)
```
╔═════════════════╗
║  FRAME TITLE    ║
╠═════════════════╣
║  Content area   ║
║                 ║
╚═════════════════╝
```

#### Card (Sectioned)
```
┌─────────────────┐
│ HEADER          │
├─────────────────┤
│ Body content    │
│                 │
├─────────────────┤
│ Footer actions  │
└─────────────────┘
```

#### List (Homogeneous)
```
┌─────────────────┐
│ > Item 1        │
│   Item 2        │
│ > Item 3        │
│   Item 4        │
└─────────────────┘
```
(> indicates selection)

---

### Layer 4: Complex Interactive Components

#### TextBox (Editable)
```
Label: [Text content here with cursor|________________]
       [Multi-line text area                          ]
       [Second line of text                           ]
```

#### Dropdown
```
Category: [Electronics      ▼]

(Expanded state):
Category: [Electronics      ▲]
          ┌─────────────────┐
          │ Electronics     │
          │ Books           │
          │ Clothing        │
          │ Food            │
          └─────────────────┘
```

#### Slider
```
Volume: [----●----------] 40%
        0              100
```

#### Progress Bar
```
Loading... [████████░░░░░░░░] 50%
```

#### Menu (Vertical)
```
┌─────────────────┐
│ > File          │
│   Edit          │
│   View          │
│   Help          │
└─────────────────┘
```

---

### Layer 5: Composite Views

#### Dialog Box
```
╔═══════════════════════════════════════╗
║           CONFIRM ACTION              ║
╚═══════════════════════════════════════╝

  Are you sure you want to delete this item?
  This action cannot be undone.

  Item: Gaming Laptop

  [Delete]  [Cancel]
```

#### Form
```
┌─────────────────────────────────────────┐
│  USER REGISTRATION                      │
├─────────────────────────────────────────┤
│  Name:     [________________________]   │
│  Email:    [________________________]   │
│  Password: [________________________]   │
│  Confirm:  [________________________]   │
│                                         │
│  [X] I agree to terms                   │
│                                         │
│  [Submit]  [Cancel]                     │
└─────────────────────────────────────────┘
```

#### Table (Simple)
```
┌──────┬──────────────┬────────┬─────────┐
│  ID  │     Name     │  Qty   │  Price  │
├──────┼──────────────┼────────┼─────────┤
│  001 │ Laptop       │   5    │ $1299   │
│  002 │ Mouse        │  15    │ $29     │
│  003 │ Keyboard     │   8    │ $89     │
└──────┴──────────────┴────────┴─────────┘
```

#### Notification
```
┌─── ✓ SUCCESS ─────────────────────────────────┐
│  Your changes have been saved successfully.   │
└───────────────────────────────────────────────┘

┌─── ⚠ WARNING ─────────────────────────────────┐
│  This action cannot be undone.                │
└───────────────────────────────────────────────┘

┌─── ✗ ERROR ───────────────────────────────────┐
│  An error occurred. Please try again.         │
└───────────────────────────────────────────────┘
```

---

### Layer 6: Advanced Data Views

#### Tree View (N-level)
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
```

#### Data Grid (with features)
```
╔═════╦═══════════════╦══════════╦═════════╦═══════╗
║  ☑  ║ Name ↑        ║ Category ║ Qty     ║ Price ║
╠═════╬═══════════════╬══════════╬═════════╬═══════╣
║ [ ] ║ Laptop        ║ Electron ║ [5___]  ║ $1299 ║
║ [X] ║ Mouse         ║ Electron ║   15    ║ $29   ║
║ [ ] ║ Keyboard      ║ Electron ║   8     ║ $89   ║
╚═════╩═══════════════╩══════════╩═════════╩═══════╝

Filter: [Category: All ▼] [Price: Any ▼]  [Apply]
Sort: Name ↑ (click to change)
Selected: 1 item
```

---

### Layer 7: Navigation & Flow Systems

#### Wizard (Multi-step)
```
╔══════════════════════════════════════════════════════════════╗
║              SETUP WIZARD - Step 2 of 4                      ║
╚══════════════════════════════════════════════════════════════╝

Progress: [████████░░░░░░░░] 50%

┌─ Step 1: Welcome       [✓]
├─ Step 2: Configuration [●] ← You are here
├─ Step 3: Review        [ ]
└─ Step 4: Complete      [ ]

─────────────────────────────────────────────────────────────────

  Configuration Options:

  [ ] Enable feature A
  [X] Enable feature B
  [ ] Enable feature C

─────────────────────────────────────────────────────────────────

  [< Back]  [Next >]  [Cancel]
```

#### Router (Navigation state)
```
Current Route: /dashboard/settings/profile

History Stack:
  /                      (Home)
  /dashboard             (Dashboard)
  /dashboard/settings    (Settings)
→ /dashboard/settings/profile  (Profile) ← Current

Available Routes:
  - /dashboard
  - /dashboard/analytics
  - /dashboard/settings
  - /dashboard/settings/profile
  - /dashboard/settings/account
```

---

### Layer 8: Graph & Spatial Navigation

#### Network Graph
```
        [Node A]
       /    |    \
      /     |     \
  [B]----[Node C]----[D]
           |
        [Node E]
```

#### 2D Navigation Map
```
╔═══════════════════════════════════════╗
║  +---+---+---+---+---+---+---+---+   ║
║  |   |   | X |   |   |   |   |   |   ║
║  +---+---+---+---+---+---+---+---+   ║
║  |   |###|###|   |   |   |   |   |   ║
║  +---+---+---+---+---+---+---+---+   ║
║  |   |###| P |   | G |   |   |   |   ║
║  +---+---+---+---+---+---+---+---+   ║
║  |   |   |   |   |   |   |   |   |   ║
║  +---+---+---+---+---+---+---+---+   ║
╚═══════════════════════════════════════╝

Legend: P = Player, G = Goal, X = Enemy, # = Wall
```

---

### Layer 9: Application-Level Widgets

#### Dashboard
```
╔══════════════════════════════════════════════════════════════════════════════╗
║                              SYSTEM DASHBOARD                                ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─── SYSTEM STATUS ─────────┬─── ACTIVE USERS ───────┬─── PERFORMANCE ────────┐
│ CPU:  [████░░] 45%        │ Online:  127           │ Response: 45ms         │
│ RAM:  [███████] 78%       │ Active:   89           │ Uptime:   45d 3h       │
│ Disk: [███░░░] 34%        │ Idle:     38           │ Errors:   3            │
└───────────────────────────┴────────────────────────┴────────────────────────┘

┌─── RECENT ACTIVITY ───────────────────────────────────────────────────────────┐
│ 14:32:15  User 'admin' logged in                                             │
│ 14:31:02  Backup completed successfully                                      │
│ 14:29:47  New user 'john_doe' registered                                     │
│ 14:28:33  System update available                                            │
└───────────────────────────────────────────────────────────────────────────────┘

┌─── QUICK ACTIONS ─────────────────────────────────────────────────────────────┐
│ [Restart Server]  [View Logs]  [Manage Users]  [System Settings]            │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

## Complete Visual Component Library

### Atomic Patterns (Building Blocks)

#### 1. Box Corners

**ASCII**:
```
+  -  |
```

**Light Unicode**:
```
┌  ┐  └  ┘  (corners)
─  │        (lines)
```

**Heavy Unicode**:
```
╔  ╗  ╚  ╝  (corners)
═  ║        (lines)
```

#### 2. Line Styles

```
Single:  ─────────────────
Double:  ═════════════════
Dashed:  - - - - - - - - -
Dotted:  . . . . . . . . .
Heavy:   ━━━━━━━━━━━━━━━━━
Wave:    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
```

#### 3. Bullets & Markers

```
• Filled circle
○ Empty circle
■ Filled square
□ Empty square
▪ Small filled square
▫ Small empty square
► Right triangle
▶ Right arrow
→ Right arrow (line)
✓ Check mark
✗ X mark
* Asterisk
- Dash
+ Plus
```

---

### Composite Patterns (Assemblies)

#### Pattern: Simple Box
```
┌────────────────┐
│    Content     │
└────────────────┘
```
**Usage**: Panel, Frame, Card
**Tier**: 3 (Light Unicode)

---

#### Pattern: Header Box
```
╔════════════════╗
║  HEADER TITLE  ║
╠════════════════╣
║  Content area  ║
╚════════════════╝
```
**Usage**: Frame, Dialog, Window
**Tier**: 4 (Heavy Unicode)

---

#### Pattern: Nested Box
```
┌──────────────────────┐
│  ┌────────────────┐  │
│  │  Inner content │  │
│  └────────────────┘  │
└──────────────────────┘
```
**Usage**: Modal, Nested containers
**Tier**: 3

---

#### Pattern: Table Grid
```
┌─────┬─────┬─────┐
│  A  │  B  │  C  │
├─────┼─────┼─────┤
│  1  │  2  │  3  │
└─────┴─────┴─────┘
```
**Usage**: Table, Data Grid
**Tier**: 3

---

#### Pattern: Tree Branch
```
root
├── child_1
│   ├── grandchild_1
│   └── grandchild_2
└── child_2
```
**Usage**: Tree View, File Browser
**Tier**: 3

---

#### Pattern: Flow Diagram
```
    [START]
       ↓
   ┌───┴───┐
   │       │
  [A]     [B]
   │       │
   └───┬───┘
       ↓
     [END]
```
**Usage**: Wizard, Router, Flow
**Tier**: 3 + 2 (arrows)

---

#### Pattern: Form Layout
```
┌─────────────────────────┐
│ Label: [______________] │
│ Label: [______________] │
│ Label: [______________] │
│                         │
│ [Submit]  [Cancel]      │
└─────────────────────────┘
```
**Usage**: Form, Dialog, Input
**Tier**: 3

---

#### Pattern: Tabs
```
┌─Tab 1─┬─Tab 2─┬─Tab 3─┐
│                        │
│  Content for Tab 1     │
│                        │
└────────────────────────┘
```
**Usage**: Tab Bar, Multi-view
**Tier**: 3

---

#### Pattern: Progress Bar
```
Progress: [████████░░░░░░] 50%
```
**Usage**: Loading, Upload, Progress
**Tier**: 2 (blocks)

---

#### Pattern: Menu Items
```
┌──────────────────┐
│ > Selected Item  │
│   Regular Item   │
│   Regular Item   │
│ ──────────────   │ (separator)
│   Regular Item   │
└──────────────────┘
```
**Usage**: Menu, List, Selection
**Tier**: 3

---

## Implementation Guidelines

### Choosing Visual Tier

#### Use Tier 1 (Pure ASCII) When:
- Maximum compatibility required
- Python standard library context
- Documentation for code comments
- Environments without Unicode support

#### Use Tier 2 (Extended ASCII) When:
- Decorative enhancements desired
- Broader compatibility still needed
- Terminal supports extended characters

#### Use Tier 3 (Light Unicode) When:
- Modern terminal environment
- Clean, professional aesthetic priority
- UTF-8 support confirmed

#### Use Tier 4 (Heavy Unicode) When:
- Emphasis required (headers, warnings)
- Formal documentation
- Visual hierarchy needs strong borders

---

### Component Selection Matrix

| Need | MenuNav Component | Taxonomy Layer | Visual Pattern | Tier |
|------|-------------------|----------------|----------------|------|
| Menu choices | choice_wrapper | Layer 3 | Numbered list in box | 3 |
| Form input | input_field | Layer 4 | Bracketed text area | 1-3 |
| Data display | collection_list | Layer 6 | Table grid | 1-3 |
| File navigation | directory_tree | Layer 6 | Tree structure | 3 |
| Multi-step process | wizard (implied) | Layer 7 | Progress + steps | 3 |
| Action button | button | Layer 2 | `[Action]` format | 1 |
| Container | wrapper/panel | Layer 3 | Box with border | 1-4 |
| Header | title/header | Layer 2 | Centered text | 1-4 |
| Separator | divider | Layer 2 | Line (─ or =) | 1-4 |
| Status | notification | Layer 5 | Alert box with icon | 3 |

---

### Responsive Design Patterns

#### Narrow Width (< 40 chars)
```
╔══════════════════════════════╗
║        SHORT MENU            ║
╚══════════════════════════════╝

1. Option A
2. Option B
3. Option C

Choice: [__]
```

#### Medium Width (40-80 chars)
```
╔══════════════════════════════════════════════════════════════════╗
║                          STANDARD MENU                           ║
╚══════════════════════════════════════════════════════════════════╝

    1. Option A          - Description of option A
    2. Option B          - Description of option B
    3. Option C          - Description of option C

    Enter your choice: [____]
```

#### Wide Width (> 80 chars)
```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                              EXTENDED MENU                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

    ┌────────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┐
    │  1. Option A           │  2. Option B           │  3. Option C           │  4. Option D           │
    │     Description A      │     Description B      │     Description C      │     Description D      │
    └────────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┘

    Enter your choice: [____]
```

---

### Animation States (Conceptual)

#### Loading Spinner
```
Frame 1: [|]
Frame 2: [/]
Frame 3: [-]
Frame 4: [\]
(repeat)
```

#### Progress Fill
```
State 1: [░░░░░░░░░░] 0%
State 2: [███░░░░░░░] 25%
State 3: [██████░░░░] 50%
State 4: [█████████░] 75%
State 5: [██████████] 100%
```

---

## Cross-Reference Index

### By MenuNav Component

| Component | Taxonomy | Visual | Section |
|-----------|----------|--------|---------|
| menu_wrapper | Layer 3, Panel | Heavy border box | MenuNav §1, §7 |
| title | Layer 2, Label | Centered header | MenuNav §1 |
| choice_object | Layer 2, Button | Numbered item | MenuNav §1 |
| dialogue_wrapper | Layer 5, Dialog | Form box | MenuNav §2 |
| input_field | Layer 4, TextBox | `[____]` | MenuNav §2 |
| summary_wrapper | Layer 3, Card | Multi-section box | MenuNav §3 |
| params_list | Layer 5, List | Key-value pairs | MenuNav §3 |
| collection_list | Layer 6, Data Grid | Table grid | MenuNav §4 |
| filter_panel | Layer 4, Accordion | Collapsible section | MenuNav §5 |
| directory_tree | Layer 6, Tree View | Tree structure | MenuNav §6 |
| settings_panel | Layer 5, Form | Settings form | MenuNav §7 |
| browser_panel | Layer 6, File Browser | Full file UI | MenuNav §6 |

### By Taxonomy Layer

| Layer | Components | Visual Examples | Section |
|-------|------------|-----------------|---------|
| 0 | Primitives | N/A | Taxonomy §0 |
| 1 | Styled Primitives | Border chars | Taxonomy §1 |
| 2 | Basic Interactive | Labels, Buttons, Dividers | Taxonomy §2 |
| 3 | Containers | Panels, Frames, Cards | Taxonomy §3 |
| 4 | Complex Interactive | TextBox, Dropdown, Slider | Taxonomy §4 |
| 5 | Composite Views | Dialogs, Forms, Tables | Taxonomy §5 |
| 6 | Advanced Data | Tree View, Data Grid, File Browser | Taxonomy §6 |
| 7 | Navigation | Wizard, Router | Taxonomy §7 |
| 8 | Graph/Spatial | Network Graph, 2D Map | Taxonomy §8 |
| 9 | Application | Dashboard | Taxonomy §9 |

### By Visual Pattern Type

| Pattern Type | Example | MenuNav | Taxonomy | Tier |
|--------------|---------|---------|----------|------|
| Box (simple) | `┌─┐` | Panel | Layer 3 | 3 |
| Box (heavy) | `╔═╗` | Frame | Layer 3 | 4 |
| Table | `├─┼─┤` | collection_list | Layer 5-6 | 3 |
| Tree | `├── └──` | directory_tree | Layer 6 | 3 |
| Flow | `[A]→[B]` | FLOW notation | Layer 7 | 2-3 |
| Form | `[___]` | input_field | Layer 4-5 | 1 |
| Menu | Numbered list | choice_object | Layer 2-3 | 1-3 |
| Button | `[Action]` | button | Layer 2 | 1 |
| Progress | `[███░░]` | N/A | Layer 4 | 2 |
| Tabs | `┬─Tab─┬` | N/A | Layer 4 | 3 |

---

## Version History

### Version 1.0 (2025-12-06)
- Initial comprehensive mapping
- MenuNav components mapped to visual patterns
- Taxonomy layers mapped to visual examples
- Complete visual component library
- Implementation guidelines
- Cross-reference index

---

**END OF COMPONENT-VISUAL MAPPING**
