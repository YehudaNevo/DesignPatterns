class GenericIterator:
    def __init__(self, container):
        self.container = container
        self.cursor = container.begin()

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor != self.container.end():
            value = self.container.get_value(self.cursor)
            self.cursor = self.container.next(self.cursor)
            return value
        else:
            raise StopIteration

# Example data structures

class ListContainer:
    def __init__(self, data):
        self.data = data

    def begin(self):
        return 0

    def end(self):
        return len(self.data)

    def next(self, cursor):
        return cursor + 1

    def get_value(self, cursor):
        return self.data[cursor]

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedListContainer:
    def __init__(self, head):
        self.head = head

    def begin(self):
        return self.head

    def end(self):
        return None

    def next(self, cursor):
        return cursor.next

    def get_value(self, cursor):
        return cursor.value

# Client code

# List
data_list = [1, 2, 3, 4, 5]
list_container = ListContainer(data_list)
list_iterator = GenericIterator(list_container)

print("List:")
for value in list_iterator:
    print(value)

# Linked List
linked_list = LinkedListNode(1, LinkedListNode(2, LinkedListNode(3)))
linked_list_container = LinkedListContainer(linked_list)
linked_list_iterator = GenericIterator(linked_list_container)

print("\nLinked List:")
for value in linked_list_iterator:
    print(value)
