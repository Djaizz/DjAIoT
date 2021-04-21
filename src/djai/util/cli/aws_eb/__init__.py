import click
import os
from pathlib import Path
from ruamel import yaml
import shutil
from typing import Optional

from ..run_cmd import run_command_with_config_file


_DJAI_AWS_EB_CLI_UTIL_DIR_PATH = Path(__file__).parent
_EB_EXTENSIONS_DIR_NAME = '.ebextensions'
_EB_IGNORE_FILE_NAME = '.ebignore'
_PLATFORM_DIR_NAME = '.platform'


@click.command(
    name='init',
    cls=click.Command,
    context_settings=None,
    help='DjAI AWS Elastic Beanstalk CLI: Initialize Configuration >>>',
    epilog='^^^ DjAI AWS Elastic Beanstalk CLI: Initialize Configuration',
    short_help='DjAI AWS-EB Init',
    options_metavar='',
    add_help_option=True,
    hidden=False,
    deprecated=False)
def init():
    """
    DjAI AWS Elastic Beanstalk CLI: Initialize Configuration
    """

    os.system(command='eb init')


@click.command(
    name='deploy',
    cls=click.Command,
    context_settings=None,
    help='DjAI AWS Elastic Beanstalk CLI: Deploy >>>',
    epilog='^^^ DjAI AWS Elastic Beanstalk CLI: Deploy',
    short_help='DjAI AWS-EB Deploy',
    options_metavar='',
    add_help_option=True,
    hidden=False,
    deprecated=False)
@click.argument(
    'djai_config_file_path',
    cls=click.Argument,
    required=True,
    type=str,
    default=None,
    callback=None,
    nargs=None,
    metavar='DJAI_CONFIG_FILE_PATH',
    expose_value=True,
    is_eager=False,
    envvar=None,
    autocompletion=None)
@click.argument(
    'aws_eb_env_name',
    cls=click.Argument,
    required=False,
    type=str,
    default=None,
    callback=None,
    nargs=None,
    metavar='AWS_EB_ENV_NAME',
    expose_value=True,
    is_eager=False,
    envvar=None,
    autocompletion=None)
@click.option(
    '--asgi',
    cls=click.Option,
    show_default=True,
    prompt=False,
    confirmation_prompt=False,
    hide_input=False,
    is_flag=False,
    # flag_value=...,
    multiple=False,
    count=False,
    allow_from_autoenv=False,
    type=str,
    help='ASGI Server (daphne, hypercorn, uvicorn) to use',
    show_choices=True,
    default='None',
    required=False,
    callback=None,
    nargs=None,
    metavar='ASGI',
    expose_value=True,
    is_eager=False,
    envvar=None)
@click.option(
    '--create',
    cls=click.Option,
    show_default=True,
    prompt=False,
    confirmation_prompt=False,
    hide_input=False,
    is_flag=True,
    flag_value=True,
    multiple=False,
    count=False,
    allow_from_autoenv=False,
    type=bool,
    help='whether to create a new AWS Elastic Beanstalk environment',
    show_choices=True,
    default=False,
    required=False,
    callback=None,
    nargs=None,
    metavar='CREATE',
    expose_value=True,
    is_eager=False,
    envvar=None)
def deploy(
        djai_config_file_path: str,
        aws_eb_env_name: Optional[str] = None,
        asgi: Optional[str] = None,
        create: bool = False):
    """
    DjAI AWS Elastic Beanstalk CLI: Deploy
    """

    configs = yaml.safe_load(stream=open(djai_config_file_path))
    aws_configs = configs['aws']
    profile = aws_configs.get('profile', 'default')
    region = aws_configs['region']
    vpc = aws_configs['vpc']
    subnets = aws_configs['subnets']
    instance_type = aws_configs['instance-type']
    assert region and vpc and subnets

    assert not os.path.exists(path=_EB_EXTENSIONS_DIR_NAME)
    shutil.copytree(
        src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _EB_EXTENSIONS_DIR_NAME,
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
            src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _EB_IGNORE_FILE_NAME,
            dst=_EB_IGNORE_FILE_NAME)
        assert os.path.isfile(_EB_IGNORE_FILE_NAME)

    assert not os.path.exists(path=_PLATFORM_DIR_NAME)
    shutil.copytree(
        src=_DJAI_AWS_EB_CLI_UTIL_DIR_PATH / _PLATFORM_DIR_NAME,
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


@click.group(
    name='aws-eb',
    cls=click.Group,
    commands={'init': init, 'deploy': deploy},
    invoke_without_command=False,
    no_args_is_help=True,
    subcommand_metavar='DJAI_AWS_EB_SUB_COMMAND',
    chain=True,
    help='DjAI AWS Elastic Beanstalk CLI >>>',
    epilog='^^^ DjAI AWS Elastic Beanstalk CLI',
    short_help='DjAI AWS-EB CLI',
    options_metavar='',
    add_help_option=True,
    hidden=False,
    deprecated=False)
def djai_aws_eb():
    """
    DjAI AWS Elastic Beanstalk CLI
    """
