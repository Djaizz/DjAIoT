"""DjAIoT Device Data: abstract models."""


# pylint: disable=line-too-long


# ForeignKey options:
# docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey
# - to:
#   docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey
# - on_delete:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.on_delete
# - limit_choices_to:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to
# - related_name:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_name
# - related_query_name:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.related_query_name
# - to_field:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.to_field
# - db_constraint:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.db_constraint
# - swappable:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey.swappable

# OneToOneField options:
# docs.djangoproject.com/en/dev/ref/models/fields/#onetoonefield
# - to:
#   docs.djangoproject.com/en/dev/ref/models/fields/#onetoonefield
# - on_delete
# - parent_link:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.OneToOneField.parent_link

# ManyToManyField options:
# docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield
# - to:
#   docs.djangoproject.com/en/dev/ref/models/fields/#manytomanyfield
# - related_name:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.related_name
# - related_query_name:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.related_query_name
# - limit_choices_to:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.limit_choices_to
# - symmetrical:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.symmetrical
# - through:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.through
# - through_fields:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.through_fields
# - db_table:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.db_table
# - db_constraint:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.db_constraint
# - swappable:
#   docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ManyToManyField.swappable


# Index options:
# docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index
# - fields:
#   docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index.fields
# - name:
#   docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index.name
# - db_tablespace:
#   docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index.db_tablespace
# - opclasses:
#   docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index.opclasses
# - condition:
#   docs.djangoproject.com/en/dev/ref/models/indexes/#django.db.models.Index.condition


from sys import version_info

from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey

from .device_class import DeviceClass

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence


__all__: Sequence[str] = ('_ModelWithDeviceClassFKABC',)


class _ModelWithDeviceClassFKABC(Model):
    machine_class = \
        ForeignKey(
            verbose_name='Device Class',
            help_text='Device Class',

            to=DeviceClass,
            on_delete=PROTECT,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
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

            limit_choices_to=None,

            # docs.djangoproject.com/en/dev/topics/db/models/#multi-table-inheritance
            # >> be careful with related_name and related_query_name
            # the following default to `Meta.default_related_name`
            # related_name='%(class)s_set',
            # related_query_name='%(class)s',

            to_field=None,
            db_constraint=True,
            swappable=True)

    class Meta:
        """Metadata."""

        abstract = True
