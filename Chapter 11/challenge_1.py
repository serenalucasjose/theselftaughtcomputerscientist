class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0

def balancedString(string):
    specialChars = Stack()
    
    for c in string:
        if c == '(' or c == '[':
            specialChars.push(c)
        if c == ')' or c == ']':
            if specialChars.isEmpty():
                return False
            else:
                specialChars.pop()
    return specialChars.isEmpty()

# Client
balancedStr = '()[]'
unBalancedStr = '())[[]'

print(balancedString(balancedStr))
print(balancedString(unBalancedStr))