from typing import Any, Dict, Optional, Union

from django.template.backends.base import BaseEngine
from django.template.backends.django import Template
from django.template.backends.jinja2 import Template

ROOT: Any

def get_default_renderer() -> DjangoTemplates: ...

class BaseRenderer:
    def get_template(self, template_name: str) -> Any: ...
    def render(
        self, template_name: str, context: Dict[str, Any], request: None = ...
    ) -> str: ...

class EngineMixin:
    def get_template(self, template_name: str) -> Union[Template, Template]: ...
    def engine(self) -> BaseEngine: ...

class DjangoTemplates(EngineMixin, BaseRenderer):
    engine: django.template.backends.django.DjangoTemplates
    backend: Any = ...

class Jinja2(EngineMixin, BaseRenderer):
    engine: django.template.backends.jinja2.Jinja2
    backend: Any = ...

class TemplatesSetting(BaseRenderer):
    def get_template(self, template_name: str) -> Template: ...
