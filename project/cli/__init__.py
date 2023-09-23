import click
from cli.fibonacci import fibonacci


@click.group()
def cli():
    ...


cli.add_command(fibonacci)
