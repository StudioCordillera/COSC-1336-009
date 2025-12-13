---
type: class
name: AsyncExitStack
module: contextlib
lineno: 631
tags:
  - python
  - class
---

# Class: AsyncExitStack

## Overview

Async context manager for dynamic management of a stack of exit
callbacks.

For example:
    async with AsyncExitStack() as stack:
        connections = [await stack.enter_async_context(get_connection())
            for i in range(5)]
        # All opened connections will automatically be released at the
        # end of the async with statement, even if attempts to open a
        # connection later in the list raise an exception.

**Module:** [[Modules/contextlib|contextlib]]
**Line:** 631

## Inheritance

**Inherits from:**
- [[Classes/_BaseExitStack|_BaseExitStack]]
- [[Classes/AbstractAsyncContextManager|AbstractAsyncContextManager]]

## Methods

### Magic Methods
- [[Functions/__aenter___5579|__aenter__()]] (line 713)
- [[Functions/__aexit___5580|__aexit__()]] (line 716)

### Methods
- [[Functions/_create_async_exit_wrapper_5572|_create_async_exit_wrapper()]] (line 645)
- [[Functions/_create_async_cb_wrapper_5573|_create_async_cb_wrapper()]] (line 649)
- [[Functions/enter_async_context_5574|async enter_async_context()]] (line 654)
- [[Functions/push_async_exit_5575|push_async_exit()]] (line 672)
- [[Functions/push_async_callback_5576|push_async_callback()]] (line 690)
- [[Functions/aclose_5577|async aclose()]] (line 703)
- [[Functions/_push_async_cm_exit_5578|_push_async_cm_exit()]] (line 707)
