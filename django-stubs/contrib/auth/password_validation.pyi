from pathlib import PosixPath
from typing import Any, Dict, List, Optional, Tuple, Union

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.utils.functional import SimpleLazyObject


def get_default_password_validators() -> Union[
    List[Union[CommonPasswordValidator, MinimumLengthValidator]],
    List[Union[UserAttributeSimilarityValidator, MinimumLengthValidator]],
    List[NumericPasswordValidator],
]: ...
def get_password_validators(
    validator_config: List[Dict[str, Union[str, Dict[str, int]]]]
) -> Union[
    List[Union[CommonPasswordValidator, MinimumLengthValidator]],
    List[Union[UserAttributeSimilarityValidator, MinimumLengthValidator]],
    List[NumericPasswordValidator],
]: ...
def validate_password(
    password: str,
    user: Optional[Union[AbstractBaseUser, SimpleLazyObject]] = ...,
    password_validators: Optional[List[Any]] = ...,
) -> None: ...
def password_changed(
    password: str,
    user: Optional[AbstractBaseUser] = ...,
    password_validators: None = ...,
) -> None: ...
def password_validators_help_texts(
    password_validators: Optional[List[Any]] = ...
) -> List[str]: ...

password_validators_help_text_html: Any

class MinimumLengthValidator:
    min_length: int = ...
    def __init__(self, min_length: int = ...) -> None: ...
    def validate(self, password: str, user: Optional[User] = ...) -> None: ...
    def get_help_text(self) -> str: ...

class UserAttributeSimilarityValidator:
    DEFAULT_USER_ATTRIBUTES: Any = ...
    user_attributes: Tuple[str, str, str, str] = ...
    max_similarity: float = ...
    def __init__(
        self,
        user_attributes: Union[Tuple[str, str, str, str], List[str]] = ...,
        max_similarity: float = ...,
    ) -> None: ...
    def validate(self, password: str, user: Optional[User] = ...) -> None: ...
    def get_help_text(self) -> str: ...

class CommonPasswordValidator:
    DEFAULT_PASSWORD_LIST_PATH: Any = ...
    passwords: Set[str] = ...
    def __init__(
        self, password_list_path: Union[str, PosixPath] = ...
    ) -> None: ...
    def validate(self, password: str, user: None = ...) -> None: ...
    def get_help_text(self) -> str: ...

class NumericPasswordValidator:
    def validate(
        self, password: str, user: Optional[AbstractBaseUser] = ...
    ) -> None: ...
    def get_help_text(self) -> str: ...
