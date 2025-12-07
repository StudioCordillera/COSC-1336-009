# CHAINMAP_METHODS

## Core Definition
**ChainMap** groups multiple dictionaries into a single view. Lookups search the underlying mappings successively until a key is found. Updates/insertions affect only the first mapping. Provides a unified view without copying data.

**Tags**: #collections #chainmap #mapping #dictionary #view #multi-dict

---

## COMPLETE CHAINMAP METHODS QUICK REFERENCE

### CHAINMAP METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# CREATION & INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════
ChainMap()                          # No args | Create empty ChainMap | Returns ChainMap with single empty dict
ChainMap(dict1)                     # Single dict | Create from one mapping | Returns ChainMap with one dict
ChainMap(dict1, dict2, ...)         # Multiple dicts | Chain multiple mappings | Returns ChainMap with all dicts
ChainMap(*mappings)                 # Iterable of dicts | Unpack mappings | Returns ChainMap from sequence
ChainMap.fromkeys(seq)              # Sequence | Create with None values | Returns ChainMap with keys from seq
ChainMap.fromkeys(seq, value)       # Sequence + value | Create with default | Returns ChainMap with keys and value

# ═══════════════════════════════════════════════════════════════════════════
# ACCESS & LOOKUP METHODS
# ═══════════════════════════════════════════════════════════════════════════
cm[key]                             # ChainMap | Get value by key | Returns value or KeyError
cm.get(key)                         # ChainMap | Get value safely | Returns value or None
cm.get(key, default)                # ChainMap | Get with default | Returns value or default if not found
key in cm                           # ChainMap | Check key existence | Returns True/False
key not in cm                       # ChainMap | Check key absence | Returns True/False
len(cm)                             # ChainMap | Count unique keys | Returns int count of all keys
cm.keys()                           # ChainMap | Get all keys | Returns KeysView of all unique keys
cm.values()                         # ChainMap | Get all values | Returns ValuesView (first occurrence)
cm.items()                          # ChainMap | Get key-value pairs | Returns ItemsView (first occurrence)
list(cm)                            # ChainMap | Convert keys to list | Returns list of keys
iter(cm)                            # ChainMap | Iterate keys | Returns iterator over keys
bool(cm)                            # ChainMap | Check if non-empty | Returns True if has keys, else False

# ═══════════════════════════════════════════════════════════════════════════
# MODIFICATION METHODS (First Mapping Only)
# ═══════════════════════════════════════════════════════════════════════════
cm[key] = value                     # ChainMap | Set/update key | Modifies first dict only
cm.setdefault(key)                  # ChainMap | Get or set to None | Returns value or sets key=None
cm.setdefault(key, default)         # ChainMap | Get or set default | Returns value or sets key=default
cm.update(dict)                     # ChainMap | Update from dict | Updates first dict with mappings
cm.update(**kwargs)                 # ChainMap | Update with keywords | Updates first dict with kwargs
cm.update(iterable)                 # ChainMap | Update from iterable | Updates first dict from key-value pairs
del cm[key]                         # ChainMap | Delete key | Deletes from first dict or KeyError
cm.pop(key)                         # ChainMap | Remove and return | Returns value or KeyError
cm.pop(key, default)                # ChainMap | Remove with default | Returns value or default if not found
cm.popitem()                        # ChainMap | Remove last item | Returns (key, value) tuple or KeyError
cm.clear()                          # ChainMap | Remove all items | Clears first dict only

# ═══════════════════════════════════════════════════════════════════════════
# CHAINMAP-SPECIFIC METHODS
# ═══════════════════════════════════════════════════════════════════════════
cm.maps                             # ChainMap | Access underlying list | Returns list of dicts
cm.new_child()                      # ChainMap | Add empty child | Returns new ChainMap with empty dict at front
cm.new_child(m)                     # ChainMap | Add child mapping | Returns new ChainMap with m at front
cm.parents                          # ChainMap | Get parent view | Returns ChainMap without first dict
cm.copy()                           # ChainMap | Shallow copy | Returns new ChainMap with same dict references

# ═══════════════════════════════════════════════════════════════════════════
# DICTIONARY COMPATIBILITY METHODS
# ═══════════════════════════════════════════════════════════════════════════
dict(cm)                            # ChainMap | Convert to dict | Returns merged dict (first occurrence wins)
{**cm}                              # ChainMap | Unpack to dict | Returns merged dict via unpacking
cm | other                          # ChainMap + dict (3.9+) | Union operator | Returns new dict merged
cm |= other                         # ChainMap + dict (3.9+) | Update operator | Updates first dict in-place
cm == other                         # Two ChainMaps | Check equality | Returns True if same keys/values
cm != other                         # Two ChainMaps | Check inequality | Returns True if different
str(cm)                             # ChainMap | String representation | Returns string like "ChainMap({...}, {...})"
repr(cm)                            # ChainMap | Detailed representation | Returns repr string

# ═══════════════════════════════════════════════════════════════════════════
# ITERATION METHODS
# ═══════════════════════════════════════════════════════════════════════════
for key in cm:                      # ChainMap | Iterate keys | Yields each unique key
for value in cm.values():           # ChainMap | Iterate values | Yields values (first occurrence)
for key, value in cm.items():       # ChainMap | Iterate pairs | Yields (key, value) tuples
enumerate(cm)                       # ChainMap | Index + iterate keys | Yields (index, key) tuples
enumerate(cm.items())               # ChainMap | Index + iterate items | Yields (index, (key, value)) tuples
reversed(cm)                        # ChainMap | Reverse key order | Yields keys in reverse
zip(cm.keys(), cm.values())         # ChainMap | Pair keys and values | Yields (key, value) tuples

# ═══════════════════════════════════════════════════════════════════════════
# ATTRIBUTE ACCESS
# ═══════════════════════════════════════════════════════════════════════════
cm.__class__                        # ChainMap | Get class type | Returns <class 'collections.ChainMap'>
cm.__doc__                          # ChainMap | Get docstring | Returns ChainMap documentation
cm.__dict__                         # ChainMap | Internal attributes | Returns instance dict
type(cm)                            # ChainMap | Get type | Returns <class 'collections.ChainMap'>
isinstance(cm, ChainMap)            # ChainMap | Type checking | Returns True/False
hasattr(cm, 'maps')                 # ChainMap | Check attribute | Returns True/False
getattr(cm, 'maps')                 # ChainMap | Get attribute | Returns attribute value or AttributeError
```

### COMMON OPERATION EXAMPLES

```python
from collections import ChainMap

# Creation examples
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'c': 5, 'd': 6}

cm = ChainMap(dict1, dict2, dict3)

# Access operations
cm['a']                             # → 1 (found in dict1)
cm['b']                             # → 2 (found in dict1, dict2 ignored)
cm['c']                             # → 4 (found in dict2, dict3 ignored)
cm['d']                             # → 6 (found in dict3)
cm.get('e', 'not found')            # → 'not found'
len(cm)                             # → 4 (unique keys: a, b, c, d)

# Modification (affects first mapping only)
cm['e'] = 7                         # dict1 = {'a': 1, 'b': 2, 'e': 7}
cm['b'] = 99                        # dict1 = {'a': 1, 'b': 99, 'e': 7}
del cm['e']                         # dict1 = {'a': 1, 'b': 99}

# ChainMap-specific operations
cm.maps                             # → [dict1, dict2, dict3]
cm.parents                          # → ChainMap(dict2, dict3)
new_cm = cm.new_child({'x': 10})    # → ChainMap({'x': 10}, dict1, dict2, dict3)

# Lookup order demonstration
lookup = ChainMap({'a': 'FIRST'}, {'a': 'SECOND'}, {'a': 'THIRD'})
lookup['a']                         # → 'FIRST' (stops at first match)

# Conversion
dict(cm)                            # → {'a': 1, 'b': 99, 'c': 4, 'd': 6}
list(cm)                            # → ['a', 'b', 'e', 'c', 'd']
list(cm.values())                   # → [1, 99, 7, 4, 6]
```

---

## DETAILED CHAINMAP OPERATIONS

### 1. LOOKUP BEHAVIOR & PRECEDENCE

```python
from collections import ChainMap

# ═══════════════════════════════════════════════════════════════════════════
# FIRST-MATCH LOOKUP PATTERN
# ═══════════════════════════════════════════════════════════════════════════

# Example: Configuration with defaults
defaults = {'theme': 'light', 'font_size': 12, 'auto_save': True}
user_prefs = {'theme': 'dark', 'font_size': 14}
session = {'font_size': 16}

config = ChainMap(session, user_prefs, defaults)

# Lookups check session → user_prefs → defaults
config['theme']                     # → 'dark' (from user_prefs)
config['font_size']                 # → 16 (from session, stops here)
config['auto_save']                 # → True (from defaults)

# Demonstrating search order
print(config.maps)
# → [{'font_size': 16}, 
#    {'theme': 'dark', 'font_size': 14}, 
#    {'theme': 'light', 'font_size': 12, 'auto_save': True}]

# ═══════════════════════════════════════════════════════════════════════════
# KEY EXISTENCE CHECKING
# ═══════════════════════════════════════════════════════════════════════════

'theme' in config                   # → True (checks all mappings)
'language' in config                # → False (not in any mapping)

# Get with default
config.get('language', 'en')        # → 'en' (not found, returns default)
config.get('theme')                 # → 'dark' (found, returns value)

# ═══════════════════════════════════════════════════════════════════════════
# VIEWING ALL KEYS (No Duplicates)
# ═══════════════════════════════════════════════════════════════════════════

list(config.keys())
# → ['font_size', 'theme', 'auto_save'] (unique keys only)

# But maps show all occurrences
for m in config.maps:
    print(list(m.keys()))
# → ['font_size']
# → ['theme', 'font_size']
# → ['theme', 'font_size', 'auto_save']
```

### 2. MODIFICATION RULES

```python
from collections import ChainMap

# ═══════════════════════════════════════════════════════════════════════════
# FIRST MAPPING ONLY RULE
# ═══════════════════════════════════════════════════════════════════════════

base = {'a': 1, 'b': 2}
overlay = {'b': 999, 'c': 3}
cm = ChainMap(overlay, base)

# All modifications affect first mapping (overlay) only
cm['a']                             # → 1 (from base, but...)
cm['a'] = 100                       # Sets in overlay
print(overlay)                      # → {'b': 999, 'c': 3, 'a': 100}
print(base)                         # → {'a': 1, 'b': 2} (unchanged!)

cm['b'] = 777                       # Updates overlay['b']
print(overlay)                      # → {'b': 777, 'c': 3, 'a': 100}
print(base)                         # → {'a': 1, 'b': 2} (base['b'] unchanged)

# Deletion from first mapping only
cm['d'] = 4                         # Sets in overlay
del cm['d']                         # Deletes from overlay
print(overlay)                      # → {'b': 777, 'c': 3, 'a': 100}

# ═══════════════════════════════════════════════════════════════════════════
# UPDATE OPERATIONS
# ═══════════════════════════════════════════════════════════════════════════

cm.update({'x': 10, 'y': 20})       # Updates overlay only
print(overlay)                      # → {'b': 777, 'c': 3, 'a': 100, 'x': 10, 'y': 20}

cm.update(z=30)                     # Keyword update
print(overlay)                      # → {..., 'z': 30}

# ═══════════════════════════════════════════════════════════════════════════
# CLEAR OPERATION (First Mapping Only)
# ═══════════════════════════════════════════════════════════════════════════

cm.clear()                          # Clears overlay only!
print(overlay)                      # → {} (empty)
print(base)                         # → {'a': 1, 'b': 2} (unchanged)
print(list(cm.keys()))              # → ['a', 'b'] (base still visible)

# ═══════════════════════════════════════════════════════════════════════════
# POP & POPITEM (First Mapping Only)
# ═══════════════════════════════════════════════════════════════════════════

overlay = {'x': 1, 'y': 2}
base = {'a': 10, 'b': 20}
cm = ChainMap(overlay, base)

# Pop from first mapping
val = cm.pop('x')                   # → 1 (removes from overlay)
print(overlay)                      # → {'y': 2}

# Trying to pop from non-first mapping raises KeyError
cm.pop('a')                         # KeyError! ('a' is in base, not overlay)
cm.pop('a', 'default')              # → 'default' (not in first mapping)

# PopItem from first mapping
cm.popitem()                        # → ('y', 2)
print(overlay)                      # → {} (empty)
cm.popitem()                        # KeyError! (first mapping is empty)
```

### 3. CHAINMAP-SPECIFIC METHODS

```python
from collections import ChainMap

# ═══════════════════════════════════════════════════════════════════════════
# new_child() - CREATE CHILD CONTEXT
# ═══════════════════════════════════════════════════════════════════════════

# Common use: Function scope simulation
global_vars = {'x': 10, 'y': 20}
cm = ChainMap(global_vars)

# Enter new scope (add child context)
def function_scope():
    local_cm = cm.new_child()       # Add empty dict at front
    local_cm['x'] = 100             # Local override
    local_cm['z'] = 30              # Local-only variable
    
    print(local_cm['x'])            # → 100 (local)
    print(local_cm['y'])            # → 20 (inherited from global)
    print(local_cm['z'])            # → 30 (local only)
    
    print(local_cm.maps)
    # → [{'x': 100, 'z': 30}, {'x': 10, 'y': 20}]
    
    return local_cm

local_cm = function_scope()
print(cm['x'])                      # → 10 (global unchanged)

# new_child() with initial mapping
child = cm.new_child({'a': 1, 'b': 2})
print(child.maps)
# → [{'a': 1, 'b': 2}, {'x': 10, 'y': 20}]

# ═══════════════════════════════════════════════════════════════════════════
# parents - ACCESS PARENT CONTEXT
# ═══════════════════════════════════════════════════════════════════════════

d1 = {'a': 1}
d2 = {'b': 2}
d3 = {'c': 3}
cm = ChainMap(d1, d2, d3)

# Get parent view (skip first mapping)
parents = cm.parents
print(parents.maps)                 # → [{'b': 2}, {'c': 3}]
print(parents['b'])                 # → 2
# parents['a']                      # KeyError! (d1 excluded)

# Chaining parents
grandparents = parents.parents
print(grandparents.maps)            # → [{'c': 3}]

# Empty parents
great_grandparents = grandparents.parents
print(great_grandparents.maps)      # → [{}] (empty dict)

# ═══════════════════════════════════════════════════════════════════════════
# maps - DIRECT MAPPING ACCESS
# ═══════════════════════════════════════════════════════════════════════════

cm = ChainMap({'a': 1}, {'b': 2}, {'c': 3})

# Access the underlying list
print(cm.maps)
# → [{'a': 1}, {'b': 2}, {'c': 3}]

# Manipulate the list directly (ADVANCED)
cm.maps.append({'d': 4})            # Add mapping to end
print(list(cm.keys()))              # → ['a', 'b', 'c', 'd']

cm.maps.insert(0, {'a': 999})       # Insert at front
print(cm['a'])                      # → 999 (new first mapping wins)

cm.maps.pop()                       # Remove last mapping
print(list(cm.keys()))              # → ['a', 'b', 'c']

# Replace maps list entirely
cm.maps = [{'x': 10}, {'y': 20}]
print(list(cm.keys()))              # → ['x', 'y']

# ═══════════════════════════════════════════════════════════════════════════
# copy() - SHALLOW COPY
# ═══════════════════════════════════════════════════════════════════════════

original = ChainMap({'a': 1}, {'b': 2})
copied = original.copy()

# Copies share the same underlying dicts!
print(copied.maps is original.maps)         # → False (new list)
print(copied.maps[0] is original.maps[0])   # → True (same dict objects!)

# Modifying first mapping affects both
copied['a'] = 999
print(original['a'])                # → 999 (shared dict modified)

# True deep copy requires manual work
import copy as cp
deep_copied = ChainMap(*[cp.deepcopy(m) for m in original.maps])
deep_copied['a'] = 100
print(original['a'])                # → 999 (unchanged, different dicts)
```

### 4. USE CASES & PATTERNS

```python
from collections import ChainMap

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 1: LAYERED CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

# Layer priority: command-line > environment > user config > defaults
defaults = {'debug': False, 'port': 8000, 'host': 'localhost'}
user_config = {'port': 8080, 'host': '0.0.0.0'}
env_vars = {'debug': True}
cli_args = {}  # Empty initially

config = ChainMap(cli_args, env_vars, user_config, defaults)

print(config['debug'])              # → True (from env_vars)
print(config['port'])               # → 8080 (from user_config)
print(config['host'])               # → '0.0.0.0' (from user_config)

# Add CLI override
cli_args['port'] = 9000
print(config['port'])               # → 9000 (CLI takes precedence)

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 2: SCOPE SIMULATION (Like Python's locals/globals)
# ═══════════════════════════════════════════════════════════════════════════

class SimpleInterpreter:
    def __init__(self):
        self.globals = {'print': print, 'len': len}
        self.scopes = ChainMap(self.globals)
    
    def enter_function(self, params):
        """Simulate entering function scope"""
        self.scopes = self.scopes.new_child(params)
    
    def exit_function(self):
        """Simulate exiting function scope"""
        self.scopes = self.scopes.parents
    
    def get_var(self, name):
        return self.scopes[name]
    
    def set_var(self, name, value):
        self.scopes[name] = value

interp = SimpleInterpreter()

# Global scope
interp.set_var('x', 10)
print(interp.get_var('x'))          # → 10

# Enter function scope with params
interp.enter_function({'x': 100, 'y': 200})
print(interp.get_var('x'))          # → 100 (local shadows global)
print(interp.get_var('y'))          # → 200 (local only)
interp.set_var('z', 300)            # Create local variable

# Exit function scope
interp.exit_function()
print(interp.get_var('x'))          # → 10 (back to global)
# interp.get_var('y')               # KeyError! (was local only)

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 3: TEMPLATE VARIABLE RESOLUTION
# ═══════════════════════════════════════════════════════════════════════════

# Template with multiple context layers
from string import Template

page_defaults = {'title': 'My Site', 'year': 2025}
section_vars = {'title': 'About Us'}
request_vars = {'user': 'Alice'}

context = ChainMap(request_vars, section_vars, page_defaults)

template = Template('$title - $year | User: $user')
result = template.substitute(context)
print(result)                       # → "About Us - 2025 | User: Alice"

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 4: FUNCTION DEFAULT ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════════

def process_data(data, **options):
    """Process data with layered options"""
    defaults = {'verbose': False, 'timeout': 30, 'retries': 3}
    settings = ChainMap(options, defaults)
    
    if settings['verbose']:
        print(f"Processing with timeout={settings['timeout']}")
    
    # ... processing logic using settings
    return f"Processed with {settings['retries']} retries"

# Use defaults
result = process_data([1, 2, 3])

# Override specific options
result = process_data([1, 2, 3], verbose=True, timeout=60)

# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 5: MULTI-LEVEL CACHING
# ═══════════════════════════════════════════════════════════════════════════

class CacheSystem:
    def __init__(self):
        self.memory_cache = {}      # Fast, small
        self.disk_cache = {}        # Slower, larger
        self.database = {}          # Slowest, permanent
        
        self.cache = ChainMap(
            self.memory_cache,
            self.disk_cache,
            self.database
        )
    
    def get(self, key):
        """Get from cache, checking memory → disk → database"""
        if key in self.cache:
            value = self.cache[key]
            # Promote to memory cache
            self.memory_cache[key] = value
            return value
        return None
    
    def set(self, key, value):
        """Set in memory cache (first mapping)"""
        self.cache[key] = value

cache_sys = CacheSystem()
cache_sys.set('user:123', {'name': 'Bob'})
print(cache_sys.memory_cache)       # → {'user:123': {'name': 'Bob'}}
```

### 5. ADVANCED TECHNIQUES

```python
from collections import ChainMap

# ═══════════════════════════════════════════════════════════════════════════
# REVERSING LOOKUP ORDER
# ═══════════════════════════════════════════════════════════════════════════

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Normal: d1 has priority
cm_normal = ChainMap(d1, d2)
print(cm_normal['b'])               # → 2 (from d1)

# Reversed: d2 has priority
cm_reversed = ChainMap(d2, d1)
print(cm_reversed['b'])             # → 3 (from d2)

# ═══════════════════════════════════════════════════════════════════════════
# MERGING TO SINGLE DICT
# ═══════════════════════════════════════════════════════════════════════════

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {'c': 5, 'd': 6}
cm = ChainMap(d1, d2, d3)

# Method 1: dict() constructor
merged = dict(cm)
print(merged)                       # → {'a': 1, 'b': 2, 'c': 4, 'd': 6}

# Method 2: Dictionary unpacking (reverse order!)
merged_reversed = {k: v for k, v in cm.items()}
print(merged_reversed)              # → Same as merged

# Method 3: Update in reverse for different priority
final = {}
for m in reversed(cm.maps):
    final.update(m)
print(final)                        # → {'a': 1, 'b': 3, 'c': 5, 'd': 6}
# Note: Later mappings overwrite earlier ones

# ═══════════════════════════════════════════════════════════════════════════
# DYNAMIC MAPPING REORDERING
# ═══════════════════════════════════════════════════════════════════════════

low_priority = {'setting': 'low'}
medium_priority = {'setting': 'medium'}
high_priority = {'setting': 'high'}

cm = ChainMap(low_priority, medium_priority, high_priority)
print(cm['setting'])                # → 'low'

# Dynamically reorder priority
cm.maps = [high_priority, medium_priority, low_priority]
print(cm['setting'])                # → 'high'

# ═══════════════════════════════════════════════════════════════════════════
# FILTERED VIEW
# ═══════════════════════════════════════════════════════════════════════════

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'd': 4}
cm = ChainMap(d1, d2)

# Create filtered view (only keys starting with 'a' or 'b')
filtered = {k: v for k, v in cm.items() if k.startswith(('a', 'b'))}
print(filtered)                     # → {'a': 1, 'b': 2}

# ═══════════════════════════════════════════════════════════════════════════
# CHAINMAP WITH PROPERTY ACCESS
# ═══════════════════════════════════════════════════════════════════════════

class AttributeChainMap(ChainMap):
    """ChainMap with attribute access"""
    
    def __getattr__(self, name):
        if name.startswith('_'):
            raise AttributeError(name)
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)
    
    def __setattr__(self, name, value):
        if name in ('maps',):  # Special attributes
            super().__setattr__(name, value)
        else:
            self[name] = value

config = AttributeChainMap({'a': 1}, {'b': 2})
print(config.a)                     # → 1 (attribute access)
print(config.b)                     # → 2
config.c = 3                        # Sets in first mapping
print(config['c'])                  # → 3

# ═══════════════════════════════════════════════════════════════════════════
# CHAINMAP FOR PLUGIN SYSTEMS
# ═══════════════════════════════════════════════════════════════════════════

class PluginRegistry:
    def __init__(self):
        self.core_plugins = {'logger': self.log, 'validator': self.validate}
        self.user_plugins = {}
        self.plugins = ChainMap(self.user_plugins, self.core_plugins)
    
    def log(self, msg):
        return f"[LOG] {msg}"
    
    def validate(self, data):
        return bool(data)
    
    def register_plugin(self, name, func):
        """Register user plugin (higher priority)"""
        self.user_plugins[name] = func
    
    def call_plugin(self, name, *args):
        return self.plugins[name](*args)

registry = PluginRegistry()
print(registry.call_plugin('logger', 'Hello'))  # → "[LOG] Hello"

# Override core plugin
registry.register_plugin('logger', lambda msg: f"[CUSTOM] {msg}")
print(registry.call_plugin('logger', 'Hello'))  # → "[CUSTOM] Hello"
```

---

## COMMON PATTERNS & IDIOMS

### Pattern 1: Configuration Hierarchy
```python
from collections import ChainMap

config = ChainMap(
    {},                             # Runtime overrides (highest priority)
    {},                             # Command-line arguments
    {},                             # Environment variables
    {},                             # User config file
    {}                              # System defaults (lowest priority)
)
```

### Pattern 2: Temporary Context Override
```python
original = ChainMap({'a': 1, 'b': 2})

# Create temporary override
with_override = original.new_child({'a': 999})
print(with_override['a'])           # → 999 (overridden)
print(original['a'])                # → 1 (unchanged)

# Exit context
print(original['a'])                # → 1
```

### Pattern 3: Search Path Implementation
```python
system_path = {'/usr/bin': ['ls', 'cat']}
user_path = {'/home/user/bin': ['custom_tool']}
local_path = {'./': ['script.py']}

paths = ChainMap(local_path, user_path, system_path)

def find_executable(name):
    for path, executables in paths.items():
        if name in executables:
            return f"{path}/{name}"
    return None
```

---

## PERFORMANCE CHARACTERISTICS

```python
# ═══════════════════════════════════════════════════════════════════════════
# TIME COMPLEXITY
# ═══════════════════════════════════════════════════════════════════════════

# Lookup: O(n) - where n is number of mappings
#   Must search through each mapping until key found
#   Worst case: key in last mapping or not present

# Insertion: O(1) - always inserts into first mapping

# Deletion: O(1) - always deletes from first mapping (if present)

# Length: O(n) - must check all mappings for unique keys

# ═══════════════════════════════════════════════════════════════════════════
# SPACE COMPLEXITY
# ═══════════════════════════════════════════════════════════════════════════

# O(1) - ChainMap stores only references to dicts, not copies
# Memory-efficient for large dictionaries

# ═══════════════════════════════════════════════════════════════════════════
# PERFORMANCE TIPS
# ═══════════════════════════════════════════════════════════════════════════

# 1. Put most frequently accessed mappings first
# 2. Keep number of chained mappings small (< 5 ideally)
# 3. For read-heavy workloads, consider caching lookups
# 4. For write-heavy workloads, regular dict may be better
```

---

## COMPARISON WITH ALTERNATIVES

### ChainMap vs dict.update()
```python
# ChainMap: No copying, preserves originals
d1 = {'a': 1}
d2 = {'b': 2}
cm = ChainMap(d1, d2)
cm['a'] = 999
print(d1)                           # → {'a': 999} (d1 modified directly)

# dict.update(): Copies data, creates new dict
merged = {**d1, **d2}
merged['a'] = 999
print(d1)                           # → {'a': 1} (d1 unchanged)
```

### ChainMap vs {**d1, **d2}
```python
# ChainMap: Lazy evaluation, no copying
cm = ChainMap(d1, d2, d3)           # O(1) - just stores references

# Unpacking: Eager evaluation, copies all data
merged = {**d1, **d2, **d3}         # O(n) - copies all key-value pairs
```

### ChainMap vs collections.UserDict
```python
# ChainMap: Multiple source mappings, lookup chain
# UserDict: Single dict wrapper for customization
```

---

## COMMON ERRORS & SOLUTIONS

### Error 1: Modifying Non-First Mapping
```python
d1 = {'a': 1}
d2 = {'b': 2}
cm = ChainMap(d1, d2)

# WRONG: Trying to modify d2 through ChainMap
cm['b'] = 999                       # Modifies d1, not d2!
print(d1)                           # → {'a': 1, 'b': 999}
print(d2)                           # → {'b': 2} (unchanged)

# RIGHT: Modify d2 directly
d2['b'] = 999
print(cm['b'])                      # → 999 (d2 is not first, but lookup finds it)
```

### Error 2: Deleting Keys Not in First Mapping
```python
d1 = {'a': 1}
d2 = {'b': 2}
cm = ChainMap(d1, d2)

del cm['b']                         # KeyError! ('b' not in first mapping)

# SOLUTION: Check or use pop with default
cm.pop('b', None)                   # Returns None, no error
```

### Error 3: Confusion with .maps Order
```python
cm = ChainMap(d1, d2, d3)
# Maps are ordered: [d1, d2, d3]
# Lookup order: d1 → d2 → d3 (first match wins)
# Modification: d1 only

# WRONG: Assuming last mapping has priority
# RIGHT: First mapping has priority
```

---

## SUMMARY

### Key Takeaways
1. **ChainMap groups multiple dicts into single view** - no data copying
2. **Lookups search in order until key found** - first match wins
3. **Modifications affect only first mapping** - other mappings unchanged
4. **Perfect for layered configurations** - command-line > env > config > defaults
5. **Ideal for scope simulation** - local > enclosing > global
6. **Memory efficient** - stores references, not copies

### When to Use ChainMap
- ✅ Layered configuration systems
- ✅ Scope/namespace management
- ✅ Template variable resolution
- ✅ Plugin systems with override capability
- ✅ When you need to preserve original dicts
- ✅ Read-heavy workloads with fallback values

### When NOT to Use ChainMap
- ❌ Need to merge dicts into single copy
- ❌ Need equal priority for all mappings
- ❌ Write-heavy workloads (first mapping only)
- ❌ Need to modify all underlying mappings
- ❌ Performance critical (O(n) lookup)

---

## SEE ALSO
- [[DICTIONARY_METHODS]] - Standard dict operations
- [[COLLECTIONS_MODULE]] - Other collection types
- [[MAPPING_PROTOCOL]] - Abstract mapping interface
- [[CONTEXT_MANAGERS]] - For scope management patterns
