# testing doubly_linked_list

import unittest
from LinkedList.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    def tearDown(self):
        self.list = None

    def test_print_list(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.assertEqual(self.list.to_array(), ["A", "B", "C"])

    def test_tail_if_list_empty(self):
        self.assertIsNone(self.list.tail, 'tail should return None for empty DLL')

    def test_tail_same_as_head_if_one_node(self):
        self.list.push("A")
        self.assertEqual(self.list.head, self.list.tail, 'tail should be the same as head for DLL with one Node')

    def test_tail_gives_last(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("T")
        self.assertEqual("T", self.list.tail.data, 'tail should give the last Node in the DLL')
    
    def test_push_empty(self):
        self.list.push("T")
        self.assertEqual(self.list.to_array(), ["T"], 'error inserting Node in the front of an empty DLL')

    def test_push_non_empty(self):
        self.list.push("A")
        self.list.push("T")
        self.assertEqual(self.list.to_array(), ["T", "A"], 'error inserting Node in the front of a non-empty DLL')

    def test_append_empty(self):
        self.list.append("T")
        self.assertEqual(self.list.to_array(), ["T"], 'error appending to an empty DLL')

    def test_append_non_empty(self):
        self.list.push("A")
        self.list.append("T")
        self.assertEqual(self.list.to_array(), ["A", "T"], 'error appending to a non-empty DLL')

    def test_insert_after(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.list.insert_after(self.list.head, "T")
        self.assertEqual(self.list.to_array(), ["A", "T", "B", "C"], 'error inserting after a Node in DLL')

    def test_insert_before(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.list.insert_before(self.list.tail, "T")
        self.assertEqual(self.list.to_array(), ["A", "B", "T", "C"], 'error inserting before a Node in DLL')

    def test_delete_node(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        target = self.list.head.next
        self.list.delete_node(target)
        self.assertEqual(self.list.to_array(), ["A", "C"], 'error deleting node in DLL')

    def test_delete_only_node(self):
        self.list.append("A")
        self.list.delete_node(self.list.head)
        self.assertEqual(self.list.to_array(), [], 'error deleting the only node in DLL')

    def test_delete_first_node(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.list.delete_node(self.list.head)
        self.assertEqual(self.list.to_array(), ["B", "C"], 'error deleting first node in DLL')

    def test_delete_last_node(self):
        self.list.append("A")
        self.list.append("B")
        self.list.append("C")
        self.list.delete_node(self.list.tail)
        self.assertEqual(self.list.to_array(), ["A", "B"], 'error deleting last node in DLL')
