from LinkedList.node import Node

# reference: https://www.geeksforgeeks.org/doubly-linked-list/
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    '''
    tail is computed on the fly instead of stored
    '''
    @property
    def tail(self):
        last = self.head
        if last is None:
            return None
        while last.next is not None:
            last = last.next
        return last

    '''
    insert new node at the beginning
    '''
    def push(self, new_data):
        new_node = Node(data = new_data)
        new_node.prev = None # at the beginning
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    '''
    insert new node after a given one
    '''
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Error: given prev_node is None")
            return
        new_node = Node(data = new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        if new_node.next is not None: # if new_node.next (prev_node.next) is None it means we are at the end of the list
            new_node.next.prev = new_node    
        prev_node.next = new_node

    '''
    insert new node at the end
    '''
    def append(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = None # at the last
        last = self.tail
        # if list is empty then this is the first node
        if last is None:
            new_node.prev = None
            self.head = new_node
            return
        last.next = new_node
        new_node.prev = last

    '''
    insert new node before a given one
    '''
    def insert_before(self, next_node, new_data):
        if next_node is None:
            print("Error: given next_node is None")
            return
        new_node = Node(data = new_data)
        new_node.next = next_node
        new_node.prev = next_node.prev
        if new_node.prev is not None: # if new_node.prev (next_node.prev) is None it means we are at the beginning of the list
            new_node.prev.next = new_node
        next_node.prev = new_node

    '''
    return the list in the form of an array
    '''
    def to_array(self):
        result = []
        last = self.head
        while (last is not None):
            result.append(last.data)
            last = last.next
        return result
