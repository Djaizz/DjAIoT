"""DjAIoT Device Data Module Config."""


import sys

from django.apps.config import AppConfig

if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('DjAIoTDeviceDataModuleConfig',)


class DjAIoTDeviceDataModuleConfig(AppConfig):
    """DjAIoT Device Data Module Config."""

    name: str = 'djaiot.device_data'

    label: str = 'IoTDeviceData'

    verbose_name: str = 'DjAIoT: Device Data'

    # path: str = ...

    default: bool = True

    default_auto_field: str = 'django.db.models.fields.AutoField'

    def ready(self) -> None:
        """Run tasks to initialize module."""
