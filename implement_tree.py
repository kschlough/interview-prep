# generic tree implementation from Coding Cart YT tutorial

#######################################
# BST from Brian Faure YT tutorial
# at most 2 child nodes for each node
# every child node to the right is larger than parent, every child node left is smaller than parent

class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None # added for del function

class binary_search_tree: # wrapper that handles managing all node classes
    def __init__(self):
        self.root = None

    def insert(self, value): # non-recursive, public
        # check if the root has a value yet
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root) # _ means "private" function, don't call outside of class

    # private insert function is recursive
    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = node(value)
                current_node.left.parent = current_node # set parent
            else:
                self._insert(value, current_node.left) # recursion down left part of tree
        elif value > current_node.value: # value larger than current_node
            if current_node.right == None:
                current_node.right = node(value)
                current_node.right.parent = current_node # set parent
            else:
                self._insert(value, current_node.right)
        else: # if they're the exact same, no dupes (in this iteration)
            print("value already in tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root) # another private, recursive

    def _print_tree(self, current_node):
        if current_node != None:
            # effectively an in-order traversal, sorted order
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)

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

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node): # same as search function, but gives value instead of T/F bool
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left != None:
            return self._find(value, current_node.left)
        elif value > current_node.value and current_node.right != None:
            return self._find(value, current_node.right)
    
    def delete_value(self, value): # passed integer - calling delete node with param passed as return val of find func
        return self.delete_node(self.find(value))

    def delete_node(self, current_node): # passed node
        
        def min_value_node(n): # passed a node treated as root, traverse the left until smallest elem
            # use this to find the next in-order successor
            current_node = n
            while current_node.left != None:
                current_node = current_node.left
            return current_node

        def num_children(n):
            num_children = 0
            if n.left != None:
                num_children += 1
            if n.right !=None:
                num_children += 1
            return num_children
        
        # get parent of node to be deleted
        parent_node = current_node.parent

        # get # of children of node to be deleted
        node_children = num_children(current_node)

        #if node has no children
        if node_children == 0:
            # set pointer in parent to none to remove leaf node
            if parent_node.left == current_node:
                parent_node.left = None
            else:
                parent_node.right = None

        # if node has single child
        if node_children == 1:
            # get child node
            if current_node.left != None:
                child = current_node.left
            else:
                child = current_node.right

            # replace node to be deleted with its child
            if parent_node.left == current_node:
                parent_node.left = child
            else:
                parent_node.right = child

            # corret the parent pointer
            child.parent = parent_node 

        # if node has 2 children
        if node_children == 2:
            # get next in-order successor
            successor = min_value_node(current_node.right)
            # copy value found in successor node to the node formerly holding val we want to delete
            current_node.value = successor.value
            # then delete the successor
            self.delete_node(successor)

        


def fillTree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fillTree(tree)
tree.insert(10)

tree.print_tree()
print(tree.height())
print(tree.search(935))
print(tree.search(10))









#######################################
# deletion function BST from Brian Faure YT tutorial

#######################################
# validator function BST from Brian Faure YT tutorial