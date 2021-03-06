from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser


class TemplateCommand(BaseCommand):
    requires_system_checks: bool = ...
    url_schemes: Any = ...
    rewrite_template_suffixes: Any = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    app_or_project: Any = ...
    paths_to_remove: Any = ...
    verbosity: Any = ...
    def handle(
        self,
        app_or_project: Any,
        name: Any,
        target: Optional[Any] = ...,
        **options: Any
    ): ...
    def handle_template(self, template: Any, subdir: Any): ...
    def validate_name(self, name: Any, app_or_project: Any) -> None: ...
    def download(self, url: Any): ...
    def splitext(self, the_path: Any): ...
    def extract(self, filename: Any): ...
    def is_url(self, template: Any): ...
    def make_writeable(self, filename: Any) -> None: ...
