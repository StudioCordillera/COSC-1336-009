---
type: function
name: communicate
module: subprocess
lineno: 1178
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: communicate()

## Overview

Interact with process: Send data to stdin and close it.
Read data from stdout and stderr, until end-of-file is
reached.  Wait for process to terminate.

The optional "input" argument should be data to be sent to the
child process, or None, if no data should be sent to the child.
communicate() returns a tuple (stdout, stderr).

By default, all communication is in bytes, and therefore any
"input" should be bytes, and the (stdout, stderr) will be bytes.
If in text mode (indicated by self.text_mode), any "input" should
be a string, and (stdout, stderr) will be strings decoded
according to locale encoding, or by "encoding" if set. Text mode
is triggered by setting any of text, encoding, errors or
universal_newlines.

```python
def communicate(self, input, timeout)
```

**Module:** [[Modules/subprocess|subprocess]]
**Class:** [[Classes/Popen|Popen]]
**Type:** Method
**Line:** 1178

## Categories

- [[Taxonomy/public_method|public_method]]
