# PYCLBR_MODULE

## Core Definition
**pyclbr** (Python Class Browser) is a standard library module that provides limited information about functions, classes, and methods defined in Python-coded modules. Extracts information from source code without importing, making it safe for untrusted code. Used for implementing module browsers and code analysis tools.

**Tags**: #pyclbr #module-browser #code-analysis #ast #introspection #static-analysis

---

## COMPLETE PYCLBR METHODS QUICK REFERENCE

### PYCLBR FUNCTIONS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# MAIN FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════
pyclbr.readmodule(module)           # Module name | Read class info | Returns dict of class descriptors
pyclbr.readmodule(module, path)     # Module name + path | Read with custom path | Returns dict of class descriptors
pyclbr.readmodule_ex(module)        # Module name | Read all definitions | Returns dict of functions & classes
pyclbr.readmodule_ex(module, path)  # Module name + path | Read all with custom path | Returns dict of functions & classes
```

---

## PYCLBR DESCRIPTOR CLASSES

### Function Class Attributes

```python
# ═══════════════════════════════════════════════════════════════════════════
# FUNCTION DESCRIPTOR ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
Function.file                       # Attribute | Filename where defined | Returns str filepath
Function.module                     # Attribute | Module name | Returns str module name
Function.name                       # Attribute | Function name | Returns str function name
Function.lineno                     # Attribute | Line number of definition | Returns int line number
Function.parent                     # Attribute | Parent for nested functions | Returns Function/Class or None
Function.children                   # Attribute | Nested functions/classes | Returns dict of descriptors
Function.is_async                   # Attribute | Async function check | Returns True/False (Python 3.10+)
```

### Class Descriptor Attributes

```python
# ═══════════════════════════════════════════════════════════════════════════
# CLASS DESCRIPTOR ATTRIBUTES
# ═══════════════════════════════════════════════════════════════════════════
Class.file                          # Attribute | Filename where defined | Returns str filepath
Class.module                        # Attribute | Module name | Returns str module name
Class.name                          # Attribute | Class name | Returns str class name
Class.lineno                        # Attribute | Line number of definition | Returns int line number
Class.parent                        # Attribute | Parent for nested classes | Returns Class or None
Class.children                      # Attribute | Nested functions/classes | Returns dict of descriptors
Class.super                         # Attribute | Immediate base classes | Returns list of Class objects/strings
Class.methods                       # Attribute | Method names to line numbers | Returns dict (legacy)
```

---

## DETAILED EXAMPLES

### 1. Basic Module Reading

```python
import pyclbr

# Read only class information (backward compatibility)
classes = pyclbr.readmodule('mymodule')

for class_name, class_data in classes.items():
    print(f"Class: {class_name}")
    print(f"  Defined in: {class_data.file}")
    print(f"  At line: {class_data.lineno}")
    print(f"  Base classes: {class_data.super}")
```

**Output:**
```
Class: MyClass
  Defined in: /path/to/mymodule.py
  At line: 5
  Base classes: ['BaseClass', 'MixinClass']
```

---

### 2. Reading All Module Definitions

```python
import pyclbr

# Read both functions and classes
definitions = pyclbr.readmodule_ex('mymodule')

for name, descriptor in definitions.items():
    if isinstance(descriptor, pyclbr.Class):
        print(f"Class: {name} at line {descriptor.lineno}")
        # Show methods
        for method_name, method_line in descriptor.methods.items():
            print(f"  Method: {method_name} at line {method_line}")
    elif isinstance(descriptor, pyclbr.Function):
        print(f"Function: {name} at line {descriptor.lineno}")
```

**Output:**
```
Class: DatabaseConnection at line 10
  Method: connect at line 15
  Method: disconnect at line 25
Function: initialize_app at line 5
Function: cleanup at line 30
```

---

### 3. Analyzing Package Structure

```python
import pyclbr

# Read a package module
module_data = pyclbr.readmodule_ex('mypackage.submodule')

# Check if it's a package
if '__path__' in module_data:
    print(f"Package search path: {module_data['__path__']}")

# Analyze each definition
for name, descriptor in module_data.items():
    if name == '__path__':
        continue
    
    print(f"\n{name}:")
    print(f"  Type: {type(descriptor).__name__}")
    print(f"  Module: {descriptor.module}")
    print(f"  File: {descriptor.file}")
```

**Output:**
```
Package search path: ['/path/to/mypackage']

MyClass:
  Type: Class
  Module: mypackage.submodule
  File: /path/to/mypackage/submodule.py
```

---

### 4. Working with Custom Paths

```python
import pyclbr
import sys

# Provide custom search paths
custom_paths = ['/path/to/custom/modules', '/another/path']

# Read module with custom path
module_info = pyclbr.readmodule_ex('custom_module', path=custom_paths)

for name, descriptor in module_info.items():
    print(f"{name}: {descriptor.file}")
```

---

### 5. Analyzing Nested Classes and Functions

```python
import pyclbr

# Read module with nested definitions
data = pyclbr.readmodule_ex('complex_module')

def print_nested(descriptor, indent=0):
    """Recursively print nested structures"""
    prefix = "  " * indent
    
    if isinstance(descriptor, pyclbr.Class):
        print(f"{prefix}Class: {descriptor.name} (line {descriptor.lineno})")
    elif isinstance(descriptor, pyclbr.Function):
        print(f"{prefix}Function: {descriptor.name} (line {descriptor.lineno})")
    
    # Print children recursively
    for child_name, child_desc in descriptor.children.items():
        print_nested(child_desc, indent + 1)

# Print top-level items
for name, descriptor in data.items():
    if hasattr(descriptor, 'children'):
        print_nested(descriptor)
```

**Output:**
```
Class: OuterClass (line 5)
  Class: InnerClass (line 10)
    Function: inner_method (line 15)
  Function: outer_method (line 20)
Function: top_level_function (line 25)
```

---

### 6. Checking for Async Functions

```python
import pyclbr
import sys

if sys.version_info >= (3, 10):
    # Check for async functions (Python 3.10+)
    module_data = pyclbr.readmodule_ex('async_module')
    
    for name, descriptor in module_data.items():
        if isinstance(descriptor, pyclbr.Function):
            async_status = "async" if descriptor.is_async else "sync"
            print(f"Function {name} is {async_status}")
```

**Output:**
```
Function fetch_data is async
Function process_data is sync
Function save_data is async
```

---

### 7. Analyzing Base Classes

```python
import pyclbr

classes = pyclbr.readmodule('inheritance_example')

for class_name, class_data in classes.items():
    print(f"\nClass: {class_name}")
    print(f"  Direct base classes:")
    
    for base in class_data.super:
        if isinstance(base, pyclbr.Class):
            # Base class was discovered
            print(f"    - {base.name} (from {base.module})")
        else:
            # Base class is just a string (couldn't be discovered)
            print(f"    - {base} (not discoverable)")
```

**Output:**
```
Class: MyClass
  Direct base classes:
    - BaseClass (from base_module)
    - object (not discoverable)
```

---

### 8. Building a Module Browser

```python
import pyclbr
import os

def browse_module(module_name):
    """Simple module browser implementation"""
    try:
        data = pyclbr.readmodule_ex(module_name)
    except Exception as e:
        print(f"Error reading module: {e}")
        return
    
    print(f"Module Browser: {module_name}")
    print("=" * 60)
    
    # Separate classes and functions
    classes = {k: v for k, v in data.items() if isinstance(v, pyclbr.Class)}
    functions = {k: v for k, v in data.items() if isinstance(v, pyclbr.Function)}
    
    # Display classes
    if classes:
        print("\nCLASSES:")
        for name, cls in sorted(classes.items()):
            print(f"  {name} (line {cls.lineno})")
            if cls.super:
                bases = [b.name if isinstance(b, pyclbr.Class) else b 
                        for b in cls.super]
                print(f"    Inherits from: {', '.join(bases)}")
            if cls.methods:
                print(f"    Methods: {', '.join(cls.methods.keys())}")
    
    # Display functions
    if functions:
        print("\nFUNCTIONS:")
        for name, func in sorted(functions.items()):
            async_marker = " (async)" if hasattr(func, 'is_async') and func.is_async else ""
            print(f"  {name}{async_marker} (line {func.lineno})")

# Usage
browse_module('collections')
```

**Output:**
```
Module Browser: collections
============================================================

CLASSES:
  Counter (line 450)
    Inherits from: dict
    Methods: most_common, elements, update
  OrderedDict (line 80)
    Inherits from: dict
    Methods: popitem, move_to_end, __reversed__

FUNCTIONS:
  namedtuple (line 300)
```

---

### 9. Extracting Method Information

```python
import pyclbr

def analyze_class_methods(module_name, class_name):
    """Analyze all methods in a specific class"""
    data = pyclbr.readmodule(module_name)
    
    if class_name not in data:
        print(f"Class {class_name} not found in {module_name}")
        return
    
    cls = data[class_name]
    print(f"Methods in {class_name}:")
    print(f"  File: {cls.file}")
    print(f"  Class defined at line: {cls.lineno}")
    print(f"\n  Methods:")
    
    for method_name, line_num in sorted(cls.methods.items(), key=lambda x: x[1]):
        print(f"    {method_name:30} line {line_num}")

# Usage
analyze_class_methods('mymodule', 'DatabaseHandler')
```

**Output:**
```
Methods in DatabaseHandler:
  File: /path/to/mymodule.py
  Class defined at line: 10
  
  Methods:
    __init__                      line 15
    connect                       line 20
    disconnect                    line 35
    execute_query                 line 45
    close                         line 60
```

---

### 10. Safe Code Inspection

```python
import pyclbr
import tempfile
import os

def safe_inspect_code(code_string):
    """Safely inspect untrusted code without importing"""
    # Write code to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code_string)
        temp_path = f.name
    
    try:
        # Get directory and module name
        module_dir = os.path.dirname(temp_path)
        module_name = os.path.splitext(os.path.basename(temp_path))[0]
        
        # Read module safely without importing
        data = pyclbr.readmodule_ex(module_name, path=[module_dir])
        
        # Analyze structure
        print("Code Structure Analysis:")
        print(f"  Classes: {sum(1 for v in data.values() if isinstance(v, pyclbr.Class))}")
        print(f"  Functions: {sum(1 for v in data.values() if isinstance(v, pyclbr.Function))}")
        
        return data
    finally:
        # Cleanup
        os.unlink(temp_path)

# Usage with untrusted code
untrusted_code = """
class MaliciousClass:
    def __init__(self):
        pass
    
    def suspicious_method(self):
        pass

def safe_function():
    pass
"""

result = safe_inspect_code(untrusted_code)
```

**Output:**
```
Code Structure Analysis:
  Classes: 1
  Functions: 1
```

---

## COMMON USE CASES

### 1. IDE/Editor Features

```python
import pyclbr

def get_autocomplete_data(module_name):
    """Provide autocomplete suggestions for a module"""
    data = pyclbr.readmodule_ex(module_name)
    
    suggestions = {
        'classes': [],
        'functions': [],
        'methods': {}
    }
    
    for name, descriptor in data.items():
        if isinstance(descriptor, pyclbr.Class):
            suggestions['classes'].append(name)
            suggestions['methods'][name] = list(descriptor.methods.keys())
        elif isinstance(descriptor, pyclbr.Function):
            suggestions['functions'].append(name)
    
    return suggestions

# Usage
completions = get_autocomplete_data('os')
print(f"Available classes: {', '.join(completions['classes'][:5])}")
print(f"Available functions: {', '.join(completions['functions'][:5])}")
```

---

### 2. Documentation Generator

```python
import pyclbr

def generate_module_docs(module_name):
    """Generate simple documentation from module structure"""
    data = pyclbr.readmodule_ex(module_name)
    
    docs = [f"# {module_name} Module Documentation\n"]
    
    # Document classes
    classes = {k: v for k, v in data.items() if isinstance(v, pyclbr.Class)}
    if classes:
        docs.append("## Classes\n")
        for name, cls in sorted(classes.items()):
            docs.append(f"### {name}")
            docs.append(f"Defined at line {cls.lineno}\n")
            
            if cls.super:
                bases = [b.name if isinstance(b, pyclbr.Class) else str(b) 
                        for b in cls.super]
                docs.append(f"**Inherits from:** {', '.join(bases)}\n")
            
            if cls.methods:
                docs.append("**Methods:**")
                for method in sorted(cls.methods.keys()):
                    docs.append(f"- `{method}()`")
                docs.append("")
    
    # Document functions
    functions = {k: v for k, v in data.items() if isinstance(v, pyclbr.Function)}
    if functions:
        docs.append("## Functions\n")
        for name, func in sorted(functions.items()):
            docs.append(f"### {name}()")
            docs.append(f"Defined at line {func.lineno}\n")
    
    return "\n".join(docs)

# Usage
documentation = generate_module_docs('mymodule')
print(documentation)
```

---

### 3. Code Complexity Analysis

```python
import pyclbr

def analyze_complexity(module_name):
    """Simple complexity metrics based on structure"""
    data = pyclbr.readmodule_ex(module_name)
    
    metrics = {
        'total_classes': 0,
        'total_functions': 0,
        'total_methods': 0,
        'max_methods_per_class': 0,
        'inheritance_depth': 0,
        'nested_definitions': 0
    }
    
    for name, descriptor in data.items():
        if isinstance(descriptor, pyclbr.Class):
            metrics['total_classes'] += 1
            method_count = len(descriptor.methods)
            metrics['total_methods'] += method_count
            metrics['max_methods_per_class'] = max(
                metrics['max_methods_per_class'], 
                method_count
            )
            
            # Count nested definitions
            metrics['nested_definitions'] += len(descriptor.children)
            
        elif isinstance(descriptor, pyclbr.Function):
            metrics['total_functions'] += 1
            metrics['nested_definitions'] += len(descriptor.children)
    
    return metrics

# Usage
complexity = analyze_complexity('mymodule')
print("Module Complexity Metrics:")
for metric, value in complexity.items():
    print(f"  {metric}: {value}")
```

---

### 4. Dependency Visualization

```python
import pyclbr

def visualize_class_hierarchy(module_name):
    """Create a simple class hierarchy visualization"""
    classes = pyclbr.readmodule(module_name)
    
    def print_hierarchy(class_name, indent=0):
        if class_name not in classes:
            print("  " * indent + f"└─ {class_name} (external)")
            return
        
        cls = classes[class_name]
        print("  " * indent + f"└─ {class_name} (line {cls.lineno})")
        
        # Find child classes
        for name, potential_child in classes.items():
            for base in potential_child.super:
                base_name = base.name if isinstance(base, pyclbr.Class) else base
                if base_name == class_name:
                    print_hierarchy(name, indent + 1)
    
    # Find root classes (those not inheriting from others in module)
    print(f"Class Hierarchy for {module_name}:")
    print("=" * 60)
    
    for name, cls in classes.items():
        is_root = True
        for base in cls.super:
            base_name = base.name if isinstance(base, pyclbr.Class) else base
            if base_name in classes and base_name != 'object':
                is_root = False
                break
        
        if is_root:
            print_hierarchy(name)

# Usage
visualize_class_hierarchy('mymodule')
```

---

## LIMITATIONS AND CONSIDERATIONS

### What pyclbr CAN Do:
```python
# ✓ Read Python source files safely without importing
# ✓ Extract class and function names
# ✓ Get line numbers for definitions
# ✓ Identify base classes
# ✓ List method names
# ✓ Handle nested classes and functions
# ✓ Work with packages
```

### What pyclbr CANNOT Do:
```python
# ✗ Work with extension modules (C/C++)
# ✗ Get function signatures or parameters
# ✗ Extract docstrings
# ✗ Analyze function bodies or logic
# ✗ Get decorators
# ✗ Extract type hints
# ✗ Handle dynamically generated code
# ✗ Get class attributes (only methods)
```

### When to Use pyclbr:
```python
# • Building module browsers or code explorers
# • Implementing autocomplete features
# • Analyzing untrusted code safely
# • Generating simple documentation
# • Quick structural analysis
# • Legacy codebase exploration
```

### When NOT to Use pyclbr:
```python
# • Need detailed AST analysis → Use 'ast' module
# • Need runtime introspection → Use 'inspect' module
# • Need type information → Use 'typing' module
# • Need full code analysis → Use 'ast' + 'inspect'
# • Working with compiled extensions → Use different approach
```

---

## ALTERNATIVES AND RELATED MODULES

### ast - Abstract Syntax Trees
```python
import ast

# Full AST parsing for detailed analysis
with open('mymodule.py') as f:
    tree = ast.parse(f.read())

# Get all function definitions
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(f"Function: {node.name} at line {node.lineno}")
```

### inspect - Live Object Inspection
```python
import inspect
import mymodule

# Get live information (requires import)
for name, obj in inspect.getmembers(mymodule, inspect.isclass):
    print(f"Class: {name}")
    print(f"  Methods: {[m[0] for m in inspect.getmembers(obj, inspect.isfunction)]}")
```

### pkgutil - Package Utilities
```python
import pkgutil

# Find all modules in a package
for importer, modname, ispkg in pkgutil.walk_packages(path=['mypackage']):
    print(f"{'Package' if ispkg else 'Module'}: {modname}")
```

---

## BEST PRACTICES

### 1. Error Handling

```python
import pyclbr

def safe_read_module(module_name, custom_path=None):
    """Safely read module with proper error handling"""
    try:
        if custom_path:
            return pyclbr.readmodule_ex(module_name, path=custom_path)
        return pyclbr.readmodule_ex(module_name)
    except FileNotFoundError:
        print(f"Module {module_name} not found")
        return {}
    except SyntaxError as e:
        print(f"Syntax error in {module_name}: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error reading {module_name}: {e}")
        return {}
```

---

### 2. Version Compatibility

```python
import pyclbr
import sys

def get_function_info(func_descriptor):
    """Get function info with version compatibility"""
    info = {
        'name': func_descriptor.name,
        'file': func_descriptor.file,
        'lineno': func_descriptor.lineno,
        'parent': func_descriptor.parent,
        'children': func_descriptor.children
    }
    
    # is_async only available in Python 3.10+
    if sys.version_info >= (3, 10):
        info['is_async'] = func_descriptor.is_async
    
    return info
```

---

### 3. Performance Considerations

```python
import pyclbr
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_read_module(module_name):
    """Cache module reads for performance"""
    return pyclbr.readmodule_ex(module_name)

# Reuse cached data
data1 = cached_read_module('mymodule')  # Reads from disk
data2 = cached_read_module('mymodule')  # Returns cached result
```

---

## INTEGRATION EXAMPLES

### With pathlib

```python
import pyclbr
from pathlib import Path

def analyze_project_structure(project_path):
    """Analyze all Python files in a project"""
    project_path = Path(project_path)
    results = {}
    
    for py_file in project_path.rglob('*.py'):
        if py_file.name.startswith('__'):
            continue
        
        # Convert path to module name
        rel_path = py_file.relative_to(project_path)
        module_name = str(rel_path.with_suffix('')).replace('/', '.')
        
        try:
            data = pyclbr.readmodule_ex(module_name, path=[str(project_path)])
            results[module_name] = data
        except Exception as e:
            print(f"Skipping {module_name}: {e}")
    
    return results
```

---

### With JSON Export

```python
import pyclbr
import json

def export_module_structure(module_name, output_file):
    """Export module structure to JSON"""
    data = pyclbr.readmodule_ex(module_name)
    
    export_data = {'classes': [], 'functions': []}
    
    for name, descriptor in data.items():
        if isinstance(descriptor, pyclbr.Class):
            export_data['classes'].append({
                'name': name,
                'file': descriptor.file,
                'lineno': descriptor.lineno,
                'methods': list(descriptor.methods.keys()),
                'bases': [b.name if isinstance(b, pyclbr.Class) else str(b) 
                         for b in descriptor.super]
            })
        elif isinstance(descriptor, pyclbr.Function):
            export_data['functions'].append({
                'name': name,
                'file': descriptor.file,
                'lineno': descriptor.lineno
            })
    
    with open(output_file, 'w') as f:
        json.dump(export_data, f, indent=2)

# Usage
export_module_structure('mymodule', 'module_structure.json')
```

---

## SUMMARY TABLE

| Feature | Description | Use Case |
|---------|-------------|----------|
| **readmodule()** | Read class info only | Legacy compatibility, quick class lookup |
| **readmodule_ex()** | Read all definitions | Complete module analysis |
| **Function class** | Function descriptors | Analyze function structure |
| **Class class** | Class descriptors | Analyze class hierarchy |
| **Safe analysis** | No code execution | Untrusted code inspection |
| **Source-based** | Parses source files | Works without importing |
| **Line numbers** | Definition locations | Editor navigation, docs |
| **Nested support** | Children attribute | Complex structure analysis |
| **Package support** | __path__ detection | Package browsing |

---

## KEY TAKEAWAYS

1. **Safe by Design**: pyclbr never executes code, making it safe for untrusted sources
2. **Python Only**: Cannot analyze C extensions or non-Python modules
3. **Structural Only**: Provides names and locations, not detailed analysis
4. **Legacy Support**: readmodule() kept for backward compatibility
5. **Modern Features**: Use readmodule_ex() for complete information
6. **Nested Definitions**: Python 3.7+ supports analyzing nested classes/functions
7. **Async Support**: Python 3.10+ detects async functions
8. **Limited Scope**: For detailed analysis, use `ast` or `inspect` modules instead

---

## EXTERNAL RESOURCES

- **Official Docs**: https://docs.python.org/3/library/pyclbr.html
- **Source Code**: https://github.com/python/cpython/tree/main/Lib/pyclbr.py
- **Related Modules**: ast, inspect, pkgutil, importlib
- **PEP References**: None specific to pyclbr

---

**Last Updated**: December 2025  
**Python Version**: 3.7+ (with nested definitions support)  
**Module Status**: Stable, part of standard library
