---
type: function
name: process
module: logging
lineno: 1890
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: process()

## Overview

Process the logging message and keyword arguments passed in to
a logging call to insert contextual information. You can either
manipulate the message itself, the keyword args or both. Return
the message and kwargs modified (or not) to suit your needs.

Normally, you'll only need to override this one method in a
LoggerAdapter subclass for your specific needs.

```python
def process(self, msg, kwargs)
```

**Module:** [[Modules/logging|logging]]
**Class:** [[Classes/LoggerAdapter|LoggerAdapter]]
**Type:** Method
**Line:** 1890

## Categories

- [[Taxonomy/public_method|public_method]]
