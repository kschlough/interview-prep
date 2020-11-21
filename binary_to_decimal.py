# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        current_node = head
        values = []
        
        # not current_node.next bc that stops to early
        # while current_node because when list ends it's NoneType so false
        while current_node:
            values.append(current_node.val)
            current_node = current_node.next

        # which is better for this use case - reversed or .reverse()? unsure 
        values.reverse()
        
        final_count = 0
        multiplier = 1

        for num in values:
            value = num * multiplier
            multiplier = multiplier * 2
            final_count += value
            
        return final_count
        
# questions:
# i would ask how you convert binary to base 10
    # In base ten, you have columns or "places" for 100 = 1, 101 = 10, 102 = 100, 103 = 1000
    # Similarly in base two, you have columns or "places" for 20 = 1, 21 = 2, 22 = 4, 23 = 8, 24 = 16
# i would ask how you do a square root in python
    # sqrt()
# the expansion is: divide each place by two moving back, or multiply each by two going forwards
# ex: 16 base 10 / 10000 base 2 / 1 sixteen, 0 eights, 0 fours, 0 twos, and 0 ones
# link: https://www.purplemath.com/modules/numbbase.htm
        
# pseudocode
# step through the linked list
# set pointer = head node
# values = []
    # while pointer.next is true (meaning not end of list):
        # values.append(pointer.val)
        # update pointer to pointer.next
# reverse the list of values
# final count = 0
# multiplier = 0
# for item in values:
    # multiplier = multiplier * 2
    # value = item * multiplier
    # final count += value