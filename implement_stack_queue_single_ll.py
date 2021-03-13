# Live Python YT tutorial

# stack structure
# last in, last out - pushed in, then popped out from the top
# most recently added object is the first to be removed

# useful: word processor, anything that allows you to undo the most recent action

class IsEmptyError(Exception):
    pass # when you pass a string to this argument, it then becomes the extra error message

class singleLinkedStack:
    # node class
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0 # true or false bool

    def push(self, data):
        self.head = self.Node(data, self.head) # becomes the new head, old head is next
        self.size += 1

    def pop(self):
        if self.is_empty(): # can't pop if the stack is empty
            # defining our own error - create a class from subclass Exception
            raise IsEmptyError('stack is empty, cannot pop') 
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        return result

    def peek(self):
        if self.is_empty():
            raise IsEmptyError('stack is empty, cannot pop') 
        return self.head.data

# queue structure
# first in, first out

class IsEmptyError(Exception):
    pass

# instantiate both the head and tail in init method
class singleLinkedQueue:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None # we have to perform operations on both ends of the queue
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0 

    def enqueue(self, data): # adding to the back
        new = self.Node(data, None) # becomes new tail node
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size += 1


    def dequeue(self): # take out from the top
        if self.is_empty():
            raise IsEmptyError('queue is empty, cannot remove')
        
        result = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty(): # if that was the last thing in the queue
            self.tail = None
        return head

    def peek(self): # look at the first item in the queue
        if self.is_empty():
            raise IsEmptyError('queue is empty, cannot view')
        return self.head.data

