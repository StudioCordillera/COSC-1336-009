---
type: module
name: pydoc
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pydoc.py
is_package: False
analyzed_at: 2025-12-10T03:46:24.251465
tags:
  - python
  - module
---

# Module: pydoc

## Overview

Generate Python documentation in HTML or text for interactive use.

At the Python interactive prompt, calling help(thing) on a Python object
documents the object, and calling help() starts up an interactive
help session.

Or, at the shell command line outside of Python:

Run "pydoc <name>" to show documentation on something.  <name> may be
the name of a function, module, package, or a dotted reference to a
class or function within a module or module in a package.  If the
argument contains a path segment delimiter (e.g. slash on Unix,
backslash on Windows) it is treated as the path to a Python source file.

Run "pydoc -k <keyword>" to search for a keyword in the synopsis lines
of all available modules.

Run "pydoc -n <hostname>" to start an HTTP server with the given
hostname (default: localhost) on the local machine.

Run "pydoc -p <port>" to start an HTTP server on the given port on the
local machine.  Port number 0 can be used to get an arbitrary unused port.

Run "pydoc -b" to start an HTTP server on an arbitrary unused port and
open a web browser to interactively browse documentation.  Combine with
the -n and -p options to control the hostname and port used.

Run "pydoc -w <name>" to write out the HTML documentation for a module
to a file named "<name>.html".

Module docs for core modules are assumed to be in

    https://docs.python.org/X.Y/library/

This can be overridden by setting the PYTHONDOCS environment variable
to a different URL or to a local directory containing the Library
Reference Manual pages.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pydoc.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:24

## Dependencies

This module imports:
- [[Modules/select|select]]
- [[Modules/time|time]]
- [[Modules/threading|threading]]
- [[Modules/io|io]]
- [[Modules/platform|platform]]
- [[Modules/webbrowser|webbrowser]]
- [[Modules/collections|collections]]
- [[Modules/textwrap|textwrap]]
- [[Modules/getopt|getopt]]
- [[Modules/os|os]]
- [[Modules/re|re]]
- [[Modules/reprlib|reprlib]]

## Used By

This module is imported by:
- [[Modules/pdb|pdb]]

## Classes

- [[Classes/Repr|Repr]] (line 38)
- [[Classes/ErrorDuringImport|ErrorDuringImport]] (line 448)
- [[Classes/Doc|Doc]] (line 529)
- [[Classes/HTMLRepr|HTMLRepr]] (line 587)
- [[Classes/HTMLDoc|HTMLDoc]] (line 629)
- [[Classes/TextRepr|TextRepr]] (line 1222)
- [[Classes/TextDoc|TextDoc]] (line 1254)
- [[Classes/_PlainTextDoc|_PlainTextDoc]] (line 1654)
- [[Classes/Helper|Helper]] (line 1800)
- [[Classes/ModuleScanner|ModuleScanner]] (line 2217)

## Functions

- [[Functions/format_exception_only_4864|format_exception_only()]] (line 158)
- [[Functions/get_pager_4865|get_pager()]] (line 17)
- [[Functions/plain_4866|plain()]] (line 66)
- [[Functions/pipe_pager_4867|pipe_pager()]] (line 127)
- [[Functions/plain_pager_4868|plain_pager()]] (line 122)
- [[Functions/tempfile_pager_4869|tempfile_pager()]] (line 165)
- [[Functions/tty_pager_4870|tty_pager()]] (line 71)
- [[Functions/pathdirs_4871|pathdirs()]] (line 95)
- [[Functions/_findclass_4872|_findclass()]] (line 107)
- [[Functions/_finddoc_4873|_finddoc()]] (line 117)
- [[Functions/_getowndoc_4874|_getowndoc()]] (line 167)
- [[Functions/_getdoc_4875|_getdoc()]] (line 182)
- [[Functions/getdoc_4876|getdoc()]] (line 198)
- [[Functions/splitdoc_4877|splitdoc()]] (line 203)
- [[Functions/_getargspec_4878|_getargspec()]] (line 212)
- [[Functions/classname_4879|classname()]] (line 233)
- [[Functions/parentname_4880|parentname()]] (line 240)
- [[Functions/isdata_4881|isdata()]] (line 253)
- [[Functions/replace_4882|replace()]] (line 259)
- [[Functions/cram_4883|cram()]] (line 266)
- [[Functions/stripid_4884|stripid()]] (line 275)
- [[Functions/_is_bound_method_4885|_is_bound_method()]] (line 280)
- [[Functions/allmethods_4886|allmethods()]] (line 293)
- [[Functions/_split_list_4887|_split_list()]] (line 303)
- [[Functions/visiblename_4888|visiblename()]] (line 322)
- [[Functions/classify_class_attrs_4889|classify_class_attrs()]] (line 347)
- [[Functions/sort_attributes_4890|sort_attributes()]] (line 360)
- [[Functions/ispackage_4891|ispackage()]] (line 374)
- [[Functions/source_synopsis_4892|source_synopsis()]] (line 384)
- [[Functions/synopsis_4893|synopsis()]] (line 409)
- [[Functions/importfile_4896|importfile()]] (line 467)
- [[Functions/safeimport_4897|safeimport()]] (line 485)
- [[Functions/pager_4944|pager()]] (line 1661)
- [[Functions/describe_4945|describe()]] (line 1667)
- [[Functions/locate_4946|locate()]] (line 1694)
- [[Functions/resolve_4947|resolve()]] (line 1719)
- [[Functions/render_doc_4948|render_doc()]] (line 1733)
- [[Functions/doc_4949|doc()]] (line 1760)
- [[Functions/writedoc_4950|writedoc()]] (line 1785)
- [[Functions/writedocs_4951|writedocs()]] (line 1793)
- [[Functions/apropos_4970|apropos()]] (line 2278)
- [[Functions/_start_server_4971|_start_server()]] (line 2292)
- [[Functions/_url_handler_4972|_url_handler()]] (line 2445)
- [[Functions/browse_4973|browse()]] (line 2681)
- [[Functions/ispath_4974|ispath()]] (line 2718)
- [[Functions/_get_revised_path_4975|_get_revised_path()]] (line 2721)
- [[Functions/_adjust_cli_sys_path_4976|_adjust_cli_sys_path()]] (line 2749)
- [[Functions/cli_4977|cli()]] (line 2759)
