class Node:  
    def __init__(self, value, prev_item=None, max_value=None):  
        self.value = value  
        self.prev_item = prev_item
        self.max_value = max_value

class Stack:
    def __init__(self):
        self.nodes = [Node(value=None)]
        self.new_max = None

    def push(self, value):
        value = int(value)
        self.new_max = self.nodes[-1].max_value
        if self.nodes[-1].max_value == None:
            self.new_max = value
        else:
            if self.nodes[-1].max_value < value:
                self.new_max = value
        self.nodes.append(Node(value=value, prev_item=self.nodes[-1], max_value=self.new_max))
        # for i in range(len(self.nodes)):
        #     print(f'el{i} - value - {self.nodes[i].value} max_value - {self.nodes[i].max_value}')
        # print(f'переменная new_max = {self.new_max}')

    def pop(self):
        if self.nodes[-1].value == None:
            print('error')
        else:
            self.nodes.pop()
        # for i in range(len(self.nodes)):
        #     print(f'el{i} - value - {self.nodes[i].value} max_value - {self.nodes[i].max_value}')
        # print(f'переменная new_max = {self.new_max}')

    def get_max(self):
        if self.nodes[-1].max_value == None:
            print('None')
        else:
            print(self.nodes[-1].max_value)




def run():
    stack = Stack()
    n = input()
    for i in range(n):
        command = input().split()
        if command[0] == 'push':
            stack.push(command[1])
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()



if __name__ == '__main__':
    run()