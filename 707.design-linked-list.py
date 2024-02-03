#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class MyDoublyLinkedList:
    def __init__(self, val=0):
        self.prev = None
        self.next = None
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        
    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if not current:  # If current is None, index is out of bounds
                return -1
            current = current.next
        return current.val if current else -1

    def printnode(self) -> None:
        current = self.head
        while current:
            print(f" {current.val}")
            current = current.next

    def getnode(self, index: int) -> MyDoublyLinkedList:
        if index < 0:
            return None  # Handle negative indices gracefully
        current = self.head
        for _ in range(index):
            if not current:  # If current is None before reaching the desired index
                return None
            current = current.next
        return current

    def addAtHead(self, val: int) -> None:
        new_node = MyDoublyLinkedList(val)
        if not self.head:  # If the list is empty, initialize head and tail
            self.head = self.tail = new_node
        else:  # Otherwise, adjust pointers to insert the new node at the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def addAtTail(self, val: int) -> None:
        #print ("Adding at tail ", val)
        new_node = MyDoublyLinkedList(val)
        if self.tail:  # If the list is not empty
            self.tail.next = new_node  # Set the current tail's next to the new node
            new_node.prev = self.tail  # Set the new node's prev to the current tail
        else:  # If the list is empty
            self.head = new_node  # The new node becomes the head
        self.tail = new_node 
        #self.printnode()


    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0: #Add it at the head
            self.addAtHead(val)
            return
        if index >= 1 and self.head == None: 
            return
        current = self.head
        if current == None: #Add it at the end
            self.addAtTail(val)
            return
        i = 0
        while i < index and current:
            current = current.next
            i += 1

        if not current: #Add it at the end
            self.addAtTail(val)
        else:
            newnode =  MyDoublyLinkedList(val)
            prev = current.prev
            prev.next = newnode
            newnode.prev = prev
            newnode.next = current
            current.prev = newnode

        return None


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return  # Invalid index or empty list
        current = self.head
        for _ in range(index):
            current = current.next
            if not current:
                return  # Index out of bounds
        if current == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None  # List becomes empty
        elif current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

