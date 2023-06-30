from importlib.metadata import version, PackageNotFoundError

from .model_admin import RelativesMixin, RelativesAdmin


try:
    __version__ = version("django-relatives")
except PackageNotFoundError:
    # package is not installed
    pass


__all__ = ["RelativesMixin", "RelativesAdmin"]
