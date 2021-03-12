# tutorial from Brian Faure, YT
# implement a linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data # value of current data point
        self.next = next # pointer to next node

        # next default is none because of end pointer points to none

class LinkedList:
    def __init__(self):
        self.head = Node()
        # wraps around created nodes

    # append function
    def append(self, data):
        new_node = Node(data)
        current = self.head
        
        # once we get to next node is None, we insert another
        while current.next is not None:
            current = current.next
        current.next = new_node

    # figure out length
    def length(self):
        current = self.head
        total = 0

        while current.next is not None:
            total += 1
            current = current.next
        return total

    # helper function - display current contents of the list
    def display_list(self):
        elements = []
        current = self.head

        while current.next is not None:
            current = current.next
            elements.append(current.data)
        
        print(elements)

    # extractor function to pull out data point at a certain index
    def get(self, index):
        # make sure index isn't out of the range of the ll
        if index >= self.length():
            print("index is out of range")
            return None
        
        current_index = 0
        current = self.head
        
        while current.next is not None:
            current = current.next
            if current_index == index:
                return current.data
            else:
                current_index += 1

    # erase function to erase a node at a given index
    def erase(self, index):
        # make sure index isn't out of the range of the ll
        if index >= self.length():
            print("index is out of range")
            return 

        current_index = 0
        current = self.head

        while True:
            # track last node to make sure we can point to the skip node
            last_node = current
            current = current.next
            if current_index == index:
                # effectively erases current node
                last_node.next = current.next
                return
            
            current_index += 1
                
        
        
        
test_list = LinkedList()

test_list.append(1)
test_list.append(2)
test_list.append(3)
test_list.append(4)

test_list.display_list()
print(test_list.get(2))

test_list.erase(2)
test_list.display_list()

