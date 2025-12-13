---
type: function
name: script_from_examples
module: doctest
lineno: 2638
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: script_from_examples()

## Overview

Extract script from text with examples.

Converts text with examples to a Python script.  Example input is
converted to regular code.  Example output and all other words
are converted to comments:

>>> text = '''
...       Here are examples of simple math.
...
...           Python has super accurate integer addition
...
...           >>> 2 + 2
...           5
...
...           And very friendly error messages:
...
...           >>> 1/0
...           To Infinity
...           And
...           Beyond
...
...           You can use logic if you want:
...
...           >>> if 0:
...           ...    blah
...           ...    blah
...           ...
...
...           Ho hum
...           '''

>>> print(script_from_examples(text))
# Here are examples of simple math.
#
#     Python has super accurate integer addition
#
2 + 2
# Expected:
## 5
#
#     And very friendly error messages:
#
1/0
# Expected:
## To Infinity
## And
## Beyond
#
#     You can use logic if you want:
#
if 0:
   blah
   blah
#
#     Ho hum
<BLANKLINE>

```python
def script_from_examples(s)
```

**Module:** [[Modules/doctest|doctest]]
**Type:** Module-level function
**Line:** 2638
