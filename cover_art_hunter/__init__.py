"""Cover Art Hunter package.

Provides the `cli` entry point exposed as the console script
`cover-art-hunter`.
"""

from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:  # pragma: no cover - metadata lookup
    __version__ = version("cover-art-hunter")
except (
    PackageNotFoundError
):  # pragma: no cover - during editable installs before metadata exists
    __version__ = "0.0.0"
