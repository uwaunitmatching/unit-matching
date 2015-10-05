
#basic stack IS ACTUALLY A QUE NOW NEED TO RENAME A BUNCH OF STUFF


class _Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack(object):

    def __init__(self):
        self.top = None
        self.bottom = None
        self._size = 0

    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, item):
        n = self.bottom
        self.bottom = _Node(item)
        if self.isEmpty():
            self._first = self.bottom
        else:
            n.next = self.bottom
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        n = self._first
        self._first = self._first.next
        self._size -= 1
        return n.item

