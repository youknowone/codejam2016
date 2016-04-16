#!/usr/bin/env python

import util
# util.DEBUG = True


class Tree(object):
    def __init__(self):
        self.left = Node()
        self.right = Node()

    @property
    def leftmost(self):
        top = self.left
        while top.item is not None:
            top = top[0]
        return top

    @property
    def rightmost(self):
        top = self.root[1]
        while top.item is not None:
            top = top[0]
        return top


class Node(object):
    def __init__(self):
        self.item = None


class Person(list):
    pass


class Circle(object):

    def __init__(self, n):
        self.people = []

        for _ in range(0, n):
            self.people.append(Person())

    def put_rel(self, i, j):
        j = j - 1
        self.people[i].append(j)

    def evaluate_link(self, root, parent, idx, people, depth=0):
        person = people.pop(idx)
        #print '\t' * depth, 'try:', idx, person, people
        maxpeople = people
        picked = []
        for i in person:
            if i not in people:
                continue
            speople = people.copy()
            rpeople, rpicked = self.evaluate_link(root, idx, i, speople, depth + 1)
            if maxpeople is None or len(rpeople) <= len(maxpeople):
                maxpeople = rpeople
                picked = rpicked
        if not picked:
            if root in person or parent in person:
                return maxpeople, [idx]
            else:
                return people, []
        else:
            return maxpeople, [idx] + picked

    def search_tree(self, i):
        people = {i: person for i, person in enumerate(self.people)}

        rpeople, picked = self.evaluate_link(i, None, i, people)
        #print 'r1', rpeople.keys(), picked
        return rpeople
        rpeople[i] = self.people[i]
        rpeople, picked = self.evaluate_link(i, i, rpeople)
        #print 'r2', rpeople.keys(), picked

        return rpeople

    def search(self):
        minimum = len(self.people)
        for i, p in enumerate(self.people):
            #print 'searching'
            rpeople = self.search_tree(i)
            minimum = min(minimum, len(rpeople))
        #print minimum
        return len(self.people) - minimum


def solution(idx):
    count = util.int_input()
    rels = map(int, util.list_input())
    assert count == len(rels)
    circle = Circle(count)
    for i, rel in enumerate(rels):
        # #print i, rel - 1
        circle.put_rel(i, rel)
    for i, person in enumerate(circle.people):
        pass
         #print i, person
    sol = circle.search()
    util.print_case(idx, sol)


if __name__ == '__main__':
    count = util.int_input()  # float_input, list_input
    util.loop(count, solution)