---
type: function
name: do_alias
module: pdb
lineno: 2022
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: do_alias()

## Overview

alias [name [command]]

Create an alias called 'name' that executes 'command'.  The
command must *not* be enclosed in quotes.  Replaceable
parameters can be indicated by %1, %2, and so on, while %* is
replaced by all the parameters.  If no command is given, the
current alias for name is shown. If no name is given, all
aliases are listed.

Aliases may be nested and can contain anything that can be
legally typed at the pdb prompt.  Note!  You *can* override
internal pdb commands with aliases!  Those internal commands
are then hidden until the alias is removed.  Aliasing is
recursively applied to the first word of the command line; all
other words in the line are left alone.

As an example, here are two useful aliases (especially when
placed in the .pdbrc file):

# Print instance variables (usage "pi classInst")
alias pi for k in %1.__dict__.keys(): print("%1.",k,"=",%1.__dict__[k])
# Print instance variables in self
alias ps pi self

```python
def do_alias(self, arg)
```

**Module:** [[Modules/pdb|pdb]]
**Class:** [[Classes/Pdb|Pdb]]
**Type:** Method
**Line:** 2022

## Categories

- [[Taxonomy/public_method|public_method]]
