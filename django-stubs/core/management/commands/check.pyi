from typing import Any, Optional

from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    requires_system_checks: bool = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    def handle(self, *app_labels: Any, **options: Any) -> None: ...
