class Queue:
  def __init__(self):
    self.queue = list()

  def enqueue(self, element):
    if element not in self.queue:
      self.queue.insert(0, element)
      return True
    return False

  def dequeue(self):
    if len(self.queue) > 0:
      return self.queue.pop()
    return ("Queue is Empty")

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)

  def print(self):
    print("Q Queue contains: ")
    for x in self.queue:
      print(x)
    print()

Q=Queue()
Q.print()

Q.enqueue(5)
Q.print()

Q.enqueue(3)
Q.print()

print("Amount of elements in queue: ")
print(Q.size())
print()

Q.dequeue()
Q.print()

print("Is Q Queue empty?")
print(Q.isEmpty())
print()

Q.dequeue()
Q.print()

print("Is Q Queue empty?")
print(Q.isEmpty())
print()

Q.dequeue()
Q.print()

Q.enqueue(7)
Q.print()

Q.enqueue(9)
Q.print()

print("The first element of Q Queue: ")
print(Q.peek())
print()

Q.enqueue(4)
Q.print()

print("Amount of elements in queue: ")
print(Q.size())
print()

Q.dequeue()
Q.print()