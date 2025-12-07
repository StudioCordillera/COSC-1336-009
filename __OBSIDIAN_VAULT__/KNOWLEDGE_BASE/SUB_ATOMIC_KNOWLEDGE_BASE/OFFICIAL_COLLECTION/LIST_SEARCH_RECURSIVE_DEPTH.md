t # LIST_SEARCH_RECURSIVE_DEPTH

## Core Definition
**Recursive depth searching** in nested list structures enables traversal through multiple levels of list-of-list pairs to locate, validate, and extract values at specific depths. Essential for key-value pair navigation in nested data structures.

**Tags**: #list #nested #recursive #search #depth #key-value #traversal #validation

---

## NESTED LIST STRUCTURE PATTERNS

### Common List-of-List Pair Formats

```python
# ═══════════════════════════════════════════════════════════════════════════
# DEPTH 1: SIMPLE KEY-VALUE PAIRS
# ═══════════════════════════════════════════════════════════════════════════
# Format: [[key, value], [key, value], ...]
simple_pairs = [[0, 45], [1, 87], [2, 32], [3, 46]]
# Access: pairs[index][0] = key, pairs[index][1] = value

# ═══════════════════════════════════════════════════════════════════════════
# DEPTH 2: NESTED PAIR STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════
# Format: [[key, [subkey, value]], ...]
nested_pairs = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
# Access: nested[index][0] = key, nested[index][1][0] = subkey, nested[index][1][1] = value

# ═══════════════════════════════════════════════════════════════════════════
# DEPTH 3: MULTI-LEVEL NESTING
# ═══════════════════════════════════════════════════════════════════════════
# Format: [[key, [subkey, [subsubkey, value]]], ...]
deep_nested = [[0, [0, [0, 45]]], [1, [1, [1, 87]]]]
# Access requires multiple depth traversals

# ═══════════════════════════════════════════════════════════════════════════
# MIXED DEPTH STRUCTURES (VARIABLE DEPTH)
# ═══════════════════════════════════════════════════════════════════════════
mixed = [
    [0, 45],              # Depth 1
    [1, [1, 87]],         # Depth 2
    [2, [2, [2, 32]]],    # Depth 3
]
```

---

## SEARCH VALIDATION METHODS QUICK REFERENCE

### VALIDATION METHODS - Target | Operation | Output

```python
# ═══════════════════════════════════════════════════════════════════════════
# EXISTENCE VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
key in [pair[0] for pair in pairs]     # List pairs | Check key exists | Returns True/False
any(pair[0] == key for pair in pairs)  # List pairs | Find key match | Returns True/False
all(isinstance(p, list) for p in data) # List | Validate all pairs | Returns True/False
len(pair) >= 2                         # Single pair | Check pair structure | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# TYPE VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
isinstance(data, list)                 # Data | Check if list | Returns True/False
isinstance(data[i], list)              # Element | Check if nested list | Returns True/False
type(data) == list                     # Data | Exact type check | Returns True/False
hasattr(data, '__iter__')              # Data | Check iterable | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# STRUCTURE VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
len(pair) == 2                         # Pair | Validate pair format | Returns True/False
0 <= index < len(pairs)                # Index | Validate bounds | Returns True/False
isinstance(pair[0], (int, str))        # Key | Validate key type | Returns True/False
isinstance(pair[1], (int, str, list))  # Value | Validate value type | Returns True/False

# ═══════════════════════════════════════════════════════════════════════════
# DEPTH VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
get_depth(data)                        # List | Calculate max depth | Returns int depth
is_at_depth(data, target_depth)        # List + depth | Check depth level | Returns True/False
validate_depth_range(data, min, max)   # List + range | Check depth bounds | Returns True/False
```

---

## DETAILED SEARCH OPERATIONS

### 1. BASIC KEY-VALUE SEARCH (DEPTH 1)

```python
# Simple list of pairs: [[key, value], ...]
L2 = [[0, 45], [1, 87], [2, 32], [3, 46], [4, 45]]

# ═══════════════════════════════════════════════════════════════════════════
# METHOD 1: LINEAR SEARCH WITH VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
def search_by_key(pairs, target_key):
    """
    Search for value by key with validation
    
    Args:
        pairs: List of [key, value] pairs
        target_key: Key to search for
    
    Returns:
        Value if found, None otherwise
    """
    # Validate input
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list")
    
    for pair in pairs:
        # Validate pair structure
        if not isinstance(pair, list) or len(pair) != 2:
            continue  # Skip invalid pairs
        
        key, value = pair
        if key == target_key:
            return value
    
    return None  # Key not found

# Usage
result = search_by_key(L2, 2)  # → 32
result = search_by_key(L2, 99)  # → None


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 2: INDEX-BASED SEARCH
# ═══════════════════════════════════════════════════════════════════════════
def search_by_index(pairs, index):
    """
    Search by index position with bounds checking
    
    Args:
        pairs: List of [key, value] pairs
        index: Index to access
    
    Returns:
        [key, value] pair if valid, None otherwise
    """
    # Validate bounds
    if not (0 <= index < len(pairs)):
        return None
    
    # Validate pair structure
    pair = pairs[index]
    if isinstance(pair, list) and len(pair) >= 2:
        return pair
    
    return None

# Usage
result = search_by_index(L2, 2)  # → [2, 32]
result = search_by_index(L2, 99)  # → None


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 3: FIND ALL MATCHING KEYS
# ═══════════════════════════════════════════════════════════════════════════
def find_all_by_key(pairs, target_key):
    """
    Find all values for a given key (handles duplicate keys)
    
    Args:
        pairs: List of [key, value] pairs
        target_key: Key to search for
    
    Returns:
        List of all matching values
    """
    matches = []
    
    for pair in pairs:
        if isinstance(pair, list) and len(pair) >= 2:
            if pair[0] == target_key:
                matches.append(pair[1])
    
    return matches

# Usage with duplicate keys
L2_dups = [[0, 45], [1, 87], [0, 32], [0, 46]]
result = find_all_by_key(L2_dups, 0)  # → [45, 32, 46]


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 4: SAFE VALUE EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════
def safe_get_value(pairs, key, default=None):
    """
    Safely get value with default fallback
    
    Args:
        pairs: List of [key, value] pairs
        key: Key to search for
        default: Default value if not found
    
    Returns:
        Value if found, default otherwise
    """
    try:
        for pair in pairs:
            if pair[0] == key:
                return pair[1]
    except (IndexError, TypeError):
        pass  # Handle malformed data
    
    return default

# Usage
result = safe_get_value(L2, 2)  # → 32
result = safe_get_value(L2, 99, "NOT_FOUND")  # → "NOT_FOUND"
```

### 2. NESTED SEARCH (DEPTH 2)

```python
# Nested pairs: [[key, [subkey, value]], ...]
L3 = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]], [3, [3, 46]]]

# ═══════════════════════════════════════════════════════════════════════════
# METHOD 1: TWO-LEVEL SEARCH WITH VALIDATION
# ═══════════════════════════════════════════════════════════════════════════
def search_depth2(pairs, target_key):
    """
    Search nested pairs at depth 2
    
    Args:
        pairs: List of [key, [subkey, value]] pairs
        target_key: Key to search for
    
    Returns:
        [subkey, value] pair if found, None otherwise
    """
    # Validate input
    if not isinstance(pairs, list):
        raise TypeError("Input must be a list")
    
    for pair in pairs:
        # Validate depth 1 structure
        if not isinstance(pair, list) or len(pair) != 2:
            continue
        
        key, nested = pair
        
        # Validate depth 2 structure
        if not isinstance(nested, list) or len(nested) != 2:
            continue
        
        if key == target_key:
            return nested  # Returns [subkey, value]
    
    return None

# Usage
result = search_depth2(L3, 2)  # → [2, 32]
if result:
    subkey, value = result
    print(f"Subkey: {subkey}, Value: {value}")


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 2: EXTRACT DEPTH 2 VALUE DIRECTLY
# ═══════════════════════════════════════════════════════════════════════════
def get_depth2_value(pairs, target_key):
    """
    Get value directly from depth 2 structure
    
    Args:
        pairs: List of [key, [subkey, value]] pairs
        target_key: Key to search for
    
    Returns:
        Value at depth 2, None otherwise
    """
    for pair in pairs:
        try:
            if pair[0] == target_key:
                # Access: pair[1][1] = nested[1] = value
                return pair[1][1]
        except (IndexError, TypeError):
            continue  # Skip malformed pairs
    
    return None

# Usage
value = get_depth2_value(L3, 2)  # → 32


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 3: EXTRACT BOTH SUBKEY AND VALUE
# ═══════════════════════════════════════════════════════════════════════════
def get_depth2_pair(pairs, target_key):
    """
    Get both subkey and value from depth 2
    
    Args:
        pairs: List of [key, [subkey, value]] pairs
        target_key: Key to search for
    
    Returns:
        Tuple (subkey, value) if found, (None, None) otherwise
    """
    for pair in pairs:
        try:
            if pair[0] == target_key and isinstance(pair[1], list):
                subkey, value = pair[1][0], pair[1][1]
                return (subkey, value)
        except (IndexError, TypeError, ValueError):
            continue
    
    return (None, None)

# Usage
subkey, value = get_depth2_pair(L3, 2)  # → (2, 32)


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 4: VALIDATE AND SEARCH WITH TYPE CHECKING
# ═══════════════════════════════════════════════════════════════════════════
def validated_depth2_search(pairs, target_key, expected_type=None):
    """
    Search with structure and type validation
    
    Args:
        pairs: List of [key, [subkey, value]] pairs
        target_key: Key to search for
        expected_type: Expected type of value (optional)
    
    Returns:
        Value if found and valid, None otherwise
    """
    if not isinstance(pairs, list):
        return None
    
    for pair in pairs:
        # Validate structure at each level
        if not isinstance(pair, list) or len(pair) < 2:
            continue
        
        key, nested = pair[0], pair[1]
        
        if key != target_key:
            continue
        
        # Validate nested structure
        if not isinstance(nested, list) or len(nested) < 2:
            continue
        
        value = nested[1]
        
        # Optional type validation
        if expected_type is not None:
            if isinstance(value, expected_type):
                return value
        else:
            return value
    
    return None

# Usage
value = validated_depth2_search(L3, 2, int)  # → 32 (type-validated)
value = validated_depth2_search(L3, 2, str)  # → None (type mismatch)
```

### 3. RECURSIVE DEPTH SEARCH (VARIABLE DEPTH)

```python
# ═══════════════════════════════════════════════════════════════════════════
# METHOD 1: CALCULATE MAXIMUM DEPTH
# ═══════════════════════════════════════════════════════════════════════════
def get_max_depth(data):
    """
    Calculate maximum nesting depth of list structure
    
    Args:
        data: Nested list structure
    
    Returns:
        Maximum depth as integer
    """
    if not isinstance(data, list):
        return 0
    
    if not data:  # Empty list
        return 1
    
    max_sub_depth = 0
    for item in data:
        if isinstance(item, list):
            sub_depth = get_max_depth(item)
            max_sub_depth = max(max_sub_depth, sub_depth)
    
    return 1 + max_sub_depth

# Usage
simple = [[0, 45], [1, 87]]
nested = [[0, [0, 45]], [1, [1, 87]]]
deep = [[0, [0, [0, 45]]], [1, [1, [1, 87]]]]

print(get_max_depth(simple))   # → 2
print(get_max_depth(nested))   # → 3
print(get_max_depth(deep))     # → 4


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 2: RECURSIVE VALUE SEARCH AT TARGET DEPTH
# ═══════════════════════════════════════════════════════════════════════════
def search_at_depth(data, target_key, target_depth, current_depth=0):
    """
    Search for key at specific depth level
    
    Args:
        data: Nested list structure
        target_key: Key to search for
        target_depth: Depth level to search at
        current_depth: Current recursion depth (internal)
    
    Returns:
        Value at target depth if found, None otherwise
    """
    if not isinstance(data, list):
        return None
    
    # At target depth, search for key
    if current_depth == target_depth:
        for pair in data:
            if isinstance(pair, list) and len(pair) >= 2:
                if pair[0] == target_key:
                    return pair[1]
        return None
    
    # Recurse deeper
    for item in data:
        if isinstance(item, list):
            result = search_at_depth(item, target_key, target_depth, current_depth + 1)
            if result is not None:
                return result
    
    return None

# Usage
nested_data = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
value = search_at_depth(nested_data, 2, depth=1)  # Search at depth 1
# → [2, 32]


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 3: EXTRACT VALUE FROM SPECIFIC DEPTH PATH
# ═══════════════════════════════════════════════════════════════════════════
def extract_by_path(data, *indices):
    """
    Extract value by navigating through index path
    
    Args:
        data: Nested list structure
        *indices: Variable number of indices to traverse
    
    Returns:
        Value at path, None if invalid path
    """
    current = data
    
    for idx in indices:
        try:
            if isinstance(current, list) and 0 <= idx < len(current):
                current = current[idx]
            else:
                return None
        except (IndexError, TypeError):
            return None
    
    return current

# Usage
# For L3 = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
# Extract: L3[2][1][1] = 32
value = extract_by_path(L3, 2, 1, 1)  # → 32
value = extract_by_path(L3, 1, 1, 0)  # → 1 (subkey)


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 4: FIND ALL VALUES AT SPECIFIC DEPTH
# ═══════════════════════════════════════════════════════════════════════════
def find_all_at_depth(data, target_depth, current_depth=0):
    """
    Find all values at a specific depth level
    
    Args:
        data: Nested list structure
        target_depth: Depth level to extract from
        current_depth: Current recursion depth (internal)
    
    Returns:
        List of all values at target depth
    """
    if not isinstance(data, list):
        return []
    
    results = []
    
    # At target depth, collect all items
    if current_depth == target_depth:
        return [item for item in data if not isinstance(item, list)]
    
    # Recurse into nested lists
    for item in data:
        if isinstance(item, list):
            results.extend(find_all_at_depth(item, target_depth, current_depth + 1))
    
    return results

# Usage
nested = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
values = find_all_at_depth(nested, depth=2)  # Get all at depth 2
# → [0, 45, 1, 87, 2, 32]


# ═══════════════════════════════════════════════════════════════════════════
# METHOD 5: RECURSIVE SEARCH WITH PATH TRACKING
# ═══════════════════════════════════════════════════════════════════════════
def search_with_path(data, target_value, path=[]):
    """
    Search for value and return the path to it
    
    Args:
        data: Nested list structure
        target_value: Value to search for
        path: Current path (internal, don't pass)
    
    Returns:
        List of indices representing path to value, None if not found
    """
    if data == target_value:
        return path
    
    if isinstance(data, list):
        for i, item in enumerate(data):
            result = search_with_path(item, target_value, path + [i])
            if result is not None:
                return result
    
    return None

# Usage
nested = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
path = search_with_path(nested, 32)  # → [2, 1, 1]
# This means: nested[2][1][1] = 32
```

### 4. ADVANCED SEARCH PATTERNS

```python
# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 1: BINARY SEARCH ON SORTED KEY-VALUE PAIRS
# ═══════════════════════════════════════════════════════════════════════════
def binary_search_pairs(pairs, target_key):
    """
    Binary search on sorted list of [key, value] pairs
    Requires pairs to be sorted by key
    
    Args:
        pairs: Sorted list of [key, value] pairs
        target_key: Key to search for
    
    Returns:
        Value if found, None otherwise
    
    Time Complexity: O(log n)
    """
    left, right = 0, len(pairs) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Validate pair structure
        if not isinstance(pairs[mid], list) or len(pairs[mid]) < 2:
            return None
        
        mid_key = pairs[mid][0]
        
        if mid_key == target_key:
            return pairs[mid][1]
        elif mid_key < target_key:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

# Usage
sorted_pairs = [[0, 10], [1, 20], [2, 30], [3, 40], [4, 50]]
value = binary_search_pairs(sorted_pairs, 3)  # → 40


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 2: BUILD INDEX FOR FAST LOOKUP
# ═══════════════════════════════════════════════════════════════════════════
class IndexedPairs:
    """
    Index structure for fast O(1) lookup
    Useful when doing many searches on same data
    """
    def __init__(self, pairs):
        """Build index from list of pairs"""
        self.index = {}
        self.pairs = pairs
        
        for i, pair in enumerate(pairs):
            if isinstance(pair, list) and len(pair) >= 2:
                key = pair[0]
                # Store index for lookup
                if key not in self.index:
                    self.index[key] = []
                self.index[key].append(i)
    
    def search(self, key):
        """Search by key with O(1) average time"""
        if key in self.index:
            indices = self.index[key]
            # Return first match
            return self.pairs[indices[0]][1]
        return None
    
    def search_all(self, key):
        """Get all values for key"""
        if key in self.index:
            return [self.pairs[i][1] for i in self.index[key]]
        return []
    
    def exists(self, key):
        """Check if key exists"""
        return key in self.index

# Usage
pairs = [[0, 45], [1, 87], [2, 32], [0, 99]]  # Duplicate key 0
indexed = IndexedPairs(pairs)
value = indexed.search(0)      # → 45 (first match)
all_vals = indexed.search_all(0)  # → [45, 99] (all matches)
exists = indexed.exists(2)     # → True


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 3: DEPTH-LIMITED SEARCH WITH CALLBACK
# ═══════════════════════════════════════════════════════════════════════════
def search_with_callback(data, callback, max_depth=None, current_depth=0):
    """
    Search with custom callback function and depth limit
    
    Args:
        data: Nested list structure
        callback: Function(item, depth) -> bool (return True to collect)
        max_depth: Maximum depth to search (None = unlimited)
        current_depth: Current depth (internal)
    
    Returns:
        List of items matching callback condition
    """
    results = []
    
    # Check depth limit
    if max_depth is not None and current_depth > max_depth:
        return results
    
    if not isinstance(data, list):
        if callback(data, current_depth):
            results.append(data)
        return results
    
    for item in data:
        if isinstance(item, list):
            # Recurse into nested lists
            results.extend(search_with_callback(item, callback, max_depth, current_depth + 1))
        else:
            # Check callback condition
            if callback(item, current_depth):
                results.append(item)
    
    return results

# Usage
nested = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]

# Find all values > 50 at any depth
results = search_with_callback(nested, lambda x, d: isinstance(x, int) and x > 50)
# → [87]

# Find all items at depth 2
results = search_with_callback(nested, lambda x, d: d == 2)
# → [0, 45, 1, 87, 2, 32]

# Find items at depth 2 or less
results = search_with_callback(nested, lambda x, d: d <= 2, max_depth=2)


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 4: BREADTH-FIRST SEARCH (BFS) FOR LEVEL-ORDER TRAVERSAL
# ═══════════════════════════════════════════════════════════════════════════
from collections import deque

def bfs_search(data, target_key):
    """
    Breadth-first search through nested structure
    Finds shallowest occurrence of key
    
    Args:
        data: Nested list structure
        target_key: Key to search for
    
    Returns:
        (value, depth) tuple if found, (None, -1) otherwise
    """
    if not isinstance(data, list):
        return (None, -1)
    
    # Queue stores (item, depth)
    queue = deque([(data, 0)])
    
    while queue:
        current, depth = queue.popleft()
        
        if isinstance(current, list):
            # Check if this is a key-value pair
            if len(current) == 2 and current[0] == target_key:
                return (current[1], depth)
            
            # Add children to queue
            for item in current:
                queue.append((item, depth + 1))
    
    return (None, -1)

# Usage
nested = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
value, depth = bfs_search(nested, 2)  # → (32, depth_level)


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN 5: DEPTH-FIRST SEARCH (DFS) WITH EARLY TERMINATION
# ═══════════════════════════════════════════════════════════════════════════
def dfs_search_first(data, predicate, visited=None):
    """
    Depth-first search with early termination
    Stops at first match
    
    Args:
        data: Nested list structure
        predicate: Function(item) -> bool
        visited: Set of visited items (internal)
    
    Returns:
        First matching item, None if not found
    """
    if visited is None:
        visited = set()
    
    # Avoid infinite loops on circular references
    data_id = id(data)
    if data_id in visited:
        return None
    visited.add(data_id)
    
    # Check current item
    if predicate(data):
        return data
    
    # Recurse if list
    if isinstance(data, list):
        for item in data:
            result = dfs_search_first(item, predicate, visited)
            if result is not None:
                return result  # Early termination
    
    return None

# Usage
nested = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]

# Find first value > 50
result = dfs_search_first(nested, lambda x: isinstance(x, int) and x > 50)
# → 87

# Find first list with length 2
result = dfs_search_first(nested, lambda x: isinstance(x, list) and len(x) == 2)
```

### 5. VALIDATION AND ERROR HANDLING

```python
# ═══════════════════════════════════════════════════════════════════════════
# COMPREHENSIVE VALIDATION CLASS
# ═══════════════════════════════════════════════════════════════════════════
class PairValidator:
    """Comprehensive validation for list pair structures"""
    
    @staticmethod
    def is_valid_pair(pair):
        """Check if item is valid [key, value] pair"""
        return isinstance(pair, list) and len(pair) >= 2
    
    @staticmethod
    def is_valid_nested_pair(pair, depth=2):
        """Validate nested pair structure to specific depth"""
        if not isinstance(pair, list) or len(pair) < 2:
            return False
        
        if depth == 1:
            return True
        
        # Check nested structure
        return PairValidator.is_valid_nested_pair(pair[1], depth - 1)
    
    @staticmethod
    def validate_structure(data, expected_depth=None):
        """
        Validate entire structure
        
        Returns:
            (is_valid, errors) tuple
        """
        errors = []
        
        if not isinstance(data, list):
            errors.append("Root must be a list")
            return (False, errors)
        
        if not data:
            errors.append("Empty list")
            return (False, errors)
        
        for i, item in enumerate(data):
            if not isinstance(item, list):
                errors.append(f"Item {i} is not a list")
                continue
            
            if len(item) < 2:
                errors.append(f"Item {i} has fewer than 2 elements")
        
        # Check depth if specified
        if expected_depth is not None:
            actual_depth = get_max_depth(data)
            if actual_depth != expected_depth:
                errors.append(f"Expected depth {expected_depth}, got {actual_depth}")
        
        return (len(errors) == 0, errors)
    
    @staticmethod
    def validate_keys(data, key_type=None, unique=False):
        """
        Validate keys in pair structure
        
        Args:
            data: List of pairs
            key_type: Expected type for keys (None = any)
            unique: Whether keys must be unique
        
        Returns:
            (is_valid, errors) tuple
        """
        errors = []
        seen_keys = set()
        
        for i, pair in enumerate(data):
            if not isinstance(pair, list) or len(pair) < 2:
                errors.append(f"Invalid pair at index {i}")
                continue
            
            key = pair[0]
            
            # Check key type
            if key_type is not None and not isinstance(key, key_type):
                errors.append(f"Key at index {i} has wrong type: {type(key)}, expected {key_type}")
            
            # Check uniqueness
            if unique:
                if key in seen_keys:
                    errors.append(f"Duplicate key: {key} at index {i}")
                seen_keys.add(key)
        
        return (len(errors) == 0, errors)

# Usage
validator = PairValidator()

# Validate basic structure
pairs = [[0, 45], [1, 87], [2, 32]]
is_valid, errors = validator.validate_structure(pairs)
print(f"Valid: {is_valid}, Errors: {errors}")

# Validate key types and uniqueness
is_valid, errors = validator.validate_keys(pairs, key_type=int, unique=True)

# Validate nested structure
nested = [[0, [0, 45]], [1, [1, 87]]]
is_valid = validator.is_valid_nested_pair(nested[0], depth=2)


# ═══════════════════════════════════════════════════════════════════════════
# SAFE SEARCH WITH EXCEPTION HANDLING
# ═══════════════════════════════════════════════════════════════════════════
class SearchError(Exception):
    """Custom exception for search errors"""
    pass

def safe_depth_search(data, target_key, depth, strict=False):
    """
    Safe search with comprehensive error handling
    
    Args:
        data: Nested list structure
        target_key: Key to search for
        depth: Expected depth of structure
        strict: If True, raise exceptions; if False, return None
    
    Returns:
        Value if found, None otherwise
    
    Raises:
        SearchError: If strict=True and validation fails
    """
    try:
        # Validate input type
        if not isinstance(data, list):
            if strict:
                raise SearchError("Data must be a list")
            return None
        
        # Validate depth
        actual_depth = get_max_depth(data)
        if actual_depth < depth:
            if strict:
                raise SearchError(f"Insufficient depth: {actual_depth} < {depth}")
            return None
        
        # Perform search based on depth
        if depth == 1:
            for pair in data:
                if isinstance(pair, list) and len(pair) >= 2:
                    if pair[0] == target_key:
                        return pair[1]
        
        elif depth == 2:
            for pair in data:
                if isinstance(pair, list) and len(pair) >= 2:
                    if pair[0] == target_key:
                        nested = pair[1]
                        if isinstance(nested, list) and len(nested) >= 2:
                            return nested[1]
        
        else:
            # Recursive search for depth > 2
            return search_at_depth(data, target_key, depth - 1)
        
        return None
    
    except (IndexError, TypeError) as e:
        if strict:
            raise SearchError(f"Search failed: {str(e)}")
        return None

# Usage
pairs = [[0, 45], [1, 87], [2, 32]]

# Non-strict mode (returns None on error)
value = safe_depth_search(pairs, 2, depth=1, strict=False)  # → 32
value = safe_depth_search("invalid", 2, depth=1, strict=False)  # → None

# Strict mode (raises exceptions)
try:
    value = safe_depth_search("invalid", 2, depth=1, strict=True)
except SearchError as e:
    print(f"Error: {e}")
```

---

## PERFORMANCE OPTIMIZATION PATTERNS

### Time Complexity Comparison

```python
# ═══════════════════════════════════════════════════════════════════════════
# OPERATION COMPLEXITY ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

"""
SEARCH OPERATION TIME COMPLEXITIES:

1. Linear Search (Unordered)
   - Time: O(n) where n = number of pairs
   - Space: O(1)
   - Use when: Small datasets, unsorted data

2. Binary Search (Sorted)
   - Time: O(log n)
   - Space: O(1)
   - Use when: Large sorted datasets, multiple searches

3. Indexed Search (Hash-based)
   - Build Index: O(n)
   - Search: O(1) average
   - Space: O(n)
   - Use when: Many searches on same data

4. Recursive Depth Search
   - Time: O(n * d) where d = average depth
   - Space: O(d) stack space
   - Use when: Unknown or variable depth

5. BFS (Breadth-First)
   - Time: O(n) visits all nodes
   - Space: O(w) where w = max width
   - Use when: Need shallowest result

6. DFS (Depth-First)
   - Time: O(n) visits all nodes
   - Space: O(h) where h = max height
   - Use when: Deep structures, early termination
"""


# ═══════════════════════════════════════════════════════════════════════════
# OPTIMIZATION: CACHING FOR REPEATED SEARCHES
# ═══════════════════════════════════════════════════════════════════════════
from functools import lru_cache

class CachedSearch:
    """Cache search results for repeated queries"""
    
    def __init__(self, pairs):
        self.pairs = tuple(tuple(p) if isinstance(p, list) else p for p in pairs)
        self._cache = {}
    
    @lru_cache(maxsize=128)
    def search(self, key):
        """Cached search with LRU eviction"""
        for pair in self.pairs:
            if pair[0] == key:
                return pair[1]
        return None
    
    def clear_cache(self):
        """Clear search cache"""
        self.search.cache_clear()

# Usage
pairs = [[i, i**2] for i in range(1000)]
cached = CachedSearch(pairs)

# First search: O(n)
value1 = cached.search(500)

# Subsequent searches for same key: O(1)
value2 = cached.search(500)  # Retrieved from cache


# ═══════════════════════════════════════════════════════════════════════════
# OPTIMIZATION: LAZY EVALUATION WITH GENERATORS
# ═══════════════════════════════════════════════════════════════════════════
def lazy_search_generator(pairs, target_key):
    """
    Generator-based search for memory efficiency
    Yields matches as found (lazy evaluation)
    """
    for pair in pairs:
        if isinstance(pair, list) and len(pair) >= 2:
            if pair[0] == target_key:
                yield pair[1]

# Usage - processes one item at a time
pairs = [[i % 10, i] for i in range(10000)]  # Many duplicate keys
matches = lazy_search_generator(pairs, 5)

# Get first match without processing entire list
first_match = next(matches, None)

# Get all matches (if needed)
all_matches = list(lazy_search_generator(pairs, 5))


# ═══════════════════════════════════════════════════════════════════════════
# OPTIMIZATION: PARALLEL SEARCH FOR LARGE DATASETS
# ═══════════════════════════════════════════════════════════════════════════
from concurrent.futures import ThreadPoolExecutor
import math

def parallel_search(pairs, target_key, num_workers=4):
    """
    Parallel search across multiple threads
    Useful for very large datasets
    """
    chunk_size = math.ceil(len(pairs) / num_workers)
    chunks = [pairs[i:i+chunk_size] for i in range(0, len(pairs), chunk_size)]
    
    def search_chunk(chunk):
        for pair in chunk:
            if isinstance(pair, list) and len(pair) >= 2:
                if pair[0] == target_key:
                    return pair[1]
        return None
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(search_chunk, chunk) for chunk in chunks]
        
        for future in futures:
            result = future.result()
            if result is not None:
                return result
    
    return None

# Usage - beneficial for datasets > 10,000 items
large_pairs = [[i, i**2] for i in range(100000)]
value = parallel_search(large_pairs, 50000, num_workers=8)
```

---

## PRACTICAL USAGE PATTERNS

### Pattern 1: Building Sorted List Index Map
```python
# Mapping place values to actual values for sorting
L1 = [45, 87, 32, 46, 45, 2, 77, 82]
L2 = []  # Key-value pairs: [[index, value], ...]

# Build index map
for i in range(len(L1)):
    L2.append([i, L1[i]])

# L2 now: [[0, 45], [1, 87], [2, 32], [3, 46], [4, 45], [5, 2], [6, 77], [7, 82]]

# Search by original index
def get_by_index(pairs, index):
    for pair in pairs:
        if pair[0] == index:
            return pair[1]
    return None

original_value = get_by_index(L2, 3)  # → 46

# Sort by values while maintaining key relationship
L2_sorted = sorted(L2, key=lambda x: x[1])
# [[5, 2], [2, 32], [0, 45], [4, 45], [3, 46], [6, 77], [7, 82], [1, 87]]
```

### Pattern 2: Multi-Level Sorting State Tracking
```python
# Track sorting states with nested pairs
# Format: [[original_index, [sorted_position, value]], ...]

def build_sorting_map(original_list):
    """
    Build nested map for sorting algorithm tracking
    
    Returns:
        List of [original_index, [current_position, value]]
    """
    mapping = []
    
    for original_idx, value in enumerate(original_list):
        mapping.append([original_idx, [original_idx, value]])
    
    return mapping

# Usage
L1 = [45, 87, 32, 46]
sort_map = build_sorting_map(L1)
# [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]], [3, [3, 46]]]

# Track movement during sort
def update_position(sort_map, original_idx, new_position):
    """Update sorted position for an element"""
    for pair in sort_map:
        if pair[0] == original_idx:
            pair[1][0] = new_position
            return True
    return False

# Simulate moving element
update_position(sort_map, 2, 0)  # Move index 2 to position 0
# [[0, [0, 45]], [1, [1, 87]], [2, [0, 32]], [3, [3, 46]]]
```

### Pattern 3: Validation State Machine
```python
class SearchValidator:
    """State machine for validated searching"""
    
    def __init__(self, data):
        self.data = data
        self.state = "INIT"
        self.errors = []
    
    def validate_structure(self):
        """Validate data structure"""
        if not isinstance(self.data, list):
            self.errors.append("Data must be list")
            self.state = "ERROR"
            return False
        
        self.state = "VALIDATED"
        return True
    
    def search(self, key, depth=1):
        """Search with state validation"""
        if self.state == "ERROR":
            return None
        
        if self.state == "INIT":
            if not self.validate_structure():
                return None
        
        # Perform search based on depth
        if depth == 1:
            return self._search_depth1(key)
        elif depth == 2:
            return self._search_depth2(key)
        else:
            return None
    
    def _search_depth1(self, key):
        """Search at depth 1"""
        for pair in self.data:
            if isinstance(pair, list) and len(pair) >= 2:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def _search_depth2(self, key):
        """Search at depth 2"""
        for pair in self.data:
            if isinstance(pair, list) and len(pair) >= 2:
                if pair[0] == key and isinstance(pair[1], list):
                    if len(pair[1]) >= 2:
                        return pair[1][1]
        return None

# Usage
data = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]
validator = SearchValidator(data)
value = validator.search(2, depth=2)  # → 32
```

---

## COMPLETE EXAMPLE: SORTING CLASS INTEGRATION

```python
class SortingWithSearch:
    """
    Complete sorting implementation with depth-2 search
    Integrates all validation and search patterns
    """
    
    def __init__(self, original_list):
        """
        Initialize with original list
        
        Args:
            original_list: List of values to sort
        """
        self.L1 = original_list  # Original unsorted list
        self.L2 = []  # Key-value pairs: [[index, [sorted_key, value]], ...]
        self.L3 = []  # Keys remaining to sort
        self.L4 = []  # Sorted keys
        
        self._initialize()
    
    def _initialize(self):
        """Build initial nested structure"""
        for i in range(len(self.L1)):
            # Format: [original_index, [current_position, value]]
            self.L2.append([i, [i, self.L1[i]]])
            self.L3.append(i)  # All keys start unsorted
    
    def search_by_original_index(self, index):
        """
        Search L2 by original index (depth 1 key)
        
        Args:
            index: Original index to search for
        
        Returns:
            [current_position, value] if found, None otherwise
        """
        for pair in self.L2:
            if pair[0] == index:
                return pair[1]  # Returns nested pair
        return None
    
    def get_value_by_index(self, index):
        """
        Get value from depth 2 structure
        
        Args:
            index: Original index
        
        Returns:
            Value at depth 2
        """
        nested = self.search_by_original_index(index)
        if nested and isinstance(nested, list) and len(nested) >= 2:
            return nested[1]  # Extract value
        return None
    
    def get_position_by_index(self, index):
        """
        Get current sorted position
        
        Args:
            index: Original index
        
        Returns:
            Current position in sort
        """
        nested = self.search_by_original_index(index)
        if nested and isinstance(nested, list) and len(nested) >= 2:
            return nested[0]  # Extract position
        return None
    
    def update_position(self, index, new_position):
        """
        Update sorted position for element
        
        Args:
            index: Original index
            new_position: New sorted position
        
        Returns:
            True if updated, False otherwise
        """
        for pair in self.L2:
            if pair[0] == index:
                if isinstance(pair[1], list) and len(pair[1]) >= 2:
                    pair[1][0] = new_position
                    return True
        return False
    
    def compare_values(self, index1, index2):
        """
        Compare values of two indices
        
        Args:
            index1: First index
            index2: Second index
        
        Returns:
            -1 if val1 < val2, 0 if equal, 1 if val1 > val2
        """
        val1 = self.get_value_by_index(index1)
        val2 = self.get_value_by_index(index2)
        
        if val1 is None or val2 is None:
            return 0
        
        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:
            return 0
    
    def validate_structure(self):
        """
        Validate L2 structure
        
        Returns:
            (is_valid, errors) tuple
        """
        errors = []
        
        # Check L2 format
        for i, pair in enumerate(self.L2):
            if not isinstance(pair, list) or len(pair) != 2:
                errors.append(f"L2[{i}] invalid structure")
                continue
            
            nested = pair[1]
            if not isinstance(nested, list) or len(nested) != 2:
                errors.append(f"L2[{i}][1] invalid nested structure")
        
        return (len(errors) == 0, errors)
    
    def get_sorted_values(self):
        """
        Get values in sorted order based on current positions
        
        Returns:
            List of values in sorted order
        """
        # Build list of (position, value) tuples
        items = []
        for pair in self.L2:
            if isinstance(pair[1], list) and len(pair[1]) >= 2:
                position, value = pair[1][0], pair[1][1]
                items.append((position, value))
        
        # Sort by position and extract values
        items.sort(key=lambda x: x[0])
        return [value for pos, value in items]

# Usage Example
L1 = [45, 87, 32, 46, 45, 2, 77, 82]
sorter = SortingWithSearch(L1)

# Search operations
value = sorter.get_value_by_index(2)  # → 32
position = sorter.get_position_by_index(2)  # → 2

# Comparison
result = sorter.compare_values(0, 2)  # Compare L1[0] vs L1[2]: 45 vs 32 → 1

# Update positions (simulate sorting)
sorter.update_position(2, 0)  # Move index 2 to position 0
sorter.update_position(0, 1)  # Move index 0 to position 1

# Validate
is_valid, errors = sorter.validate_structure()
print(f"Valid: {is_valid}")

# Get sorted result
sorted_values = sorter.get_sorted_values()
```

---

## SUMMARY CHEAT SHEET

```python
# ═══════════════════════════════════════════════════════════════════════════
# QUICK REFERENCE - SEARCH AT DEPTH 2
# ═══════════════════════════════════════════════════════════════════════════

# Structure: [[key, [subkey, value]], ...]
nested_pairs = [[0, [0, 45]], [1, [1, 87]], [2, [2, 32]]]

# DIRECT ACCESS (fastest, no validation)
value = nested_pairs[2][1][1]  # → 32

# SAFE SEARCH (with validation)
def safe_get(pairs, key):
    for pair in pairs:
        if isinstance(pair, list) and len(pair) >= 2 and pair[0] == key:
            nested = pair[1]
            if isinstance(nested, list) and len(nested) >= 2:
                return nested[1]
    return None

value = safe_get(nested_pairs, 2)  # → 32

# INDEX-BASED (O(1) with preprocessing)
index = {pair[0]: pair[1][1] for pair in nested_pairs if isinstance(pair, list) and len(pair) >= 2}
value = index.get(2)  # → 32

# RECURSIVE (variable depth)
def recursive_get(data, key, depth=0, target_depth=1):
    if depth == target_depth:
        for pair in data:
            if isinstance(pair, list) and pair[0] == key:
                return pair[1]
    return None
```

---

**Key Takeaways**:
1. Always validate structure before accessing nested elements
2. Use indexing for repeated searches (O(1) vs O(n))
3. Choose BFS for shallowest results, DFS for deep searches
4. Implement error handling for malformed data
5. Consider caching for repeated queries on same dataset
6. Use generators for memory-efficient searches
7. Depth-first recursive search for variable depth structures

**Reference**: For integration with sorting algorithms, see `sortingClass.py` implementation patterns

**Last Updated**: December 6, 2025
