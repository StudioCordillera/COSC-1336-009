---
type: module
name: fileinput
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\fileinput.py
is_package: False
analyzed_at: 2025-12-10T03:46:15.084851
tags:
  - python
  - module
---

# Module: fileinput

## Overview

Helper class to quickly write a loop over all standard input files.

Typical use is:

    import fileinput
    for line in fileinput.input(encoding="utf-8"):
        process(line)

This iterates over the lines of all files listed in sys.argv[1:],
defaulting to sys.stdin if the list is empty.  If a filename is '-' it
is also replaced by sys.stdin and the optional arguments mode and
openhook are ignored.  To specify an alternative list of filenames,
pass it as the argument to input().  A single file name is also allowed.

Functions filename(), lineno() return the filename and cumulative line
number of the line that has just been read; filelineno() returns its
line number in the current file; isfirstline() returns true iff the
line just read is the first line of its file; isstdin() returns true
iff the line was read from sys.stdin.  Function nextfile() closes the
current file so that the next iteration will read the first line from
the next file (if any); lines not read from the file will not count
towards the cumulative line count; the filename is not changed until
after the first line of the next file has been read.  Function close()
closes the sequence.

Before any lines have been read, filename() returns None and both line
numbers are zero; nextfile() has no effect.  After all lines have been
read, filename() and the line number functions return the values
pertaining to the last line read; nextfile() has no effect.

All files are opened in text mode by default, you can override this by
setting the mode parameter to input() or FileInput.__init__().
If an I/O error occurs during opening or reading a file, the OSError
exception is raised.

If sys.stdin is used more than once, the second and further use will
return no lines, except perhaps for interactive use, or if it has been
explicitly reset (e.g. using sys.stdin.seek(0)).

Empty files are opened and immediately closed; the only time their
presence in the list of filenames is noticeable at all is when the
last file opened is empty.

It is possible that the last line of a file doesn't end in a newline
character; otherwise lines are returned including the trailing
newline.

Class FileInput is the implementation; its methods filename(),
lineno(), fileline(), isfirstline(), isstdin(), nextfile() and close()
correspond to the functions in the module.  In addition it has a
readline() method which returns the next input line, and a
__getitem__() method which implements the sequence behavior.  The
sequence must be accessed in strictly sequential order; sequence
access and readline() cannot be mixed.

Optional in-place filtering: if the keyword argument inplace=True is
passed to input() or to the FileInput constructor, the file is moved
to a backup file and standard output is directed to the input file.
This makes it possible to write a filter that rewrites its input file
in place.  If the keyword argument backup=".<some extension>" is also
given, it specifies the extension for the backup file, and the backup
file remains around; by default, the extension is ".bak" and it is
deleted when the output file is closed.  In-place filtering is
disabled when standard input is read.  XXX The current implementation
does not work for MS-DOS 8+3 filesystems.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\fileinput.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:15

## Dependencies

This module imports:
- [[Modules/types|types]]

## Classes

- [[Classes/FileInput|FileInput]] (line 171)

## Functions

- [[Functions/input_1118|input()]] (line 78)
- [[Functions/close_1119|close()]] (line 93)
- [[Functions/nextfile_1120|nextfile()]] (line 101)
- [[Functions/filename_1121|filename()]] (line 115)
- [[Functions/lineno_1122|lineno()]] (line 124)
- [[Functions/filelineno_1123|filelineno()]] (line 134)
- [[Functions/fileno_1124|fileno()]] (line 144)
- [[Functions/isfirstline_1125|isfirstline()]] (line 153)
- [[Functions/isstdin_1126|isstdin()]] (line 162)
- [[Functions/hook_compressed_1143|hook_compressed()]] (line 401)
- [[Functions/hook_encoded_1144|hook_encoded()]] (line 420)
- [[Functions/_test_1145|_test()]] (line 426)
