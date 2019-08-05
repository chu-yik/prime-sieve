from LinkedList.node import Node

# reference: https://www.geeksforgeeks.org/doubly-linked-list/
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tail(self):
        last = self.head
        if last is None:
            return None
        while last.next is not None:
            last = last.next
        return last

    # insert new node at the beginning
    def push(self, new_data):
        new_node = Node(data = new_data)
        new_node.prev = None # at the beginning
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    # insert new node after a given one
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Error: prev_node is None")
            return
        new_node = Node(data = new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        if new_node.next is not None:
            new_node.next.prev = new_node    
        prev_node.next = new_node

    # insert new node at the end
    def append(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = None # at the last
        # if list is empty then this is the first node
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        # traverse till end
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

        
    