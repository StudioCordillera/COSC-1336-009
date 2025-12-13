---
type: module
name: doctest
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\doctest.py
is_package: False
analyzed_at: 2025-12-10T03:46:24.537990
tags:
  - python
  - module
---

# Module: doctest

## Overview

Module doctest -- a framework for running examples in docstrings.

In simplest use, end each module M to be tested with:

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

Then running the module as a script will cause the examples in the
docstrings to get executed and verified:

python M.py

This won't display anything unless an example fails, in which case the
failing example(s) and the cause(s) of the failure(s) are printed to stdout
(why not stderr? because stderr is a lame hack <0.2 wink>), and the final
line of output is "Test failed.".

Run it with the -v switch instead:

python M.py -v

and a detailed report of all examples tried is printed to stdout, along
with assorted summaries at the end.

You can force verbose mode by passing "verbose=True" to testmod, or prohibit
it by passing "verbose=False".  In either of those cases, sys.argv is not
examined by testmod.

There are a variety of other ways to run doctests, including integration
with the unittest framework, and support for running non-Python text
files containing doctests.  There are also many ways to override parts
of doctest's default behaviors.  See the Library Reference Manual for
details.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\doctest.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:24

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/re|re]]
- [[Modules/difflib|difflib]]
- [[Modules/io|io]]
- [[Modules/argparse|argparse]]
- [[Modules/collections|collections]]
- [[Modules/linecache|linecache]]

## Used By

This module is imported by:
- [[Modules/pickletools|pickletools]]

## Classes

- [[Classes/ANSIColors|ANSIColors]] (line 13)
- [[Classes/TestResults|TestResults]] (line 111)
- [[Classes/_SpoofOut|_SpoofOut]] (line 280)
- [[Classes/_OutputRedirectingPdb|_OutputRedirectingPdb]] (line 378)
- [[Classes/Example|Example]] (line 461)
- [[Classes/DocTest|DocTest]] (line 529)
- [[Classes/DocTestParser|DocTestParser]] (line 606)
- [[Classes/DocTestFinder|DocTestFinder]] (line 841)
- [[Classes/DocTestRunner|DocTestRunner]] (line 1178)
- [[Classes/OutputChecker|OutputChecker]] (line 1685)
- [[Classes/DocTestFailure|DocTestFailure]] (line 1831)
- [[Classes/UnexpectedException|UnexpectedException]] (line 1850)
- [[Classes/DebugRunner|DebugRunner]] (line 1869)
- [[Classes/DocTestCase|DocTestCase]] (line 2275)
- [[Classes/SkipDocTestCase|SkipDocTestCase]] (line 2439)
- [[Classes/_DocTestSuite|_DocTestSuite]] (line 2456)
- [[Classes/DocFileCase|DocFileCase]] (line 2526)
- [[Classes/_TestClass|_TestClass]] (line 2775)

## Functions

- [[Functions/namedtuple_4978|namedtuple()]] (line 358)
- [[Functions/can_colorize_4979|can_colorize()]] (line 79)
- [[Functions/register_optionflag_4982|register_optionflag()]] (line 150)
- [[Functions/_extract_future_flags_4983|_extract_future_flags()]] (line 201)
- [[Functions/_normalize_module_4984|_normalize_module()]] (line 213)
- [[Functions/_newline_convert_4985|_newline_convert()]] (line 238)
- [[Functions/_load_testfile_4986|_load_testfile()]] (line 242)
- [[Functions/_indent_4987|_indent()]] (line 260)
- [[Functions/_exception_traceback_4988|_exception_traceback()]] (line 268)
- [[Functions/_ellipsis_match_4991|_ellipsis_match()]] (line 295)
- [[Functions/_comment_line_4992|_comment_line()]] (line 344)
- [[Functions/_strip_exception_details_4993|_strip_exception_details()]] (line 352)
- [[Functions/_module_relative_path_4998|_module_relative_path()]] (line 415)
- [[Functions/_n_items_5034|_n_items()]] (line 1676)
- [[Functions/testmod_5046|testmod()]] (line 1981)
- [[Functions/testfile_5047|testfile()]] (line 2086)
- [[Functions/run_docstring_examples_5048|run_docstring_examples()]] (line 2210)
- [[Functions/set_unittest_reportflags_5049|set_unittest_reportflags()]] (line 2239)
- [[Functions/DocTestSuite_5066|DocTestSuite()]] (line 2462)
- [[Functions/DocFileTest_5070|DocFileTest()]] (line 2539)
- [[Functions/DocFileSuite_5071|DocFileSuite()]] (line 2565)
- [[Functions/script_from_examples_5072|script_from_examples()]] (line 2638)
- [[Functions/testsource_5073|testsource()]] (line 2720)
- [[Functions/debug_src_5074|debug_src()]] (line 2736)
- [[Functions/debug_script_5075|debug_script()]] (line 2741)
- [[Functions/debug_5076|debug()]] (line 2761)
- [[Functions/_test_5080|_test()]] (line 2870)
