from typing import Any, Optional

from django.db.backends.sqlite3.schema import DatabaseSchemaEditor
from django.db.migrations.operations.base import Operation
from django.db.migrations.state import ProjectState


class CreateExtension(Operation):
    reversible: bool = ...
    name: Any = ...
    def __init__(self, name: str) -> None: ...
    def state_forwards(self, app_label: str, state: ProjectState) -> None: ...
    def database_forwards(
        self,
        app_label: str,
        schema_editor: DatabaseSchemaEditor,
        from_state: ProjectState,
        to_state: ProjectState,
    ) -> None: ...
    def database_backwards(
        self, app_label: Any, schema_editor: Any, from_state: Any, to_state: Any
    ) -> None: ...
    def describe(self): ...

class BtreeGinExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class BtreeGistExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class CITextExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class CryptoExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class HStoreExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class TrigramExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...

class UnaccentExtension(CreateExtension):
    name: str = ...
    def __init__(self) -> None: ...
