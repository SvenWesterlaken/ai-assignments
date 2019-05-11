class NumberNode(object):

    def __init__(self, result, goal, left_overs, nr='', prev=None, op=None):
        self.prev = prev
        self.op = op
        self.nr = nr
        self.result = result
        self.goal = goal
        self.left_overs = left_overs

        self.equation = self.__set_equation()

    def __gt__(self, value):
        current_nr = abs(self.goal - self.result)
        new_nr = abs(self.goal - value)

        return current_nr > new_nr

    def __lt__(self, value):
        current_nr = abs(self.goal - self.result)
        new_nr = abs(self.goal - value)

        return current_nr < new_nr

    def __eq__(self, value):
        return self.result == value

    def __rsub__(self, value):
        return self.result - value

    def __str__(self):
        return str(self.result)

    def __add__(self, value):
        return result + value

    def __repr__(self):
        return str(self.equation)

    def __set_equation(self):
        if not self.prev:
            return self.nr

        prev_e = f'({self.prev.equation})' if self.prev and self.op in ['/', '*'] and self.prev.op in ['-', '+'] else self.prev.equation

        return f'{prev_e} {self.op} {self.nr}' if self.prev else self.nr

    def is_solution(self):
        return int(self.result) == self.goal
