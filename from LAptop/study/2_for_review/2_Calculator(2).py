# 67329972
class Error(Exception):
    pass


class Node:
    def __init__(self, value, prev_item=None):
        self.value = value
        self.prev_item = prev_item


class Stack:
    def __init__(self):
        self.size = 0
        self.last = None

    def put(self, num):
        node = Node(value=num)
        if self.size == 0:
            self.last = node
        else:
            node.prev_item = self.last
        self.last = node
        self.size += 1

    def pop(self):
        if self.size != 0:
            x = self.last
            self.last = self.last.prev_item
            self.size -= 1
            return x.value
        else:
            raise Error


def run():
    calc = Stack()
    inp = input()
    seq = inp.split()
    add = lambda x, y: x + y
    sub = lambda x, y: x - y
    mul = lambda x, y: x * y
    floordiv = lambda x, y: x // y
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
    }
    for i in seq:
        if i in operators:
            b = calc.pop()
            a = calc.pop()
            res = operators[i](a, b)
            calc.put(res)
        else:
            i = int(i)
            calc.put(i)
    print(calc.pop())


if __name__ == '__main__':
    run()
