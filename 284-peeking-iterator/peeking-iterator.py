
# Below is the interface for Iterator, which is already defined for you.

class PeekingIterator:

    def __init__(self, iterator):
        self.iterator = iterator

        self.has_next = iterator.hasNext()
        self.next_val = iterator.next() if self.has_next else None

    def peek(self):
        return self.next_val

    def next(self):
        result = self.next_val

        self.has_next = self.iterator.hasNext()
        if self.has_next:
            self.next_val = self.iterator.next()
        else:
            self.next_val = None

        return result

    def hasNext(self):
        return self.has_next
