---
type: function
name: filter_traces
module: tracemalloc
lineno: 452
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: filter_traces()

## Overview

Create a new Snapshot instance with a filtered traces sequence, filters
is a list of Filter or DomainFilter instances.  If filters is an empty
list, return a new Snapshot instance with a copy of the traces.

```python
def filter_traces(self, filters)
```

**Module:** [[Modules/tracemalloc|tracemalloc]]
**Class:** [[Classes/Snapshot|Snapshot]]
**Type:** Method
**Line:** 452

## Categories

- [[Taxonomy/public_method|public_method]]
