from typing import Any, Iterator, Optional, Type

from django.db.models.base import Model

MODELS_MODULE_NAME: str

class AppConfig:
    name: str = ...
    module: Any = ...
    apps: None = ...
    label: str = ...
    verbose_name: str = ...
    path: str = ...
    models_module: None = ...
    models: None = ...
    def __init__(self, app_name: str, app_module: None) -> None: ...
    @classmethod
    def create(cls, entry: str) -> AppConfig: ...
    def get_model(
        self, model_name: str, require_ready: bool = ...
    ) -> Type[Model]: ...
    def get_models(
        self, include_auto_created: bool = ..., include_swapped: bool = ...
    ) -> Iterator[Type[Model]]: ...
    def import_models(self) -> None: ...
    def ready(self) -> None: ...
