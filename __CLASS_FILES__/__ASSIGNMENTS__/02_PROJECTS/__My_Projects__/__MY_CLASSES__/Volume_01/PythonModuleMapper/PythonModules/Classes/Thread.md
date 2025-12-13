---
type: class
name: Thread
module: threading
lineno: 858
tags:
  - python
  - class
---

# Class: Thread

## Overview

A class that represents a thread of control.

This class can be safely subclassed in a limited fashion. There are two ways
to specify the activity: by passing a callable object to the constructor, or
by overriding the run() method in a subclass.

**Module:** [[Modules/threading|threading]]
**Line:** 858

## Inheritance

**Subclasses:**
- [[Classes/Timer|Timer]]
- [[Classes/_MainThread|_MainThread]]
- [[Classes/_DummyThread|_DummyThread]]

## Methods

### Constructors
- [[Functions/__init___2567|__init__()]] (line 869)

### Magic Methods
- [[Functions/__repr___2569|__repr__()]] (line 942)

### Methods
- [[Functions/_after_fork_2568|_after_fork()]] (line 928)
- [[Functions/start_2570|start()]] (line 955)
- [[Functions/run_2571|run()]] (line 983)
- [[Functions/_bootstrap_2572|_bootstrap()]] (line 1000)
- [[Functions/_set_ident_2573|_set_ident()]] (line 1020)
- [[Functions/_set_native_id_2574|_set_native_id()]] (line 1024)
- [[Functions/_bootstrap_inner_2575|_bootstrap_inner()]] (line 1027)
- [[Functions/_delete_2576|_delete()]] (line 1049)
- [[Functions/join_2577|join()]] (line 1058)
- [[Functions/name_2578|name()]] (line 1108)
- [[Functions/ident_2579|ident()]] (line 1113)
- [[Functions/native_id_2580|native_id()]] (line 1126)
- [[Functions/is_alive_2581|is_alive()]] (line 1136)
- [[Functions/daemon_2582|daemon()]] (line 1163)
- [[Functions/isDaemon_2583|isDaemon()]] (line 1172)
- [[Functions/setDaemon_2584|setDaemon()]] (line 1183)
- [[Functions/getName_2585|getName()]] (line 1194)
- [[Functions/setName_2586|setName()]] (line 1205)
