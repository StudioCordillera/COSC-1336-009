# Menu Class Generator - Project Requirements

## Project Goal
Build a Python application that reads menu configurations from a CSV file and generates modular, lightweight menu class boilerplate code. The generated menus are UI-only and delegate all business logic to a separate action handler module.

---

## Core Requirements

### 1. Input: CSV Menu Definitions
- **Purpose**: Define menu structure, options, and navigation in a data-driven way
- **Format**: CSV file with menu hierarchy and option definitions
- **Location**: `00_IMPORT/menu_definitions.csv`

**Required CSV Columns:**
- `menu_id` - Unique identifier for each menu (e.g., "main_menu", "calc_menu")
- `menu_name` - Display name for the menu (e.g., "Main Menu", "Calculator")
- `option_key` - User input key for selection (e.g., "1", "2", "a", "q")
- `option_text` - Text displayed for the option (e.g., "Add Numbers", "Exit")
- `target_menu` - Which menu to navigate to (leave empty if action-only)
- `action_id` - Optional action identifier to trigger in action handler

**Example CSV Structure:**
```csv
menu_id,menu_name,option_key,option_text,target_menu,action_id
main,Main Menu,1,Calculator,calc_menu,
main,Main Menu,2,File Manager,file_menu,
main,Main Menu,0,Exit,,exit_app
calc_menu,Calculator,1,Add Numbers,calc_menu,calc_add
calc_menu,Calculator,2,Subtract Numbers,calc_menu,calc_subtract
calc_menu,Calculator,b,Back,main,
```

---

### 2. Output: Generated Menu Classes
- **Purpose**: Create Python class boilerplate for each menu defined in CSV
- **Location**: `02_FINALS/generated_menus.py`
- **Characteristics**: 
  - Lightweight - only handles display and user input
  - Modular - each menu is independent
  - Navigation-aware - knows which menu to show next
  - Action-delegating - passes action_id to external handler

**Expected Menu Class Structure:**
```python
class Menu:
    """Base class for all menus"""
    def __init__(self, action_handler=None):
        self.action_handler = action_handler
    
    def display(self):
        """Show menu options to user"""
        pass
    
    def get_choice(self):
        """Get and validate user input"""
        pass
    
    def process_choice(self, choice):
        """Return next menu or trigger action"""
        pass

class MainMenu(Menu):
    """Generated main menu"""
    # Auto-generated from CSV
    pass

class CalcMenu(Menu):
    """Generated calculator menu"""
    # Auto-generated from CSV
    pass
```

---

### 3. Action Handler Module (User-Created)
- **Purpose**: Connect menu options to actual program functionality
- **Location**: `02_FINALS/action_handler.py`
- **Responsibility**: YOU write this to implement business logic
- **Usage**: Generated menus call methods in this module

**Example Action Handler Structure:**
```python
class ActionHandler:
    """User implements this to connect menus to functionality"""
    
    def calc_add(self):
        # Your implementation
        pass
    
    def calc_subtract(self):
        # Your implementation
        pass
    
    def exit_app(self):
        # Your implementation
        pass
```

---

## Project Architecture

### Module Breakdown

#### **1. `csv_parser.py` - CSV Reader Class**
**Responsibility**: Read and parse the CSV file into usable data structures

**Class: CSVParser**
- `__init__(self, csv_filepath)` - Initialize with path to CSV
- `parse(self)` - Read CSV and return structured data
- `validate(self)` - Check CSV has required columns
- `get_menus(self)` - Return dictionary of menus grouped by menu_id

**Data Structure Output:**
```python
{
    'main': {
        'menu_name': 'Main Menu',
        'options': [
            {'key': '1', 'text': 'Calculator', 'target': 'calc_menu', 'action': ''},
            {'key': '2', 'text': 'File Manager', 'target': 'file_menu', 'action': ''},
            {'key': '0', 'text': 'Exit', 'target': '', 'action': 'exit_app'}
        ]
    },
    'calc_menu': { ... }
}
```

#### **2. `menu_generator.py` - Code Generation Engine**
**Responsibility**: Generate Python class code from parsed menu data

**Class: MenuGenerator**
- `__init__(self, menu_data)` - Initialize with parsed CSV data
- `generate_base_class(self)` - Create the base Menu class code
- `generate_menu_class(self, menu_id, menu_info)` - Generate specific menu class
- `generate_all_classes(self)` - Generate all menu classes
- `write_to_file(self, output_path)` - Write generated code to .py file

**Code Generation Strategy:**
- Use string templates or f-strings to build Python code
- Each menu becomes a class that inherits from base Menu
- Methods are generated based on CSV options
- Include docstrings and comments in generated code

#### **3. `menu_class_template.py` - Base Template**
**Responsibility**: Provide the base Menu class structure to be generated

**Contains:**
- Base Menu class with core methods
- Common menu display logic
- Input validation patterns
- Navigation return structure

#### **4. `main.py` - Orchestration**
**Responsibility**: Tie everything together and run the generator

**Flow:**
```python
def main():
    # 1. Parse CSV
    parser = CSVParser('00_IMPORT/menu_definitions.csv')
    menu_data = parser.parse()
    
    # 2. Generate menu classes
    generator = MenuGenerator(menu_data)
    generator.generate_all_classes()
    
    # 3. Write output
    generator.write_to_file('02_FINALS/generated_menus.py')
    
    print("Menu classes generated successfully!")
```

---

## OOP Concepts to Implement

### 1. **Encapsulation**
- CSVParser encapsulates file reading logic
- MenuGenerator encapsulates code generation logic
- Each generated menu class encapsulates its own options

### 2. **Inheritance**
- All generated menus inherit from base Menu class
- Shared functionality (display, input validation) in base class
- Menu-specific details in subclasses

### 3. **Composition**
- Menu objects contain MenuItem objects (option data)
- MenuGenerator uses CSVParser (has-a relationship)
- Generated menus use ActionHandler (dependency injection)

### 4. **Abstraction**
- Base Menu class defines interface all menus follow
- CSVParser abstracts away file reading details
- Action handlers abstract business logic from UI

### 5. **Single Responsibility Principle**
- CSVParser: only reads/parses CSV
- MenuGenerator: only generates code
- Generated Menus: only handle UI
- ActionHandler: only implements business logic

---

## Implementation Steps

### Phase 1: Setup & Planning ✓
- [x] Create project structure
- [x] Define requirements
- [ ] Design CSV schema
- [ ] Sketch class diagrams

### Phase 2: CSV Parser
- [ ] Create CSVParser class
- [ ] Implement CSV reading
- [ ] Implement data validation
- [ ] Test with sample CSV

### Phase 3: Base Menu Template
- [ ] Design base Menu class
- [ ] Implement display() method
- [ ] Implement get_choice() method
- [ ] Implement process_choice() method

### Phase 4: Menu Generator
- [ ] Create MenuGenerator class
- [ ] Implement code generation for base class
- [ ] Implement code generation for menu subclasses
- [ ] Test code generation output

### Phase 5: Integration & Testing
- [ ] Wire up main.py orchestration
- [ ] Generate test menu classes from CSV
- [ ] Create sample action_handler.py
- [ ] Test generated menus in live application

### Phase 6: Enhancement (Optional)
- [ ] Add error handling
- [ ] Support nested submenus
- [ ] Add menu styling options
- [ ] Generate action_handler skeleton

---

## Design Considerations

### Menu Class Design
**Key Decision**: How should menus handle navigation?

**Option A - Return Next Menu ID:**
```python
def process_choice(self, choice):
    # Return string ID of next menu
    return 'calc_menu'  # or None to stay on same menu
```

**Option B - Return Menu Object:**
```python
def process_choice(self, choice):
    # Return actual menu object
    return CalcMenu(self.action_handler)
```

**Recommendation**: Start with Option A (simpler), upgrade to Option B if needed

### Code Generation Approach
**Key Decision**: How to generate Python code?

**Option A - String Templates:**
```python
template = """
class {class_name}(Menu):
    def __init__(self, action_handler=None):
        super().__init__(action_handler)
        self.menu_name = "{menu_name}"
"""
```

**Option B - AST (Abstract Syntax Tree):**
- More complex but type-safe
- Better for advanced generation

**Recommendation**: Use string templates (easier for beginners)

### Action Handler Integration
**Key Decision**: How should generated menus call actions?

**Option A - Direct Method Calls:**
```python
if self.action_handler:
    self.action_handler.calc_add()
```

**Option B - Dynamic Lookup:**
```python
if action_id and self.action_handler:
    method = getattr(self.action_handler, action_id, None)
    if method:
        method()
```

**Recommendation**: Use Option B (more flexible, data-driven)

---

## Testing Strategy

### Unit Tests
- Test CSVParser with various CSV formats
- Test MenuGenerator output is valid Python
- Test generated menus display correctly

### Integration Tests
- Test full pipeline: CSV → Generator → Working Menu
- Test menu navigation flows correctly
- Test action handler integration

### Manual Tests
- Run generated menus interactively
- Verify all options work as expected
- Test edge cases (invalid input, empty menus)

---

## File Organization Reference

```
01_MenuClassCreator/
├── PROJECT_REQUIREMENTS.md          # This file
├── 00_IMPORT/
│   ├── menu_definitions.csv         # Your menu data (YOU CREATE)
│   └── notes.py                     # Scratch notes
├── 01_WORKING/
│   ├── main.py                      # Orchestration script (YOU WRITE)
│   ├── csv_parser.py                # CSV reader class (YOU WRITE)
│   ├── menu_generator.py            # Code generator (YOU WRITE)
│   ├── menus.txt                    # Notes/planning
│   └── templates/
│       └── menu_class_template.py   # Base template (YOU WRITE)
└── 02_FINALS/
    ├── generated_menus.py           # OUTPUT: Generated classes
    └── action_handler.py            # YOUR custom logic module
```

---

## Expected Workflow (When Complete)

1. **Define menus in CSV:**
   - Edit `00_IMPORT/menu_definitions.csv`
   - Add menu structure, options, navigation

2. **Run generator:**
   ```bash
   python 01_WORKING/main.py
   ```

3. **Implement action handler:**
   - Edit `02_FINALS/action_handler.py`
   - Write functions for each action_id

4. **Use generated menus:**
   ```python
   from generated_menus import MainMenu
   from action_handler import ActionHandler
   
   handler = ActionHandler()
   menu = MainMenu(handler)
   menu.display()
   ```

---

## Learning Outcomes

By completing this project, you will practice:

✓ **Class Design** - Creating cohesive, single-purpose classes
✓ **Inheritance** - Building class hierarchies
✓ **File I/O** - Reading CSV, writing Python files
✓ **Data Structures** - Organizing complex menu data
✓ **Code Generation** - Programmatically creating Python code
✓ **Separation of Concerns** - UI vs. business logic
✓ **Dependency Injection** - Pluggable action handlers
✓ **Factory Pattern** - Creating objects from data
✓ **Template Method Pattern** - Consistent structure with variation

---

## Next Steps

1. Create sample CSV file with 2-3 simple menus
2. Start with CSVParser class - get CSV reading working
3. Create base Menu class template
4. Build MenuGenerator to output simple class code
5. Test, iterate, expand

**Start simple, build incrementally!**

Good luck with your project! 🚀
