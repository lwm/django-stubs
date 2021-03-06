from datetime import date as real_date
from datetime import datetime as real_datetime
from datetime import time as real_time
from typing import Any, Optional, Union


class date(real_date):
    def strftime(self, fmt: str) -> str: ...

class datetime(real_datetime):
    def strftime(self, fmt: str) -> str: ...
    @classmethod
    def combine(cls, date: Any, time: Any): ...
    def date(self): ...

class time(real_time): ...

def new_date(d: date) -> date: ...
def new_datetime(d: date) -> datetime: ...
def strftime(dt: Union[date, datetime], fmt: str) -> str: ...
