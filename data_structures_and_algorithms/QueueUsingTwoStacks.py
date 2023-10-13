class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # For enqueuing items
        self.stack2 = []  # For dequeuing items

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            # If stack2 is empty, transfer items from stack1
            if not self.stack1:
                return None  # Queue is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2 to simulate dequeue
        return self.stack2.pop()

# Example usage:
queue = QueueUsingTwoStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Outputs: 1
print(queue.dequeue())  # Outputs: 2
print(queue.dequeue())  # Outputs: 3
