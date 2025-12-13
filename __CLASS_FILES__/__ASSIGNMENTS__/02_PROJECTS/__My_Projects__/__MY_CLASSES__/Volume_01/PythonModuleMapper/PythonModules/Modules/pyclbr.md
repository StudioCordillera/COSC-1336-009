---
type: module
name: pyclbr
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\pyclbr.py
is_package: False
analyzed_at: 2025-12-10T03:46:28.054019
tags:
  - python
  - module
---

# Module: pyclbr

## Overview

Parse a Python module and describe its classes and functions.

Parse enough of a Python file to recognize imports and class and
function definitions, and to find out the superclasses of a class.

The interface consists of a single function:
    readmodule_ex(module, path=None)
where module is the name of a Python module, and path is an optional
list of directories where the module is to be searched.  If present,
path is prepended to the system search path sys.path.  The return value
is a dictionary.  The keys of the dictionary are the names of the
classes and functions defined in the module (including classes that are
defined via the from XXX import YYY construct).  The values are
instances of classes Class and Function.  One special key/value pair is
present for packages: the key '__path__' has a list as its value which
contains the package search path.

Classes and Functions have a common superclass: _Object.  Every instance
has the following attributes:
    module  -- name of the module;
    name    -- name of the object;
    file    -- file in which the object is defined;
    lineno  -- line in the file where the object's definition starts;
    end_lineno -- line in the file where the object's definition ends;
    parent  -- parent of this object, if any;
    children -- nested objects contained in this object.
The 'children' attribute is a dictionary mapping names to objects.

Instances of Function describe functions with the attributes from _Object,
plus the following:
    is_async -- if a function is defined with an 'async' prefix

Instances of Class describe classes with the attributes from _Object,
plus the following:
    super   -- list of super classes (Class instances if possible);
    methods -- mapping of method names to beginning line numbers.
If the name of a super class is not recognized, the corresponding
entry in the list of super classes is not a class instance but a
string giving the name of the super class.  Since import statements
are recognized and imported modules are scanned as well, this
shouldn't happen often.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\pyclbr.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:28

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/ast|ast]]
- [[Modules/sys|sys]]

## Classes

- [[Classes/_Object|_Object]] (line 53)
- [[Classes/Function|Function]] (line 68)
- [[Classes/Class|Class]] (line 78)
- [[Classes/_ModuleBrowser|_ModuleBrowser]] (line 186)

## Functions

- [[Functions/_nest_function_6133|_nest_function()]] (line 89)
- [[Functions/_nest_class_6134|_nest_class()]] (line 94)
- [[Functions/readmodule_6135|readmodule()]] (line 100)
- [[Functions/readmodule_ex_6136|readmodule_ex()]] (line 112)
- [[Functions/_readmodule_6137|_readmodule()]] (line 122)
- [[Functions/_create_tree_6144|_create_tree()]] (line 269)
- [[Functions/_main_6145|_main()]] (line 275)
