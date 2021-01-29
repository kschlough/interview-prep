# Given the head of a linked list, remove the nth node from the end of the list, then return the head of the modified list
# for instance, given a list containing [1, 2, 3, 4, 5],
# if n = 2,
# your output should be [1, 2, 3, 5]

################################

# Pseudocode:
    # Define the node class
    # Define the linked list class
    # Not double list, but need to access the previous values so maybe need to create indexing to access the 2nd from last
    # Define length, define index
    # Define what index n is at relative to length
    # No append needed, but define remove .pop()?
    # Remember to change the pointers for next and for tail

    # So for example [1, 2, 3, 4, 5]
    # We want to access n from the end - 2 from the end of a list with length 5 is at index 3
    # Pointer to index n-1 (2) needs to then lead to pointer for index n+1 (4)
    # Remove index 3 - do it after because as long as you change the pointers in the list removing is extraneous and just memory-related??
    
    # Then update head and tail values

################################

# node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.head = None

    def length(self):
        counter = 0
        node_pointer = self.head # make sure next isn’t None
        while(node_pointer != None):
            counter += 1
            node_pointer = node_pointer.next
            # print statement to print out list of nodes while getting length
            print(node_pointer)
        return counter

    def delete_nth(self, head, n):
		# delete the nth item, so:
        index_n = counter - n	
        if index_n > self.length:
            raise Exception(f'Index is out of list range')
        index_prev = index_n - 1
        index_next = index_n + 1
        index_prev.next = index_next
		# do I even need to .pop 3? I’m just changing the pointers since it’s linked
        # a: repointing is effectively removing, that's fine
		
        return self.head



# refactoring
# single linked list class - got rid of this because would have to add append to set up the list, vs. just nodes
# class SingleLinkedList:
# 	def __init__(self):
# 		self.head = None
# 		# self.tail = None


# solution

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class RemoveN:
    def remove_nth(self, head, n):
        pointer1 = head
        pointer2 = head

        for index in range(n):
            pointer1 = pointer1.next
            # pointer one is the distance you eventually want to be from the tail
            # so then move both pointers, and pointer two will be on the index that you want to remove
            # pointer 1 will be the end of the list, as you step through pointer 2 will be n behind and will hit the one you want to remove

        if not pointer1:
            # handling edge case where n is the full length of the list
            # removing head
            head = head.next
            return head
        
        while pointer1.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next 
        
        print(pointer2.val)