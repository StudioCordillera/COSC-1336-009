---
type: module
name: configparser
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\configparser.py
is_package: False
analyzed_at: 2025-12-10T03:46:16.956665
tags:
  - python
  - module
---

# Module: configparser

## Overview

Configuration file parser.

A configuration file consists of sections, lead by a "[section]" header,
and followed by "name: value" entries, with continuations and such in
the style of RFC 822.

Intrinsic defaults can be specified by passing them into the
ConfigParser constructor as a dictionary.

class:

ConfigParser -- responsible for parsing a list of
                    configuration files, and managing the parsed database.

    methods:

    __init__(defaults=None, dict_type=_default_dict, allow_no_value=False,
             delimiters=('=', ':'), comment_prefixes=('#', ';'),
             inline_comment_prefixes=None, strict=True,
             empty_lines_in_values=True, default_section='DEFAULT',
             interpolation=<unset>, converters=<unset>,
             allow_unnamed_section=False):
        Create the parser. When `defaults` is given, it is initialized into the
        dictionary or intrinsic defaults. The keys must be strings, the values
        must be appropriate for %()s string interpolation.

        When `dict_type` is given, it will be used to create the dictionary
        objects for the list of sections, for the options within a section, and
        for the default values.

        When `delimiters` is given, it will be used as the set of substrings
        that divide keys from values.

        When `comment_prefixes` is given, it will be used as the set of
        substrings that prefix comments in empty lines. Comments can be
        indented.

        When `inline_comment_prefixes` is given, it will be used as the set of
        substrings that prefix comments in non-empty lines.

        When `strict` is True, the parser won't allow for any section or option
        duplicates while reading from a single source (file, string or
        dictionary). Default is True.

        When `empty_lines_in_values` is False (default: True), each empty line
        marks the end of an option. Otherwise, internal empty lines of
        a multiline option are kept as part of the value.

        When `allow_no_value` is True (default: False), options without
        values are accepted; the value presented for these is None.

        When `default_section` is given, the name of the special section is
        named accordingly. By default it is called ``"DEFAULT"`` but this can
        be customized to point to any other valid section name. Its current
        value can be retrieved using the ``parser_instance.default_section``
        attribute and may be modified at runtime.

        When `interpolation` is given, it should be an Interpolation subclass
        instance. It will be used as the handler for option value
        pre-processing when using getters. RawConfigParser objects don't do
        any sort of interpolation, whereas ConfigParser uses an instance of
        BasicInterpolation. The library also provides a ``zc.buildout``
        inspired ExtendedInterpolation implementation.

        When `converters` is given, it should be a dictionary where each key
        represents the name of a type converter and each value is a callable
        implementing the conversion from string to the desired datatype. Every
        converter gets its corresponding get*() method on the parser object and
        section proxies.

        When `allow_unnamed_section` is True (default: False), options
        without section are accepted: the section for these is
        ``configparser.UNNAMED_SECTION``.

    sections()
        Return all the configuration section names, sans DEFAULT.

    has_section(section)
        Return whether the given section exists.

    has_option(section, option)
        Return whether the given option exists in the given section.

    options(section)
        Return list of configuration options for the named section.

    read(filenames, encoding=None)
        Read and parse the iterable of named configuration files, given by
        name.  A single filename is also allowed.  Non-existing files
        are ignored.  Return list of successfully read files.

    read_file(f, filename=None)
        Read and parse one configuration file, given as a file object.
        The filename defaults to f.name; it is only used in error
        messages (if f has no `name` attribute, the string `<???>` is used).

    read_string(string)
        Read configuration from a given string.

    read_dict(dictionary)
        Read configuration from a dictionary. Keys are section names,
        values are dictionaries with keys and values that should be present
        in the section. If the used dictionary type preserves order, sections
        and their keys will be added in order. Values are automatically
        converted to strings.

    get(section, option, raw=False, vars=None, fallback=_UNSET)
        Return a string value for the named option.  All % interpolations are
        expanded in the return values, based on the defaults passed into the
        constructor and the DEFAULT section.  Additional substitutions may be
        provided using the `vars` argument, which must be a dictionary whose
        contents override any pre-existing defaults. If `option` is a key in
        `vars`, the value from `vars` is used.

    getint(section, options, raw=False, vars=None, fallback=_UNSET)
        Like get(), but convert value to an integer.

    getfloat(section, options, raw=False, vars=None, fallback=_UNSET)
        Like get(), but convert value to a float.

    getboolean(section, options, raw=False, vars=None, fallback=_UNSET)
        Like get(), but convert value to a boolean (currently case
        insensitively defined as 0, false, no, off for False, and 1, true,
        yes, on for True).  Returns False or True.

    items(section=_UNSET, raw=False, vars=None)
        If section is given, return a list of tuples with (name, value) for
        each option in the section. Otherwise, return a list of tuples with
        (section_name, section_proxy) for each section, including DEFAULTSECT.

    remove_section(section)
        Remove the given file section and all its options.

    remove_option(section, option)
        Remove the given option from the given section.

    set(section, option, value)
        Set the given option.

    write(fp, space_around_delimiters=True)
        Write the configuration state in .ini format. If
        `space_around_delimiters` is True (the default), delimiters
        between keys and values are surrounded by spaces.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\configparser.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:16

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/functools|functools]]
- [[Modules/itertools|itertools]]
- [[Modules/types|types]]
- [[Modules/collections|collections]]

## Classes

- [[Classes/_ChainMap|_ChainMap]] (line 989)
- [[Classes/Error|Error]] (line 177)
- [[Classes/NoSectionError|NoSectionError]] (line 190)
- [[Classes/DuplicateSectionError|DuplicateSectionError]] (line 199)
- [[Classes/DuplicateOptionError|DuplicateOptionError]] (line 225)
- [[Classes/NoOptionError|NoOptionError]] (line 252)
- [[Classes/InterpolationError|InterpolationError]] (line 263)
- [[Classes/InterpolationMissingOptionError|InterpolationMissingOptionError]] (line 273)
- [[Classes/InterpolationSyntaxError|InterpolationSyntaxError]] (line 285)
- [[Classes/InterpolationDepthError|InterpolationDepthError]] (line 293)
- [[Classes/ParsingError|ParsingError]] (line 306)
- [[Classes/MissingSectionHeaderError|MissingSectionHeaderError]] (line 338)
- [[Classes/MultilineContinuationError|MultilineContinuationError]] (line 352)
- [[Classes/_UnnamedSection|_UnnamedSection]] (line 365)
- [[Classes/Interpolation|Interpolation]] (line 380)
- [[Classes/BasicInterpolation|BasicInterpolation]] (line 396)
- [[Classes/ExtendedInterpolation|ExtendedInterpolation]] (line 468)
- [[Classes/_ReadState|_ReadState]] (line 544)
- [[Classes/_Line|_Line]] (line 558)
- [[Classes/RawConfigParser|RawConfigParser]] (line 590)
- [[Classes/ConfigParser|ConfigParser]] (line 1229)
- [[Classes/SectionProxy|SectionProxy]] (line 1261)
- [[Classes/ConverterMapping|ConverterMapping]] (line 1331)

## Functions

