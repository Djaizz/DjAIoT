from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application

from importlib.util import module_from_spec, spec_from_file_location
import os
from pathlib import Path
from ruamel import yaml
from typing import Optional


_DJAI_CONFIG_FILE_NAME = '.config.yml'


def parse_config_file(path: Optional[str] = None):
    if path is None:
        path = os.environ.get(
                'DJAI_CONFIG_FILE_PATH',
                _DJAI_CONFIG_FILE_NAME)

    assert os.path.isfile(path), \
        FileNotFoundError(f'*** CONFIG FILE {path} NOT FOUND ***')

    # parse whole YAML config file
    config = yaml.safe_load(stream=open(path))

    # read and adjust DB config section
    db_config = config.get('db')
    assert db_config, f'*** "db" KEY NOT FOUND IN {config} ***'

    db_engine = db_config.get('engine')
    assert db_engine, f'*** "engine" KEY NOT FOUND IN {db_config} ***'
    assert db_engine in ('postgresql', 'mysql', 'sqlite3'), \
        ValueError(f'*** "{db_engine}" DATABASE ENGINE NOT SUPPORTED ***')

    db_name = db_config.get('name')
    assert db_name, f'*** "name" KEY NOT FOUND IN {db_config} ***'

    db_host = db_config.get('host')
    db_user = db_config.get('user')
    db_password = db_config.get('password')
    if db_engine != 'sqlite3':
        assert db_host, f'*** HOST NOT FOUND IN {db_config} ***'
        assert db_user, f'*** USER NOT FOUND IN {db_config} ***'
        assert db_password, f'*** PASSWORD NOT FOUND IN {db_config} ***'

    config['db'] = dict(ENGINE=f'django.db.backends.{db_engine}',
                        NAME=db_name,
                        HOST=db_host,
                        PORT=(5432
                                if db_engine == 'postgresql'
                                else (3306
                                    if db_engine == 'mysql'
                                    else None)),
                        USER=db_user,
                        PASSWORD=db_password)

    return config


def config_app(app_dir_path: str, config_file_path: str, asgi: bool = False):
    # docs.python.org/3/library/importlib.html#importing-a-source-file-directly
    import_spec = \
        spec_from_file_location(
            name='settings',
            location=Path(app_dir_path) / 'settings.py')
    _settings = module_from_spec(spec=import_spec)
    import_spec.loader.exec_module(module=_settings)

    config = parse_config_file(path=config_file_path)
    _settings.DATABASES['default'] = config['db']

    os.chdir(path=app_dir_path)

    # ref: https://code.djangoproject.com/ticket/31056
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    settings.configure(
        **{setting_key: setting_value
           for setting_key, setting_value in _settings.__dict__.items()
           if setting_key.isupper()})

    if asgi:
        get_asgi_application()
    else:
        get_wsgi_application()
