"""DjAIoT Device Performance module config."""


from sys import version_info

from django.apps.config import AppConfig

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('DjAIoTDevicePerformanceModuleConfig',)


class DjAIoTDevicePerformanceModuleConfig(AppConfig):
    """DjAIoT Device Performance Module Config."""

    name: str = 'djaiot.device_perf'

    label: str = 'IoTDevicePerf'

    verbose_name: str = 'DjAIoT: Device Performance'

    # path: str = ...

    default: bool = True

    default_auto_field: str = 'django.db.models.fields.AutoField'

    def ready(self) -> None:
        """Run tasks to initialize module."""
