import os
import pandas

from ...util import PGSQL_IDENTIFIER_MAX_LEN, end_path_with_slash
from ..apps import DjAIDataModuleConfig
from .base import _FileStoredDataSet, _NamedDataSet


class CSVDataSet(_FileStoredDataSet):
    class Meta(_FileStoredDataSet.Meta):
        verbose_name = 'CSV Data Set'
        verbose_name_plural = 'CSV Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'csv_data_sets'

    def to_pandas(self, **kwargs):
        # set AWS credentials if applicable
        from django.conf import settings
        aws_key = settings.__dict__.get('AWS_ACCESS_KEY_ID')
        aws_secret = settings.__dict__.get('AWS_SECRET_ACCESS_KEY')
        if aws_key and aws_secret:
            os.environ['AWS_ACCESS_KEY_ID'] = aws_key
            os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret

        return pandas.read_csv(
                self.path,
                **kwargs)

    def load(self):
        return self.to_pandas()


class NamedCSVDataSet(_NamedDataSet, CSVDataSet):
    class Meta(_NamedDataSet.Meta, CSVDataSet.Meta):
        verbose_name = 'Named CSV Data Set'
        verbose_name_plural = 'Named CSV Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_csv_data_sets'

    def __str__(self) -> str:
        return f'"{self.name}" {type(self).__name__} @ ' \
            f'{end_path_with_slash(self.path) if self.is_dir else self.path}'
