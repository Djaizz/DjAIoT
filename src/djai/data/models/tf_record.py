from ...util import PGSQL_IDENTIFIER_MAX_LEN, end_path_with_slash
from ..apps import DjAIDataModuleConfig
from .base import _FileStoredDataSet, _NamedDataSet


class TFRecordDataSet(_FileStoredDataSet):
    class Meta(_FileStoredDataSet.Meta):
        verbose_name = 'TFRecord Data Set'
        verbose_name_plural = 'TFRecord Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'tfrecord_data_sets'


class NamedTFRecordDataSet(_NamedDataSet, TFRecordDataSet):
    class Meta(_NamedDataSet.Meta, TFRecordDataSet.Meta):
        verbose_name = 'Named TFRecord Data Set'
        verbose_name_plural = 'Named TFRecord Data Sets'

        db_table = f"{DjAIDataModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'named_tfrecord_data_sets'

    def __str__(self) -> str:
        return f'"{self.name}" {type(self).__name__} @ ' \
            f'{end_path_with_slash(self.path) if self.is_dir else self.path}'
