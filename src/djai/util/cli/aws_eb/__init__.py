import click
import os
from pathlib import Path
from ruamel import yaml
import shutil
from typing import Optional

from .. import run_command_with_config_file, __path__


_EB_EXTENSIONS_DIR_NAME = '.ebextensions'
_EB_IGNORE_FILE_NAME = '.ebignore'
_PLATFORM_DIR_NAME = '.platform'


def aws_eb_init():
    os.system(command='eb init')


def aws_eb_deploy(
        djai_config_file_path: str,
        aws_eb_env_name: Optional[str] = None,
        asgi: Optional[str] = None,
        create: bool = False):
    configs = yaml.safe_load(stream=open(djai_config_file_path))
    aws_configs = configs['aws']
    profile = aws_configs.get('profile', 'default')
    region = aws_configs['region']
    vpc = aws_configs['vpc']
    subnets = aws_configs['subnets']
    instance_type = aws_configs['instance-type']
    assert region and vpc and subnets

    _aws_eb_cli_util_dir_path = Path(__path__[0]) / 'aws_eb'

    assert not os.path.exists(path=_EB_EXTENSIONS_DIR_NAME)
    shutil.copytree(
        src=_aws_eb_cli_util_dir_path / _EB_EXTENSIONS_DIR_NAME,
        dst=_EB_EXTENSIONS_DIR_NAME,
        symlinks=False,
        ignore=None,
        ignore_dangling_symlinks=False,
        dirs_exist_ok=False)
    assert os.path.isdir(_EB_EXTENSIONS_DIR_NAME)

    _eb_ignore_exists = os.path.exists(path=_EB_IGNORE_FILE_NAME)

    if _eb_ignore_exists:
        assert os.path.isfile(_EB_IGNORE_FILE_NAME)

    else:
        shutil.copyfile(
            src=_aws_eb_cli_util_dir_path / _EB_IGNORE_FILE_NAME,
            dst=_EB_IGNORE_FILE_NAME)
        assert os.path.isfile(_EB_IGNORE_FILE_NAME)

    assert not os.path.exists(path=_PLATFORM_DIR_NAME)
    shutil.copytree(
        src=_aws_eb_cli_util_dir_path / _PLATFORM_DIR_NAME,
        dst=_PLATFORM_DIR_NAME,
        symlinks=False,
        ignore=None,
        ignore_dangling_symlinks=False,
        dirs_exist_ok=False)
    assert os.path.isdir(_PLATFORM_DIR_NAME)

    run_command_with_config_file(
        command=('eb ' +
                 ((f'create --region {region} --vpc.id {vpc}'
                   f' --vpc.dbsubnets {subnets} --vpc.ec2subnets {subnets}'
                   f' --vpc.elbsubnets {subnets} --vpc.elbpublic'
                   ' --vpc.publicip'
                   f' --instance_type {instance_type}')
                  if create
                  else 'deploy') +
                 (f' --profile {profile}'
                  f" {aws_eb_env_name if aws_eb_env_name else ''}")),
        djai_config_file_path=djai_config_file_path,
        copy_standard_files=True,
        asgi=asgi)

    shutil.rmtree(
        path=_EB_EXTENSIONS_DIR_NAME,
        ignore_errors=False,
        onerror=None)
    assert not os.path.exists(path=_EB_EXTENSIONS_DIR_NAME)

    if not _eb_ignore_exists:
        os.remove(_EB_IGNORE_FILE_NAME)
        assert not os.path.exists(path=_EB_IGNORE_FILE_NAME)

    shutil.rmtree(
        path=_PLATFORM_DIR_NAME,
        ignore_errors=False,
        onerror=None)
    assert not os.path.exists(path=_PLATFORM_DIR_NAME)


@click.command(
    name='aws-eb',
    cls=click.Command,
    context_settings=None,
    help='DjAI AWS Elastic Beanstalk CLI >>>',
    epilog='^^^ DjAI AWS Elastic Beanstalk CLI',
    short_help='DjAI AWS-EB',
    options_metavar='',
    add_help_option=True,
    hidden=False,
    deprecated=False)
@click.argument(
    'command',
    cls=click.Argument,
    required=True,
    type=str,
    default=None)
def djai_aws_eb(command: str):
    """
    DjAI AWS Elastic Beanstalk CLI
    """


if __name__ == '__main__':
    djai_aws_eb()
