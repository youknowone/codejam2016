
import util
util.DEBUG = True
from util import Plain

def test_plain():
    p = Plain((5, 7))
    p.debug()
    p[1, 2] = 10
    assert p[1, 2] == 10
    p.debug()
    assert p.data[1 * 7 + 2] == 10
    p[3, 5] = 12
    assert p[3, 5] == 12
    p.debug()
    assert p.data[3 * 7 + 5] == 12

if __name__ == '__main__':
    test_plain()