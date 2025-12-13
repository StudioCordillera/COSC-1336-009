---
type: class
name: ConverterMapping
module: configparser
lineno: 1331
tags:
  - python
  - class
---

# Class: ConverterMapping

## Overview

Enables reuse of get*() methods between the parser and section proxies.

If a parser class implements a getter directly, the value for the given
key will be ``None``. The presence of the converter name here enables
section proxies to find and use the implementation on the parser class.

**Module:** [[Modules/configparser|configparser]]
**Line:** 1331

## Methods

### Constructors
- [[Functions/__init___1976|__init__()]] (line 1341)

### Magic Methods
- [[Functions/__getitem___1977|__getitem__()]] (line 1350)
- [[Functions/__setitem___1978|__setitem__()]] (line 1353)
- [[Functions/__delitem___1979|__delitem__()]] (line 1369)
- [[Functions/__iter___1980|__iter__()]] (line 1383)
- [[Functions/__len___1981|__len__()]] (line 1386)
