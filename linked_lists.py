# bare minimum linked list: only has a class for node
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# linked list class keeps track of head, then ListNode tells us where to find the next node
class LinkedList:
    def __init__(self, head_node):
        self.head_node = head_node

# these two classes are singly linked list, each node points to one following it

def merge_linked_lists(self, sorted_list1_head_node, sorted_list2_head_node):
    
    merged_head = None # this is what will be returned
    current = None # track where you are in the list
    
    if sorted_list1_head_node < sorted_list2_head_node:
        merged_linked_lists = ListNode(sorted_list1_head_node)
    else:
        merged_linked_lists = ListNode(sorted_list2_head_node)




# first_node = ListNode(3)
# -- value 3, next none
# second_node = ListNode(3, third)
# third = ListNode(5, fourth)
# assume not empty, at least one node in each list
# one can be longer than the other

###########################################
# implementation of the linked list
# then test out doubly linked list
# draw.io tool can be useful

# each node points not just to next node but also to previous node

class DoubleLinkedList:
    # have head and tail
    def __init__(self):
        # start values are none for the nodes
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)
        new_node.prev = self.tail
        
        if(self.tail):
            self.tail.next = new_node

        if(not self.head):
            self.head = new_node
        
        self.tail = new_node

    def __repr__(self):
        return f'<self.data>'

class DoubleNode:
    # prev and next
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous
        self.next = None



