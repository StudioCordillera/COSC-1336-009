---
type: class
name: BaseSelector
module: selectors
lineno: 84
tags:
  - python
  - class
---

# Class: BaseSelector

## Overview

Selector abstract base class.

A selector supports registering file objects to be monitored for specific
I/O events.

A file object is a file descriptor or any object with a `fileno()` method.
An arbitrary object can be attached to the file object, which can be used
for example to store context information, a callback, etc.

A selector can use various implementations (select(), poll(), epoll()...)
depending on the platform. The default `Selector` class uses the most
efficient implementation on the current platform.

**Module:** [[Modules/selectors|selectors]]
**Line:** 84

## Inheritance

**Subclasses:**
- [[Classes/_BaseSelectorImpl|_BaseSelectorImpl]]

## Methods

### Magic Methods
- [[Functions/__enter___2901|__enter__()]] (line 203)
- [[Functions/__exit___2902|__exit__()]] (line 206)

### Methods
- [[Functions/register_2894|register()]] (line 100)
- [[Functions/unregister_2895|unregister()]] (line 123)
- [[Functions/modify_2896|modify()]] (line 141)
- [[Functions/select_2897|select()]] (line 159)
- [[Functions/close_2898|close()]] (line 177)
- [[Functions/get_key_2899|get_key()]] (line 184)
- [[Functions/get_map_2900|get_map()]] (line 199)
