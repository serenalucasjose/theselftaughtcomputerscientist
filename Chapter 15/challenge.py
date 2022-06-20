class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        if self.left_child == None:
           self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
           self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

def is_min_heap(tree):
    if tree:
        if (tree.left_child is not None and tree.key > tree.left_child.key):
            return False
        if (tree.right_child is not None and tree.key > tree.right_child.key):
            return False
        else:
            return is_min_heap(tree.left_child) and is_min_heap(tree.right_child)
    return True

# Client
min_heap_tree = BinaryTree(1)
min_heap_tree.insert_left(2)
min_heap_tree.insert_right(3)
min_heap_tree.left_child.insert_left(6)
min_heap_tree.left_child.insert_right(4)
min_heap_tree.right_child.insert_left(8)
min_heap_tree.right_child.insert_right(10)

normal_tree = BinaryTree(1)
normal_tree.insert_left(4)
normal_tree.insert_right(5)
normal_tree.left_child.insert_left(2)
normal_tree.left_child.insert_right(6)
normal_tree.right_child.insert_right(3)

print(is_min_heap(min_heap_tree))
print(is_min_heap(normal_tree))