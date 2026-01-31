#!/usr/bin/pthon3

class CountedIterator:
    def __init__(self, items):
        self.items = items
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.items):
            raise StopIteration
        self.count += 1
        return self.items[self.count - 1]

    def get_count(self):
        return self.count
