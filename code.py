class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if len(self.items):
            self.items.pop()
        else:
            # return self.items.append('error')
            print('error')

    def get_max(self):
        if len(self.items):
            print(max(self.items))
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
    # return stack.items

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
