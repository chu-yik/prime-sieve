# basic Gries-Misra as per section 4 of:
# https://research.cs.wisc.edu/techreports/1990/TR909.pdf
from LinkedList.doubly_linked_list import DoublyLinkedList
from LinkedList.node import Node

class GriesMisra:
    @classmethod
    def find_prime(cls, n):
        # initialization
        s = DoublyLinkedList()
        for i in range(2, n):
            s.append(i)
        # main loop
        prime = s.head
        outer = 0
        while prime.data ** 2 < n:
            outer += 1
            checking = s.tail
            inner = 0
            while checking.data > prime.data:
                inner += 1
                temp = checking.prev
                if checking.data % prime.data == 0:
                    s.delete_node(checking)    
                checking = temp
            print("out: %s, in: %s" % (outer, inner))
            # print("after prime %s - %s" % (prime.data, s.to_array()))
            prime = prime.next

        return s.to_array()
