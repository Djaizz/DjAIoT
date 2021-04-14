from polymorphic.models import PolymorphicModel

from ...util import PGSQL_IDENTIFIER_MAX_LEN
from ...util.models import _ModelWithUUIDPKAndTimestamps
from ..apps import DjAIModelModuleConfig


class AIModel(PolymorphicModel, _ModelWithUUIDPKAndTimestamps):
    class Meta(_ModelWithUUIDPKAndTimestamps.Meta):
        verbose_name = 'AI Model'
        verbose_name_plural = 'AI Models'

        db_table = \
            f"{DjAIModelModuleConfig.label}_{__qualname__.split('.')[0]}"
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'ai_models'

    def __str__(self) -> str:
        return f'{type(self).__name__} #{self.uuid}'
