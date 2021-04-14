from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.json import JSONField

from json.decoder import JSONDecoder

from ...util import PGSQL_IDENTIFIER_MAX_LEN
from ..apps import DjAIDataModuleConfig
from .base import DataSet, _NamedDataSet


class JSONDataSet(DataSet):
    json = \
        JSONField(
            verbose_name='JSON Data Content',
            help_text='JSON Data Content',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=True,
            blank=True,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(DataSet.Meta):
        verbose_name = 'JSON Data Set'
        verbose_name_plural = 'JSON Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'json_data_sets'

    def load(self):
        return self.json


class NamedJSONDataSet(_NamedDataSet, JSONDataSet):
    class Meta(_NamedDataSet.Meta, JSONDataSet.Meta):
        verbose_name = 'Named JSON Data Set'
        verbose_name_plural = 'Named JSON Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_json_data_sets'
