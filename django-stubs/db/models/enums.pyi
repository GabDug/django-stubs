import enum
import sys
from typing import Any

from typing_extensions import Self

if sys.version_info >= (3, 11):
    enum_property = enum.property
else:
    enum_property = property

class ChoicesMeta(enum.EnumMeta):
    names: list[str]
    choices: list[tuple[Any, str]]
    labels: list[str]
    values: list[Any]
    def __contains__(self, member: Any) -> bool: ...
    def __new__(metacls, classname: str, bases: tuple[type, ...], classdict: dict[str, Any], **kwds: Any) -> Any: ...

class Choices(enum.Enum, metaclass=ChoicesMeta):
    @property
    def label(self) -> str: ...
    @enum_property
    def value(self) -> Any: ...
    @property
    def do_not_call_in_templates(self) -> bool: ...

# fake
class _IntegerChoicesMeta(ChoicesMeta):
    names: list[str]
    choices: list[tuple[int, str]]
    labels: list[str]
    values: list[int]

class IntegerChoices(int, Choices, metaclass=_IntegerChoicesMeta):
    @enum_property
    def value(self) -> int: ...
    def __new__(cls, value: object) -> Self: ...

# fake
class _TextChoicesMeta(ChoicesMeta):
    names: list[str]
    choices: list[tuple[str, str]]
    labels: list[str]
    values: list[str]

class TextChoices(str, Choices, metaclass=_TextChoicesMeta):
    @enum_property
    def value(self) -> str: ...
    def __new__(cls, value: object) -> Self: ...
