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

# Client
myList = LinkedList()

for num in range(100):
    myList.append(Node(num))

myList.printList()