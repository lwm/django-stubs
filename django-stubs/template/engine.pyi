from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from django.template.base import Origin, Template
from django.template.library import Library
from django.template.loaders.base import Loader
from django.utils.safestring import SafeText

from .base import Context, Template
from .context import _builtin_context_processors
from .exceptions import TemplateDoesNotExist
from .library import import_library


class Engine:
    template_context_processors: Tuple[Callable]
    template_loaders: List[django.template.loaders.base.Loader]
    default_builtins: Any = ...
    dirs: List[str] = ...
    app_dirs: bool = ...
    autoescape: bool = ...
    context_processors: Union[Tuple[str], List[str]] = ...
    debug: bool = ...
    loaders: Union[
        List[List[Union[str, Dict[str, str]]]],
        List[Union[Tuple[str, Dict[str, str]], str]],
        List[Tuple[str, List[str]]],
        List[Tuple[str, List[Tuple[str, Dict[str, str]]]]],
    ] = ...
    string_if_invalid: str = ...
    file_charset: str = ...
    libraries: Dict[str, str] = ...
    template_libraries: Dict[str, django.template.library.Library] = ...
    builtins: List[str] = ...
    template_builtins: List[django.template.library.Library] = ...
    def __init__(
        self,
        dirs: Optional[List[str]] = ...,
        app_dirs: bool = ...,
        context_processors: Optional[Union[Tuple[str], List[str]]] = ...,
        debug: bool = ...,
        loaders: Optional[
            Union[
                List[List[Union[str, Dict[str, str]]]],
                List[Union[Tuple[str, Dict[str, str]], str]],
                List[Tuple[str, List[str]]],
                List[Tuple[str, List[Tuple[str, Dict[str, str]]]]],
            ]
        ] = ...,
        string_if_invalid: str = ...,
        file_charset: str = ...,
        libraries: Optional[Dict[str, str]] = ...,
        builtins: Optional[List[str]] = ...,
        autoescape: bool = ...,
    ) -> None: ...
    @staticmethod
    def get_default() -> Engine: ...
    def template_context_processors(self) -> Tuple[Callable]: ...
    def get_template_builtins(self, builtins: List[str]) -> List[Library]: ...
    def get_template_libraries(
        self, libraries: Dict[str, str]
    ) -> Dict[str, Library]: ...
    def template_loaders(self) -> List[Loader]: ...
    def get_template_loaders(
        self,
        template_loaders: Union[
            List[Union[Tuple[str, Dict[str, str]], str]],
            List[List[Union[str, Dict[str, str]]]],
            List[Tuple[str, List[str]]],
            List[Tuple[str, List[Tuple[str, Dict[str, str]]]]],
        ],
    ) -> List[Loader]: ...
    def find_template_loader(
        self,
        loader: Union[
            Tuple[
                str,
                Union[
                    List[Tuple[str, Dict[str, str]]],
                    Dict[str, str],
                    List[Any],
                    List[str],
                ],
            ],
            str,
            List[Union[str, Dict[str, str]]],
        ],
    ) -> Loader: ...
    def find_template(
        self, name: str, dirs: None = ..., skip: Optional[List[Origin]] = ...
    ) -> Tuple[Template, Origin]: ...
    def from_string(self, template_code: str) -> Template: ...
    def get_template(self, template_name: str) -> Template: ...
    def render_to_string(
        self, template_name: str, context: Any = ...
    ) -> SafeText: ...
    def select_template(self, template_name_list: List[str]) -> Template: ...
