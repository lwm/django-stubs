from typing import Any, Dict, List, Optional, Tuple

from django.contrib import admin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.response import HttpResponse
from django.urls.resolvers import URLPattern

csrf_protect_m: Any
sensitive_post_parameters_m: Any

class GroupAdmin(admin.ModelAdmin):
    admin_site: django.contrib.admin.sites.AdminSite
    formfield_overrides: Dict[
        Type[
            Union[
                django.db.models.fields.DateField,
                django.db.models.fields.TimeField,
                django.db.models.fields.TextField,
                django.db.models.fields.IntegerField,
                django.db.models.fields.CharField,
                django.db.models.fields.files.FileField,
            ]
        ],
        Dict[
            str,
            Type[
                Union[
                    django.forms.fields.SplitDateTimeField,
                    django.contrib.admin.widgets.AdminSplitDateTime,
                    django.contrib.admin.widgets.AdminDateWidget,
                    django.contrib.admin.widgets.AdminTimeWidget,
                    django.contrib.admin.widgets.AdminTextareaWidget,
                    django.contrib.admin.widgets.AdminURLFieldWidget,
                    django.contrib.admin.widgets.AdminIntegerFieldWidget,
                    django.contrib.admin.widgets.AdminTextInputWidget,
                    django.contrib.admin.widgets.AdminFileWidget,
                    django.contrib.admin.widgets.AdminEmailInputWidget,
                ]
            ],
        ],
    ]
    model: Type[django.contrib.auth.models.Group]
    opts: django.db.models.options.Options
    search_fields: Any = ...
    ordering: Any = ...
    filter_horizontal: Any = ...
    def formfield_for_manytomany(
        self,
        db_field: ManyToManyField,
        request: WSGIRequest = ...,
        **kwargs: Any
    ) -> ModelMultipleChoiceField: ...

class UserAdmin(admin.ModelAdmin):
    admin_site: django.contrib.admin.sites.AdminSite
    formfield_overrides: Dict[
        Type[
            Union[
                django.db.models.fields.DateField,
                django.db.models.fields.TimeField,
                django.db.models.fields.TextField,
                django.db.models.fields.IntegerField,
                django.db.models.fields.CharField,
                django.db.models.fields.files.FileField,
            ]
        ],
        Dict[
            str,
            Type[
                Union[
                    django.forms.fields.SplitDateTimeField,
                    django.contrib.admin.widgets.AdminSplitDateTime,
                    django.contrib.admin.widgets.AdminDateWidget,
                    django.contrib.admin.widgets.AdminTimeWidget,
                    django.contrib.admin.widgets.AdminTextareaWidget,
                    django.contrib.admin.widgets.AdminURLFieldWidget,
                    django.contrib.admin.widgets.AdminIntegerFieldWidget,
                    django.contrib.admin.widgets.AdminTextInputWidget,
                    django.contrib.admin.widgets.AdminFileWidget,
                    django.contrib.admin.widgets.AdminEmailInputWidget,
                ]
            ],
        ],
    ]
    model: Type[django.contrib.auth.models.User]
    opts: django.db.models.options.Options
    add_form_template: str = ...
    change_user_password_template: Any = ...
    fieldsets: Any = ...
    add_fieldsets: Any = ...
    form: Any = ...
    add_form: Any = ...
    change_password_form: Any = ...
    list_display: Any = ...
    list_filter: Any = ...
    search_fields: Any = ...
    ordering: Any = ...
    filter_horizontal: Any = ...
    def get_fieldsets(
        self, request: WSGIRequest, obj: None = ...
    ) -> Tuple[Tuple[None, Dict[str, Tuple[str]]]]: ...
    def get_form(
        self, request: Any, obj: Optional[Any] = ..., **kwargs: Any
    ): ...
    def get_urls(self) -> List[URLPattern]: ...
    def lookup_allowed(self, lookup: str, value: str) -> bool: ...
    def add_view(
        self,
        request: WSGIRequest,
        form_url: str = ...,
        extra_context: None = ...,
    ) -> Any: ...
    def user_change_password(
        self, request: WSGIRequest, id: str, form_url: str = ...
    ) -> HttpResponse: ...
    def response_add(
        self, request: WSGIRequest, obj: User, post_url_continue: None = ...
    ) -> HttpResponse: ...
