---
type: function
name: isgenerator
module: inspect
lineno: 457
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: isgenerator()

## Overview

Return true if the object is a generator.

Generator objects provide these attributes:
    __iter__        defined to support iteration over container
    close           raises a new GeneratorExit exception inside the
                    generator to terminate the iteration
    gi_code         code object
    gi_frame        frame object or possibly None once the generator has
                    been exhausted
    gi_running      set to 1 when generator is executing, 0 otherwise
    next            return the next item from the container
    send            resumes the generator and "sends" a value that becomes
                    the result of the current yield-expression
    throw           used to raise an exception inside the generator

```python
def isgenerator(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 457
