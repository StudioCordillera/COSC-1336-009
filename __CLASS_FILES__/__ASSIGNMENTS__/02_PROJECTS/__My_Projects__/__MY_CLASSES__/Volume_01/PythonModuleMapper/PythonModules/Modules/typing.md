---
type: module
name: typing
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\typing.py
is_package: False
analyzed_at: 2025-12-10T03:46:23.822201
tags:
  - python
  - module
---

# Module: typing

## Overview

The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs.

Among other things, the module includes the following:
* Generic, Protocol, and internal machinery to support generic aliases.
  All subscripted types like X[int], Union[int, str] are generic aliases.
* Various "special forms" that have unique meanings in type annotations:
  NoReturn, Never, ClassVar, Self, Concatenate, Unpack, and others.
* Classes whose instances can be type arguments to generic classes and functions:
  TypeVar, ParamSpec, TypeVarTuple.
* Public helper functions: get_type_hints, overload, cast, final, and others.
* Several protocols to support duck-typing:
  SupportsFloat, SupportsIndex, SupportsAbs, and others.
* Special types: NewType, NamedTuple, TypedDict.
* Deprecated aliases for builtin types and collections.abc ABCs.

Any name not present in __all__ is an implementation detail
that may be changed without notice. Use at your own risk!

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\typing.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:23

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/operator|operator]]
- [[Modules/functools|functools]]
- [[Modules/types|types]]
- [[Modules/copyreg|copyreg]]
- [[Modules/collections|collections]]

## Classes

- [[Classes/_Sentinel|_Sentinel]] (line 454)
- [[Classes/_Final|_Final]] (line 506)
- [[Classes/_NotIterable|_NotIterable]] (line 516)
- [[Classes/_SpecialForm|_SpecialForm]] (line 536)
- [[Classes/_TypedCacheSpecialForm|_TypedCacheSpecialForm]] (line 579)
- [[Classes/_AnyMeta|_AnyMeta]] (line 586)
- [[Classes/Any|Any]] (line 598)
- [[Classes/ForwardRef|ForwardRef]] (line 1015)
- [[Classes/_BaseGenericAlias|_BaseGenericAlias]] (line 1297)
- [[Classes/_GenericAlias|_GenericAlias]] (line 1397)
- [[Classes/_SpecialGenericAlias|_SpecialGenericAlias]] (line 1622)
- [[Classes/_DeprecatedGenericAlias|_DeprecatedGenericAlias]] (line 1682)
- [[Classes/_CallableGenericAlias|_CallableGenericAlias]] (line 1697)
- [[Classes/_CallableType|_CallableType]] (line 1714)
- [[Classes/_TupleType|_TupleType]] (line 1747)
- [[Classes/_UnionGenericAlias|_UnionGenericAlias]] (line 1761)
- [[Classes/_LiteralGenericAlias|_LiteralGenericAlias]] (line 1806)
- [[Classes/_ConcatenateGenericAlias|_ConcatenateGenericAlias]] (line 1817)
- [[Classes/_UnpackGenericAlias|_UnpackGenericAlias]] (line 1877)
- [[Classes/_TypingEllipsis|_TypingEllipsis]] (line 1906)
- [[Classes/_ProtocolMeta|_ProtocolMeta]] (line 2051)
- [[Classes/Protocol|Protocol]] (line 2162)
- [[Classes/_AnnotatedAlias|_AnnotatedAlias]] (line 2215)
- [[Classes/SupportsInt|SupportsInt]] (line 2903)
- [[Classes/SupportsFloat|SupportsFloat]] (line 2914)
- [[Classes/SupportsComplex|SupportsComplex]] (line 2925)
- [[Classes/SupportsBytes|SupportsBytes]] (line 2936)
- [[Classes/SupportsIndex|SupportsIndex]] (line 2947)
- [[Classes/SupportsAbs|SupportsAbs]] (line 2958)
- [[Classes/SupportsRound|SupportsRound]] (line 2969)
- [[Classes/NamedTupleMeta|NamedTupleMeta]] (line 2997)
- [[Classes/_TypedDictMeta|_TypedDictMeta]] (line 3141)
- [[Classes/NewType|NewType]] (line 3390)
- [[Classes/IO|IO]] (line 3460)
- [[Classes/BinaryIO|BinaryIO]] (line 3559)
- [[Classes/TextIO|TextIO]] (line 3573)
- [[Classes/_IdentityCallable|_IdentityCallable]] (line 3627)

## Functions

- [[Functions/_type_convert_4635|_type_convert()]] (line 164)
- [[Functions/_type_check_4636|_type_check()]] (line 173)
- [[Functions/_is_param_expr_4637|_is_param_expr()]] (line 206)
- [[Functions/_should_unflatten_callable_args_4638|_should_unflatten_callable_args()]] (line 211)
- [[Functions/_type_repr_4639|_type_repr()]] (line 235)
- [[Functions/_collect_type_parameters_4640|_collect_type_parameters()]] (line 260)
- [[Functions/_check_generic_specialization_4641|_check_generic_specialization()]] (line 310)
- [[Functions/_unpack_args_4642|_unpack_args()]] (line 341)
- [[Functions/_deduplicate_4643|_deduplicate()]] (line 351)
- [[Functions/_deduplicate_unhashable_4644|_deduplicate_unhashable()]] (line 361)
- [[Functions/_compare_args_orderless_4645|_compare_args_orderless()]] (line 368)
- [[Functions/_remove_dups_flatten_4646|_remove_dups_flatten()]] (line 379)
- [[Functions/_flatten_literal_params_4647|_flatten_literal_params()]] (line 395)
- [[Functions/_tp_cache_4648|_tp_cache()]] (line 410)
- [[Functions/_deprecation_warning_for_no_type_params_passed_4649|_deprecation_warning_for_no_type_params_passed()]] (line 441)
- [[Functions/_eval_type_4651|_eval_type()]] (line 463)
- [[Functions/NoReturn_4668|NoReturn()]] (line 617)
- [[Functions/Never_4669|Never()]] (line 638)
- [[Functions/Self_4670|Self()]] (line 663)
- [[Functions/LiteralString_4671|LiteralString()]] (line 683)
- [[Functions/ClassVar_4672|ClassVar()]] (line 710)
- [[Functions/Final_4673|Final()]] (line 732)
- [[Functions/Union_4674|Union()]] (line 754)
- [[Functions/_make_union_4675|_make_union()]] (line 797)
- [[Functions/Optional_4676|Optional()]] (line 807)
- [[Functions/Literal_4677|Literal()]] (line 814)
- [[Functions/TypeAlias_4678|TypeAlias()]] (line 848)
- [[Functions/Concatenate_4679|Concatenate()]] (line 865)
- [[Functions/TypeGuard_4680|TypeGuard()]] (line 891)
- [[Functions/TypeIs_4681|TypeIs()]] (line 947)
- [[Functions/_is_unpacked_typevartuple_4689|_is_unpacked_typevartuple()]] (line 1122)
- [[Functions/_is_typevar_like_4690|_is_typevar_like()]] (line 1127)
- [[Functions/_typevar_subst_4691|_typevar_subst()]] (line 1131)
- [[Functions/_typevartuple_prepare_subst_4692|_typevartuple_prepare_subst()]] (line 1140)
- [[Functions/_paramspec_subst_4693|_paramspec_subst()]] (line 1181)
- [[Functions/_paramspec_prepare_subst_4694|_paramspec_prepare_subst()]] (line 1190)
- [[Functions/_generic_class_getitem_4695|_generic_class_getitem()]] (line 1208)
- [[Functions/_generic_init_subclass_4696|_generic_init_subclass()]] (line 1256)
- [[Functions/_is_dunder_4697|_is_dunder()]] (line 1294)
- [[Functions/_value_and_type_iter_4742|_value_and_type_iter()]] (line 1802)
- [[Functions/Unpack_4746|Unpack()]] (line 1827)
- [[Functions/_get_protocol_attrs_4751|_get_protocol_attrs()]] (line 1927)
- [[Functions/_no_init_or_replace_init_4752|_no_init_or_replace_init()]] (line 1944)
- [[Functions/_caller_4753|_caller()]] (line 1973)
- [[Functions/_allow_reckless_class_checks_4754|_allow_reckless_class_checks()]] (line 1984)
- [[Functions/_lazy_load_getattr_static_4755|_lazy_load_getattr_static()]] (line 2004)
- [[Functions/_pickle_psargs_4756|_pickle_psargs()]] (line 2013)
- [[Functions/_pickle_pskwargs_4757|_pickle_pskwargs()]] (line 2018)
- [[Functions/_type_check_issubclass_arg_1_4758|_type_check_issubclass_arg_1()]] (line 2034)
- [[Functions/_proto_hook_4763|_proto_hook()]] (line 2139)
- [[Functions/Annotated_4773|Annotated()]] (line 2269)
- [[Functions/runtime_checkable_4774|runtime_checkable()]] (line 2329)
- [[Functions/cast_4775|cast()]] (line 2371)
- [[Functions/assert_type_4776|assert_type()]] (line 2382)
- [[Functions/get_type_hints_4777|get_type_hints()]] (line 2403)
- [[Functions/_strip_annotations_4778|_strip_annotations()]] (line 2503)
- [[Functions/get_origin_4779|get_origin()]] (line 2528)
- [[Functions/get_args_4780|get_args()]] (line 2558)
- [[Functions/is_typeddict_4781|is_typeddict()]] (line 2584)
- [[Functions/assert_never_4782|assert_never()]] (line 2605)
- [[Functions/no_type_check_4783|no_type_check()]] (line 2630)
- [[Functions/no_type_check_decorator_4784|no_type_check_decorator()]] (line 2666)
- [[Functions/_overload_dummy_4785|_overload_dummy()]] (line 2683)
- [[Functions/overload_4786|overload()]] (line 2696)
- [[Functions/get_overloads_4787|get_overloads()]] (line 2737)
- [[Functions/clear_overloads_4788|clear_overloads()]] (line 2749)
- [[Functions/final_4789|final()]] (line 2754)
- [[Functions/_make_nmtuple_4797|_make_nmtuple()]] (line 2979)
- [[Functions/NamedTuple_4799|NamedTuple()]] (line 3048)
- [[Functions/_namedtuple_mro_entries_4800|_namedtuple_mro_entries()]] (line 3112)
- [[Functions/_get_typeddict_qualifiers_4801|_get_typeddict_qualifiers()]] (line 3119)
- [[Functions/TypedDict_4804|TypedDict()]] (line 3240)
- [[Functions/Required_4805|Required()]] (line 3328)
- [[Functions/NotRequired_4806|NotRequired()]] (line 3352)
- [[Functions/ReadOnly_4807|ReadOnly()]] (line 3371)
- [[Functions/reveal_type_4842|reveal_type()]] (line 3608)
- [[Functions/dataclass_transform_4844|dataclass_transform()]] (line 3632)
- [[Functions/override_4845|override()]] (line 3719)
- [[Functions/is_protocol_4846|is_protocol()]] (line 3754)
- [[Functions/get_protocol_members_4847|get_protocol_members()]] (line 3775)
- [[Functions/__getattr___4848|__getattr__()]] (line 3794)
