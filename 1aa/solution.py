#!/usr/bin/env python

import util
# util.DEBUG = True

class Word(object):

    def __init__(self):
        self.word = []

    def put(self, c):
        if not self.word:
            self.word.append(c)
        elif c >= self.word[0]:
            self.word.insert(0, c)
        else:
            self.word.append(c)

    def __str__(self):
        return ''.join(self.word)


def solution(idx):
    raw = raw_input()
    word = Word()
    for c in raw:
        word.put(c)
    s = str(word)
    util.print_case(idx, s)


if __name__ == '__main__':
    count = util.int_input()  # float_input, list_input
    util.loop(count, solution)
