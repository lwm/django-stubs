from typing import Any, Dict, Optional

from django.forms.forms import Form
from django.http.response import HttpResponseRedirect


class SuccessMessageMixin:
    success_message: str = ...
    def form_valid(self, form: Form) -> HttpResponseRedirect: ...
    def get_success_message(self, cleaned_data: Dict[str, str]) -> str: ...
