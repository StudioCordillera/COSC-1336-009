---
type: class
name: HtmlDiff
module: difflib
lineno: 1666
tags:
  - python
  - class
---

# Class: HtmlDiff

## Overview

For producing HTML side by side comparison with change highlights.

This class can be used to create an HTML table (or a complete HTML file
containing the table) showing a side by side, line by line comparison
of text with inter-line and intra-line change highlights.  The table can
be generated in either full or contextual difference mode.

The following methods are provided for HTML generation:

make_table -- generates HTML for a single side by side table
make_file -- generates complete HTML file with a single side by side table

See tools/scripts/diff.py for an example usage of this class.

**Module:** [[Modules/difflib|difflib]]
**Line:** 1666

## Methods

### Constructors
- [[Functions/__init___89|__init__()]] (line 1688)

### Methods
- [[Functions/make_file_90|make_file()]] (line 1705)
- [[Functions/_tab_newline_replace_91|_tab_newline_replace()]] (line 1732)
- [[Functions/_split_line_92|_split_line()]] (line 1755)
- [[Functions/_line_wrapper_93|_line_wrapper()]] (line 1810)
- [[Functions/_collect_lines_94|_collect_lines()]] (line 1838)
- [[Functions/_format_line_95|_format_line()]] (line 1859)
- [[Functions/_make_prefix_96|_make_prefix()]] (line 1882)
- [[Functions/_convert_flags_97|_convert_flags()]] (line 1893)
- [[Functions/make_table_98|make_table()]] (line 1940)
