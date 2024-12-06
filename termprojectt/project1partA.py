class DequeUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # For operations on the "right" end
        self.stack2 = []  # For operations on the "left" end

    def push_to_left(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())  # Transfer all elements to stack2
        self.stack2.append(value)  # Add the new value to the left
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())  # Transfer all elements back to stack1

    def push_to_right(self, value):
        self.stack1.append(value)  # Push directly to stack1

    def pop_from_left(self):
        if len(self.stack1) == 0:
            raise IndexError("Pop from empty deque")
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())  # Transfer all elements to stack2
        value = self.stack2.pop()  # Pop the leftmost element
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())  # Transfer all elements back to stack1
        return value

    def pop_from_right(self):
        if len(self.stack1) == 0:
            raise IndexError("Pop from empty deque")
        return self.stack1.pop()  # Pop directly from stack1

# Example usage
deque1 = DequeUsingTwoStacks()
deque1.push_to_left(10)
deque1.push_to_right(20)
deque1.push_to_left(5)
print(deque1.pop_from_right())  # Output: 20
print(deque1.pop_from_left())   # Output: 5
print(deque1.pop_from_left())   # Output: 10
