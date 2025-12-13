---
type: module
name: trace
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\trace.py
is_package: False
analyzed_at: 2025-12-10T03:46:25.362469
tags:
  - python
  - module
---

# Module: trace

## Overview

program/module to trace Python program or function execution

Sample use, command line:
  trace.py -c -f counts --ignore-dir '$prefix' spam.py eggs
  trace.py -t --ignore-dir '$prefix' spam.py eggs
  trace.py --trackcalls spam.py eggs

Sample use, programmatically
  import sys

  # create a Trace object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix,],
                       trace=0, count=1)
  # run the new command using the given tracer
  tracer.run('main()')
  # make a report, placing output in /tmp
  r = tracer.results()
  r.write_results(show_missing=True, coverdir="/tmp")

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\trace.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:25

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/threading|threading]]
- [[Modules/pickle|pickle]]
- [[Modules/io|io]]
- [[Modules/time|time]]
- [[Modules/argparse|argparse]]
- [[Modules/linecache|linecache]]

## Classes

- [[Classes/_Ignore|_Ignore]] (line 69)
- [[Classes/CoverageResults|CoverageResults]] (line 154)
- [[Classes/Trace|Trace]] (line 393)

## Functions

- [[Functions/_modname_5288|_modname()]] (line 119)
- [[Functions/_fullmodname_5289|_fullmodname()]] (line 126)
- [[Functions/_find_lines_from_code_5295|_find_lines_from_code()]] (line 334)
- [[Functions/_find_lines_5296|_find_lines()]] (line 344)
- [[Functions/_find_strings_5297|_find_strings()]] (line 356)
- [[Functions/_find_executable_linenos_5298|_find_executable_linenos()]] (line 379)
- [[Functions/main_5311|main()]] (line 607)
