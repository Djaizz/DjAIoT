import click

from .aws_eb import djai_aws_eb


@click.command(
    name='admin',
    cls=click.Command,
    context_settings=None,
    help='DjAI Admin CLI >>>',
    epilog='^^^ DjAI Admin CLI',
    short_help='DjAI Admin CLI',
    options_metavar='[OPTIONS]',
    add_help_option=True,
    hidden=False,
    deprecated=False)
def admin():
    """
    DjAI Admin CLI
    """


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
