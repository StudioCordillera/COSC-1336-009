---
type: module
name: subprocess
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\subprocess.py
is_package: False
analyzed_at: 2025-12-10T03:46:18.883786
tags:
  - python
  - module
---

# Module: subprocess

## Overview

Subprocesses with accessible I/O streams

This module allows you to spawn processes, connect to their
input/output/error pipes, and obtain their return codes.

For a complete description of this module see the Python documentation.

Main API
========
run(...): Runs a command, waits for it to complete, then returns a
          CompletedProcess instance.
Popen(...): A class for flexibly executing a command in a new process

Constants
---------
DEVNULL: Special value that indicates that os.devnull should be used
PIPE:    Special value that indicates a pipe should be created
STDOUT:  Special value that indicates that stderr should go to stdout


Older API
=========
call(...): Runs a command, waits for it to complete, then returns
    the return code.
check_call(...): Same as call() but raises CalledProcessError()
    if return code is not 0
check_output(...): Same as check_call() but returns the contents of
    stdout instead of a return code
getoutput(...): Runs a command in the shell, waits for it to complete,
    then returns the output
getstatusoutput(...): Runs a command in the shell, waits for it to complete,
    then returns a (exitcode, output) tuple

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\subprocess.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:18

## Dependencies

This module imports:
- [[Modules/time|time]]
- [[Modules/threading|threading]]
- [[Modules/errno|errno]]
- [[Modules/io|io]]
- [[Modules/types|types]]
- [[Modules/os|os]]

## Used By

This module is imported by:
- [[Modules/asyncio|asyncio]]
- [[Modules/webbrowser|webbrowser]]
- [[Modules/imaplib|imaplib]]
- [[Modules/uuid|uuid]]
- [[Modules/ensurepip|ensurepip]]
- [[Modules/venv|venv]]

## Classes

- [[Classes/_del_safe|_del_safe]] (line 116)
- [[Classes/SubprocessError|SubprocessError]] (line 129)
- [[Classes/CalledProcessError|CalledProcessError]] (line 132)
- [[Classes/TimeoutExpired|TimeoutExpired]] (line 169)
- [[Classes/STARTUPINFO|STARTUPINFO]] (line 198)
- [[Classes/Handle|Handle]] (line 221)
- [[Classes/CompletedProcess|CompletedProcess]] (line 476)
- [[Classes/Popen|Popen]] (line 759)

## Functions

- [[Functions/_cleanup_2623|_cleanup()]] (line 274)
- [[Functions/_optim_args_from_interpreter_flags_2624|_optim_args_from_interpreter_flags()]] (line 296)
- [[Functions/_args_from_interpreter_flags_2625|_args_from_interpreter_flags()]] (line 306)
- [[Functions/_text_encoding_2626|_text_encoding()]] (line 367)
- [[Functions/call_2627|call()]] (line 387)
- [[Functions/check_call_2628|check_call()]] (line 404)
- [[Functions/check_output_2629|check_output()]] (line 423)
- [[Functions/run_2633|run()]] (line 512)
- [[Functions/list2cmdline_2634|list2cmdline()]] (line 582)
- [[Functions/getstatusoutput_2635|getstatusoutput()]] (line 655)
- [[Functions/getoutput_2636|getoutput()]] (line 687)
- [[Functions/_use_posix_spawn_2637|_use_posix_spawn()]] (line 701)
