---
type: module
name: logging
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\logging\__init__.py
is_package: True
analyzed_at: 2025-12-10T03:46:17.867329
tags:
  - python
  - module
---

# Module: logging

## Overview

Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2022 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\logging\__init__.py`
**Type:** Package
**Analyzed:** 2025-12-10 03:46:17

## Dependencies

This module imports:
- [[Modules/string|string]]
- [[Modules/re|re]]
- [[Modules/os|os]]
- [[Modules/pickle|pickle]]
- [[Modules/io|io]]
- [[Modules/types|types]]
- [[Modules/time|time]]
- [[Modules/weakref|weakref]]

## Used By

This module is imported by:
- [[Modules/venv|venv]]

## Classes

- [[Classes/Template|Template]] (line 57)
- [[Classes/StrFormatter|StrFormatter]] (line 188)
- [[Classes/LogRecord|LogRecord]] (line 286)
- [[Classes/PercentStyle|PercentStyle]] (line 444)
- [[Classes/StrFormatStyle|StrFormatStyle]] (line 477)
- [[Classes/StringTemplateStyle|StringTemplateStyle]] (line 511)
- [[Classes/Formatter|Formatter]] (line 554)
- [[Classes/BufferingFormatter|BufferingFormatter]] (line 736)
- [[Classes/Filter|Filter]] (line 778)
- [[Classes/Filterer|Filterer]] (line 815)
- [[Classes/Handler|Handler]] (line 922)
- [[Classes/StreamHandler|StreamHandler]] (line 1111)
- [[Classes/FileHandler|FileHandler]] (line 1190)
- [[Classes/_StderrHandler|_StderrHandler]] (line 1272)
- [[Classes/PlaceHolder|PlaceHolder]] (line 1296)
- [[Classes/Manager|Manager]] (line 1338)
- [[Classes/Logger|Logger]] (line 1463)
- [[Classes/RootLogger|RootLogger]] (line 1842)
- [[Classes/LoggerAdapter|LoggerAdapter]] (line 1859)
- [[Classes/NullHandler|NullHandler]] (line 2277)

## Functions

- [[Functions/getLevelNamesMapping_2237|getLevelNamesMapping()]] (line 126)
- [[Functions/getLevelName_2238|getLevelName()]] (line 129)
- [[Functions/addLevelName_2239|addLevelName()]] (line 156)
- [[Functions/currentframe_2240|currentframe()]] (line 169)
- [[Functions/_is_internal_frame_2241|_is_internal_frame()]] (line 197)
- [[Functions/_checkLevel_2242|_checkLevel()]] (line 205)
- [[Functions/_prepareFork_2243|_prepareFork()]] (line 231)
- [[Functions/_afterFork_2244|_afterFork()]] (line 245)
- [[Functions/_register_at_fork_reinit_lock_2245|_register_at_fork_reinit_lock()]] (line 265)
- [[Functions/_after_at_fork_child_reinit_locks_2246|_after_at_fork_child_reinit_locks()]] (line 269)
- [[Functions/setLogRecordFactory_2250|setLogRecordFactory()]] (line 408)
- [[Functions/getLogRecordFactory_2251|getLogRecordFactory()]] (line 418)
- [[Functions/makeLogRecord_2252|makeLogRecord()]] (line 425)
- [[Functions/_removeHandlerRef_2281|_removeHandlerRef()]] (line 883)
- [[Functions/_addHandlerRef_2282|_addHandlerRef()]] (line 899)
- [[Functions/getHandlerByName_2283|getHandlerByName()]] (line 907)
- [[Functions/getHandlerNames_2284|getHandlerNames()]] (line 915)
- [[Functions/setLoggerClass_2315|setLoggerClass()]] (line 1319)
- [[Functions/getLoggerClass_2316|getLoggerClass()]] (line 1332)
- [[Functions/basicConfig_2371|basicConfig()]] (line 2016)
- [[Functions/getLogger_2372|getLogger()]] (line 2141)
- [[Functions/critical_2373|critical()]] (line 2151)
- [[Functions/fatal_2374|fatal()]] (line 2161)
- [[Functions/error_2375|error()]] (line 2167)
- [[Functions/exception_2376|exception()]] (line 2177)
- [[Functions/warning_2377|warning()]] (line 2185)
- [[Functions/warn_2378|warn()]] (line 2195)
- [[Functions/info_2379|info()]] (line 2200)
- [[Functions/debug_2380|debug()]] (line 2210)
- [[Functions/log_2381|log()]] (line 2220)
- [[Functions/disable_2382|disable()]] (line 2230)
- [[Functions/shutdown_2383|shutdown()]] (line 2237)
- [[Functions/_showwarning_2388|_showwarning()]] (line 2303)
- [[Functions/captureWarnings_2389|captureWarnings()]] (line 2323)
