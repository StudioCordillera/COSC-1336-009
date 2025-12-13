---
type: class
name: _Unparser
module: ast
lineno: 739
tags:
  - python
  - class
---

# Class: _Unparser

## Overview

Methods in this class recursively traverse an AST and
output source code for the abstract syntax; original formatting
is disregarded.

**Module:** [[Modules/ast|ast]]
**Line:** 739

## Inheritance

**Inherits from:**
- [[Classes/NodeVisitor|NodeVisitor]]

## Methods

### Constructors
- [[Functions/__init___5932|__init__()]] (line 744)

### Methods
- [[Functions/interleave_5933|interleave()]] (line 751)
- [[Functions/items_view_5934|items_view()]] (line 763)
- [[Functions/maybe_newline_5935|maybe_newline()]] (line 773)
- [[Functions/fill_5936|fill()]] (line 778)
- [[Functions/write_5937|write()]] (line 784)
- [[Functions/buffered_5938|buffered()]] (line 789)
- [[Functions/block_5939|block()]] (line 799)
- [[Functions/delimit_5940|delimit()]] (line 813)
- [[Functions/delimit_if_5941|delimit_if()]] (line 821)
- [[Functions/require_parens_5942|require_parens()]] (line 827)
- [[Functions/get_precedence_5943|get_precedence()]] (line 831)
- [[Functions/set_precedence_5944|set_precedence()]] (line 834)
- [[Functions/get_raw_docstring_5945|get_raw_docstring()]] (line 838)
- [[Functions/get_type_comment_5946|get_type_comment()]] (line 854)
- [[Functions/traverse_5947|traverse()]] (line 859)
- [[Functions/visit_5948|visit()]] (line 869)
- [[Functions/_write_docstring_and_traverse_body_5949|_write_docstring_and_traverse_body()]] (line 876)
- [[Functions/visit_Module_5950|visit_Module()]] (line 883)
- [[Functions/visit_FunctionType_5951|visit_FunctionType()]] (line 891)
- [[Functions/visit_Expr_5952|visit_Expr()]] (line 900)
- [[Functions/visit_NamedExpr_5953|visit_NamedExpr()]] (line 905)
- [[Functions/visit_Import_5954|visit_Import()]] (line 912)
- [[Functions/visit_ImportFrom_5955|visit_ImportFrom()]] (line 916)
- [[Functions/visit_Assign_5956|visit_Assign()]] (line 924)
- [[Functions/visit_AugAssign_5957|visit_AugAssign()]] (line 934)
- [[Functions/visit_AnnAssign_5958|visit_AnnAssign()]] (line 940)
- [[Functions/visit_Return_5959|visit_Return()]] (line 950)
- [[Functions/visit_Pass_5960|visit_Pass()]] (line 956)
- [[Functions/visit_Break_5961|visit_Break()]] (line 959)
- [[Functions/visit_Continue_5962|visit_Continue()]] (line 962)
- [[Functions/visit_Delete_5963|visit_Delete()]] (line 965)
- [[Functions/visit_Assert_5964|visit_Assert()]] (line 969)
- [[Functions/visit_Global_5965|visit_Global()]] (line 976)
- [[Functions/visit_Nonlocal_5966|visit_Nonlocal()]] (line 980)
- [[Functions/visit_Await_5967|visit_Await()]] (line 984)
- [[Functions/visit_Yield_5968|visit_Yield()]] (line 992)
- [[Functions/visit_YieldFrom_5969|visit_YieldFrom()]] (line 1000)
- [[Functions/visit_Raise_5970|visit_Raise()]] (line 1008)
- [[Functions/do_visit_try_5971|do_visit_try()]] (line 1020)
- [[Functions/visit_Try_5972|visit_Try()]] (line 1035)
- [[Functions/visit_TryStar_5973|visit_TryStar()]] (line 1043)
- [[Functions/visit_ExceptHandler_5974|visit_ExceptHandler()]] (line 1051)
- [[Functions/visit_ClassDef_5975|visit_ClassDef()]] (line 1062)
- [[Functions/visit_FunctionDef_5976|visit_FunctionDef()]] (line 1088)
- [[Functions/visit_AsyncFunctionDef_5977|visit_AsyncFunctionDef()]] (line 1091)
- [[Functions/_function_helper_5978|_function_helper()]] (line 1094)
- [[Functions/_type_params_helper_5979|_type_params_helper()]] (line 1111)
- [[Functions/visit_TypeVar_5980|visit_TypeVar()]] (line 1116)
- [[Functions/visit_TypeVarTuple_5981|visit_TypeVarTuple()]] (line 1125)
- [[Functions/visit_ParamSpec_5982|visit_ParamSpec()]] (line 1131)
- [[Functions/visit_TypeAlias_5983|visit_TypeAlias()]] (line 1137)
- [[Functions/visit_For_5984|visit_For()]] (line 1144)
- [[Functions/visit_AsyncFor_5985|visit_AsyncFor()]] (line 1147)
- [[Functions/_for_helper_5986|_for_helper()]] (line 1150)
- [[Functions/visit_If_5987|visit_If()]] (line 1163)
- [[Functions/visit_While_5988|visit_While()]] (line 1181)
- [[Functions/visit_With_5989|visit_With()]] (line 1191)
- [[Functions/visit_AsyncWith_5990|visit_AsyncWith()]] (line 1197)
- [[Functions/_str_literal_helper_5991|_str_literal_helper()]] (line 1203)
- [[Functions/_write_str_avoiding_backslashes_5992|_write_str_avoiding_backslashes()]] (line 1241)
- [[Functions/visit_JoinedStr_5993|visit_JoinedStr()]] (line 1247)
- [[Functions/_write_fstring_inner_5994|_write_fstring_inner()]] (line 1299)
- [[Functions/visit_FormattedValue_5995|visit_FormattedValue()]] (line 1318)
- [[Functions/visit_Name_5996|visit_Name()]] (line 1336)
- [[Functions/_write_docstring_5997|_write_docstring()]] (line 1339)
- [[Functions/_write_constant_5998|_write_constant()]] (line 1345)
- [[Functions/visit_Constant_5999|visit_Constant()]] (line 1357)
- [[Functions/visit_List_6000|visit_List()]] (line 1369)
- [[Functions/visit_ListComp_6001|visit_ListComp()]] (line 1373)
- [[Functions/visit_GeneratorExp_6002|visit_GeneratorExp()]] (line 1379)
- [[Functions/visit_SetComp_6003|visit_SetComp()]] (line 1385)
- [[Functions/visit_DictComp_6004|visit_DictComp()]] (line 1391)
- [[Functions/visit_comprehension_6005|visit_comprehension()]] (line 1399)
- [[Functions/visit_IfExp_6006|visit_IfExp()]] (line 1413)
- [[Functions/visit_Set_6007|visit_Set()]] (line 1423)
- [[Functions/visit_Dict_6008|visit_Dict()]] (line 1432)
- [[Functions/visit_Tuple_6009|visit_Tuple()]] (line 1454)
- [[Functions/visit_UnaryOp_6010|visit_UnaryOp()]] (line 1470)
- [[Functions/visit_BinOp_6011|visit_BinOp()]] (line 1515)
- [[Functions/visit_Compare_6012|visit_Compare()]] (line 1545)
- [[Functions/visit_BoolOp_6013|visit_BoolOp()]] (line 1556)
- [[Functions/visit_Attribute_6014|visit_Attribute()]] (line 1570)
- [[Functions/visit_Call_6015|visit_Call()]] (line 1581)
- [[Functions/visit_Subscript_6016|visit_Subscript()]] (line 1599)
- [[Functions/visit_Starred_6017|visit_Starred()]] (line 1615)
- [[Functions/visit_Ellipsis_6018|visit_Ellipsis()]] (line 1620)
- [[Functions/visit_Slice_6019|visit_Slice()]] (line 1623)
- [[Functions/visit_Match_6020|visit_Match()]] (line 1633)
- [[Functions/visit_arg_6021|visit_arg()]] (line 1640)
- [[Functions/visit_arguments_6022|visit_arguments()]] (line 1646)
- [[Functions/visit_keyword_6023|visit_keyword()]] (line 1697)
- [[Functions/visit_Lambda_6024|visit_Lambda()]] (line 1705)
- [[Functions/visit_alias_6025|visit_alias()]] (line 1716)
- [[Functions/visit_withitem_6026|visit_withitem()]] (line 1721)
- [[Functions/visit_match_case_6027|visit_match_case()]] (line 1727)
- [[Functions/visit_MatchValue_6028|visit_MatchValue()]] (line 1736)
- [[Functions/visit_MatchSingleton_6029|visit_MatchSingleton()]] (line 1739)
- [[Functions/visit_MatchSequence_6030|visit_MatchSequence()]] (line 1742)
- [[Functions/visit_MatchStar_6031|visit_MatchStar()]] (line 1748)
- [[Functions/visit_MatchMapping_6032|visit_MatchMapping()]] (line 1754)
- [[Functions/visit_MatchClass_6033|visit_MatchClass()]] (line 1774)
- [[Functions/visit_MatchAs_6034|visit_MatchAs()]] (line 1797)
- [[Functions/visit_MatchOr_6035|visit_MatchOr()]] (line 1810)
