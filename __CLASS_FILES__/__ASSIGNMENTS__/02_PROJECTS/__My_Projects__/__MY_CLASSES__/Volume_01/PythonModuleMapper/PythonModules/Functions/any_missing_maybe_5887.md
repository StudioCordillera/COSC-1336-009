---
type: function
name: any_missing_maybe
module: modulefinder
lineno: 538
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: any_missing_maybe()

## Overview

Return two lists, one with modules that are certainly missing
and one with modules that *may* be missing. The latter names could
either be submodules *or* just global names in the package.

The reason it can't always be determined is that it's impossible to
tell which names are imported when "from module import *" is done
with an extension module, short of actually importing it.

```python
def any_missing_maybe(self)
```

**Module:** [[Modules/modulefinder|modulefinder]]
**Class:** [[Classes/ModuleFinder|ModuleFinder]]
**Type:** Method
**Line:** 538

## Categories

- [[Taxonomy/public_method|public_method]]
