# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# questions:
    # is it ever going to be an empty list? (head would just be none)
    # just a single node - return that node? yes
    # return type is head node of new list? yes
    # will the duplicates always appear in order? yes
    
# pseudocode:
    # create a pointer to current node (head)
    # set previous pointer to head
    # while current node isn't NoneType - starting at the second position:
        # update current node to current position
        # compare current node (value) to previous pointer
        # if they're the same:
            # save next current value to variable = current.next
            # update current to that variable
            # and have pointer.next set to that variable
        # otherwise:
            # update pointer to current
            # current to pointer.next
    # return head
    

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head            
        
        previous_pointer = head
        current_node = head.next
        
        while current_node:
            if previous_pointer.val == current_node.val:
                current_node = current_node.next
                previous_pointer.next = current_node
            else:
                previous_pointer = current_node
                current_node = previous_pointer.next
        
        return head

