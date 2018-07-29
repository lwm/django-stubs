# Stubs for django.db.models.sql.datastructures (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from collections import OrderedDict
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.fields.related import ForeignObject
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.query_utils import FilteredRelation, PathInfo
from django.db.models.sql.compiler import SQLCompiler
from typing import Any, Dict, List, Optional, Tuple, Union

class MultiJoin(Exception):
    level: Any = ...
    names_with_path: Any = ...
    def __init__(
        self, names_pos: int, path_with_names: List[Tuple[str, List[PathInfo]]]
    ) -> None: ...

class Empty: ...

class Join:
    table_name: Any = ...
    parent_alias: Any = ...
    table_alias: Any = ...
    join_type: Any = ...
    join_cols: Any = ...
    join_field: Any = ...
    nullable: Any = ...
    filtered_relation: Any = ...
    def __init__(
        self,
        table_name: str,
        parent_alias: str,
        table_alias: Optional[str],
        join_type: str,
        join_field: Union[ForeignObjectRel, ForeignObject],
        nullable: bool,
        filtered_relation: Optional[FilteredRelation] = ...,
    ) -> None: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Union[Tuple[str, List[int]], Tuple[str, List[str]], Tuple[str, List[Any]]]: ...
    def relabeled_clone(self, change_map: Union[OrderedDict, Dict[str, str]]) -> Join: ...
    def equals(
        self, other: Union[BaseTable, Join], with_filtered_relation: bool
    ) -> bool: ...
    def __eq__(self, other: Union[BaseTable, Join]) -> bool: ...
    def demote(self) -> Join: ...
    def promote(self) -> Join: ...

class BaseTable:
    join_type: Any = ...
    parent_alias: Any = ...
    filtered_relation: Any = ...
    table_name: Any = ...
    table_alias: Any = ...
    def __init__(self, table_name: str, alias: Optional[str]) -> None: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[Any]]: ...
    def relabeled_clone(self, change_map: OrderedDict) -> BaseTable: ...
    def equals(self, other: Join, with_filtered_relation: bool) -> bool: ...