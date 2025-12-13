---
type: module
name: selectors
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\selectors.py
is_package: False
analyzed_at: 2025-12-10T03:46:19.568265
tags:
  - python
  - module
---

# Module: selectors

## Overview

Selectors module.

This module allows high-level and efficient I/O multiplexing, built upon the
`select` module primitives.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\selectors.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:19

## Dependencies

This module imports:
- [[Modules/math|math]]
- [[Modules/select|select]]
- [[Modules/collections|collections]]

## Used By

This module is imported by:
- [[Modules/socketserver|socketserver]]

## Classes

- [[Classes/_SelectorMapping|_SelectorMapping]] (line 60)
- [[Classes/BaseSelector|BaseSelector]] (line 84)
- [[Classes/_BaseSelectorImpl|_BaseSelectorImpl]] (line 210)
- [[Classes/SelectSelector|SelectSelector]] (line 281)
- [[Classes/_PollLikeSelector|_PollLikeSelector]] (line 330)
- [[Classes/PollSelector|PollSelector]] (line 414)
- [[Classes/EpollSelector|EpollSelector]] (line 426)
- [[Classes/DevpollSelector|DevpollSelector]] (line 472)
- [[Classes/KqueueSelector|KqueueSelector]] (line 488)

## Functions

- [[Functions/namedtuple_2887|namedtuple()]] (line 358)
- [[Functions/_fileobj_to_fd_2888|_fileobj_to_fd()]] (line 21)
- [[Functions/_can_use_2931|_can_use()]] (line 568)
