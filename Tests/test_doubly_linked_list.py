# testing doubly_linked_list

import unittest
from LinkedList.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_tail_if_list_empty(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.tail, 'tail should return None for empty DLL')

    def test_tail_same_as_head_if_one_node(self):
        list = DoublyLinkedList()
        list.push("A")
        self.assertEqual(list.head, list.tail, 'tail should be the same as head for DLL with one Node')

    def test_tail_gives_last(self):
        list = DoublyLinkedList()
        list.append("A")
        list.append("B")
        list.append("C")
        self.assertEqual("C", list.tail.data, 'tail should give the last Node in the DLL')
    
    def test_push_empty(self):
        list = DoublyLinkedList()
        list.push("T")
        self.assertEqual("T", list.head.data, 'error inserting Node in the front of an empty DLL')

    def test_push_non_empty(self):
        list = DoublyLinkedList()
        list.push("A")
        list.push("T")
        self.assertEqual("T", list.head.data, 'error inserting Node in the front of a non-empty DLL')

    def test_append_empty(self):
        list = DoublyLinkedList()
        list.append("T")
        self.assertEqual("T", list.head.data, 'error appending to an empty DLL')

    def test_append_non_empty(self):
        list = DoublyLinkedList()
        list.push("A")
        list.append("T")
        self.assertEqual("T", list.tail.data, 'error appending to a non-empty DLL')

    def test_insert_after(self):
        list = DoublyLinkedList()
        list.append("A")
        list.append("B")
        list.append("C")
        list.insert_after(list.head, "T")
        self.assertEqual("T", list.head.next.data, 'error inserting after a Node in DLL')
