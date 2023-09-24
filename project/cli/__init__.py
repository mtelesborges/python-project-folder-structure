import click

from project.cli.fibonacci import fibonacci


@click.group()
def cli():
    ...


cli.add_command(fibonacci)
