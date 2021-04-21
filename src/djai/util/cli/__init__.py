import click

from .aws_eb import djai_aws_eb
from .run_cmd import run_command_with_config_file


# click.palletsprojects.com/en/master/advanced/#forwarding-unknown-options
@click.command(
    name='admin',
    cls=click.Command,
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
    help='DjAI Admin CLI >>>',
    epilog='^^^ DjAI Admin CLI',
    short_help='DjAI Admin CLI',
    options_metavar='[OPTIONS]',
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
    'django_admin_command',
    cls=click.Argument,
    required=True,
    type=str,
    default=None,
    callback=None,
    nargs=None,
    metavar='DJANGO_ADMIN_COMMAND',
    expose_value=True,
    is_eager=False,
    envvar=None,
    autocompletion=None)
@click.argument(
    'django_admin_args_and_opts',
    cls=click.Argument,
    required=False,
    type=click.UNPROCESSED,
    default=None,
    callback=None,
    nargs=-1,
    metavar='[DJANGO_ADMIN_CMD_ARGS_AND_OPTS]',
    expose_value=True,
    is_eager=False,
    envvar=None,
    autocompletion=None)
def admin(
        djai_config_file_path: str,
        django_admin_command: str,
        django_admin_args_and_opts: tuple):
    """
    DjAI Admin CLI
    """

    run_command_with_config_file(
        command=f'python3 -m django {django_admin_command} --settings settings'
                f" {' '.join(django_admin_args_and_opts)}",
        djai_config_file_path=djai_config_file_path)


@click.group(
    name='djai',
    cls=click.Group,
    commands={'admin': admin, 'aws-eb': djai_aws_eb},
    invoke_without_command=False,
    no_args_is_help=True,
    subcommand_metavar='DJAI_SUB_COMMAND',
    chain=False,
    help='DjAI CLI >>>',
    epilog='^^^ DjAI CLI',
    short_help='DjAI CLI',
    options_metavar='[OPTIONS]',
    add_help_option=True,
    hidden=False,
    deprecated=False)
def djai():
    """
    DjAI CLI
    """
