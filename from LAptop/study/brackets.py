class Node:  
    def __init__(self, value, prev_item=None):  
        self.value = value  
        self.prev_item = prev_item


class Stack:
    def __init__(self):
        self.nodes = [Node(value=None)]

    def push(self, value):
        self.nodes.append(Node(value=value, prev_item=self.nodes[-1]))

    def pop(self):
        return self.nodes.pop()

def run():
    stack = Stack()
    # inp = '[{}()]'
    inp = input()
    opening = ('[','(','{')
    closing = (']',')','}')
    pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
}
    for i in inp:
        if i in opening:
            stack.push(i)
        if i in closing:
            poping = stack.pop()
            if poping.value != pairs[i]:
                return False
    if len(stack.nodes) > 1:
        return False
    return True




if __name__ == '__main__':
    print(run())