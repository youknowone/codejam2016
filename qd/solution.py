#!/usr/bin/env python

import util
# util.DEBUG = True


class Fractal(object):
    def __init__(self, sequence_size, complexity):
        self.sequence_size = sequence_size
        self.complexity = complexity

    @property
    def volume(self):
        return self.sequence_size ** self.complexity

    def factors_from_index(self, index):
        assert 0 <= index < self.volume
        factors = []
        for dim in range(0, self.complexity):
            m = index / (self.sequence_size ** dim)
            factors.append(m % self.sequence_size)
        assert len(factors) == self.complexity
        return factors

    def index_from_factors(self, factors):
        assert len(factors) == self.complexity
        index = 0
        for dim, factor in enumerate(factors):
            index += factor * (self.sequence_size ** dim)
        return index

    def search_indexset(self):
        factor_space = list(range(0, self.sequence_size))  # 탐색해야 하는 factors

        indexset = []
        while factor_space:
            factors = factor_space[:self.complexity]  # 한번에 탐색할 수 있는 차원
            del factor_space[:self.complexity]
            if len(factors) < self.complexity:
                factors += [0] * self.complexity
                factors = factors[:self.complexity]
            index = self.index_from_factors(factors)
            indexset.append(index)
        indexset.sort()
        assert self.validate_indexset(indexset)
        return indexset

    def validate_indexset(self, indexset):
        factorss = [self.factors_from_index(i) for i in indexset]
        factors = reduce(lambda a, b: a + b, factorss, [])
        return set(range(0, self.sequence_size)) == set(factors)


def humanize(x):
    return map(lambda e: e + 1, x)


def machinize(x):
    return map(lambda e: e - 1, x)


def solution(idx):
    K, C, S = map(int, util.list_input())
    sequence_size = K
    complexity = C
    tester_count = S

    # K진수의 C자리 숫자(0이 패딩)에서 모든 수를 뽑는 문제와 같음
    # 한번에 C자리 뽑을 수 있으므로 C*S가 K보다 작으면 망함
    f = Fractal(sequence_size, complexity)
    indexset = humanize(f.search_indexset())
    if len(indexset) > tester_count:
        util.print_case(idx, 'IMPOSSIBLE')
    else:
        util.print_case(idx, ' '.join(map(str, indexset)))


if __name__ == '__main__':
    count = util.int_input()  # float_input, list_input
    util.loop(count, solution)