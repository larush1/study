class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None
    
    def put(self, x):
        node = Node(value=x)
        if self.size == 0:
            self.head = node
        else:
            self.last.next_item = node
        self.last = node
        self.size += 1

    def get(self):
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
    q = Queue()
    for _ in range(num_com):
        command = input().split()
        if command[0] == 'put':
            q.put(command[1])
        if command[0] == 'get':
            q.get()
        if command[0] == 'size':
            q.get_size()



if __name__ == '__main__':
    run()