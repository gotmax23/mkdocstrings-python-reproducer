from __future__ import annotations

from collections.abc import Collection


def abc(
    schemes: Collection[str] | None = ("http", "ftp", "file", "https")
) -> str | None:
    """
    This is a test function to show that separate_signature is broken
    """
    pass
