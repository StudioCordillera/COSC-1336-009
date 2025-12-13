---
type: module
name: inspect
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\inspect.py
is_package: False
analyzed_at: 2025-12-10T03:46:26.679222
tags:
  - python
  - module
---

# Module: inspect

## Overview

Get useful information from live Python objects.

This module encapsulates the interface provided by the internal special
attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
It also provides some help for examining source code and class layout.

Here are some of the useful functions provided by this module:

    ismodule(), isclass(), ismethod(), isfunction(), isgeneratorfunction(),
        isgenerator(), istraceback(), isframe(), iscode(), isbuiltin(),
        isroutine() - check object types
    getmembers() - get members of an object that satisfy a given condition

    getfile(), getsourcefile(), getsource() - find an object's source code
    getdoc(), getcomments() - get documentation on an object
    getmodule() - determine the module that an object came from
    getclasstree() - arrange classes so as to represent their hierarchy

    getargvalues(), getcallargs() - get info about function arguments
    getfullargspec() - same, with support for Python 3 features
    formatargvalues() - format an argument spec
    getouterframes(), getinnerframes() - get info about frames
    currentframe() - get the current stack frame
    stack(), trace() - get info about frames on the stack or in a traceback

    signature() - get a Signature object for the callable

    get_annotations() - safely compute an object's annotations

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\inspect.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:26

## Dependencies

This module imports:
- [[Modules/weakref|weakref]]
- [[Modules/operator|operator]]
- [[Modules/functools|functools]]
- [[Modules/types|types]]
- [[Modules/builtins|builtins]]
- [[Modules/collections|collections]]
- [[Modules/argparse|argparse]]
- [[Modules/sys|sys]]
- [[Modules/enum|enum]]
- [[Modules/itertools|itertools]]
- [[Modules/linecache|linecache]]
- [[Modules/os|os]]
- [[Modules/re|re]]
- [[Modules/abc|abc]]

## Used By

This module is imported by:
- [[Modules/pkgutil|pkgutil]]
- [[Modules/ast|ast]]

## Classes

- [[Classes/attrgetter|attrgetter]] (line 232)
- [[Classes/OrderedDict|OrderedDict]] (line 86)
- [[Classes/ClassFoundException|ClassFoundException]] (line 1048)
- [[Classes/EndOfBlock|EndOfBlock]] (line 1156)
- [[Classes/BlockFinder|BlockFinder]] (line 1158)
- [[Classes/Traceback|Traceback]] (line 1638)
- [[Classes/FrameInfo|FrameInfo]] (line 1710)
- [[Classes/_void|_void]] (line 2690)
- [[Classes/_empty|_empty]] (line 2694)
- [[Classes/_ParameterKind|_ParameterKind]] (line 2698)
- [[Classes/Parameter|Parameter]] (line 2722)
- [[Classes/BoundArguments|BoundArguments]] (line 2882)
- [[Classes/Signature|Signature]] (line 3012)
- [[Classes/BufferFlags|BufferFlags]] (line 3379)

## Functions

- [[Functions/namedtuple_5656|namedtuple()]] (line 358)
- [[Functions/get_annotations_5680|get_annotations()]] (line 176)
- [[Functions/ismodule_5681|ismodule()]] (line 298)
- [[Functions/isclass_5682|isclass()]] (line 302)
- [[Functions/ismethod_5683|ismethod()]] (line 306)
- [[Functions/ismethoddescriptor_5684|ismethoddescriptor()]] (line 310)
- [[Functions/isdatadescriptor_5685|isdatadescriptor()]] (line 338)
- [[Functions/ismemberdescriptor_5686|ismemberdescriptor()]] (line 362)
- [[Functions/isgetsetdescriptor_5687|isgetsetdescriptor()]] (line 379)
- [[Functions/isfunction_5688|isfunction()]] (line 386)
- [[Functions/_has_code_flag_5689|_has_code_flag()]] (line 399)
- [[Functions/isgeneratorfunction_5690|isgeneratorfunction()]] (line 412)
- [[Functions/_has_coroutine_mark_5691|_has_coroutine_mark()]] (line 422)
- [[Functions/markcoroutinefunction_5692|markcoroutinefunction()]] (line 428)
- [[Functions/iscoroutinefunction_5693|iscoroutinefunction()]] (line 437)
- [[Functions/isasyncgenfunction_5694|isasyncgenfunction()]] (line 445)
- [[Functions/isasyncgen_5695|isasyncgen()]] (line 453)
- [[Functions/isgenerator_5696|isgenerator()]] (line 457)
- [[Functions/iscoroutine_5697|iscoroutine()]] (line 474)
- [[Functions/isawaitable_5698|isawaitable()]] (line 478)
- [[Functions/istraceback_5699|istraceback()]] (line 485)
- [[Functions/isframe_5700|isframe()]] (line 495)
- [[Functions/iscode_5701|iscode()]] (line 509)
- [[Functions/isbuiltin_5702|isbuiltin()]] (line 534)
- [[Functions/ismethodwrapper_5703|ismethodwrapper()]] (line 543)
- [[Functions/isroutine_5704|isroutine()]] (line 547)
- [[Functions/isabstract_5705|isabstract()]] (line 555)
- [[Functions/_getmembers_5706|_getmembers()]] (line 579)
- [[Functions/getmembers_5707|getmembers()]] (line 621)
- [[Functions/getmembers_static_5708|getmembers_static()]] (line 626)
- [[Functions/classify_class_attrs_5709|classify_class_attrs()]] (line 642)
- [[Functions/getmro_5710|getmro()]] (line 758)
- [[Functions/unwrap_5711|unwrap()]] (line 764)
- [[Functions/indentsize_5712|indentsize()]] (line 796)
- [[Functions/_findclass_5713|_findclass()]] (line 801)
- [[Functions/_finddoc_5714|_finddoc()]] (line 811)
- [[Functions/getdoc_5715|getdoc()]] (line 872)
- [[Functions/cleandoc_5716|cleandoc()]] (line 891)
- [[Functions/getfile_5717|getfile()]] (line 919)
- [[Functions/getmodulename_5718|getmodulename()]] (line 947)
- [[Functions/getsourcefile_5719|getsourcefile()]] (line 959)
- [[Functions/getabsfile_5720|getabsfile()]] (line 988)
- [[Functions/getmodule_5721|getmodule()]] (line 1000)
- [[Functions/findsource_5722|findsource()]] (line 1052)
- [[Functions/getcomments_5723|getcomments()]] (line 1111)
- [[Functions/getblock_5726|getblock()]] (line 1212)
- [[Functions/getsourcelines_5727|getsourcelines()]] (line 1231)
- [[Functions/getsource_5728|getsource()]] (line 1252)
- [[Functions/walktree_5729|walktree()]] (line 1262)
- [[Functions/getclasstree_5730|getclasstree()]] (line 1272)
- [[Functions/getargs_5731|getargs()]] (line 1301)
- [[Functions/getfullargspec_5732|getfullargspec()]] (line 1331)
- [[Functions/getargvalues_5733|getargvalues()]] (line 1426)
- [[Functions/formatannotation_5734|formatannotation()]] (line 1436)
- [[Functions/formatannotationrelativeto_5735|formatannotationrelativeto()]] (line 1450)
- [[Functions/formatargvalues_5736|formatargvalues()]] (line 1457)
- [[Functions/_missing_arguments_5737|_missing_arguments()]] (line 1480)
- [[Functions/_too_many_5738|_too_many()]] (line 1496)
- [[Functions/getcallargs_5739|getcallargs()]] (line 1517)
- [[Functions/getclosurevars_5740|getclosurevars()]] (line 1579)
- [[Functions/_get_code_position_from_tb_5743|_get_code_position_from_tb()]] (line 1650)
- [[Functions/_get_code_position_5744|_get_code_position()]] (line 1654)
- [[Functions/getframeinfo_5745|getframeinfo()]] (line 1661)
- [[Functions/getlineno_5746|getlineno()]] (line 1704)
- [[Functions/getouterframes_5749|getouterframes()]] (line 1722)
- [[Functions/getinnerframes_5750|getinnerframes()]] (line 1735)
- [[Functions/currentframe_5751|currentframe()]] (line 1748)
- [[Functions/stack_5752|stack()]] (line 1752)
- [[Functions/trace_5753|trace()]] (line 1756)
- [[Functions/_check_instance_5754|_check_instance()]] (line 1770)
- [[Functions/_check_class_5755|_check_class()]] (line 1779)
- [[Functions/_shadowed_dict_from_weakref_mro_tuple_5756|_shadowed_dict_from_weakref_mro_tuple()]] (line 1787)
- [[Functions/_shadowed_dict_5757|_shadowed_dict()]] (line 1805)
- [[Functions/getattr_static_5758|getattr_static()]] (line 1818)
- [[Functions/getgeneratorstate_5759|getgeneratorstate()]] (line 1875)
- [[Functions/getgeneratorlocals_5760|getgeneratorlocals()]] (line 1893)
- [[Functions/getcoroutinestate_5761|getcoroutinestate()]] (line 1917)
- [[Functions/getcoroutinelocals_5762|getcoroutinelocals()]] (line 1935)
- [[Functions/getasyncgenstate_5763|getasyncgenstate()]] (line 1956)
- [[Functions/getasyncgenlocals_5764|getasyncgenlocals()]] (line 1974)
- [[Functions/_signature_get_user_defined_method_5765|_signature_get_user_defined_method()]] (line 2003)
- [[Functions/_signature_get_partial_5766|_signature_get_partial()]] (line 2029)
- [[Functions/_signature_bound_method_5767|_signature_bound_method()]] (line 2105)
- [[Functions/_signature_is_builtin_5768|_signature_is_builtin()]] (line 2131)
- [[Functions/_signature_is_functionlike_5769|_signature_is_functionlike()]] (line 2145)
- [[Functions/_signature_strip_non_python_syntax_5770|_signature_strip_non_python_syntax()]] (line 2170)
- [[Functions/_signature_fromstr_5771|_signature_fromstr()]] (line 2220)
- [[Functions/_signature_from_builtin_5772|_signature_from_builtin()]] (line 2367)
- [[Functions/_signature_from_function_5773|_signature_from_function()]] (line 2383)
- [[Functions/_descriptor_get_5774|_descriptor_get()]] (line 2478)
- [[Functions/_signature_from_callable_5775|_signature_from_callable()]] (line 2487)
- [[Functions/signature_5815|signature()]] (line 3373)
- [[Functions/_main_5816|_main()]] (line 3401)
