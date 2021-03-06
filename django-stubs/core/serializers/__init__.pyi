from collections import OrderedDict
from typing import (Any, Callable, Dict, Iterator, List, Optional, Tuple, Type,
                    Union)

from django.apps.config import AppConfig
from django.core.serializers.python import Serializer
from django.core.serializers.xml_serializer import Deserializer, Serializer
from django.db.models.base import Model
from django.db.models.query import QuerySet

BUILTIN_SERIALIZERS: Any

class BadSerializer:
    internal_use_only: bool = ...
    exception: ModuleNotFoundError = ...
    def __init__(self, exception: ImportError) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def register_serializer(
    format: str,
    serializer_module: str,
    serializers: Optional[Dict[str, Any]] = ...,
) -> None: ...
def unregister_serializer(format: str) -> None: ...
def get_serializer(
    format: str
) -> Union[Type[Union[Serializer, Serializer]], BadSerializer]: ...
def get_serializer_formats() -> List[str]: ...
def get_public_serializer_formats() -> List[str]: ...
def get_deserializer(format: str) -> Union[Callable, Type[Deserializer]]: ...
def serialize(
    format: str,
    queryset: Union[QuerySet, List[Model], Iterator[Any]],
    **options: Any
) -> Optional[Union[str, bytes, List[OrderedDict]]]: ...
def deserialize(
    format: str, stream_or_string: Any, **options: Any
) -> Union[Deserializer, Iterator[Any]]: ...
def sort_dependencies(
    app_list: Union[
        List[Tuple[str, List[Type[Model]]]], List[Tuple[AppConfig, None]]
    ]
) -> List[Type[Model]]: ...
