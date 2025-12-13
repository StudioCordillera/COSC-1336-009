---
type: module
name: copy
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\copy.py
is_package: False
analyzed_at: 2025-12-10T03:46:13.789380
tags:
  - python
  - module
---

# Module: copy

## Overview

Generic (shallow and deep) copying operations.

Interface summary:

        import copy

        x = copy.copy(y)                # make a shallow copy of y
        x = copy.deepcopy(y)            # make a deep copy of y
        x = copy.replace(y, a=1, b=2)   # new object with fields replaced, as defined by `__replace__`

For module specific errors, copy.Error is raised.

The difference between shallow and deep copying is only relevant for
compound objects (objects that contain other objects, like lists or
class instances).

- A shallow copy constructs a new compound object and then (to the
  extent possible) inserts *the same objects* into it that the
  original contains.

- A deep copy constructs a new compound object and then, recursively,
  inserts *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don't exist
with shallow copy operations:

 a) recursive objects (compound objects that, directly or indirectly,
    contain a reference to themselves) may cause a recursive loop

 b) because deep copy copies *everything* it may copy too much, e.g.
    administrative data structures that should be shared even between
    copies

Python's deep copy operation avoids these problems by:

 a) keeping a table of objects already copied during the current
    copying pass

 b) letting user-defined classes override the copying operation or the
    set of components copied

This version does not copy types like module, class, function, method,
nor stack trace, stack frame, nor file, socket, window, nor any
similar types.

Classes can use the same interfaces to control copying that they use
to control pickling: they can define methods called __getinitargs__(),
__getstate__() and __setstate__().  See the documentation for module
"pickle" for information on these methods.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\copy.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:13

## Dependencies

This module imports:
- [[Modules/types|types]]
- [[Modules/weakref|weakref]]

## Used By

This module is imported by:
- [[Modules/tarfile|tarfile]]
- [[Modules/argparse|argparse]]
- [[Modules/mailbox|mailbox]]
- [[Modules/webbrowser|webbrowser]]
- [[Modules/smtplib|smtplib]]
- [[Modules/gettext|gettext]]
- [[Modules/turtle|turtle]]
- [[Modules/dataclasses|dataclasses]]

## Classes

- [[Classes/Error|Error]] (line 56)

## Functions

- [[Functions/copy_542|copy()]] (line 62)
- [[Functions/_copy_immutable_543|_copy_immutable()]] (line 103)
- [[Functions/deepcopy_544|deepcopy()]] (line 119)
- [[Functions/_deepcopy_atomic_545|_deepcopy_atomic()]] (line 173)
- [[Functions/_deepcopy_list_546|_deepcopy_list()]] (line 192)
- [[Functions/_deepcopy_tuple_547|_deepcopy_tuple()]] (line 201)
- [[Functions/_deepcopy_dict_548|_deepcopy_dict()]] (line 218)
- [[Functions/_deepcopy_method_549|_deepcopy_method()]] (line 226)
- [[Functions/_keep_alive_550|_keep_alive()]] (line 232)
- [[Functions/_reconstruct_551|_reconstruct()]] (line 248)
- [[Functions/replace_552|replace()]] (line 296)
