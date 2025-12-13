---
type: class
name: WeakKeyDictionary
module: weakref
lineno: 356
tags:
  - python
  - class
---

# Class: WeakKeyDictionary

## Overview

Mapping class that references keys weakly.

Entries in the dictionary will be discarded when there is no
longer a strong reference to the key. This can be used to
associate additional data with an object owned by other parts of
an application without adding attributes to those objects. This
can be especially useful with objects that override attribute
accesses.

**Module:** [[Modules/weakref|weakref]]
**Line:** 356

## Methods

### Constructors
- [[Functions/__init___480|__init__()]] (line 367)

### Magic Methods
- [[Functions/__delitem___483|__delitem__()]] (line 410)
- [[Functions/__getitem___484|__getitem__()]] (line 414)
- [[Functions/__len___485|__len__()]] (line 417)
- [[Functions/__repr___486|__repr__()]] (line 424)
- [[Functions/__setitem___487|__setitem__()]] (line 427)
- [[Functions/__deepcopy___489|__deepcopy__()]] (line 441)
- [[Functions/__contains___491|__contains__()]] (line 454)
- [[Functions/__ior___500|__ior__()]] (line 520)
- [[Functions/__or___501|__or__()]] (line 524)
- [[Functions/__ror___502|__ror__()]] (line 531)

### Methods
- [[Functions/_commit_removals_481|_commit_removals()]] (line 387)
- [[Functions/_scrub_removals_482|_scrub_removals()]] (line 405)
- [[Functions/copy_488|copy()]] (line 430)
- [[Functions/get_490|get()]] (line 451)
- [[Functions/items_492|items()]] (line 461)
- [[Functions/keys_493|keys()]] (line 468)
- [[Functions/values_494|values()]] (line 477)
- [[Functions/keyrefs_495|keyrefs()]] (line 483)
- [[Functions/popitem_496|popitem()]] (line 495)
- [[Functions/pop_497|pop()]] (line 503)
- [[Functions/setdefault_498|setdefault()]] (line 507)
- [[Functions/update_499|update()]] (line 510)
