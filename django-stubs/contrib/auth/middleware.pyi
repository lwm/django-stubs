from typing import Any, Optional, Union

from django.contrib.auth.models import AnonymousUser, User
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.utils.deprecation import MiddlewareMixin


def get_user(request: WSGIRequest) -> Union[AnonymousUser, User]: ...

class AuthenticationMiddleware(MiddlewareMixin):
    get_response: Callable
    def process_request(self, request: HttpRequest) -> None: ...

class RemoteUserMiddleware(MiddlewareMixin):
    get_response: Callable
    header: str = ...
    force_logout_if_no_header: bool = ...
    def process_request(self, request: WSGIRequest) -> None: ...
    def clean_username(self, username: str, request: WSGIRequest) -> str: ...

class PersistentRemoteUserMiddleware(RemoteUserMiddleware):
    get_response: Callable
    force_logout_if_no_header: bool = ...
