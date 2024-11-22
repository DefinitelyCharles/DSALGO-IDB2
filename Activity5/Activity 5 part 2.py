class PositionalList:

    class Position:
        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise IndexError("The list is empty.")
        return self.head

    def last(self):
        if self.is_empty():
            raise IndexError("The list is empty.")
        return self.tail

    def add_last(self, element):
        new_node = self.Position(element, self.tail, None)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, pos):
        if pos is self.head:
            self.head = self.head.next
        if pos is self.tail:
            self.tail = self.tail.prev
        if pos.prev:
            pos.prev.next = pos.next
        if pos.next:
            pos.next.prev = pos.prev
        self.size -= 1

    def insert_after(self, pos, element):
        new_node = self.Position(element, pos, pos.next)
        if pos.next:
            pos.next.prev = new_node
        pos.next = new_node
        if pos == self.tail:
            self.tail = new_node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.element
            current = current.next


class LinkedStack:

    class Node:
        def __init__(self, element, next=None):
            self.element = element
            self.next = next

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, element):
        new_node = self.Node(element, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_element = self._top.element
        self._top = self._top.next
        self._size -= 1
        return popped_element

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.element

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


def insertion_sort(lst, ascending=True):
    current = lst.head
    while current is not None:
        key = current
        current = current.next
        while key.prev and (key.prev.element > key.element if ascending else key.prev.element < key.element):
            key.element, key.prev.element = key.prev.element, key.element
            key = key.prev


def main():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))

    pos_list = PositionalList()
    for num in numbers:
        pos_list.add_last(num)

    print("Original list:", list(pos_list))
    insertion_sort(pos_list, ascending=True)
    print("Sorted in Ascending Order:", list(pos_list))

    insertion_sort(pos_list, ascending=False)
    print("Sorted in Descending Order:", list(pos_list))


if __name__ == "__main__":
    main()
