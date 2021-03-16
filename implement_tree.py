# generic tree implementation from Coding Cart YT tutorial

#######################################
# BST from Brian Faure YT tutorial
# at most 2 child nodes for each node
# every child node to the right is larger than parent, every child node left is smaller than parent

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree: # wrapper that handles managing all node classes
    def __init__(self):
        self.root = None

    def insert(self, value): # non-recursive, public
        # check if the root has a value yet
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root) # _ means "private" function, don't call outside of class

    # private insert function is recursive
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left) # recursion down left part of tree
        elif value > current_node.value: # value larger than current_node
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)
        else: # if they're the exact same, no dupes (in this iteration)
            print("value already in tree")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root) # another private, recursive

    def _printTree(self, current_node):
        if current_node != None:
            # effectively an in-order traversal, sorted order
            self._printTree(current_node.left)
            print(str(current_node.value))
            self._printTree(current_node.right)

    def height(self): # can call tree.height
        if self.root != None:
            return self._height(self.root, 0) 
        else:
            return 0

    def _height(self, current_node, current_height):
        # passing int to store height seen on each recursive call
        if current_node == None:
            return current_height
        # compare left and right heights to leaf & return which is larger
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left != None:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right != None:
            return self._search(value, current_node.right)
        else: # no value
            return False




def fillTree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binarySearchTree()
tree = fillTree(tree)
tree.insert(10)

tree.printTree()
print(tree.height())
print(tree.search(935))
print(tree.search(10))









#######################################
# deletion function BST from Brian Faure YT tutorial

#######################################
# validator function BST from Brian Faure YT tutorial