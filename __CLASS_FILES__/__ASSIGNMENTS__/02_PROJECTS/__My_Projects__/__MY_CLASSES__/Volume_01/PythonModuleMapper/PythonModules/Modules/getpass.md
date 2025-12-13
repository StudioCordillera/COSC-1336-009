---
type: module
name: getpass
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\getpass.py
is_package: False
analyzed_at: 2025-12-10T03:46:18.185755
tags:
  - python
  - module
---

# Module: getpass

## Overview

Utilities to get a password and/or the current user name.

getpass(prompt[, stream]) - Prompt for a password, with echo turned off.
getuser() - Get the user name from the environment or password database.

GetPassWarning - This UserWarning is issued when getpass() cannot prevent
                 echoing of the password contents while reading.

On Windows, the msvcrt module will be used.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\getpass.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:18

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/io|io]]

## Used By

This module is imported by:
- [[Modules/imaplib|imaplib]]

## Classes

- [[Classes/GetPassWarning|GetPassWarning]] (line 25)

## Functions

- [[Functions/unix_getpass_2390|unix_getpass()]] (line 28)
- [[Functions/win_getpass_2391|win_getpass()]] (line 96)
- [[Functions/fallback_getpass_2392|fallback_getpass()]] (line 119)
- [[Functions/_raw_input_2393|_raw_input()]] (line 129)
- [[Functions/getuser_2394|getuser()]] (line 154)
