import pytest
from click.testing import CliRunner

from project.cli import cli


@pytest.fixture()
def runner():
    return CliRunner()


def test_cli_should_show_help_message(runner):
    result = runner.invoke(cli, ['--help'])

    assert result.output is not None
    assert result.exit_code == 0


def test_cli_should_show_help_message_if_no_argument_is_provided(runner):
    result = runner.invoke(cli, [])

    assert result.output is not None
    assert result.exit_code == 0
