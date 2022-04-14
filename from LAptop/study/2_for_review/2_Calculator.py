# 67280076
class Node:
    def __init__(self, value, prev_item=None):
        self.value = value
        self.prev_item = prev_item


class Calculator:
    def __init__(self):
        self.size = 0
        self.last = None

    def get_last_value(self):
        return self.last.value

    def put_num(self, num):
        node = Node(value=num)
        if self.size == 0:
            self.last = node
        else:
            node.prev_item = self.last
        self.last = node
        self.size += 1

    def plus(self):
        res = self.last.prev_item.value + self.last.value
        node = Node(value=res)
        node.prev_item = self.last.prev_item.prev_item
        self.last = node

    def minus(self):
        res = self.last.prev_item.value - self.last.value
        node = Node(value=res)
        node.prev_item = self.last.prev_item.prev_item
        self.last = node

    def multiplication(self):
        res = self.last.prev_item.value * self.last.value
        node = Node(value=res)
        node.prev_item = self.last.prev_item.prev_item
        self.last = node

    def division(self):
        res = self.last.prev_item.value // self.last.value
        node = Node(value=res)
        node.prev_item = self.last.prev_item.prev_item
        self.last = node


def run():
    calc = Calculator()
    inp = input()
    seq = inp.split()
    # Не смог понять зачем здесь лямбда функции или
    # модуль operator... Ведь для выполнения задачи
    # я должен оперировать объектом класса Calculator
    # и вызывать его методы...
    operators = {
        '+': calc.plus,
        '-': calc.minus,
        '*': calc.multiplication,
        '/': calc.division,
    }
    for i in seq:
        if i in operators:
            operators[i]()
        else:
            i = int(i)
            calc.put_num(i)
    print(calc.get_last_value())


if __name__ == '__main__':
    run()
