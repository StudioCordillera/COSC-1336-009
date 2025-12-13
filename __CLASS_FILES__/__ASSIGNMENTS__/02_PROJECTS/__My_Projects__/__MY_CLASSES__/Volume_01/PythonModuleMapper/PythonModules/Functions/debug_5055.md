---
type: function
name: debug
module: doctest
lineno: 2341
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: debug()

## Overview

Run the test case without results and without catching exceptions

The unit test framework includes a debug method on test cases
and test suites to support post-mortem debugging.  The test code
is run in such a way that errors are not caught.  This way a
caller can catch the errors and initiate post-mortem debugging.

The DocTestCase provides a debug method that raises
UnexpectedException errors if there is an unexpected
exception:

  >>> test = DocTestParser().get_doctest('>>> raise KeyError\n42',
  ...                {}, 'foo', 'foo.py', 0)
  >>> case = DocTestCase(test)
  >>> try:
  ...     case.debug()
  ... except UnexpectedException as f:
  ...     failure = f

The UnexpectedException contains the test, the example, and
the original exception:

  >>> failure.test is test
  True

  >>> failure.example.want
  '42\n'

  >>> exc_info = failure.exc_info
  >>> raise exc_info[1] # Already has the traceback
  Traceback (most recent call last):
  ...
  KeyError

If the output doesn't match, then a DocTestFailure is raised:

  >>> test = DocTestParser().get_doctest('''
  ...      >>> x = 1
  ...      >>> x
  ...      2
  ...      ''', {}, 'foo', 'foo.py', 0)
  >>> case = DocTestCase(test)

  >>> try:
  ...    case.debug()
  ... except DocTestFailure as f:
  ...    failure = f

DocTestFailure objects provide access to the test:

  >>> failure.test is test
  True

As well as to the example:

  >>> failure.example.want
  '2\n'

and the actual output:

  >>> failure.got
  '1\n'

```python
def debug(self)
```

**Module:** [[Modules/doctest|doctest]]
**Class:** [[Classes/DocTestCase|DocTestCase]]
**Type:** Method
**Line:** 2341

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
