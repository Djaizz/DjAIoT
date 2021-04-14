from django.db.models.fields import BinaryField

import joblib
from tempfile import TemporaryFile

from ..base import AIModel


class _MLModel(AIModel):
    artifact = \
        BinaryField(
            verbose_name='Model Artifact (raw binary data)',
            help_text='Model Artifact (raw binary data)',

            max_length=None,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=False,
            db_tablespace=None,
            default=None,
            editable=False,
            # error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    obj = None

    class Meta(AIModel.Meta):
        abstract = True

    # by default, serialize model object by JobLib/Pickle
    def serialize(self):
        assert self.obj, ValueError(f'*** MODEL OBJECT {self.obj} INVALID ***')

        with TemporaryFile() as f:
            joblib.dump(
                value=self.obj,
                filename=f,
                compress=0,
                protocol=3,   # default protocol in Python 3.0–3.7
                cache_size=None)
            f.seek(0)
            self.artifact = f.read()

    # by default, deserialize model object by JobLib/Pickle
    def deserialize(self):
        with TemporaryFile() as f:
            f.write(self.artifact)
            f.seek(0)
            self.obj = joblib.load(filename=f, mmap_mode=None)

        assert self.obj, ValueError(f'*** MODEL OBJECT {self.obj} INVALID ***')

    def save(self, *args, **kwargs):
        self.serialize()
        super().save(*args, **kwargs)
