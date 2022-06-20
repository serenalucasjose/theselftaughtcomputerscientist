class MinFixedStack:
    def __init__(self, maxItems=10):
        self.items = []
        self.maxItems = maxItems
        self.max = -1
    
    def size(self):
        return len(self.items)

    def push(self, item):
        if self.size() < self.maxItems:
            self.items.append(item)
            if item > self.max:
                self.max = item
        else:
            return False

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

    def maxItem(self):
        return self.max


fixedStack = MinFixedStack(2)
fixedStack.push(4)
fixedStack.push(2)

print('Biggest item: ', fixedStack.maxItem(), '. Total size: ', fixedStack.size())