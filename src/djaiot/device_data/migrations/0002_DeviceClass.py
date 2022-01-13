"""DjAIoT Device Class model."""


# pylint: disable=invalid-name


from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    """DjAIoT Device Class model."""

    dependencies = [
        ('IoTDeviceData', '0001_JSONInfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceClass',

            fields=[
                ('jsoninfo_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='IoTDeviceData.jsoninfo')),

                ('name',
                 models.CharField(
                     db_index=True,
                     default=None,
                     help_text='Unique Name',
                     max_length=255,
                     unique=True,
                     verbose_name='Unique Name')),

                ('created',
                 model_utils.fields.AutoCreatedField(
                     default=django.utils.timezone.now,
                     editable=False,
                     verbose_name='created')),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(
                     default=django.utils.timezone.now,
                     editable=False,
                     verbose_name='modified'))
            ],

            options={
                'verbose_name': 'Device Class',
                'verbose_name_plural': 'Device Classes',
                'db_table': 'IoTDeviceData_DeviceClass',
                'ordering': ('name',),
                'permissions': (),
                'db_tablespace': '',
                'abstract': False,
                'managed': True,
                'proxy': False,
                'default_permissions': ('add', 'change', 'delete', 'view'),
                'select_on_save': False,
                'default_related_name': 'device_classes',
                'required_db_features': (),
                'base_manager_name': 'objects',
                'default_manager_name': 'objects'
            },

            bases=('IoTDeviceData.jsoninfo',
                   models.Model)
        )
    ]
