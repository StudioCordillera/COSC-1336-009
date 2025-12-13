---
type: function
name: check_output
module: subprocess
lineno: 423
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: check_output()

## Overview

Run command with arguments and return its output.

If the exit code was non-zero it raises a CalledProcessError.  The
CalledProcessError object will have the return code in the returncode
attribute and output in the output attribute.

The arguments are the same as for the Popen constructor.  Example:

>>> check_output(["ls", "-l", "/dev/null"])
b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

The stdout argument is not allowed as it is used internally.
To capture standard error in the result, use stderr=STDOUT.

>>> check_output(["/bin/sh", "-c",
...               "ls -l non_existent_file ; exit 0"],
...              stderr=STDOUT)
b'ls: non_existent_file: No such file or directory\n'

There is an additional optional argument, "input", allowing you to
pass a string to the subprocess's stdin.  If you use this argument
you may not also use the Popen constructor's "stdin" argument, as
it too will be used internally.  Example:

>>> check_output(["sed", "-e", "s/foo/bar/"],
...              input=b"when in the course of fooman events\n")
b'when in the course of barman events\n'

By default, all communication is in bytes, and therefore any "input"
should be bytes, and the return value will be bytes.  If in text mode,
any "input" should be a string, and the return value will be a string
decoded according to locale encoding, or by "encoding" if set. Text mode
is triggered by setting any of text, encoding, errors or universal_newlines.

```python
def check_output()
```

**Module:** [[Modules/subprocess|subprocess]]
**Type:** Module-level function
**Line:** 423
