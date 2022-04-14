# XXXXXXXXXXX
class Node:
    def __init__(self, value, prev_item=None, next_item=None):
        self.value = value
        self.prev_item = prev_item
        self.next_item = next_item


class Queue():
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.head = None
        self.last = None

    def push_back(self, x):
        node = Node(value=x)
        if self.max_size != self.size:
            if self.size == 0:
                self.head = node
                self.last = node
            else:
                node.prev_item = self.last
                self.last.next_item = node
            self.last = node
            self.size += 1
        else:
            print('error')

    def push_front(self, x):
        node = Node(value=x)
        if self.max_size != self.size:
            if self.size == 0:
                self.head = node
                self.last = node
            else:
                node.next_item = self.head
                self.head.prev_item = node
            self.head = node
            self.size += 1
        else:
            print('error')

    def pop_back(self):
        if self.size == 0:
            print('error')
        else:
            x = self.last
            self.last = self.last.prev_item
            self.size -= 1
            print(x.value)

    def pop_front(self):
        if self.size == 0:
            print('error')
        else:
            x = self.head
            self.head = self.head.next_item
            self.size -= 1
            print(x.value)

    def get_size(self):
        print(self.size)


def run():
    num_com = int(input())
    max_size = int(input())
    q = Queue(max_size) 
    for _ in range(num_com):
        command = input().split()
        if command[0] == 'push_back':
            q.push_back(command[1])
        if command[0] == 'push_front':
            q.push_front(command[1])
        if command[0] == 'pop_back':
            q.pop_back()
        if command[0] == 'pop_front':
            q.pop_front()

if __name__ == '__main__':
    run()