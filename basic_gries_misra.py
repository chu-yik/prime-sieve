# basic Gries-Misra as per section 4 of:
# https://research.cs.wisc.edu/techreports/1990/TR909.pdf
from LinkedList.doubly_linked_list import DoublyLinkedList
from LinkedList.node import Node
from LinkedList.array_dll import ArrayDLL
from LinkedList.array_dll import Record

class GriesMisra:
    @classmethod
    def find_prime(cls, n):
        # initialization
        s = ArrayDLL(n)
        # main loop
        p = 2
        while p ** 2 <= n:
            f = p
            while p * s.next(f) <= n:
                f = s.next(f)
            while f >= p:
                s.remove(p * f)
                f = s.prev(f)
            p = s.next(p)
        return s.to_array()


