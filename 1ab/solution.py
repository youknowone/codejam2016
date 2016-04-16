#!/usr/bin/env python

import util
# util.DEBUG = True


class Grid(object):

    def __init__(self, n):
        self.n = n
        self.grid = {}
        self.hist = set()
        for i in range(0, n * n):
            for j in range(0, n * n):
                self.grid[i, j] = None

    def populate_row(self, order):
        for i in range(0, self.n):
            yield self.grid[order, i]

    def populate_col(self, order):
        for i in range(0, self.n):
            yield self.grid[i, order]

    def populate_order(self, order):
        order, col = order
        if col:
            return self.populate_col(order)
        else:
            return self.populate_row(order)

    def put_row(self, order, sequence):
        for i, height in enumerate(sequence):
            self.grid[order, i] = height

    def put_col(self, order, sequence):
        for i, height in enumerate(sequence):
            self.grid[i, order] = height

    def put_order(self, _order, sequence):
        order, col = _order
        if col:
            self.put_col(order, sequence)
        else:
            self.put_row(order, sequence)

    def validate_populated(self, populated, sequence):
        for s, p in zip(sequence, populated):
            if p is None:
                continue
            if s == p:
                continue
            return False
        return True

    def validate_order(self, order, sequence):
        order, col = order
        if col:
            populated = self.populate_col(order)
        else:
            populated = self.populate_row(order)
        return self.validate_populated(populated, sequence)

    def put(self, sequence):
        import random
        for order in range(0, self.n):
            colrow = [False, True]
            random.shuffle(colrow)
            for col in colrow:
                if (order, col) in self.hist:
                    continue

                is_valid = self.validate_order((order, col), sequence)
                if not is_valid:
                    continue

                self.put_order((order, col), sequence)
                self.hist.add((order, col))
                return

    def __repr__(self):
        s = []
        for i in range(0, self.n):
            for j in range(0, self.n):
                s.append(self.grid[i, j])
                s.append(' ')
            s.append('\n')
        return ''.join(map(str, s))

    @property
    def missed(self):
        assert len(self.hist) == self.n * 2 - 1
        for order in range(0, self.n):
            for col in [False, True]:
                if (order, col) in self.hist:
                    continue
                return self.populate_order((order, col))
        assert False

    def populate_missed(self):
        populated = self.missed
        return populated

    def put_sequences(self, sequences):
        sequences.sort()
        for sequence in sequences:
            self.put(sequence)

    @classmethod
    def solve(self, sequences):
        while True:
            grid = Grid(count)
            grid.put_sequences(sequences)
            try:
                grid.populate_missed()
            except AssertionError:
                raise
            else:
                return grid


def solution(idx):
    count = util.int_input()
    sequences = []
    for _ in range(0, count * 2 - 1):
        sequence = map(int, util.list_input())
        sequences.append(sequence)
    grid = Grid.solve(sequences)
    sol = grid.populate_missed()
    util.print_case(idx, ' '.join(map(str, sol)))


if __name__ == '__main__':
    count = util.int_input()  # float_input, list_input
    util.loop(count, solution)