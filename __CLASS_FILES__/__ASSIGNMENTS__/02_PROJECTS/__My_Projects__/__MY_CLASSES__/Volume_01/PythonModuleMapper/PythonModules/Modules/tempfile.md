---
type: module
name: tempfile
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\tempfile.py
is_package: False
analyzed_at: 2025-12-10T03:46:15.232428
tags:
  - python
  - module
---

# Module: tempfile

## Overview

Temporary files.

This module provides generic, low- and high-level interfaces for
creating temporary files and directories.  All of the interfaces
provided by this module can be used without fear of race conditions
except for 'mktemp'.  'mktemp' is subject to race conditions and
should not be used; it is provided for backward compatibility only.

The default path names are returned as str.  If you supply bytes as
input, all return values will be in bytes.  Ex:

    >>> tempfile.mkstemp()
    (4, '/tmp/tmptpu9nin8')
    >>> tempfile.mkdtemp(suffix=b'')
    b'/tmp/tmppbi8f0hy'

This module also provides some data items to the user:

  TMP_MAX  - maximum number of names that will be tried before
             giving up.
  tempdir  - If this is set to a string before the first use of
             any routine from this module, it will be considered as
             another candidate location to store temporary files.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\tempfile.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:15

## Dependencies

This module imports:
- [[Modules/random|random]]
- [[Modules/functools|functools]]
- [[Modules/types|types]]
- [[Modules/weakref|weakref]]

## Used By

This module is imported by:
- [[Modules/ensurepip|ensurepip]]

## Classes

- [[Classes/_Random|_Random]] (line 103)
- [[Classes/_RandomNameSequence|_RandomNameSequence]] (line 132)
- [[Classes/_TemporaryFileCloser|_TemporaryFileCloser]] (line 432)
- [[Classes/_TemporaryFileWrapper|_TemporaryFileWrapper]] (line 475)
- [[Classes/SpooledTemporaryFile|SpooledTemporaryFile]] (line 685)
- [[Classes/TemporaryDirectory|TemporaryDirectory]] (line 864)

## Functions

- [[Functions/_exists_1194|_exists()]] (line 76)
- [[Functions/_infer_return_type_1195|_infer_return_type()]] (line 85)
- [[Functions/_sanitize_params_1196|_sanitize_params()]] (line 114)
- [[Functions/_candidate_tempdir_list_1200|_candidate_tempdir_list()]] (line 156)
- [[Functions/_get_default_tempdir_1201|_get_default_tempdir()]] (line 183)
- [[Functions/_get_candidate_names_1202|_get_candidate_names()]] (line 229)
- [[Functions/_mkstemp_inner_1203|_mkstemp_inner()]] (line 243)
- [[Functions/_dont_follow_symlinks_1204|_dont_follow_symlinks()]] (line 272)
- [[Functions/_resetperms_1205|_resetperms()]] (line 279)
- [[Functions/gettempprefix_1206|gettempprefix()]] (line 291)
- [[Functions/gettempprefixb_1207|gettempprefixb()]] (line 295)
- [[Functions/_gettempdir_1208|_gettempdir()]] (line 301)
- [[Functions/gettempdir_1209|gettempdir()]] (line 313)
- [[Functions/gettempdirb_1210|gettempdirb()]] (line 317)
- [[Functions/mkstemp_1211|mkstemp()]] (line 321)
- [[Functions/mkdtemp_1212|mkdtemp()]] (line 360)
- [[Functions/mktemp_1213|mktemp()]] (line 400)
- [[Functions/NamedTemporaryFile_1224|NamedTemporaryFile()]] (line 537)
- [[Functions/TemporaryFile_1225|TemporaryFile()]] (line 610)
