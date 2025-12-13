---
type: function
name: _check_prompt_blank
module: doctest
lineno: 811
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _check_prompt_blank()

## Overview

Given the lines of a source string (including prompts and
leading indentation), check to make sure that every prompt is
followed by a space character.  If any line is not followed by
a space character, then raise ValueError.

```python
def _check_prompt_blank(self, lines, indent, name, lineno)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/DocTestParser|DocTestParser]]
**Type:** Method
**Line:** 811

## Categories

- [[Taxonomy/protected_method|protected_method]]
