class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self._size = 0
    
    def enqueue(self, item):
        self.s1.append(item)
        self._size += 1

    def dequeue(self):
        while(len(self.s1) != 0):
            self.s2.append(self.s1.pop())
        temp = self.s2.pop()
        while(len(self.s2) != 0):
            self.s1.append(self.s2.pop())
        self._size -= 1        
        return temp

    def size(self):
        return self._size

# Client
wordsQueue = Queue()

wordsQueue.enqueue('First')
wordsQueue.enqueue('Second')
wordsQueue.enqueue('Third')
wordsQueue.enqueue('Fourth')
wordsQueue.enqueue('Fifth')

while(wordsQueue.size() > 0):
    print(wordsQueue.dequeue())