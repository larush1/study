# ID 67280378
class Error(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, x):
        if self.max_size != self.size:
            self.queue[(self.head - 1) % self.max_size] = x
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            raise Error

    def push_front(self, x):
        if self.max_size != self.size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            raise Error

    def pop_back(self):
        if self.size != 0:
            x = self.queue[(self.head)]
            self.queue[(self.head)] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return x
        else:
            raise Error

    def pop_front(self):
        if self.size != 0:
            x = self.queue[(self.tail - 1) % self.max_size]
            self.queue[(self.tail - 1) % self.max_size] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return x
        else:
            raise Error


def run():
    num_com = int(input())
    max_size = int(input())
    q = Deque(max_size)
    for _ in range(num_com):
        command = input().split()
        method = getattr(q, command[0])
        # Не разобрался как получить по индексу объект из списка
        # если он есть по аналогии с dict.get(), чтобы не делать ветвление
        # Вместо if len() можно сделать try except IndexError, но наверное
        # делать вложенные try except не правильно.
        if len(command) > 1:
            try:
                method(command[1])
            except Error:
                print('error')
        else:
            try:
                print(method())
            except Error:
                print('error')


if __name__ == '__main__':
    run()
