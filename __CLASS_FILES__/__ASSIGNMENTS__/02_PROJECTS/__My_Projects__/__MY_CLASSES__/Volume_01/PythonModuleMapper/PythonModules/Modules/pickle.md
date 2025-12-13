---
type: module
name: pickle
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pickle.py
is_package: False
analyzed_at: 2025-12-10T03:46:15.649126
tags:
  - python
  - module
---

# Module: pickle

## Overview

Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(bytes) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pickle.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:15

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/struct|struct]]
- [[Modules/functools|functools]]
- [[Modules/itertools|itertools]]
- [[Modules/types|types]]
- [[Modules/codecs|codecs]]
- [[Modules/pprint|pprint]]

## Used By

This module is imported by:
- [[Modules/shelve|shelve]]
- [[Modules/logging|logging]]
- [[Modules/trace|trace]]
- [[Modules/tracemalloc|tracemalloc]]
- [[Modules/pickletools|pickletools]]

## Classes

- [[Classes/partial|partial]] (line 279)
- [[Classes/PickleError|PickleError]] (line 73)
- [[Classes/PicklingError|PicklingError]] (line 77)
- [[Classes/UnpicklingError|UnpicklingError]] (line 84)
- [[Classes/_Stop|_Stop]] (line 97)
- [[Classes/_Framer|_Framer]] (line 194)
- [[Classes/_Unframer|_Unframer]] (line 257)
- [[Classes/_Pickler|_Pickler]] (line 404)
- [[Classes/_Unpickler|_Unpickler]] (line 1180)

## Functions

- [[Functions/_getattribute_1379|_getattribute()]] (line 316)
- [[Functions/whichmodule_1380|whichmodule()]] (line 330)
- [[Functions/encode_long_1381|encode_long()]] (line 349)
- [[Functions/decode_long_1382|decode_long()]] (line 379)
- [[Functions/_dump_1489|_dump()]] (line 1792)
- [[Functions/_dumps_1490|_dumps()]] (line 1796)
- [[Functions/_load_1491|_load()]] (line 1804)
- [[Functions/_loads_1492|_loads()]] (line 1809)
- [[Functions/_test_1493|_test()]] (line 1835)
