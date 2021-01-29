# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

# pseudocode

# pointer_current_l1 = l1
# pointer_current_l2 = l2

# compare first two vals of sorted lists & decide which is smaller
# add the smaller one as head node in your merged list (save to variable)
# based on which is smaller, enter the comparison

# compare next value in current list to next value in other list
    # whichever is smaller, add to merged list (update merged head.next to point here) 
    # update the pointer of the value you add to meged list to reflect where you are in the list
        # pointer_current_l1 = pointer_current_l1.next
    # address easy edge cases:
        # if nothing in both lists:
            # return empty list
        # if nothing in one list:
            # return other list