from ....util import PGSQL_IDENTIFIER_MAX_LEN
from ...apps import DjAIModelModuleConfig
from .base import _MLModel


class TorchModel(_MLModel):
    class Meta(_MLModel.Meta):
        verbose_name = 'Torch Model'
        verbose_name_plural = 'Torch Models'

        db_table = \
            f"{DjAIModelModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'torch_models'
