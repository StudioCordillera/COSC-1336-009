---
type: module
name: sched
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\sched.py
is_package: False
analyzed_at: 2025-12-10T03:46:19.044601
tags:
  - python
  - module
---

# Module: sched

## Overview

A generally useful event scheduler class.

Each instance of this class manages its own queue.
No multi-threading is implied; you are supposed to hack that
yourself, or use a single instance per application.

Each instance is parametrized with two functions, one that is
supposed to return the current time, one that is supposed to
implement a delay.  You can implement real-time scheduling by
substituting time and sleep from built-in module time, or you can
implement simulated time by writing your own functions.  This can
also be used to integrate scheduling with STDWIN events; the delay
function is allowed to modify the queue.  Time can be expressed as
integers or floating-point numbers, as long as it is consistent.

Events are specified by tuples (time, priority, action, argument, kwargs).
As in UNIX, lower priority numbers mean higher priority; in this
way the queue can be maintained as a priority queue.  Execution of the
event means calling the action function, passing it the argument
sequence in "argument" (remember that in Python, multiple function
arguments are be packed in a sequence) and keyword parameters in "kwargs".
The action function may be an instance method so it
has another way to reference private data (besides global variables).

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\sched.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:19

## Dependencies

This module imports:
- [[Modules/threading|threading]]
- [[Modules/heapq|heapq]]
- [[Modules/itertools|itertools]]
- [[Modules/time|time]]
- [[Modules/collections|collections]]

## Classes

- [[Classes/scheduler|scheduler]] (line 51)

## Functions

- [[Functions/namedtuple_2669|namedtuple()]] (line 358)
