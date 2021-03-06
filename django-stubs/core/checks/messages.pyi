from typing import Any, Optional, Union

DEBUG: int
INFO: int
WARNING: int
ERROR: int
CRITICAL: int

class CheckMessage:
    level: Any = ...
    msg: Any = ...
    hint: Any = ...
    obj: Any = ...
    id: Any = ...
    def __init__(
        self,
        level: int,
        msg: str,
        hint: Optional[str] = ...,
        obj: Any = ...,
        id: Optional[str] = ...,
    ) -> None: ...
    def __eq__(self, other: Union[str, CheckMessage]) -> bool: ...
    def is_serious(self, level: int = ...) -> bool: ...
    def is_silenced(self) -> bool: ...

class Debug(CheckMessage):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Info(CheckMessage):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Warning(CheckMessage):
    hint: str
    id: str
    level: int
    msg: str
    obj: django.db.models.fields.related.ForeignKey
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Error(CheckMessage):
    hint: None
    id: str
    level: int
    msg: str
    obj: Type[django.contrib.admin.options.ModelAdmin]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Critical(CheckMessage):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
