---
type: function
name: DocTestSuite
module: doctest
lineno: 2462
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: DocTestSuite()

## Overview

Convert doctest tests for a module to a unittest test suite.

This converts each documentation string in a module that
contains doctest tests to a unittest test case.  If any of the
tests in a doc string fail, then the test case fails.  An exception
is raised showing the name of the file containing the test and a
(sometimes approximate) line number.

The `module` argument provides the module to be tested.  The argument
can be either a module or a module name.

If no argument is given, the calling module is used.

A number of options may be provided as keyword arguments:

setUp
  A set-up function.  This is called before running the
  tests in each file. The setUp function will be passed a DocTest
  object.  The setUp function can access the test globals as the
  globs attribute of the test passed.

tearDown
  A tear-down function.  This is called after running the
  tests in each file.  The tearDown function will be passed a DocTest
  object.  The tearDown function can access the test globals as the
  globs attribute of the test passed.

globs
  A dictionary containing initial global variables for the tests.

optionflags
   A set of doctest option flags expressed as an integer.

```python
def DocTestSuite(module, globs, extraglobs, test_finder)
```

**Module:** [[Modules/doctest|doctest]]
**Type:** Module-level function
**Line:** 2462
