class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        done = False
        current = self.root
        
        while not done:
            if current.value > new_val:
                if current.left is None:
                    current.left = Node(new_val)
                    done = True
                else:
                    current = current.left
            elif current.value <= new_val:
                if current.right is None:
                    current.right = Node(new_val)
                    done = True
                else:
                    current = current.right
            
    def print_recursive(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        traversal.append(str(start.value))
        if start.left is not None:
            self.print_recursive(start.left, traversal)
        if start.right is not None:
            self.print_recursive(start.right, traversal)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        traversal = []
        self.print_recursive(self.root, traversal)
        return "-".join(traversal)
        
    def search(self, find_val):
        
        found = False
        current = self.root
        
        while current and not found:
            
            if current.value == find_val:
                found = True
            if current.value > find_val:
                    current = current.left
            elif current.value < find_val:
                    current = current.right
        return found

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
