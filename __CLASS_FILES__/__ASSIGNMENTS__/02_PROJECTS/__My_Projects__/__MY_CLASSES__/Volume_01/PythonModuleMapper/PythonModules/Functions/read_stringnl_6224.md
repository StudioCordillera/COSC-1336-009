---
type: function
name: read_stringnl
module: pickletools
lineno: 315
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: read_stringnl()

## Overview

>>> import io
>>> read_stringnl(io.BytesIO(b"'abcd'\nefg\n"))
'abcd'

>>> read_stringnl(io.BytesIO(b"\n"))
Traceback (most recent call last):
...
ValueError: no string quotes around b''

>>> read_stringnl(io.BytesIO(b"\n"), stripquotes=False)
''

>>> read_stringnl(io.BytesIO(b"''\n"))
''

>>> read_stringnl(io.BytesIO(b'"abcd"'))
Traceback (most recent call last):
...
ValueError: no newline found when trying to read stringnl

Embedded escapes are undone in the result.
>>> read_stringnl(io.BytesIO(br"'a\n\\b\x00c\td'" + b"\n'e'"))
'a\n\\b\x00c\td'

```python
def read_stringnl(f, decode, stripquotes)
```

**Module:** [[Modules/pickletools|pickletools]]
**Type:** Module-level function
**Line:** 315
