import threading
import unittest
from contextlib import _GeneratorContextManager
from typing import Any, Callable, List, Optional, Tuple, Type, Union
from unittest.runner import TextTestResult

from django.core.handlers.wsgi import WSGIHandler
from django.core.servers.basehttp import WSGIRequestHandler
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.test.html import Element
from django.test.utils import CaptureQueriesContext, override_settings


class _AssertNumQueriesContext(CaptureQueriesContext):
    connection: django.db.backends.sqlite3.base.DatabaseWrapper
    final_queries: Optional[int]
    force_debug_cursor: bool
    initial_queries: int
    test_case: Union[
        django.test.testcases.TransactionTestCase,
        django.test.testcases.SerializeMixin,
    ] = ...
    num: int = ...
    def __init__(self, test_case: Any, num: Any, connection: Any) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

class _AssertTemplateUsedContext:
    test_case: django.test.testcases.SimpleTestCase = ...
    template_name: str = ...
    rendered_templates: List[django.template.base.Template] = ...
    rendered_template_names: List[str] = ...
    context: django.test.utils.ContextList = ...
    def __init__(self, test_case: Any, template_name: Any) -> None: ...
    def on_template_render(
        self,
        sender: Any,
        signal: Any,
        template: Any,
        context: Any,
        **kwargs: Any
    ) -> None: ...
    def test(self): ...
    def message(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

class _AssertTemplateNotUsedContext(_AssertTemplateUsedContext):
    context: django.test.utils.ContextList
    rendered_template_names: List[str]
    rendered_templates: List[django.template.base.Template]
    template_name: str
    test_case: django.test.testcases.SimpleTestCase
    def test(self): ...
    def message(self): ...

class _CursorFailure:
    cls_name: str = ...
    wrapped: Callable = ...
    def __init__(self, cls_name: Any, wrapped: Any) -> None: ...
    def __call__(self) -> None: ...

class SimpleTestCase(unittest.TestCase):
    client_class: Any = ...
    allow_database_queries: bool = ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def __call__(self, result: TextTestResult = ...) -> None: ...
    def settings(self, **kwargs: Any) -> override_settings: ...
    def modify_settings(self, **kwargs: Any): ...
    def assertRedirects(
        self,
        response: HttpResponse,
        expected_url: str,
        status_code: int = ...,
        target_status_code: int = ...,
        msg_prefix: str = ...,
        fetch_redirect_response: bool = ...,
    ) -> None: ...
    def assertContains(
        self,
        response: HttpResponse,
        text: Union[str, bytes],
        count: None = ...,
        status_code: int = ...,
        msg_prefix: str = ...,
        html: bool = ...,
    ) -> None: ...
    def assertNotContains(
        self,
        response: TemplateResponse,
        text: str,
        status_code: int = ...,
        msg_prefix: str = ...,
        html: bool = ...,
    ) -> None: ...
    def assertFormError(
        self,
        response: Any,
        form: Any,
        field: Any,
        errors: Any,
        msg_prefix: str = ...,
    ) -> None: ...
    def assertFormsetError(
        self,
        response: Any,
        formset: Any,
        form_index: Any,
        field: Any,
        errors: Any,
        msg_prefix: str = ...,
    ) -> None: ...
    def assertTemplateUsed(
        self,
        response: TemplateResponse = ...,
        template_name: str = ...,
        msg_prefix: str = ...,
        count: None = ...,
    ) -> None: ...
    def assertTemplateNotUsed(
        self,
        response: Optional[Any] = ...,
        template_name: Optional[Any] = ...,
        msg_prefix: str = ...,
    ): ...
    def assertRaisesMessage(
        self,
        expected_exception: Type[Exception],
        expected_message: str,
        *args: Any,
        **kwargs: Any
    ) -> _GeneratorContextManager: ...
    def assertWarnsMessage(
        self,
        expected_warning: Type[RuntimeWarning],
        expected_message: str,
        *args: Any,
        **kwargs: Any
    ) -> _GeneratorContextManager: ...
    def assertFieldOutput(
        self,
        fieldclass: Any,
        valid: Any,
        invalid: Any,
        field_args: Optional[Any] = ...,
        field_kwargs: Optional[Any] = ...,
        empty_value: str = ...,
    ) -> None: ...
    def assertHTMLEqual(
        self, html1: Any, html2: Any, msg: Optional[Any] = ...
    ) -> None: ...
    def assertHTMLNotEqual(
        self, html1: Any, html2: Any, msg: Optional[Any] = ...
    ) -> None: ...
    def assertInHTML(
        self,
        needle: Any,
        haystack: Any,
        count: Optional[Any] = ...,
        msg_prefix: str = ...,
    ) -> None: ...
    def assertJSONEqual(
        self, raw: str, expected_data: str, msg: None = ...
    ) -> None: ...
    def assertJSONNotEqual(
        self, raw: Any, expected_data: Any, msg: Optional[Any] = ...
    ) -> None: ...
    def assertXMLEqual(
        self, xml1: Any, xml2: Any, msg: Optional[Any] = ...
    ) -> None: ...
    def assertXMLNotEqual(
        self, xml1: Any, xml2: Any, msg: Optional[Any] = ...
    ) -> None: ...

class TransactionTestCase(SimpleTestCase):
    reset_sequences: bool = ...
    available_apps: Any = ...
    fixtures: Any = ...
    multi_db: bool = ...
    serialized_rollback: bool = ...
    allow_database_queries: bool = ...
    def assertQuerysetEqual(
        self,
        qs: QuerySet,
        values: Union[
            List[int],
            List[Union[str, None]],
            List[Tuple[str, Type[Model], int]],
        ],
        transform: Callable = ...,
        ordered: bool = ...,
        msg: None = ...,
    ) -> None: ...
    def assertNumQueries(
        self,
        num: int,
        func: Optional[Union[Callable, Type[list]]] = ...,
        *args: Any,
        using: Any = ...,
        **kwargs: Any
    ) -> Optional[_AssertNumQueriesContext]: ...

class TestCase(TransactionTestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    @classmethod
    def setUpTestData(cls) -> None: ...

class CheckCondition:
    conditions: Tuple[Tuple[Callable, str]] = ...
    def __init__(self, *conditions: Any) -> None: ...
    def add_condition(self, condition: Any, reason: Any): ...
    def __get__(self, instance: None, cls: Type[TestCase] = ...) -> bool: ...

def skipIfDBFeature(*features: Any): ...
def skipUnlessDBFeature(*features: Any): ...

class QuietWSGIRequestHandler(WSGIRequestHandler):
    def log_message(*args: Any) -> None: ...

class FSFilesHandler(WSGIHandler):
    application: Any = ...
    base_url: Any = ...
    def __init__(self, application: Any) -> None: ...
    def file_path(self, url: Any): ...
    def get_response(self, request: Any): ...
    def serve(self, request: Any): ...
    def __call__(self, environ: Any, start_response: Any): ...

class _StaticFilesHandler(FSFilesHandler):
    def get_base_dir(self): ...
    def get_base_url(self): ...

class _MediaFilesHandler(FSFilesHandler):
    def get_base_dir(self): ...
    def get_base_url(self): ...

class LiveServerThread(threading.Thread):
    host: str = ...
    port: int = ...
    is_ready: threading.Event = ...
    error: Optional[django.core.exceptions.ImproperlyConfigured] = ...
    static_handler: Type[
        Union[
            django.contrib.staticfiles.handlers.StaticFilesHandler,
            django.test.testcases._StaticFilesHandler,
        ]
    ] = ...
    connections_override: Dict[
        str, django.db.backends.sqlite3.base.DatabaseWrapper
    ] = ...
    def __init__(
        self,
        host: Any,
        static_handler: Any,
        connections_override: Optional[Any] = ...,
        port: int = ...,
    ) -> None: ...
    httpd: django.core.servers.basehttp.ThreadedWSGIServer = ...
    def run(self) -> None: ...
    def terminate(self) -> None: ...

class LiveServerTestCase(TransactionTestCase):
    host: str = ...
    port: int = ...
    server_thread_class: Any = ...
    static_handler: Any = ...
    def live_server_url(cls): ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...

class SerializeMixin:
    lockfile: Any = ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
