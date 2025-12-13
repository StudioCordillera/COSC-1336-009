---
type: class
name: CompletedProcess
module: subprocess
lineno: 476
tags:
  - python
  - class
---

# Class: CompletedProcess

## Overview

A process that has finished running.

This is returned by run().

Attributes:
  args: The list or str args passed to run().
  returncode: The exit code of the process, negative for signals.
  stdout: The standard output (None if not captured).
  stderr: The standard error (None if not captured).

**Module:** [[Modules/subprocess|subprocess]]
**Line:** 476

## Methods

### Constructors
- [[Functions/__init___2630|__init__()]] (line 487)

### Magic Methods
- [[Functions/__repr___2631|__repr__()]] (line 493)

### Methods
- [[Functions/check_returncode_2632|check_returncode()]] (line 505)
