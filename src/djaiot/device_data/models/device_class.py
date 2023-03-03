"""DjAIoT Device Class object model."""


from sys import version_info

from model_utils.models import TimeStampedModel

from djaiot.device_data.apps import DjAIoTDeviceDataModuleConfig

from djutil.models import (PGSQL_IDENTIFIER_MAX_LEN,
                           _ModelWithSnakeCaseUniqueNameABC,
                           modify_abstract_model_field_attrs)

from .json_info import JSONInfo

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('DeviceClass',)


@modify_abstract_model_field_attrs(name=dict(verbose_name='Device Class'))
class DeviceClass(_ModelWithSnakeCaseUniqueNameABC,
                  JSONInfo,
                  TimeStampedModel):
    """DjAIoT Device Class model."""

    class Meta(_ModelWithSnakeCaseUniqueNameABC.Meta, JSONInfo.Meta):
        """Metadata."""

        verbose_name: str = 'Device Class'
        verbose_name_plural: str = 'Device Classes'

        db_table: str = (f'{DjAIoTDeviceDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name: str = 'device_classes'

    class JSONAPIMeta:
        """JSON API Metadata."""

        resource_name: str = (f'{__module__}.'
                              f"{__qualname__.split(sep='.', maxsplit=1)[0]}")

    @staticmethod
    def search_fields() -> Sequence[str]:
        """Search fields."""
        return 'name', 'json_info'
