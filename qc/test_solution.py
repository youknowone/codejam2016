
from solution import JamCoin, PrimeDatabase


def test_jamcoin_str():
    assert JamCoin.from_str('100011') == [1, 1, 0, 0, 0, 1]


def test_jamcoin_generate():
    for i in range(2, 32):
        coin = JamCoin.generate(i)
        assert len(coin) == i


def test_as_base():
    coin = JamCoin.from_str('1001')
    assert coin.as_bases() == [9, 28, 65, 126, 217, 344, 513, 730, 1001]


def test_prime_database():
    db = PrimeDatabase(15485863)
    assert len(db.primes) == 1000000
