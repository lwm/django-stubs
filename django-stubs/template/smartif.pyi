from typing import Any, Dict, List, Optional, Union

from django.template.defaulttags import TemplateLiteral


class TokenBase:
    id: Any = ...
    value: Any = ...
    first: Any = ...
    second: Any = ...
    def nud(self, parser: Any) -> None: ...
    def led(self, left: Any, parser: Any) -> None: ...
    def display(self): ...

def infix(bp: Any, func: Any): ...
def prefix(bp: Any, func: Any): ...

OPERATORS: Any

class Literal(TokenBase):
    id: str = ...
    lbp: int = ...
    value: Optional[Union[List[int], int]] = ...
    def __init__(self, value: Optional[Union[List[int], int]]) -> None: ...
    def display(self): ...
    def nud(self, parser: IfParser) -> Literal: ...
    def eval(
        self, context: Dict[Any, Any]
    ) -> Optional[Union[List[int], int]]: ...

class EndToken(TokenBase):
    lbp: int = ...
    def nud(self, parser: Any) -> None: ...

class IfParser:
    error_class: Any = ...
    tokens: Any = ...
    pos: int = ...
    current_token: Any = ...
    def __init__(
        self,
        tokens: Union[
            List[Union[int, str, List[int]]],
            List[Union[None, str, List[int]]],
            List[Union[int, str, None]],
        ],
    ) -> None: ...
    def translate_token(
        self, token: Optional[Union[List[int], int, str]]
    ) -> Literal: ...
    def next_token(self) -> Literal: ...
    def parse(self) -> TemplateLiteral: ...
    def expression(self, rbp: int = ...) -> Literal: ...
    def create_var(self, value: Optional[Union[List[int], int]]) -> Literal: ...
