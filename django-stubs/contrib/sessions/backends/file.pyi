from typing import Any, Dict, Optional, Union

from django.contrib.sessions.backends.base import SessionBase


class SessionStore(SessionBase):
    accessed: bool
    serializer: Type[django.core.signing.JSONSerializer]
    storage_path: str = ...
    file_prefix: str = ...
    def __init__(self, session_key: Optional[str] = ...) -> None: ...
    def load(self) -> Dict[str, Union[str, int]]: ...
    modified: bool = ...
    def create(self) -> None: ...
    def save(self, must_create: bool = ...) -> None: ...
    def exists(self, session_key: Optional[str]) -> bool: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    def clean(self) -> None: ...
    @classmethod
    def clear_expired(cls) -> None: ...
