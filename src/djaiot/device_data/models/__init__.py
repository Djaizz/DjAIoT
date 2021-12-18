"""DjAIoT Device Data module: Object Models."""


from sys import version_info

from .json_info import JSONInfo

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = (
    'JSONInfo',
)
