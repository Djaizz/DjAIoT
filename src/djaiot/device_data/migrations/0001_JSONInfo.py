"""JSON Info."""


# pylint: disable=invalid-name


import json.decoder
import uuid

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):
    """JSON Info."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='JSONInfo',

            fields=[
                ('uuid',
                 models.UUIDField(
                     db_index=True,
                     default=uuid.uuid4,
                     editable=False,
                     help_text='UUID',
                     primary_key=True,
                     serialize=False,
                     unique=True,
                     verbose_name='UUID')),

                ('info',
                 models.JSONField(
                     blank=True,
                     decoder=json.decoder.JSONDecoder,
                     default=None,
                     encoder=django.core.serializers.json.DjangoJSONEncoder,
                     help_text='JSON Info',
                     null=True,
                     verbose_name='JSON Info'))
            ],

            options={
                'verbose_name': 'JSON Info',
                'verbose_name_plural': 'JSON Info',
                'db_table': 'IoTDeviceData_JSONInfo',
                'ordering': (),
                'permissions': (),
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'proxy': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'select_on_save': False,
                'default_related_name': 'json_info',
                'required_db_features': (),
                'base_manager_name': 'objects',
                'default_manager_name': 'objects'
            }
        )
    ]
