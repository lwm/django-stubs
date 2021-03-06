from io import BytesIO, StringIO
from tempfile import _TemporaryFileWrapper
from typing import Any, Dict, Iterator, Optional, Union

from django.core.files.base import File


class UploadedFile(File):
    file: None
    size: Any = ...
    content_type: Any = ...
    charset: Any = ...
    content_type_extra: Any = ...
    def __init__(
        self,
        file: Optional[Union[_TemporaryFileWrapper, StringIO, BytesIO]] = ...,
        name: str = ...,
        content_type: str = ...,
        size: Optional[int] = ...,
        charset: Optional[str] = ...,
        content_type_extra: Optional[Dict[str, bytes]] = ...,
    ) -> None: ...
    name: Any = ...

class TemporaryUploadedFile(UploadedFile):
    file: tempfile._TemporaryFileWrapper
    mode: str
    def __init__(
        self,
        name: str,
        content_type: str,
        size: int,
        charset: Optional[str],
        content_type_extra: Optional[Dict[Any, Any]] = ...,
    ) -> None: ...
    def temporary_file_path(self) -> str: ...
    def close(self) -> None: ...

class InMemoryUploadedFile(UploadedFile):
    file: _io.StringIO
    field_name: Any = ...
    def __init__(
        self,
        file: Union[StringIO, BytesIO],
        field_name: Optional[str],
        name: str,
        content_type: str,
        size: int,
        charset: Optional[str],
        content_type_extra: Optional[Dict[str, bytes]] = ...,
    ) -> None: ...
    def open(self, mode: Optional[str] = ...) -> InMemoryUploadedFile: ...
    def chunks(self, chunk_size: None = ...) -> Iterator[Union[str, bytes]]: ...
    def multiple_chunks(self, chunk_size: Optional[Any] = ...): ...

class SimpleUploadedFile(InMemoryUploadedFile):
    file: _io.BytesIO
    def __init__(
        self,
        name: str,
        content: Optional[Union[str, bytes]],
        content_type: str = ...,
    ) -> None: ...
    @classmethod
    def from_dict(cls, file_dict: Any): ...
