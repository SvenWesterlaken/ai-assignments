from functools import total_ordering

@total_ordering
class NumberNode(object):

    def __init__(self, result, goal, left_overs, nr='', prev=None, op=None):
        self.prev = prev
        self.op = op
        self.nr = nr
        self.result = result
        self.goal = goal
        self.left_overs = left_overs

        self.equation = self.__set_equation()

    def __set_equation(self):
        if not self.prev:
            return self.nr

        prev_e = f'({self.prev.equation})' if self.prev and self.op in ['/', '*'] and self.prev.op in ['-', '+'] else self.prev.equation

        return f'{prev_e} {self.op} {self.nr}' if self.prev else self.nr

    def __partial_equal(self, other, s, o):
        return type(self) == type(other) and s == o

    def is_solution(self):
        return int(self.result) == self.goal

    def __lt__(self, other):
        s = abs(self.goal - self.result)
        o = abs(self.goal - other)

        if self.__partial_equal(other, s, o):
            return len(self.left_overs) < len(other.left_overs)

        return s < o

    def __eq__(self, other):
        s = abs(self.goal - self.result)
        o = abs(self.goal - other)

        return self.__partial_equal(other, s, o) and len(self.left_overs) == len(other.left_overs)

    def __add__(self, other):
        return result + other

    def __rsub__(self, other):
        return self.result - other

    def __radd__(self, other):
        return self.result + other

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return str(self.equation)
