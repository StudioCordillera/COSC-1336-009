---
type: function
name: unix_getpass
module: getpass
lineno: 28
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: unix_getpass()

## Overview

Prompt for a password, with echo turned off.

Args:
  prompt: Written on stream to ask for the input.  Default: 'Password: '
  stream: A writable file object to display the prompt.  Defaults to
          the tty.  If no tty is available defaults to sys.stderr.
Returns:
  The seKr3t input.
Raises:
  EOFError: If our input tty or stdin was closed.
  GetPassWarning: When we were unable to turn echo off on the input.

Always restores terminal settings before returning.

```python
def unix_getpass(prompt, stream)
```

**Module:** [[Modules/getpass|getpass]]
**Type:** Module-level function
**Line:** 28
