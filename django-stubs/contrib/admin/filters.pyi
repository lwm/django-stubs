from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from django.contrib.admin.options import ModelAdmin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.base import Model
from django.db.models.fields import BooleanField, DateField, Field
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related import RelatedField
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.db.models.query import QuerySet


class ListFilter:
    title: Any = ...
    template: str = ...
    used_parameters: Any = ...
    def __init__(
        self,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
    ) -> None: ...
    def has_output(self) -> None: ...
    def choices(self, changelist: Any) -> None: ...
    def queryset(self, request: Any, queryset: Any) -> None: ...
    def expected_parameters(self) -> None: ...

class SimpleListFilter(ListFilter):
    parameter_name: Any = ...
    lookup_choices: Any = ...
    def __init__(
        self,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
    ) -> None: ...
    def has_output(self) -> bool: ...
    def value(self) -> Optional[str]: ...
    def lookups(self, request: Any, model_admin: Any) -> None: ...
    def expected_parameters(self): ...
    def choices(self, changelist: Any) -> None: ...

class FieldListFilter(ListFilter):
    field: Any = ...
    field_path: Any = ...
    title: Any = ...
    def __init__(
        self,
        field: Union[Field, reverse_related.ForeignObjectRel],
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    def has_output(self) -> bool: ...
    def queryset(
        self, request: WSGIRequest, queryset: QuerySet
    ) -> QuerySet: ...
    @classmethod
    def register(
        cls,
        test: Callable,
        list_filter_class: Type[
            Union[
                BooleanFieldListFilter,
                AllValuesFieldListFilter,
                DateFieldListFilter,
                RelatedFieldListFilter,
                ChoicesFieldListFilter,
            ]
        ],
        take_priority: bool = ...,
    ) -> None: ...
    @classmethod
    def create(
        cls,
        field: Union[Field, reverse_related.ForeignObjectRel],
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> FieldListFilter: ...

class RelatedFieldListFilter(FieldListFilter):
    field: django.db.models.fields.related.ForeignKey
    field_path: str
    used_parameters: Dict[Any, Any]
    lookup_kwarg: str = ...
    lookup_kwarg_isnull: str = ...
    lookup_val: None = ...
    lookup_val_isnull: None = ...
    lookup_choices: Any = ...
    lookup_title: Any = ...
    title: str = ...
    empty_value_display: Any = ...
    def __init__(
        self,
        field: FieldCacheMixin,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    @property
    def include_empty_choice(self) -> bool: ...
    def has_output(self) -> bool: ...
    def expected_parameters(self) -> List[str]: ...
    def field_choices(
        self,
        field: FieldCacheMixin,
        request: WSGIRequest,
        model_admin: ModelAdmin,
    ) -> Union[List[Tuple[str, str]], List[Tuple[int, str]]]: ...
    def choices(self, changelist: Any) -> None: ...

class BooleanFieldListFilter(FieldListFilter):
    lookup_kwarg: Any = ...
    lookup_kwarg2: Any = ...
    lookup_val: Any = ...
    lookup_val2: Any = ...
    def __init__(
        self,
        field: BooleanField,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    def expected_parameters(self) -> List[str]: ...
    def choices(self, changelist: Any) -> None: ...

class ChoicesFieldListFilter(FieldListFilter):
    field: django.db.models.fields.IntegerField
    field_path: str
    title: str
    used_parameters: Dict[Any, Any]
    lookup_kwarg: str = ...
    lookup_kwarg_isnull: str = ...
    lookup_val: None = ...
    lookup_val_isnull: None = ...
    def __init__(
        self,
        field: Field,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    def expected_parameters(self) -> List[str]: ...
    def choices(self, changelist: Any) -> None: ...

class DateFieldListFilter(FieldListFilter):
    field_generic: Any = ...
    date_params: Any = ...
    lookup_kwarg_since: Any = ...
    lookup_kwarg_until: Any = ...
    links: Any = ...
    lookup_kwarg_isnull: Any = ...
    def __init__(
        self,
        field: DateField,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    def expected_parameters(self) -> List[str]: ...
    def choices(self, changelist: Any) -> None: ...

class AllValuesFieldListFilter(FieldListFilter):
    field: django.db.models.fields.CharField
    field_path: str
    title: str
    used_parameters: Dict[Any, Any]
    lookup_kwarg: str = ...
    lookup_kwarg_isnull: str = ...
    lookup_val: None = ...
    lookup_val_isnull: None = ...
    empty_value_display: django.utils.safestring.SafeText = ...
    lookup_choices: django.db.models.query.QuerySet = ...
    def __init__(
        self,
        field: Field,
        request: WSGIRequest,
        params: Dict[str, str],
        model: Type[Model],
        model_admin: ModelAdmin,
        field_path: str,
    ) -> None: ...
    def expected_parameters(self) -> List[str]: ...
    def choices(self, changelist: Any) -> None: ...

class RelatedOnlyFieldListFilter(RelatedFieldListFilter):
    field: django.db.models.fields.related.ForeignKey
    field_path: str
    lookup_kwarg: str
    lookup_kwarg_isnull: str
    lookup_val: None
    lookup_val_isnull: None
    title: str
    used_parameters: Dict[Any, Any]
    def field_choices(
        self, field: RelatedField, request: WSGIRequest, model_admin: ModelAdmin
    ) -> Union[List[Tuple[str, str]], List[Tuple[int, str]]]: ...
