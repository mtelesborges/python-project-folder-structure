from project.resources.fibonacci import fibonacci


def test_n_lass_than_0():
    result = fibonacci(-1)
    assert result == []


def test_n_equal_0():
    result = fibonacci(0)
    assert result == []


def test_n_equal_1():
    result = fibonacci(1)
    assert result == [0]


def test_n_equal_2():
    result = fibonacci(2)
    assert result == [0, 1]


def test_n_greater_than_2():
    result = fibonacci(4)
    assert result == [0, 1, 1, 2]
