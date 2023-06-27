from collections.abc import Callable
from typing import Any, Protocol, TypeVar, overload, type_check_only

_T = TypeVar("_T")
_TCallable = TypeVar("_TCallable", bound=Callable[..., Any])

@overload
def deconstructible(_type: type[_T]) -> type[_T]: ...
@overload
def deconstructible(*, path: str | None = ...) -> Callable[[_TCallable], _TCallable]: ...

# It's not possible to mark an Intersection with this protocol from the decorator for now.
@type_check_only
class _Deconstructible(Protocol):  # noqa: Y046
    @staticmethod
    def __new__(cls: Any, *args: Any, **kwargs: Any) -> Any: ...
    def deconstruct(obj) -> tuple[str, tuple, dict]: ...
