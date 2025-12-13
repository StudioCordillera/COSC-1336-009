---
type: class
name: EnvBuilder
module: venv
lineno: 21
tags:
  - python
  - class
---

# Class: EnvBuilder

## Overview

This class exists to allow virtual environment creation to be
customized. The constructor parameters determine the builder's
behaviour when called upon to create a virtual environment.

By default, the builder makes the system (global) site-packages dir
*un*available to the created environment.

If invoked using the Python -m option, the default is to use copying
on Windows platforms but symlinks elsewhere. If instantiated some
other way, the default is to *not* use symlinks.

:param system_site_packages: If True, the system (global) site-packages
                             dir is available to created environments.
:param clear: If True, delete the contents of the environment directory if
              it already exists, before environment creation.
:param symlinks: If True, attempt to symlink rather than copy files into
                 virtual environment.
:param upgrade: If True, upgrade an existing virtual environment.
:param with_pip: If True, ensure pip is installed in the virtual
                 environment
:param prompt: Alternative terminal prefix for the environment.
:param upgrade_deps: Update the base venv modules to the latest on PyPI
:param scm_ignore_files: Create ignore files for the SCMs specified by the
                         iterable.

**Module:** [[Modules/venv|venv]]
**Line:** 21

## Methods

### Constructors
- [[Functions/__init___5398|__init__()]] (line 49)

### Methods
- [[Functions/create_5399|create()]] (line 64)
- [[Functions/clear_directory_5400|clear_directory()]] (line 94)
- [[Functions/_venv_path_5401|_venv_path()]] (line 102)
- [[Functions/_same_path_5402|_same_path()]] (line 112)
- [[Functions/ensure_directories_5403|ensure_directories()]] (line 138)
- [[Functions/create_configuration_5404|create_configuration()]] (line 211)
- [[Functions/symlink_or_copy_5405|symlink_or_copy()]] (line 257)
- [[Functions/create_git_ignore_file_5406|create_git_ignore_file()]] (line 279)
- [[Functions/setup_python_5407|setup_python()]] (line 318)
- [[Functions/_call_new_python_5408|_call_new_python()]] (line 429)
- [[Functions/_setup_pip_5409|_setup_pip()]] (line 444)
- [[Functions/setup_scripts_5410|setup_scripts()]] (line 449)
- [[Functions/post_setup_5411|post_setup()]] (line 464)
- [[Functions/replace_variables_5412|replace_variables()]] (line 474)
- [[Functions/install_scripts_5413|install_scripts()]] (line 522)
- [[Functions/upgrade_dependencies_5414|upgrade_dependencies()]] (line 585)
