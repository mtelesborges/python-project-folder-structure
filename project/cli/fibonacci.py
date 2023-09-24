import click

import project.resources


@click.command(help='Create a list with the fibonacci sequence')
@click.option('--number', '-n', default=1, type=int)
def fibonacci(number: int) -> None:
    sequence = project.resources.fibonacci.fibonacci(number)
    click.echo(sequence)
