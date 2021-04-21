import os
from pathlib import Path
import shutil
from typing import Optional

from ..config import (
    _DJAI_CONFIG_FILE_PATH_ENVVAR_NAME, _DJAI_CONFIG_FILE_NAME,
    parse_config_file
)
from ..git import _GIT_HASH_FILE_NAME, get_git_repo_head_commit_hash


_SERVER_FILES_DIR_PATH = Path(__file__).parent / '_server_files'

_ASGI_PY_FILE_NAME = 'asgi.py'
_ASGI_PY_FILE_SRC_PATH = _SERVER_FILES_DIR_PATH / _ASGI_PY_FILE_NAME

_WSGI_PY_FILE_NAME = 'wsgi.py'
_WSGI_PY_FILE_SRC_PATH = _SERVER_FILES_DIR_PATH / _WSGI_PY_FILE_NAME

_PROCFILE_NAME = 'Procfile'


def run_command_with_config_file(
        command: str,
        djai_config_file_path: Optional[str] = None,
        copy_standard_files: bool = False,
        asgi: Optional[str] = None):
    if djai_config_file_path:
        djai_config_file_path = Path(djai_config_file_path).expanduser()

    # verify config file is valid
    config = parse_config_file(path=djai_config_file_path)

    if copy_standard_files:
        assert not os.path.exists(path=_DJAI_CONFIG_FILE_NAME)
        shutil.copyfile(
            src=djai_config_file_path,
            dst=_DJAI_CONFIG_FILE_NAME)

        if asgi:
            assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
            shutil.copyfile(
                src=_ASGI_PY_FILE_SRC_PATH,
                dst=_ASGI_PY_FILE_NAME)
            assert not os.path.exists(path=_PROCFILE_NAME)
            shutil.copyfile(
                src=(_SERVER_FILES_DIR_PATH /
                     f'{_PROCFILE_NAME}.{asgi.capitalize()}'),
                dst=_PROCFILE_NAME)
        else:
            assert not os.path.exists(path=_WSGI_PY_FILE_NAME)
            shutil.copyfile(
                src=_WSGI_PY_FILE_SRC_PATH,
                dst=_WSGI_PY_FILE_NAME)

        assert not os.path.exists(path=_GIT_HASH_FILE_NAME)
        git_hash = get_git_repo_head_commit_hash()
        if git_hash:
            with open(_GIT_HASH_FILE_NAME, 'w') as f:
                f.write(git_hash)

    aws_config = config.get('aws')
    if aws_config:
        key = aws_config.get('key')
        secret = aws_config.get('secret')
        if key and secret:
            os.environ.setdefault('AWS_ACCESS_KEY_ID', key)
            os.environ.setdefault('AWS_SECRET_ACCESS_KEY', secret)

    print(f'Running Command: {command}...')
    os.system(
        (''
         if copy_standard_files
         else f'{_DJAI_CONFIG_FILE_PATH_ENVVAR_NAME}={djai_config_file_path} ')
        + command)

    if copy_standard_files:
        os.remove(_DJAI_CONFIG_FILE_NAME)
        assert not os.path.exists(path=_DJAI_CONFIG_FILE_NAME)

        if asgi:
            os.remove(_ASGI_PY_FILE_NAME)
            assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
            os.remove(_PROCFILE_NAME)
            assert not os.path.exists(path=_PROCFILE_NAME)
        else:
            os.remove(_WSGI_PY_FILE_NAME)
            assert not os.path.exists(path=_WSGI_PY_FILE_NAME)

        if git_hash:
            os.remove(_GIT_HASH_FILE_NAME)
            assert not os.path.exists(path=_GIT_HASH_FILE_NAME)
