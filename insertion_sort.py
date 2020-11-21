# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# ex 1 : 
# Input: 4->2->1->3
# Output: 1->2->3->4

# ex 2 :
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

    current_node = head

    while current_node:
        pointer = current_node
        print(pointer)
        while pointer.val > pointer.next.val:
            smaller = pointer.next
            print(smaller)
            if pointer.next.next:
                pointer.next = pointer.next.next 
                smaller.next = pointer
                print(smaller.next)
            else:
                


        current_node = current_node.next

    









# pseudocode:

# pointer = current_node #4
# if current_node > current_node.next: #4 > 2
    # smaller = current_node.next # 2
    # current_node.next = current_node.next.next # 4->1
    # smaller.next = current_node # 2->4
    
# put this all in a while current_node loop
# return head



