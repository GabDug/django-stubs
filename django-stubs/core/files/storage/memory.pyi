from django.utils._os import _PathCompatible
from django.utils.deconstruct import _Deconstructible

from .base import Storage
from .mixins import StorageSettingsMixin

class InMemoryStorage(Storage, StorageSettingsMixin, _Deconstructible):
    def __init__(
        self,
        location: _PathCompatible | None = ...,
        base_url: str | None = ...,
        file_permissions_mode: int | None = ...,
        directory_permissions_mode: int | None = ...,
    ) -> None: ...
    @property
    def base_location(self) -> _PathCompatible: ...
    @property
    def location(self) -> _PathCompatible: ...
    @property
    def base_url(self) -> str: ...
    @property
    def file_permissions_mode(self) -> int | None: ...
    @property
    def directory_permissions_mode(self) -> int | None: ...
