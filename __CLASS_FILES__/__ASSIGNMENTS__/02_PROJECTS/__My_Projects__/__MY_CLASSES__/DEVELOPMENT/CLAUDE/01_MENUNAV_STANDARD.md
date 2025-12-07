# MenuNav Standard - Formal CLI Navigation Architecture Specification

> **Version 1.0 | Extracted from menuNav.py | 2025-12-06**

---

## Table of Contents

1. [Overview](#overview)
2. [Core Concepts](#core-concepts)
3. [Endpoint Classification](#endpoint-classification)
4. [Component Definition Structure](#component-definition-structure)
5. [State Management](#state-management)
6. [Design Hierarchy](#design-hierarchy)
7. [Navigation Patterns](#navigation-patterns)
8. [Naming Conventions](#naming-conventions)
9. [Documentation Standards](#documentation-standards)
10. [Complete Component Catalog](#complete-component-catalog)
11. [**PHASE 1: Minimal UI Component Implementation**](#phase-1-minimal-ui-component-implementation)

---

## Overview

### Purpose
The MenuNav Standard defines a comprehensive architecture for CLI-based menu navigation systems. It provides:
- Formal endpoint type classification
- Standardized component hierarchy 
- State machine definitions for all interactions
- Design patterns for consistent UI structure

### Scope
This standard applies to:
- Menu-driven CLI applications
- Interactive terminal interfaces
- Multi-step workflow systems
- Form-based data entry interfaces
- File/collection browsers

### Design Philosophy
- **Explicit over Implicit**: All states, components, and flows must be explicitly defined
- **Hierarchical Composition**: Components nest predictably with clear parent-child relationships
- **Declarative Structure**: Use declarative syntax to define component trees
- **State-Driven Behavior**: Every interaction point has enumerated states

---

## Core Concepts

### The Three Pillars

Every navigation endpoint must define three mandatory aspects:

```
1. ENDPOINT TYPE (Classification)
2. STATES (State Machine)
3. DESIGN (Component Hierarchy)
```

Optional but recommended:
```
4. FLOW/FORK (Navigation Structure)
5. DEPENDENCIES (Component Requirements)
```

### Declarative Syntax Pattern

```python
{component_name: {
    type: ENDPOINT_TYPE,
    fork: {                    # or flow: {...}
        choice_id: target_component
    },
    states: {
        state_id: STATE_NAME,
        nested: {
            sub_state_id: SUB_STATE_NAME
        }
    },
    design: {
        numeric_id: component_type: {
            nested_id: nested_component
        }
    }
}}
```

---

## Endpoint Classification

### FORK
**Definition**: Branch point requiring user choice selection  
**Behavior**: Presents multiple options, waits for input, routes to target endpoint  
**Characteristics**:
- Multiple exit paths (2+)
- User-driven navigation
- No predetermined sequence
- Can return to same fork after completion

**Visual Pattern**:
```
         |
    +----+----+
    |         |
 [Opt A]   [Opt B]
```

**Examples**:
- Main menu
- Settings submenu
- Collections menu

---

### FLOW
**Definition**: Sequential process with defined step progression  
**Behavior**: Guides user through ordered steps, enforces sequence  
**Characteristics**:
- Linear progression
- Step validation gates
- Forward/backward navigation
- Completion endpoint

**Visual Pattern**:
```
start >----[Step 1]--->[Step 2]--->[Step 3]----> end
```

**Examples**:
- Registration wizard
- Multi-step form
- File browser workflow

---

### STATION
**Definition**: Terminal endpoint for data viewing/interaction  
**Behavior**: Presents information, allows limited actions, returns to origin  
**Characteristics**:
- No sub-navigation
- Display-focused
- Action-oriented interactions
- Single exit path (return)

**Visual Pattern**:
```
---------> [View/Edit] ---------> return
```

**Examples**:
- Collection viewer
- Data table display
- Detail page

---

### TERMINAL
**Definition**: Application exit point  
**Behavior**: Confirms exit, performs cleanup, terminates session  
**Characteristics**:
- No navigation options
- Optional confirmation
- Cleanup operations
- Process termination

**Visual Pattern**:
```
---------> [Exit] --> END
```

---

## Component Definition Structure

### Mandatory Sections

#### 1. TYPE Declaration
```python
TYPE: FORK | FLOW | STATION | TERMINAL
```

#### 2. Navigation Structure
For FORK:
```python
fork: {
    numeric_id: target_component_name
}
```

For FLOW:
```python
flow: {
    step_id: step_action_name,
    substep_id: {
        nested_step_id: nested_action
    }
}
```

#### 3. STATES Definition
```python
states: {
    state_id: STATE_NAME,
    nested_component_id: {
        sub_state_id: SUB_STATE_NAME
    }
}
```

#### 4. DESIGN Hierarchy
```python
design: {
    component_id: component_type: {
        child_id: child_component_type
    }
}
```

### Complete Template

```python
{component_name: {
    # Classification
    type: ENDPOINT_TYPE,
    
    # Navigation (choose one)
    fork: {
        1: target_a,
        2: target_b
    },
    # OR
    flow: {
        1: step_one,
        2: step_two
    },
    
    # State Machine
    states: {
        1: STATE_ONE,
        2: STATE_TWO,
        nested_component: {
            1: NESTED_STATE_ONE
        }
    },
    
    # Component Tree
    design: {
        1: root_component: {
            1.1: child_component,
            1.2: sibling_component: {
                1.2.1: grandchild_component
            }
        }
    }
}}
```

---

## State Management

### State Naming Convention

**Format**: `VERB_NOUN` or `ADJECTIVE_NOUN` in SCREAMING_SNAKE_CASE

**Examples**:
- `WAITING_ON_INPUT`
- `DISPLAYING`
- `VALIDATING`
- `SELECTION_ACTIVE`
- `ITEMS_SELECTED`

### Standard State Categories

#### Display States
```
DISPLAY
DISPLAYING
HIDDEN
VISIBLE
RENDERED
```

#### Input States
```
WAITING_ON_INPUT
RECEIVING_INPUT
INPUT_RECEIVED
AWAITING_CONFIRMATION
```

#### Processing States
```
VALIDATING
PROCESSING
APPLYING_CHANGES
SAVING
LOADING
```

#### Selection States
```
NO_SELECTION
ITEM_SELECTED
ITEMS_SELECTED
SELECTION_CONFIRMED
```

#### Navigation States
```
NAVIGATING
BROWSING
ROUTE_CHANGING
```

#### Lifecycle States
```
INITIALIZING
READY
ACTIVE
PAUSED
COMPLETED
TERMINATED
```

### State Machine Patterns

#### Simple Linear
```python
states: {
    1: DISPLAY,
    2: WAITING_ON_INPUT,
    3: PROCESSING,
    4: COMPLETED
}
```

#### Branching
```python
states: {
    1: DISPLAY,
    2: WAITING_ON_ACTION,
    3: CONFIRMED,      # Branch A
    4: CANCELLED       # Branch B
}
```

#### Nested Component States
```python
states: {
    1: PARENT_STATE,
    child_component: {
        1: CHILD_STATE_ONE,
        2: CHILD_STATE_TWO
    }
}
```

---

## Design Hierarchy

### Component Tree Structure

Uses **decimal notation** for hierarchical relationships:

```
1           Root level
1.1         Child of 1
1.2         Sibling of 1.1
1.2.1       Child of 1.2
1.2.2       Sibling of 1.2.1
1.2.2.1     Child of 1.2.2
```

### Nesting Rules

1. **Decimal IDs**: Each level adds a decimal point
2. **Sequential Numbering**: Siblings increment final number
3. **Parent Reference**: Remove last decimal segment to find parent
4. **Depth Limit**: Recommend max 4 levels deep (1.2.3.4)

### Component Type Vocabulary

#### Container Types
```
wrapper         - Generic container
panel           - Bordered container
frame           - Titled container
section         - Logical grouping
group           - Related items
```

#### Display Types
```
header          - Title/heading
title           - Primary label
label           - Text display
text            - Body content
message         - User notification
badge           - Status indicator
```

#### Input Types
```
input_field     - Text entry
text_field      - Single-line input
text_area       - Multi-line input
button          - Action trigger
checkbox        - Boolean toggle
radio_button    - Single selection
dropdown        - List selection
slider          - Range selection
toggle          - Binary switch
```

#### Layout Types
```
list            - Vertical collection
grid            - 2D matrix
stack           - Linear arrangement
row             - Horizontal layout
column          - Vertical layout
```

#### Navigation Types
```
menu            - Choice list
breadcrumb      - Path display
pagination      - Page control
tabs            - View switcher
```

### Example Hierarchies

#### Simple Form
```python
design: {
    1: form_wrapper: {
        1.1: header,
        1.2: fields_section: {
            1.2.1: name_field,
            1.2.2: email_field
        },
        1.3: buttons_wrapper: {
            1.3.1: submit_button,
            1.3.2: cancel_button
        }
    }
}
```

#### Complex Menu
```python
design: {
    1: menu_wrapper: {
        1.1: title,
        1.2: choice_menu_wrapper: {
            1.2.1: prompt,
            1.2.2: choices_wrapper: {
                1.2.2.1: choice_object,
                1.2.2.2: choice_object,
                1.2.2.3: choice_object
            }
        },
        1.3: status_bar
    }
}
```

---

## Navigation Patterns

### Pattern 1: Fork Menu
**Use**: Multiple unordered choices

```python
{menu_name: {
    type: FORK,
    fork: {
        1: target_a,
        2: target_b,
        3: target_c
    },
    states: {
        1: DISPLAY,
        2: WAITING_ON_INPUT,
        3: CHOICE_SELECTED
    },
    design: {
        1: menu_wrapper: {
            1.1: title,
            1.2: choices_list,
            1.3: input_prompt
        }
    }
}}
```

### Pattern 2: Linear Flow
**Use**: Sequential multi-step process

```python
{flow_name: {
    type: FLOW,
    flow: {
        1: step_one,
        2: step_two,
        3: step_three
    },
    states: {
        1: {
            1: STEP_ACTIVE,
            2: STEP_COMPLETED
        },
        2: {
            1: STEP_ACTIVE,
            2: STEP_COMPLETED
        }
    },
    design: {
        1: flow_wrapper: {
            1.1: progress_indicator,
            1.2: step_content,
            1.3: navigation_buttons
        }
    }
}}
```

### Pattern 3: Station with Actions
**Use**: Display + limited interactions

```python
{station_name: {
    type: STATION,
    states: {
        1: DISPLAYING,
        2: ACTION_SELECTED,
        3: ACTION_IN_PROGRESS
    },
    design: {
        1: station_wrapper: {
            1.1: header,
            1.2: content_display,
            1.3: action_bar
        }
    }
}}
```

### Pattern 4: Nested Fork
**Use**: Sub-menus within menu item

```python
{parent_menu: {
    type: FORK,
    fork: {
        1: simple_action,
        2: nested_menu: {
            2.1: sub_action_a,
            2.2: sub_action_b
        }
    },
    states: {
        1: PARENT_LEVEL,
        nested_menu: {
            1: SUB_LEVEL
        }
    }
}}
```

---

## Naming Conventions

### Component Names
**Format**: `snake_case`  
**Pattern**: `{purpose}_{type}`

**Examples**:
```python
menu_wrapper
choice_menu_wrapper
dialogue_wrapper
input_field
submit_button
params_list
navigation_controls
```

### Action/Function Names
**Format**: `snake_case`  
**Pattern**: `{verb}_{object}`

**Examples**:
```python
get_setup_params
display_params_summary
return_main_menu
validate_input
apply_filters
```

### State Names
**Format**: `SCREAMING_SNAKE_CASE`  
**Pattern**: `{VERB}_{OBJECT}` or `{STATUS}`

**Examples**:
```python
WAITING_ON_INPUT
DISPLAY_SUMMARY
ITEMS_SELECTED
APPLYING_CHANGES
CONFIRMED
CANCELLED
```

### Navigation Target Names
**Format**: `snake_case`  
**Pattern**: `{entity}_{action}`

**Examples**:
```python
item_registration
view_collection
batch_modify
archive_delete
change_item_fields
```

---

## Documentation Standards

### Section Headers

Use double-line separators for major sections:
```
═══════════════════════════════════════════════════════════════════════════════
                              SECTION TITLE
═══════════════════════════════════════════════════════════════════════════════
```

Use single-line separators for subsections:
```
───────────────────────────────────────────────────────────────────────────────
```

### Component Documentation Template

```python
"""
═══════════════════════════════════════════════════════════════════════════════
                            [COMPONENT NAME]
═══════════════════════════════════════════════════════════════════════════════

TYPE: [FORK | FLOW | STATION | TERMINAL]

DESCRIPTION:
    [Brief description of component purpose and behavior]

NAVIGATION:
    [List of navigation targets or flow steps]

SUBSTEPS (if applicable):
    [Detailed breakdown of complex operations]

{component_definition}
"""
```

### Visual Flow Notation

#### Fork Notation
```
         |
    +----+----+
    |         |
 [Opt A]   [Opt B]
```

#### Flow Notation
```
start >----[Step 1]--->[Step 2]----> end
```

#### Tree Notation
```
Root
├─ Child A
│  └─ Grandchild
└─ Child B
```

#### Substep Notation
```
1.1  STEP NAME
     └─ Substep description
     ├─ 1.1.1  SUB-OPTION A
     └─ 1.1.2  SUB-OPTION B
```

---

## Complete Component Catalog

### 1. Main Menu (FORK)

```python
{main_menu:{
    type: FORK,
    fork:{
        1: item_registration,
        2: view_collection, 
        3: settings,
        4: exit_app
    },
    states:{
        1: DISPLAY,
        2: WAITING_ON_INPUT,
        3: SELECTION_LOOP,
        4: CHOICE_SELECTED,
        5: CHOICE_CONFIRMED
    },
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

**Component Breakdown**:
- `menu_wrapper`: Root container
  - `title`: Display component for menu heading
  - `choice_menu_wrapper`: Container for interactive menu section
    - `prompt`: Instructional text
    - `choices_wrapper`: Container for selectable options
      - `choice_object`: Individual menu item (repeated)

---

### 2. Item Registration (FLOW)

```python
{item_registration:{
    type: FLOW,
    flow:{
        1.1: get_setup_params,
        1.2: display_params_summary,
        1.3: return_main_menu
    },
    states:{
        1.1:{
            1: DISPLAY,
            2: WAITING_ON_INPUT,
            3: RECEIVED_INPUT,
            4: CONFIRMATION_DIALOGUE
        },
        1.2:{
            1: DISPLAY_SUMMARY,
            2: WAITING_ON_USER_ACTION,
            3: CONFIRMED,
            4: REVISION_REQUESTED
        }
    },
    design:{
        1.1:{
            1: dialogue_wrapper:{
                1.1: dialogue_prompt,
                1.2: input_field,
                1.3: ok_button
            }
        },
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
}}
```

**Flow Steps**:
1. **get_setup_params**: Input collection dialogue
2. **display_params_summary**: Review screen with edit option
3. **return_main_menu**: Navigate back to origin

---

### 3. View Collection (STATION)

```python
{view_collection:{
    type: STATION,
    pagination: true,
    fork:{
        2.1: collections_menu,
        2.2: filters,
        2.3: archived_toggle,
        2.4: select_items:{
            2.4.1: batch_modify,
            2.4.2: copy,
            2.4.3: move,
            2.4.4: archive_delete
        },
        2.5: return_main_menu
    },
    states:{
        2.1:{
            1: DISPLAY,
            2: WAITING_ON_SELECTION,
            3: COLLECTION_SELECTED
        },
        2.2:{
            1: FILTERS_INACTIVE,
            2: FILTERS_ACTIVE,
            3: APPLYING_FILTERS
        },
        2.3:{
            1: ARCHIVED_HIDDEN,
            2: ARCHIVED_VISIBLE
        },
        2.4:{
            1: NO_SELECTION,
            2: ITEMS_SELECTED,
            3: ACTION_IN_PROGRESS,
            4: ACTION_COMPLETED,
            2.4.1:{
                1: EDITING,
                2: VALIDATING,
                3: APPLYING_CHANGES
            },
            2.4.2:{
                1: SELECTING_DESTINATION,
                2: COPYING,
                3: COPY_COMPLETE
            },
            2.4.3:{
                1: SELECTING_DESTINATION,
                2: MOVING,
                3: MOVE_COMPLETE
            },
            2.4.4:{
                1: CONFIRMING_ACTION,
                2: ARCHIVING,
                3: DELETING,
                4: ACTION_COMPLETE
            }
        }
    },
    design:{
        2.1:{
            1: menu_wrapper:{
                1.1: header,
                1.2: collection_list,
                1.3: navigation_controls
            }
        },
        2.2:{
            1: filter_panel:{
                1.1: filter_options,
                1.2: apply_button,
                1.3: clear_button
            }
        },
        2.3:{
            1: toggle_control:{
                1.1: label,
                1.2: switch
            }
        },
        2.4:{
            1: selection_panel:{
                1.1: item_list_checkboxes,
                1.2: action_buttons,
                1.3: cancel_button
            },
            2.4.1:{
                1: modify_dialogue:{
                    1.1: selected_items_display,
                    1.2: param_fields,
                    1.3: apply_button
                }
            },
            2.4.2:{
                1: copy_dialogue:{
                    1.1: source_items,
                    1.2: destination_selector,
                    1.3: copy_button
                }
            },
            2.4.3:{
                1: move_dialogue:{
                    1.1: source_items,
                    1.2: destination_selector,
                    1.3: move_button
                }
            },
            2.4.4:{
                1: confirmation_dialogue:{
                    1.1: warning_message,
                    1.2: selected_items_list,
                    1.3: archive_button,
                    1.4: delete_button,
                    1.5: cancel_button
                }
            }
        }
    }
}}
```

**Special Features**:
- **Pagination**: Iterable pages by count
- **Nested Fork**: Item selection triggers sub-menu
- **Complex States**: Multi-level state hierarchies for sub-actions

---

### 4. File Browser (FLOW) [Ambitious]

```python
{choose_collection:{
    type: FLOW,
    flow:{
        3.1: navigate_directory,
        3.2: input_target_name,
        3.3: save_location:{
            3.3.1: change_directory,
            3.3.2: provide_input
        }
    },
    states:{
        3.1:{
            1: BROWSING,
            2: DIRECTORY_SELECTED,
            3: NAVIGATING
        },
        3.2:{
            1: AWAITING_INPUT,
            2: VALIDATING_NAME,
            3: NAME_ACCEPTED
        },
        3.3:{
            1: CONFIGURING_SAVE,
            2: CHANGING_DIRECTORY,
            3: SAVING,
            4: SAVE_COMPLETE
        }
    },
    design:{
        3.1:{
            1: browser_panel:{
                1.1: directory_tree,
                1.2: path_breadcrumbs,
                1.3: navigation_buttons
            }
        },
        3.2:{
            1: input_dialogue:{
                1.1: prompt,
                1.2: text_field,
                1.3: file_directory_toggle,
                1.4: ok_button
            }
        },
        3.3:{
            1: save_dialogue:{
                1.1: current_path_display,
                1.2: name_field,
                1.3: change_dir_button,
                1.4: save_button
            }
        }
    }
}}
```

**Complexity Notes**:
- **Nested Flow**: Step 3.3 contains sub-steps
- **Tree Navigation**: Hierarchical filesystem traversal
- **Dynamic Content**: Directory listing changes with navigation

---

### 5. Settings (FORK)

```python
{settings:{
    type: FORK,
    fork:{
        4.1: change_item_fields,
        4.2: rotate_color_scheme,
        4.3: change_titles
    },
    states:{
        4.1:{
            1: VIEWING_FIELDS,
            2: EDITING_FIELDS,
            3: SAVING_CHANGES
        },
        4.2:{
            1: PREVIEWING,
            2: APPLYING_SCHEME
        },
        4.3:{
            1: EDITING_TITLES,
            2: PREVIEWING_CHANGES,
            3: SAVING_TITLES
        }
    },
    design:{
        4.1:{
            1: settings_panel:{
                1.1: fields_list,
                1.2: add_field_button,
                1.3: remove_field_button,
                1.4: save_button
            }
        },
        4.2:{
            1: color_picker_panel:{
                1.1: scheme_preview,
                1.2: scheme_options,
                1.3: apply_button
            }
        },
        4.3:{
            1: titles_panel:{
                1.1: title_fields,
                1.2: preview,
                1.3: save_button
            }
        }
    }
}}
```

**Pattern**: Configuration fork with isolated setting categories

---

## Component Vocabulary Index

### Containers
- `wrapper` - Generic container
- `panel` - Specialized container with border
- `frame` - Titled container
- `section` - Logical grouping
- `dialogue` - Modal interaction container
- `menu` - Navigation container

### Display Elements
- `header` - Section heading
- `title` - Primary label
- `label` - Text display
- `prompt` - User instruction
- `message` - Notification text
- `list` - Ordered collection display
- `tree` - Hierarchical display
- `preview` - Visual preview area

### Input Elements
- `input_field` - Generic input
- `text_field` - Single-line text
- `text_area` - Multi-line text
- `button` - Action trigger
- `checkbox` - Boolean toggle
- `toggle` - Binary switch
- `dropdown` - List selector
- `selector` - Choice picker

### Navigation Elements
- `breadcrumb` - Path display
- `navigation_controls` - Movement buttons
- `navigation_buttons` - Action set
- `pagination` - Page control
- `tabs` - View switcher

### Action Elements
- `button` - Generic action
- `submit_button` - Form submission
- `cancel_button` - Action abort
- `apply_button` - Change application
- `save_button` - Data persistence
- `ok_button` - Confirmation
- `confirm_button` - Explicit confirmation
- `revise_button` - Edit trigger
- `archive_button` - Archive action
- `delete_button` - Remove action

---

## Implementation Guidelines

### Component Creation Checklist

When defining a new component:

1. ✅ Declare endpoint TYPE
2. ✅ Define navigation structure (fork/flow)
3. ✅ Enumerate ALL possible states
4. ✅ Build complete design hierarchy
5. ✅ Use consistent naming conventions
6. ✅ Document with visual flow diagrams
7. ✅ Include substep details for complex flows
8. ✅ Cross-reference related components

### State Machine Design

1. Start with lifecycle states (INIT, ACTIVE, COMPLETE)
2. Add input states (WAITING, RECEIVING, RECEIVED)
3. Include processing states (VALIDATING, APPLYING)
4. Define outcome states (SUCCESS, ERROR, CANCELLED)
5. Nest child component states under parent

### Hierarchy Design

1. Start with root container
2. Add major sections (header, body, footer)
3. Decompose sections into functional groups
4. Add atomic components (buttons, fields)
5. Limit depth to 4 levels maximum
6. Use decimal notation consistently

---

## Validation Rules

### Required Elements

Every component MUST have:
- ✅ TYPE declaration
- ✅ At least one state
- ✅ Design hierarchy with root component
- ✅ Consistent naming (snake_case)

### Recommended Elements

Every component SHOULD have:
- ✅ Navigation structure (fork/flow)
- ✅ Multiple states covering full lifecycle
- ✅ Nested component states where applicable
- ✅ Documentation with visual diagrams
- ✅ Substep details for clarity

### Best Practices

- ✅ Keep fork menus under 10 choices
- ✅ Limit flow steps to 5-7 maximum
- ✅ Use nested states for complex interactions
- ✅ Group related actions under parent components
- ✅ Provide explicit return paths
- ✅ Document edge cases and error states

---

## Version History

### Version 1.0 (2025-12-06)
- Initial standardization from menuNav.py
- Complete endpoint classification
- State machine patterns
- Design hierarchy conventions
- Full component catalog

---

## PHASE 1: Minimal UI Component Implementation

### Objective
Create minimal working versions of ALL UI components from the catalog with:
- ✅ **Good formatting** - Clean, consistent visual presentation
- ✅ **Robust rendering** - Handles terminal resize, edge cases
- ✅ **Responsive layout** - Uses new terminal.py layout functions
- ✅ **Modular design** - Each component can be composed/reused

---

### Deliverables Checklist

#### Core Rendering Engine
- [ ] `ui_components.py` - Base component classes
- [ ] Component base class with render() method
- [ ] Layout calculation using terminal.py helpers
- [ ] State tracking for each component

#### Container Components
- [ ] **wrapper** - Generic container (padding, border optional)
- [ ] **panel** - Bordered container with title
- [ ] **frame** - Titled container with decorative border
- [ ] **section** - Logical grouping with separator
- [ ] **dialogue** - Centered modal container
- [ ] **menu** - Navigation container with choice list

#### Display Components
- [ ] **header** - Styled section heading
- [ ] **title** - Primary label (large text)
- [ ] **label** - Standard text display
- [ ] **prompt** - User instruction with icon/marker
- [ ] **message** - Notification text (info/warning/error styles)
- [ ] **list** - Ordered item display (numbered/bulleted)
- [ ] **tree** - Hierarchical display with indent
- [ ] **preview** - Content preview area

#### Input Components
- [ ] **input_field** - Generic single-line input
- [ ] **text_field** - Single-line text with validation
- [ ] **text_area** - Multi-line text input
- [ ] **button** - Action trigger (normal/highlighted)
- [ ] **checkbox** - Boolean toggle with visual state
- [ ] **toggle** - Binary switch (ON/OFF)
- [ ] **dropdown** - List selector (collapsed/expanded)
- [ ] **selector** - Choice picker (arrow navigation)

#### Navigation Components
- [ ] **breadcrumb** - Path display with separators
- [ ] **navigation_controls** - Movement button group
- [ ] **navigation_buttons** - Action button set
- [ ] **pagination** - Page control (prev/next/numbers)
- [ ] **tabs** - View switcher with active indicator

#### Specialized Components
- [ ] **choice_object** - Menu item (number + text + arrow)
- [ ] **param_field** - Labeled input pair
- [ ] **checkbox_list** - Multi-select list
- [ ] **directory_tree** - File browser display
- [ ] **status_bar** - Bottom info bar

---

### Implementation Strategy

#### Phase 1A: Foundation (Core + Containers)
**Priority**: CRITICAL  
**Components**: 12 items

```
1. Component base class architecture
2. wrapper, panel, frame, section
3. dialogue, menu
4. header, title, label, prompt
5. message, list
```

**Validation**: Build simple menu screen using only Phase 1A components

---

#### Phase 1B: Interaction (Input + Navigation)
**Priority**: HIGH  
**Components**: 13 items

```
1. input_field, text_field, text_area
2. button (all variants)
3. checkbox, toggle
4. dropdown, selector
5. breadcrumb, navigation_controls
6. navigation_buttons, pagination, tabs
```

**Validation**: Build registration form with navigation

---

#### Phase 1C: Specialization (Complex Components)
**Priority**: MEDIUM  
**Components**: 6 items

```
1. choice_object (menu item)
2. param_field (labeled input)
3. checkbox_list (multi-select)
4. directory_tree (file browser)
5. status_bar (bottom bar)
6. preview (content area)
```

**Validation**: Build file browser with selection

---

### Technical Requirements

#### 1. Base Component Class
```python
class Component:
    """Base class for all UI components"""
    
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col  
        self.width = width
        self.height = height
        self.state = "IDLE"
        self.children = []
    
    def render(self):
        """Draw component at current position"""
        raise NotImplementedError
    
    def set_state(self, state):
        """Update component state"""
        self.state = state
    
    def add_child(self, child):
        """Add nested component"""
        self.children.append(child)
```

#### 2. Layout Integration
- ALL components accept percentages (0.0-1.0) OR absolute values
- Use `terminal.margin()`, `padding()`, `center_box()` for positioning
- Support responsive behavior on terminal resize
- Calculate child positions using `inset()`, `split_*()` functions

#### 3. Rendering Standards
```python
# Good formatting requirements:
- Consistent box drawing (use ASCII class)
- Text alignment options (left, center, right)
- Padding/margin controls
- Text truncation with ellipsis (...)
- Color/style support (optional Phase 2)

# Robust rendering requirements:
- Handle width < minimum gracefully
- Clip content to boundaries
- Validate position bounds
- Clear background before drawing
- Handle empty content
```

#### 4. State Management
```python
# Each component tracks its own state
component.state = "IDLE" | "ACTIVE" | "FOCUSED" | "DISABLED"

# Visual feedback based on state
- IDLE: Normal display
- ACTIVE: Highlighted/selected
- FOCUSED: Cursor visible, ready for input
- DISABLED: Grayed out, no interaction
```

---

### Testing Matrix

#### Per-Component Tests
For EACH component, verify:

1. ✅ Renders at absolute position (row=10, col=20)
2. ✅ Renders with percentages (row=0.5, col=0.5)
3. ✅ Responds to terminal resize
4. ✅ Handles minimum width gracefully
5. ✅ Clips content properly
6. ✅ Children positioned correctly
7. ✅ State changes reflect visually

#### Integration Tests
1. ✅ Nested components (panel > frame > list)
2. ✅ Form layout (labels + inputs aligned)
3. ✅ Menu rendering (wrapper > title > choices)
4. ✅ Complex layout (split_vertical with panels)

---

### Example: Minimal Button Implementation

```python
from terminal import write, draw_box, ASCII, center_text

class Button(Component):
    """Minimal button with state-based rendering"""
    
    def __init__(self, row, col, width, text):
        super().__init__(row, col, width, 3)  # Buttons are 3 rows tall
        self.text = text
    
    def render(self):
        # Draw border based on state
        if self.state == "ACTIVE":
            # Highlighted border
            draw_box(self.row, self.col, self.width, self.height)
            center_text(self.row + 1, f"> {self.text} <")
        else:
            # Normal border
            border = ASCII.HLINE * self.width
            write(self.row, self.col, border)
            write(self.row + 2, self.col, border)
            center_text(self.row + 1, self.text)
```

**Usage**:
```python
btn = Button(0.5, 0.4, 20, "Click Me")
btn.set_state("ACTIVE")
btn.render()
```

---

### Deliverable Structure

```
ui_components/
├── __init__.py
├── base.py              # Component base class
├── containers.py        # wrapper, panel, frame, etc.
├── display.py           # header, title, label, etc.
├── input.py             # input_field, button, checkbox, etc.
├── navigation.py        # breadcrumb, pagination, tabs
├── specialized.py       # choice_object, directory_tree, etc.
└── demo.py              # Test/demo all components
```

---

### Success Criteria

Phase 1 is complete when:

1. ✅ All 31 components implemented with render() method
2. ✅ Each component handles responsive positioning
3. ✅ Each component clips content properly
4. ✅ State changes work correctly
5. ✅ demo.py shows every component working
6. ✅ Can compose components to build catalog examples:
   - Main menu (catalog item #1)
   - Item registration form (catalog item #2)
   - View collection screen (catalog item #3)
   - Settings menu (catalog item #5)

---

### Timeline Estimate

- **Phase 1A** (Foundation): 4-6 hours
- **Phase 1B** (Interaction): 6-8 hours  
- **Phase 1C** (Specialization): 3-4 hours
- **Testing & Polish**: 2-3 hours

**Total**: ~15-21 hours for complete minimal implementation

---

**END OF MENUNAV STANDARD**
