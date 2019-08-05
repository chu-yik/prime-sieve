# testing doubly_linked_list

import unittest
from LinkedList.doubly_linked_list import DoublyLinkedList

class TestDLL(unittest.TestCase):
    def test_tail_if_list_empty(self):
        list = DoublyLinkedList()
        self.assertIsNone(list.tail())

    def test_tail_same_as_head_if_one_node(self):
        list = DoublyLinkedList()
        list.push("A")
        self.assertEqual(list.head, list.tail())

    def test_tail_gives_last(self):
        list = DoublyLinkedList()
        list.append("A")
        list.append("B")
        list.append("C")
        self.assertEqual("C", list.tail().data)
    
    def test_push_empty(self):
        list = DoublyLinkedList()
        list.push("T")
        self.assertEqual("T", list.head.data)

    def test_push_non_empty(self):
        list = DoublyLinkedList()
        list.push("A")
        list.push("T")
        self.assertEqual("T", list.head.data)

    def test_append_empty(self):
        list = DoublyLinkedList()
        list.append("T")
        self.assertEqual("T", list.head.data)

    def test_append_non_empty(self):
        list = DoublyLinkedList()
        list.push("A")
        list.append("T")
        self.assertEqual("T", list.tail().data)

    def test_insert_after(self):
        list = DoublyLinkedList()
        list.append("A")
        list.append("B")
        list.append("C")
        list.insert_after(list.head, "T")
        self.assertEqual("T", list.head.next.data)