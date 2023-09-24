import click

from project.cli.fibonacci import fibonacci


@click.group()
def cli():
    pass  # pragma: no cover


cli.add_command(fibonacci)
