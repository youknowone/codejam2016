
from solution import Stack


def test_flip():
    s = Stack.from_str('++--+-')
    assert s == [True, True, False, False, True, False]
    assert str(s) == '++--+-'

    s.flip(2)
    assert str(s) == '----+-'


def test_regular():
    s = Stack.from_str('--+-')
    n = s.solve_regular()
    assert str(s) == '++++'
    assert n == 3


def test_quick():
    import random
    for i in range(0, 10000):
        tcount = i % 100
        fcount = 100 - tcount
        tset = [True] * tcount + [False] * fcount
        random.shuffle(tset)
        s1 = Stack(tset)
        s2 = Stack(tset)
        assert s1.solve_regular() == s2.solve_quick()
