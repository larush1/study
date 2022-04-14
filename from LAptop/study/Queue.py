class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0 

    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x 


q = Queue(8) 
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
q.push(7)
q.push(8)
q.pop()
q.pop()
q.pop()
q.pop()
q.pop()
q.pop()
q.pop()
q.push(1)
q.pop()
# q.push(6)
# q.push(7)
# q.push(8)

print(q.queue)
print(q.size)
print(q.head)
print(q.tail)