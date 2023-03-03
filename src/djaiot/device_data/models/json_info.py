"""Table to store potentially large/unstructured JSON data."""


from json import JSONDecoder
from sys import version_info

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.json import JSONField

from djaiot.device_data.apps import DjAIoTDeviceDataModuleConfig

from djutil.models import PGSQL_IDENTIFIER_MAX_LEN, _ModelWithUUIDPKABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('JSONInfo',)


class JSONInfo(_ModelWithUUIDPKABC):
    """Table to store potentially large/unstructured JSON data."""

    info: JSONField = \
        JSONField(
            verbose_name='JSON Info',
            help_text='JSON Info',

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None,
            unique_for_month=None,
            unique_for_year=None,
            # validators=(),

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder)

    class Meta(_ModelWithUUIDPKABC.Meta):
        """Metadata."""

        verbose_name: str = 'JSON Info'
        verbose_name_plural: str = 'JSON Info'

        db_table: str = (f'{DjAIoTDeviceDataModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")

        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" TOO LONG ***')

        default_related_name: str = 'json_info'
