---
type: function
name: _synthesize
module: webbrowser
lineno: 115
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _synthesize()

## Overview

Attempt to synthesize a controller based on existing controllers.

This is useful to create a controller when a user specifies a path to
an entry in the BROWSER environment variable -- we can copy a general
controller to operate using a specific installation of the desired
browser in this way.

If we can't create a controller in this way, or if there is no
executable for the requested browser, return [None, None].

```python
def _synthesize(browser)
```

**Module:** [[Modules/webbrowser|webbrowser]]
**Type:** Module-level function
**Line:** 115
