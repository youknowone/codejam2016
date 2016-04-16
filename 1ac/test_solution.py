
from solution import *

import pytest


def test_something():
    pass


@pytest.mark.parametrize("test_input,expected", [
    ('input', 'expected'),
    ('input', 'expected'),
])
def test_parametrize(test_input, expected):
    assert test_input == 'input'
    assert expected == 'expected'
