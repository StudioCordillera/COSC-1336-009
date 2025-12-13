---
type: class
name: DocTestRunner
module: doctest
lineno: 1178
tags:
  - python
  - class
---

# Class: DocTestRunner

## Overview

A class used to run DocTest test cases, and accumulate statistics.
The `run` method is used to process a single DocTest case.  It
returns a TestResults instance.

    >>> save_colorize = _colorize.COLORIZE
    >>> _colorize.COLORIZE = False

    >>> tests = DocTestFinder().find(_TestClass)
    >>> runner = DocTestRunner(verbose=False)
    >>> tests.sort(key = lambda test: test.name)
    >>> for test in tests:
    ...     print(test.name, '->', runner.run(test))
    _TestClass -> TestResults(failed=0, attempted=2)
    _TestClass.__init__ -> TestResults(failed=0, attempted=2)
    _TestClass.get -> TestResults(failed=0, attempted=2)
    _TestClass.square -> TestResults(failed=0, attempted=1)

The `summarize` method prints a summary of all the test cases that
have been run by the runner, and returns an aggregated TestResults
instance:

    >>> runner.summarize(verbose=1)
    4 items passed all tests:
       2 tests in _TestClass
       2 tests in _TestClass.__init__
       2 tests in _TestClass.get
       1 test in _TestClass.square
    7 tests in 4 items.
    7 passed.
    Test passed.
    TestResults(failed=0, attempted=7)

The aggregated number of tried examples and failed examples is also
available via the `tries`, `failures` and `skips` attributes:

    >>> runner.tries
    7
    >>> runner.failures
    0
    >>> runner.skips
    0

The comparison between expected outputs and actual outputs is done
by an `OutputChecker`.  This comparison may be customized with a
number of option flags; see the documentation for `testmod` for
more information.  If the option flags are insufficient, then the
comparison may also be customized by passing a subclass of
`OutputChecker` to the constructor.

The test runner's display output can be controlled in two ways.
First, an output function (`out) can be passed to
`TestRunner.run`; this function will be called with strings that
should be displayed.  It defaults to `sys.stdout.write`.  If
capturing the output is not sufficient, then the display output
can be also customized by subclassing DocTestRunner, and
overriding the methods `report_start`, `report_success`,
`report_unexpected_exception`, and `report_failure`.

    >>> _colorize.COLORIZE = save_colorize

**Module:** [[Modules/doctest|doctest]]
**Line:** 1178

## Inheritance

**Subclasses:**
- [[Classes/DebugRunner|DebugRunner]]

## Methods

### Constructors
- [[Functions/__init___5022|__init__()]] (line 1244)

### Methods
- [[Functions/report_start_5023|report_start()]] (line 1281)
- [[Functions/report_success_5024|report_success()]] (line 1294)
- [[Functions/report_failure_5025|report_failure()]] (line 1302)
- [[Functions/report_unexpected_exception_5026|report_unexpected_exception()]] (line 1309)
- [[Functions/_failure_header_5027|_failure_header()]] (line 1316)
- [[Functions/__run_5028|__run()]] (line 1339)
- [[Functions/__record_outcome_5029|__record_outcome()]] (line 1480)
- [[Functions/__patched_linecache_getlines_5030|__patched_linecache_getlines()]] (line 1496)
- [[Functions/run_5031|run()]] (line 1504)
- [[Functions/summarize_5032|summarize()]] (line 1585)
- [[Functions/merge_5033|merge()]] (line 1665)
