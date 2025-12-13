---
type: function
name: write_results
module: trace
lineno: 205
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: write_results()

## Overview

Write the coverage results.

:param show_missing: Show lines that had no hits.
:param summary: Include coverage summary per module.
:param coverdir: If None, the results of each module are placed in its
                 directory, otherwise it is included in the directory
                 specified.
:param ignore_missing_files: If True, counts for files that no longer
                 exist are silently ignored. Otherwise, a missing file
                 will raise a FileNotFoundError.

```python
def write_results(self, show_missing, summary, coverdir)
```

**Module:** [[Modules/trace|trace]]
**Class:** [[Classes/CoverageResults|CoverageResults]]
**Type:** Method
**Line:** 205

## Categories

- [[Taxonomy/public_method|public_method]]
