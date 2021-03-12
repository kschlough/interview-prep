# ctci linked lists chapter

# write code to remove duplicates from an unsorted linked list

# pseudocode
# create a dictionary to store all the values that we come across as keys
# as values, implement a counter
# go through the list once to get the # of times each appears
# then go through the list one more time and remove the dupes by changing pointers

# build the test linked list
class Node: 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

headnode = Node(9)
val1 = Node(10)
headnode.next = val1
val2 = Node(234)
val1.next = val2
val3 = Node(9)
val2.next = val3
val4 = Node(3)
val3.next = val4


def ll_remove_dupes(head):
    dupes_dict = {}
    current = head

    # check if there's no list
    if head == None:
        return None

    while current is not None:
        if current.data in dupes_dict:
            dupes_dict[current.data] += 1
            current = current.next
        else:
            dupes_dict[current.data] = 1
            currrent = current.next

    # reset to start loop again, this time with 2 pointers
    
    
    # check if you need to change the head first, do this until you don't
    while dupes_dict[head.data] > 1:
        head = head.next
    
    # then set the current & pointer vals
    current = head
    pointer = head.next

    while pointer is not None:
        # once the head is ok, check the other nodes
        if dupes_dict[pointer.data] > 1:
            current.next = pointer.next
            current = current.next
            pointer = current.next.next

        else:
            current = current.next
            pointer = pointer.next

# call the function
print(ll_remove_dupes(headnode))
    # should return the *new* head which will be 10