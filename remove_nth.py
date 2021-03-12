# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Follow up: Could you do this in one pass?

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_length = 0
        current_node = head
        
        while current_node is not None:
            list_length += 1
            current_node = current_node.next
        
        goal_index = list_length - n
        
        index = 0
        current_node = head
        
        # check for removing the 1st item
        if goal_index == 0:
            head = head.next
            return head
        
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
            index += 1
            if index == goal_index:
                previous_node.next = current_node.next
                return head
        
        
        
# pseudocode
# iterate through the list to find its length
# length minus n is the node that needs removing
# iterate again with pointers to last node and current node + index count
# once current node hits index count n,
# last node points to current.next