from django.apps.config import AppConfig


class DjAIModelModuleConfig(AppConfig):
    # AppConfig.name
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to.
    # It must be set in all AppConfig subclasses.
    # It must be unique across a Django project.
    name = 'djai.model'

    # AppConfig.label
    # Short name for the application, e.g. 'admin'
    # This attribute allows relabeling an application
    # when two applications have conflicting labels.
    # It defaults to the last component of name.
    # It should be a valid Python identifier.
    # It must be unique across a Django project.
    label = 'DjAIModel'

    # AppConfig.verbose_name
    # Human-readable name for the application, e.g. “Administration”.
    # This attribute defaults to label.title().
    verbose_name = 'DjAI: Models'

    # AppConfig.path
    # Filesystem path to the application directory,
    # e.g. '/usr/lib/pythonX.Y/dist-packages/django/contrib/admin'.
    # In most cases, Django can automatically detect and set this,
    # but you can also provide an explicit override as a class attribute
    # on your AppConfig subclass.
    # In a few situations this is required; for instance
    # if the app package is a namespace package with multiple paths.

    # AppConfig.default
    # New in Django 3.2.
    # Set this attribute to False
    # to prevent Django from selecting a configuration class automatically.
    # This is useful when apps.py defines only one AppConfig subclass
    # but you don’t want Django to use it by default.
    # Set this attribute to True
    # to tell Django to select a configuration class automatically.
    # This is useful when apps.py defines more than one AppConfig subclass
    # and you want Django to use one of them by default.
    # By default, this attribute isn’t set.
    default = True

    # AppConfig.default_auto_field
    # New in Django 3.2.
    # The implicit primary key type to add to models within this app.
    # You can use this to keep AutoField
    # as the primary key type for third party applications.
    # By default, this is the value of DEFAULT_AUTO_FIELD.
    default_auto_field = 'django.db.models.fields.AutoField'
