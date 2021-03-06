from collections import OrderedDict
from datetime import date, datetime, time
from itertools import chain
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, Union

from django.contrib.admin.checks import BaseModelAdminChecks
from django.contrib.admin.options import BaseModelAdmin
from django.contrib.admin.widgets import (AdminBigIntegerFieldWidget,
                                          AdminEmailInputWidget,
                                          AdminFileWidget,
                                          AdminIntegerFieldWidget,
                                          AdminRadioSelect, AdminSplitDateTime,
                                          AdminTextareaWidget,
                                          AdminTextInputWidget,
                                          AdminURLFieldWidget,
                                          AutocompleteSelect,
                                          AutocompleteSelectMultiple,
                                          ForeignKeyRawIdWidget,
                                          RelatedFieldWidgetWrapper)
from django.db.models.fields.files import FieldFile
from django.forms.fields import Field
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.forms.renderers import DjangoTemplates
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict
from django.utils.safestring import SafeText


class MediaOrderConflictWarning(RuntimeWarning): ...

class Media:
    def __init__(
        self,
        media: Optional[Type[Any]] = ...,
        css: Optional[Dict[str, List[str]]] = ...,
        js: Optional[List[str]] = ...,
    ) -> None: ...
    def render(self) -> SafeText: ...
    def render_js(self) -> List[SafeText]: ...
    def render_css(self) -> chain: ...
    def absolute_path(self, path: str) -> str: ...
    def __getitem__(self, name: str) -> Media: ...
    @staticmethod
    def merge(
        list_1: List[str],
        list_2: Union[Tuple[str, str, str, str, str], List[str]],
    ) -> List[str]: ...
    def __add__(self, other: Media) -> Media: ...

class MediaDefiningClass(type):
    def __new__(
        mcs: Type[MediaDefiningClass],
        name: str,
        bases: Tuple,
        attrs: Union[
            Dict[
                str,
                Union[
                    str,
                    Tuple,
                    None,
                    Type[Union[ModelForm, BaseModelAdminChecks]],
                    Dict[Any, Any],
                    bool,
                    Callable,
                ],
            ],
            OrderedDict,
            Dict[str, Union[str, Callable, property]],
        ],
    ) -> Type[
        Union[
            ModelForm,
            AutocompleteSelect,
            BaseModelAdmin,
            Form,
            AutocompleteSelectMultiple,
            AdminFileWidget,
            AdminRadioSelect,
            RelatedFieldWidgetWrapper,
            AdminBigIntegerFieldWidget,
        ]
    ]: ...

class Widget:
    needs_multipart_form: bool = ...
    is_localized: bool = ...
    is_required: bool = ...
    supports_microseconds: bool = ...
    attrs: Any = ...
    def __init__(self, attrs: Optional[Dict[str, str]] = ...) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any]) -> Widget: ...
    @property
    def is_hidden(self) -> bool: ...
    def subwidgets(
        self, name: Any, value: Any, attrs: Optional[Any] = ...
    ) -> None: ...
    def format_value(
        self, value: Optional[Union[int, str, datetime, List[str]]]
    ) -> Optional[str]: ...
    def get_context(
        self, name: str, value: Any, attrs: Dict[str, Union[bool, str]]
    ) -> Dict[str, Dict]: ...
    def render(
        self,
        name: str,
        value: Any,
        attrs: Dict[str, Union[bool, str]] = ...,
        renderer: Optional[DjangoTemplates] = ...,
    ) -> SafeText: ...
    def build_attrs(
        self,
        base_attrs: Dict[str, Union[int, str]],
        extra_attrs: Dict[str, Union[bool, str]] = ...,
    ) -> Dict[str, Union[int, str]]: ...
    def value_from_datadict(
        self,
        data: QueryDict,
        files: Union[Dict[Any, Any], MultiValueDict],
        name: str,
    ) -> Optional[str]: ...
    def value_omitted_from_data(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> bool: ...
    def id_for_label(self, id_: str) -> str: ...
    def use_required_attribute(self, initial: Any) -> bool: ...

class Input(Widget):
    attrs: Dict[Any, Any]
    input_type: str = ...
    template_name: str = ...
    def __init__(self, attrs: Dict[str, str] = ...) -> None: ...
    def get_context(
        self, name: str, value: Any, attrs: Dict[str, Union[bool, str]]
    ) -> Dict[
        str,
        Union[
            Dict[str, Union[str, bool, FieldFile, Dict[str, str]]],
            Dict[str, Union[str, bool, None, Dict[str, str]]],
            Dict[str, Union[str, bool, None, Dict[str, Union[int, str]]]],
            Dict[str, Union[str, bool, None, Dict[str, Union[bool, str]]]],
        ],
    ]: ...

class TextInput(Input):
    attrs: Dict[str, Union[int, str]]
    is_localized: bool
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class NumberInput(Input):
    attrs: Dict[Any, Any]
    input_type: str = ...
    template_name: str = ...

class EmailInput(Input):
    attrs: Dict[str, Union[bool, str]]
    is_required: bool
    input_type: str = ...
    template_name: str = ...

class URLInput(Input):
    input_type: str = ...
    template_name: str = ...

class PasswordInput(Input):
    attrs: Dict[str, str]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    render_value: bool = ...
    def __init__(
        self, attrs: Optional[Any] = ..., render_value: bool = ...
    ) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...

class HiddenInput(Input):
    attrs: Dict[Any, Any]
    is_localized: bool
    input_type: str = ...
    template_name: str = ...

class MultipleHiddenInput(HiddenInput):
    attrs: Dict[str, str]
    choices: List[Tuple[str, str]]
    input_type: str
    is_required: bool
    template_name: str = ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def format_value(self, value: Any): ...

class FileInput(Input):
    attrs: Dict[Any, Any]
    input_type: str = ...
    needs_multipart_form: bool = ...
    template_name: str = ...
    def format_value(self, value: Any): ...
    def value_from_datadict(
        self, data: QueryDict, files: Dict[Any, Any], name: str
    ) -> None: ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...

class ClearableFileInput(FileInput):
    attrs: Dict[Any, Any]
    clear_checkbox_label: Any = ...
    initial_text: Any = ...
    input_text: Any = ...
    template_name: str = ...
    def clear_checkbox_name(self, name: str) -> str: ...
    def clear_checkbox_id(self, name: str) -> str: ...
    def is_initial(self, value: Optional[FieldFile]) -> bool: ...
    def format_value(
        self, value: Optional[FieldFile]
    ) -> Optional[FieldFile]: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def value_from_datadict(
        self, data: QueryDict, files: Dict[Any, Any], name: str
    ) -> None: ...
    def use_required_attribute(self, initial: Optional[FieldFile]) -> bool: ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...

class Textarea(Widget):
    attrs: Dict[str, Union[int, str]]
    is_required: bool
    template_name: str = ...
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...

class DateTimeBaseInput(TextInput):
    format_key: str = ...
    supports_microseconds: bool = ...
    format: Any = ...
    def __init__(
        self, attrs: Optional[Any] = ..., format: Optional[Any] = ...
    ) -> None: ...
    def format_value(self, value: Union[date, time, str]) -> str: ...

class DateInput(DateTimeBaseInput):
    attrs: Dict[str, str]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class DateTimeInput(DateTimeBaseInput):
    attrs: Dict[Any, Any]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class TimeInput(DateTimeBaseInput):
    attrs: Dict[str, str]
    format: Optional[str]
    input_type: str
    is_localized: bool
    is_required: bool
    format_key: str = ...
    template_name: str = ...

class CheckboxInput(Input):
    input_type: str = ...
    template_name: str = ...
    check_test: Any = ...
    def __init__(
        self, attrs: Dict[str, str] = ..., check_test: Callable = ...
    ) -> None: ...
    def format_value(self, value: None) -> None: ...
    def get_context(
        self, name: str, value: Optional[bool], attrs: Dict[str, str]
    ) -> Dict[
        str,
        Union[
            Dict[str, Union[str, bool, None, Dict[str, str]]],
            Dict[str, Union[str, bool, None, Dict[str, Union[bool, str]]]],
        ],
    ]: ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> bool: ...
    def value_omitted_from_data(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> bool: ...

class ChoiceWidget(Widget):
    allow_multiple_selected: bool = ...
    input_type: Any = ...
    template_name: Any = ...
    option_template_name: Any = ...
    add_id_index: bool = ...
    checked_attribute: Any = ...
    option_inherits_attrs: bool = ...
    choices: Any = ...
    def __init__(self, attrs: None = ..., choices: Tuple = ...) -> None: ...
    def __deepcopy__(self, memo: Dict[int, Any]) -> Select: ...
    def subwidgets(
        self, name: Any, value: Any, attrs: Optional[Any] = ...
    ) -> None: ...
    def options(
        self, name: Any, value: Any, attrs: Optional[Any] = ...
    ) -> None: ...
    def optgroups(
        self,
        name: str,
        value: List[str],
        attrs: Dict[str, Union[bool, str]] = ...,
    ) -> Union[
        List[
            Tuple[None, List[Dict[str, Union[str, int, Dict[Any, Any]]]], int]
        ],
        List[Tuple[None, int, int]],
    ]: ...
    def create_option(
        self,
        name: str,
        value: Union[str, int],
        label: str,
        selected: Union[bool, Set[str]],
        index: int,
        subindex: None = ...,
        attrs: Optional[Union[Dict[str, bool], Dict[str, str]]] = ...,
    ) -> Dict[
        str, Union[str, int, Dict[Any, Any], Set[str], Dict[str, bool]]
    ]: ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[str, int, List[Any]]],
        attrs: Dict[str, Union[bool, str]],
    ) -> Dict[str, Dict]: ...
    def id_for_label(self, id_: str, index: str = ...) -> str: ...
    def value_from_datadict(
        self,
        data: QueryDict,
        files: Union[Dict[Any, Any], MultiValueDict],
        name: str,
    ) -> str: ...
    def format_value(
        self, value: Optional[Union[str, int, List[Any]]]
    ) -> List[str]: ...

class Select(ChoiceWidget):
    attrs: Dict[str, str]
    choices: Union[
        List[Union[Tuple[str, str], Tuple[int, int]]],
        List[List[str]],
        List[Tuple[int, str]],
        List[Tuple[str, Union[str, Tuple[Tuple[str, str], Tuple[str, str]]]]],
    ]
    is_required: bool
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...
    add_id_index: bool = ...
    checked_attribute: Any = ...
    option_inherits_attrs: bool = ...
    def get_context(
        self,
        name: str,
        value: Optional[Union[str, int, List[Any]]],
        attrs: Dict[str, Union[bool, str]],
    ) -> Dict[str, Dict]: ...
    def use_required_attribute(self, initial: Optional[str]) -> bool: ...

class NullBooleanSelect(Select):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def format_value(self, value: Any): ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> None: ...

class SelectMultiple(Select):
    attrs: Dict[Any, Any]
    choices: List[
        Tuple[str, Union[str, Tuple[Tuple[str, str], Tuple[str, str]]]]
    ]
    is_required: bool
    allow_multiple_selected: bool = ...
    def value_from_datadict(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> List[str]: ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...

class RadioSelect(ChoiceWidget):
    attrs: Dict[Any, Any]
    choices: List[int]
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...

class CheckboxSelectMultiple(ChoiceWidget):
    attrs: Dict[Any, Any]
    choices: Union[
        List[Tuple[str, Union[str, Tuple[Tuple[str, str], Tuple[str, str]]]]],
        List[Tuple[datetime.time, str]],
        List[Tuple[int, str]],
    ]
    is_required: bool
    allow_multiple_selected: bool = ...
    input_type: str = ...
    template_name: str = ...
    option_template_name: str = ...
    def use_required_attribute(self, initial: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
    def id_for_label(self, id_: Any, index: Optional[Any] = ...): ...

class MultiWidget(Widget):
    attrs: Dict[Any, Any]
    template_name: str = ...
    widgets: List[django.forms.widgets.ClearableFileInput] = ...
    def __init__(
        self, widgets: Tuple[DateInput, TimeInput], attrs: None = ...
    ) -> None: ...
    @property
    def is_hidden(self) -> bool: ...
    def get_context(
        self,
        name: str,
        value: Union[List[str], datetime],
        attrs: Dict[str, Union[bool, str]],
    ) -> Dict[
        str,
        Union[
            Dict[
                str,
                Union[
                    str,
                    bool,
                    Dict[str, Union[bool, str]],
                    List[
                        Dict[str, Union[str, bool, Dict[str, Union[bool, str]]]]
                    ],
                ],
            ],
            Dict[
                str,
                Union[
                    str,
                    bool,
                    Dict[str, str],
                    List[Dict[str, Union[str, bool, Dict[str, str]]]],
                ],
            ],
        ],
    ]: ...
    def id_for_label(self, id_: str) -> str: ...
    def value_from_datadict(
        self,
        data: QueryDict,
        files: Union[Dict[Any, Any], MultiValueDict],
        name: str,
    ) -> Union[List[None], List[str]]: ...
    def value_omitted_from_data(
        self, data: QueryDict, files: MultiValueDict, name: str
    ) -> bool: ...
    def decompress(self, value: Any) -> None: ...
    media: Any = ...
    def __deepcopy__(
        self,
        memo: Union[
            int, OrderedDict, Widget, List[Union[Widget, Field]], Field
        ],
    ) -> AdminSplitDateTime: ...
    @property
    def needs_multipart_form(self): ...

class SplitDateTimeWidget(MultiWidget):
    attrs: Dict[Any, Any]
    widgets: List[django.forms.widgets.DateTimeBaseInput]
    supports_microseconds: bool = ...
    template_name: str = ...
    def __init__(
        self,
        attrs: None = ...,
        date_format: None = ...,
        time_format: None = ...,
        date_attrs: None = ...,
        time_attrs: None = ...,
    ) -> None: ...
    def decompress(self, value: datetime) -> List[Union[date, time]]: ...

class SplitHiddenDateTimeWidget(SplitDateTimeWidget):
    attrs: Dict[Any, Any]
    is_required: bool
    widgets: List[django.forms.widgets.DateTimeBaseInput]
    template_name: str = ...
    def __init__(
        self,
        attrs: None = ...,
        date_format: None = ...,
        time_format: None = ...,
        date_attrs: None = ...,
        time_attrs: None = ...,
    ) -> None: ...

class SelectDateWidget(Widget):
    none_value: Any = ...
    month_field: str = ...
    day_field: str = ...
    year_field: str = ...
    template_name: str = ...
    input_type: str = ...
    select_widget: Any = ...
    date_re: Any = ...
    attrs: Any = ...
    years: Any = ...
    months: Any = ...
    year_none_value: Any = ...
    month_none_value: Any = ...
    day_none_value: Any = ...
    def __init__(
        self,
        attrs: Optional[Any] = ...,
        years: Optional[Any] = ...,
        months: Optional[Any] = ...,
        empty_label: Optional[Any] = ...,
    ) -> None: ...
    def get_context(self, name: Any, value: Any, attrs: Any): ...
    def format_value(self, value: Any): ...
    def id_for_label(self, id_: Any): ...
    def value_from_datadict(self, data: Any, files: Any, name: Any): ...
    def value_omitted_from_data(self, data: Any, files: Any, name: Any): ...
