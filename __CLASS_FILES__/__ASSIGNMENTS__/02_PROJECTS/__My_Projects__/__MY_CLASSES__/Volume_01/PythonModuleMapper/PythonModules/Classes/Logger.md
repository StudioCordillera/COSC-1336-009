---
type: class
name: Logger
module: logging
lineno: 1463
tags:
  - python
  - class
---

# Class: Logger

## Overview

Instances of the Logger class represent a single logging channel. A
"logging channel" indicates an area of an application. Exactly how an
"area" is defined is up to the application developer. Since an
application can have any number of areas, logging channels are identified
by a unique string. Application areas can be nested (e.g. an area
of "input processing" might include sub-areas "read CSV files", "read
XLS files" and "read Gnumeric files"). To cater for this natural nesting,
channel names are organized into a namespace hierarchy where levels are
separated by periods, much like the Java or Python package namespace. So
in the instance given above, channel names might be "input" for the upper
level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels.
There is no arbitrary limit to the depth of nesting.

**Module:** [[Modules/logging|logging]]
**Line:** 1463

## Inheritance

**Inherits from:**
- [[Classes/Filterer|Filterer]]

**Subclasses:**
- [[Classes/RootLogger|RootLogger]]

## Methods

### Constructors
- [[Functions/__init___2325|__init__()]] (line 1480)

### Magic Methods
- [[Functions/__repr___2349|__repr__()]] (line 1831)
- [[Functions/__reduce___2350|__reduce__()]] (line 1835)

### Methods
- [[Functions/setLevel_2326|setLevel()]] (line 1493)
- [[Functions/debug_2327|debug()]] (line 1500)
- [[Functions/info_2328|info()]] (line 1512)
- [[Functions/warning_2329|warning()]] (line 1524)
- [[Functions/warn_2330|warn()]] (line 1536)
- [[Functions/error_2331|error()]] (line 1541)
- [[Functions/exception_2332|exception()]] (line 1553)
- [[Functions/critical_2333|critical()]] (line 1559)
- [[Functions/fatal_2334|fatal()]] (line 1571)
- [[Functions/log_2335|log()]] (line 1577)
- [[Functions/findCaller_2336|findCaller()]] (line 1594)
- [[Functions/makeRecord_2337|makeRecord()]] (line 1628)
- [[Functions/_log_2338|_log()]] (line 1643)
- [[Functions/handle_2339|handle()]] (line 1669)
- [[Functions/addHandler_2340|addHandler()]] (line 1690)
- [[Functions/removeHandler_2341|removeHandler()]] (line 1698)
- [[Functions/hasHandlers_2342|hasHandlers()]] (line 1706)
- [[Functions/callHandlers_2343|callHandlers()]] (line 1728)
- [[Functions/getEffectiveLevel_2344|getEffectiveLevel()]] (line 1758)
- [[Functions/isEnabledFor_2345|isEnabledFor()]] (line 1772)
- [[Functions/getChild_2346|getChild()]] (line 1791)
- [[Functions/getChildren_2347|getChildren()]] (line 1810)
- [[Functions/_is_disabled_2348|_is_disabled()]] (line 1826)
