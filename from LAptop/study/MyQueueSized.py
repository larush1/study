class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def push(self, x):
        if self.max_size != self.size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')
    
    def pop(self):
        if self.size != 0:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            print(x)
        else:
            print('None')

    def peek(self):
        if self.size != 0:
            print(self.queue[self.head])
        else:
            print('None')
    
    def get_size(self):
        print(self.size)


def run():
    num_com = int(input())
    max_size = int(input())
    q = MyQueueSized(max_size)
    for _ in range(num_com):
        command = input().split()
        if command[0] == 'push':
            q.push(command[1])
        if command[0] == 'pop':
            q.pop()
        if command[0] == 'peek':
            q.peek()
        if command[0] == 'size':
            q.get_size()



if __name__ == '__main__':
    run()