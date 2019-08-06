# special style of doubly linked list

# Note: from https://research.cs.wisc.edu/techreports/1990/TR909.pdf
# the doubly_linked_list.py is not fit for this use case
class Record:
    def __init__(self, prime=True, prev=None, g_next=None):
        self.prime = prime
        self.prev = prev
        self.next = g_next

class ArrayDLL:
    def __init__(self, size):
        self.records = [None, Record(False, None, 2)]
        for i in range(2, size):
            r = Record(True, i-1, i+1)
            self.records.append(r)
        self.records.append(Record(True, size-1, None))

    def remove(self, index):
        r = self.records[index]
        r.prime = False
        if r.next is not None:
            self.records[r.next].prev = r.prev
        if r.prev is not None:
            self.records[r.prev].next = r.next
    
    def next(self, index):
        return self.records[index].next

    def prev(self, index):
        return self.records[index].prev

    def print_result(self):
        print(self.to_array())

    def to_array(self):
        i = 2
        result = []
        while i is not None:
            result.append(i)
            i = self.records[i].next
        return result
