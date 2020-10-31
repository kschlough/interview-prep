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

    def delete(self, n):
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


# testing here - creates the original list
head = Node(1)
print(head.value)

second = Node(2)
head.next = second
print(head.next.value)

third = Node(3)
second.next = third
print(second.next.value)
fourth = Node(4)
third.next = fourth
print(third.next.value)
fifth = Node(5)
fourth.next = fifth
print(fourth.next.value)
print(fifth.next.value) # should be NoneType

print(head.length())

print(head.delete(2))


# pointer = pointer.head
# while(pointer != None):
#     print(pointer)
#     pointer = pointer.next

# should do the same as all these prints
# print(head.value)
# print(head.next.value)
# print(head.next.next.value
# print(head.next.next.next.value)
# print(head.next.next.next.next.value)




# refactoring
# single linked list class - got rid of this because would have to add append to set up the list, vs. just nodes
# class SingleLinkedList:
# 	def __init__(self):
# 		self.head = None
# 		# self.tail = None