---
type: class
name: Cmd
module: cmd
lineno: 52
tags:
  - python
  - class
---

# Class: Cmd

## Overview

A simple framework for writing line-oriented command interpreters.

These are often useful for test harnesses, administrative tools, and
prototypes that will later be wrapped in a more sophisticated interface.

A Cmd instance or subclass instance is a line-oriented interpreter
framework.  There is no good reason to instantiate Cmd itself; rather,
it's useful as a superclass of an interpreter class you define yourself
in order to inherit Cmd's methods and encapsulate action methods.

**Module:** [[Modules/cmd|cmd]]
**Line:** 52

## Inheritance

**Subclasses:**
- [[Classes/Pdb|Pdb]]

## Methods

### Constructors
- [[Functions/__init___4077|__init__()]] (line 76)

### Methods
- [[Functions/cmdloop_4078|cmdloop()]] (line 98)
- [[Functions/precmd_4079|precmd()]] (line 158)
- [[Functions/postcmd_4080|postcmd()]] (line 165)
- [[Functions/preloop_4081|preloop()]] (line 169)
- [[Functions/postloop_4082|postloop()]] (line 173)
- [[Functions/parseline_4083|parseline()]] (line 180)
- [[Functions/onecmd_4084|onecmd()]] (line 200)
- [[Functions/emptyline_4085|emptyline()]] (line 226)
- [[Functions/default_4086|default()]] (line 236)
- [[Functions/completedefault_4087|completedefault()]] (line 245)
- [[Functions/completenames_4088|completenames()]] (line 254)
- [[Functions/complete_4089|complete()]] (line 258)
- [[Functions/get_names_4090|get_names()]] (line 288)
- [[Functions/complete_help_4091|complete_help()]] (line 293)
- [[Functions/do_help_4092|do_help()]] (line 299)
- [[Functions/print_topics_4093|print_topics()]] (line 346)
- [[Functions/columnize_4094|columnize()]] (line 354)
