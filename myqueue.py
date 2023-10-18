from node import Node

class MyQueue:
    def __init__(self, head=None, tail=None): #When a queue is instantiated, it's completely empty, with no nodes at all. So the head and
                                              #..tail properties are None or null by default.
        self.head = head
        self.tail = tail

# enqueue: add node to tail
    def enqueue(self, val):     # Enqueue: add Node to back of the queue
        n = Node(val)        # Instantiate new node with value

        if self.head is None:         # If queue is empty
            self.tail = n
            self.head = n
        else:
            self.tail.link = n   #link for old tail becomes new node. self.tail will be the parent of the new n
            self.tail = n       # tail points to new tail
        return None
# dequeue: remove node from head
    def dequeue(self):

        # Queue cannot be empty
        assert self.head, "Queue is empty."

        # Temporarily store value for node at head
        _value = self.head.value

        # Reassign head property to node
        # current head's link points to
        self.head = self.head.link

        # If final item removed
        # set tail to None as well
        if self.head is None:
            self.tail = None

        # return value
        return _value
