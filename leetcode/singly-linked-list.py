class MyLinkedList:
    """
    >>> obj = MyLinkedList()
    >>> obj.addAtIndex(1, 0)
    >>> obj.get(0)
    -1

    >>> obj = MyLinkedList()
    >>> obj.addAtHead(1)
    >>> obj.addAtTail(3)
    >>> obj.addAtIndex(1, 2)
    >>> obj.get(1)
    2
    >>> obj.deleteAtIndex(1)
    >>> obj.get(1)
    3

    >>> obj = MyLinkedList()
    >>> obj.addAtHead(1)
    >>> obj.deleteAtIndex(0)

    >>> obj = MyLinkedList()
    >>> obj.addAtHead(7)
    >>> obj.addAtHead(2)
    >>> obj.addAtHead(1)
    >>> obj.addAtIndex(3, 0)
    >>> obj.deleteAtIndex(2)
    >>> obj.addAtHead(6)
    >>> obj.addAtTail(4)
    >>> obj.get(4)
    
    >>> obj.addAtHead(4)
    >>> obj.addAtIndex(5, 0)
    >>> obj.addAtHead(6)
    """

    def __init__(self):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        if index == 0:
            if self.val is None:
                return -1

            return self.val
        else:
            if self.next is None:
                return -1

            return self.next.get(index - 1)

    def addAtHead(self, val: int) -> None:
        if self.val is None and self.next is None:
            self.val = val
        else:
            old_head = MyLinkedList()
            old_head.val = self.val
            old_head.next = self.next
            self.val = val
            self.next = old_head

    def addAtTail(self, val: int) -> None:
        if self.val is None and self.next is None:
            self.val = val
        elif self.next is None:
            tail_node = MyLinkedList()
            tail_node.val = val
            self.next = tail_node
        else:
            self.next.addAtTail(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > 0:
            if self.next is None and self.val is not None:
                self.addAtTail(val)
            elif self.next is not None:
                self.next.addAtIndex(index - 1, val)
        else:
            next_node = MyLinkedList()
            next_node.val = self.val
            next_node.next = self.next
            self.val = val
            self.next = next_node

    def deleteAtIndex(self, index: int) -> None:
        if index > 1 and self.next is not None:
            self.next.deleteAtIndex(index - 1)
        elif index == 0:
            if self.next is None:
                self.val = None
            else:
                self.val = self.next.val
                self.next = self.next.next
        elif self.next is not None:
            self.next = self.next.next


"""
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3, 0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
obj.get(4)
obj.addAtHead(4)
obj.addAtIndex(5, 0)
obj.addAtHead(6)
"""

"""
obj = MyLinkedList()
obj.addAtTail(1)
get(0)
"""

"""
obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
obj.get(5)
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)
"""

"""
obj = MyLinkedList()
obj.addAtHead(4)
obj.get(1)
obj.addAtHead(1)
obj.addAtHead(5)
obj.deleteAtIndex(3)
obj.addAtHead(7)
obj.get(3)
obj.get(3)
obj.get(3)
obj.addAtHead(1)
obj.deleteAtIndex(4)
"""

"""
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)
obj.get(3)
obj.deleteAtIndex(3)
obj.deleteAtIndex(0)
obj.get(0)
obj.deleteAtIndex(0)
obj.get(0)
"""

"""
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtIndex(3, 0)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
obj.get(4)
obj.addAtHead(4)
obj.addAtIndex(5, 0)
obj.addAtHead(6)
"""
