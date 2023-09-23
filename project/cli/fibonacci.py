import click
from resources import fibonacci as fibonacci_impl


@click.command(help='Create a list with the fibonacci sequence')
@click.option('--number', '-n', default=1, type=int)
def fibonacci(number: int) -> None:
    sequence = fibonacci_impl.fibonacci(number)
    print(sequence)
