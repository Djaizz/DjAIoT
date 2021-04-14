from ....util import PGSQL_IDENTIFIER_MAX_LEN
from ...apps import DjAIModelModuleConfig
from .base import _MLModel


class KerasModel(_MLModel):
    class Meta(_MLModel.Meta):
        verbose_name = 'Keras Model'
        verbose_name_plural = 'Keras Models'

        db_table = \
            f"{DjAIModelModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'keras_models'
