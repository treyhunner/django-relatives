import contextlib
from importlib.metadata import PackageNotFoundError, version

from .model_admin import RelativesAdmin, RelativesMixin

with contextlib.suppress(PackageNotFoundError):  # pragma: nocover
    __version__ = version("django-relatives")


__all__ = ["RelativesMixin", "RelativesAdmin"]
