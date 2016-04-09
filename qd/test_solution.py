
from solution import *

import pytest


def test_factors_from_index():
    f = Fractal(10, 6)
    for i in range(0, 100000):
        factors = f.factors_from_index(i)
        assert int(''.join(map(str, factors))[::-1]) == i


def test_index_from_factors():
    f = Fractal(7, 5)
    v = f.volume
    for i in range(0, v):
        factors = f.factors_from_index(i)
        j = f.index_from_factors(factors)
        assert i == j


@pytest.mark.parametrize("k,c,s,indexset", [
    (2, 3, 2, [2]),
    (1, 1, 1, [1]),
    (2, 1, 2, [1, 2]),
    (3, 2, 3, [2, 6]),
])
def test_search(k, c, s, indexset):
    f = Fractal(k, c)
    assert f.validate_indexset(machinize(indexset))
    assert f.validate_indexset(f.search_indexset())

    # assert indexset == humanize(f.search_indexset())
