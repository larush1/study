class Stack:

    def __init__(self):
        self.items = []
        self.last_max = None

    def push(self, item):
        if self.last_max is None:
            self.last_max = int(item)
        if int(item) > self.last_max:
            self.last_max = int(item)
        self.items.append(int(item))

    def pop(self):
        if len(self.items):
            self.items.pop()
        else:
            print('error')
        if len(self.items):
            self.last_max = max(self.items)
        else:
            self.last_max = None

    def get_max(self):
        if not self.last_max is None:
            print(self.last_max)
        else:
            # return self.items.append('None')
            print('None')

def run():
    stack = Stack()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(command[1])
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()

def print_result(items):
    for i in items:
        print(i)


if __name__ == '__main__':
    run()
    # print_result(run())
    # stack = Stack()
    # print(stack.get_max())
    # print(stack.pop())
    # stack.push('apple')
    # stack.push('banana')
    # stack.push('orange')
    # print(stack.pop())
