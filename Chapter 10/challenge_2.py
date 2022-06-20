class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = Node(node)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(node)

    def printList(self):
        current = self.head
        while current.next:
            print(current)
            current = current.next
        print(current)
    
    def detectCycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = self.next
                fast = self.next.next
                if slow == fast:
                    return True
            except:
                return False
# Client
myList = LinkedList()
myCycleList = LinkedList()

for num in range(4):
    myList.append(Node(num))
    myCycleList.append(Node(num))

# Cycle for testing
myCycleList.head.next.next.next.next = myCycleList.head

# Print
print('Loop in myList: ', myList.detectCycle())
print('Loop in myCycleList: ', myCycleList.detectCycle())