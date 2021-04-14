from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.json import JSONField

from json.decoder import JSONDecoder
import numpy

from ...util import PGSQL_IDENTIFIER_MAX_LEN
from ..apps import DjAIDataModuleConfig
from .base import _NamedDataSet
from .json import JSONDataSet


class NumPyArray(JSONDataSet):
    dtype = \
        JSONField(
            verbose_name='Data Type(s)',
            help_text='Data Type(s)',

            encoder=DjangoJSONEncoder,
            decoder=JSONDecoder,

            null=False,
            blank=False,
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

    class Meta(JSONDataSet.Meta):
        verbose_name = 'NumPy Array'
        verbose_name_plural = 'NumPy Arrays'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'numpy_arrays'

    def load(self):
        return numpy.array(
                object=self.json,
                dtype=self.dtype,
                copy=False,
                order='K',
                subok=False,
                ndmin=0)


class NamedNumPyArray(_NamedDataSet, NumPyArray):
    class Meta(_NamedDataSet.Meta, NumPyArray.Meta):
        verbose_name = 'Named NumPy Array'
        verbose_name_plural = 'Named NumPy Arrays'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_numpy_arrays'
