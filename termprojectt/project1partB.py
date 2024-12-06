class DequeUsingStackQueue:
    def __init__(self):
        self.stack = []  # Stack for right-side operations
        self.queue = []  # List as a queue for left-side operations

    def push_to_left(self, value):
        self.queue.insert(0, value)  # Insert at the front of the queue

    def push_to_right(self, value):
        self.stack.append(value)  # Push to the stack

    def pop_from_left(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)  # Remove from the front of the queue
        elif len(self.stack) > 0:
            while len(self.stack) > 0:
                self.queue.insert(0, self.stack.pop())  # Move all elements to the queue
            return self.queue.pop(0)
        else:
            raise IndexError("Pop from empty deque")

    def pop_from_right(self):
        if len(self.stack) > 0:
            return self.stack.pop()  # Remove from the stack
        elif len(self.queue) > 0:
            while len(self.queue) > 0:
                self.stack.append(self.queue.pop(0))  # Move all elements to the stack
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty deque")

# Example usage
deque2 = DequeUsingStackQueue()
deque2.push_to_left(30)
deque2.push_to_right(40)
deque2.push_to_left(20)
print(deque2.pop_from_left())   # Output: 20
print(deque2.pop_from_right())  # Output: 40
print(deque2.pop_from_left())   # Output: 30
