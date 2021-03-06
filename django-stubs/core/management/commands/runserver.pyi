from typing import Any, Optional

from django.core.handlers.wsgi import WSGIHandler
from django.core.management.base import BaseCommand, CommandParser

naiveip_re: Any

class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    requires_system_checks: bool = ...
    stealth_options: Any = ...
    default_addr: str = ...
    default_addr_ipv6: str = ...
    default_port: str = ...
    protocol: str = ...
    server_cls: Any = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    def execute(self, *args: Any, **options: Any) -> None: ...
    def get_handler(self, *args: Any, **options: Any) -> WSGIHandler: ...
    use_ipv6: Any = ...
    addr: str = ...
    port: Any = ...
    def handle(self, *args: Any, **options: Any) -> None: ...
    def run(self, **options: Any) -> None: ...
    def inner_run(self, *args: Any, **options: Any) -> None: ...

BaseRunserverCommand = Command
