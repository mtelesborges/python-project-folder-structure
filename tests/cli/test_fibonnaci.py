import pytest
from click.testing import CliRunner

from project.cli.fibonacci import fibonacci


@pytest.fixture()
def runner():
    return CliRunner()


def test_n_lass_than_0(runner):
    result = runner.invoke(fibonacci, ['--number', '-1'])

    assert result.output == '[]\n'
    assert result.exit_code == 0


def test_n_equal_0(runner):
    result = runner.invoke(fibonacci, ['--number', '0'])

    assert result.output == '[]\n'
    assert result.exit_code == 0


def test_n_equal_1(runner):
    result = runner.invoke(fibonacci, ['--number', '1'])

    assert result.output == '[0]\n'
    assert result.exit_code == 0


def test_n_equal_2(runner):
    result = runner.invoke(fibonacci, ['--number', '2'])

    assert result.output == '[0, 1]\n'
    assert result.exit_code == 0


def test_n_greater_than_2(runner):
    result = runner.invoke(fibonacci, ['--number', '4'])

    assert result.output == '[0, 1, 1, 2]\n'
    assert result.exit_code == 0
