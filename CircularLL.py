""" Circular linked List.
    No Null
    Singly and Doubly Linked List can be Circular """

class CLLNode:
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

class CLL:
    def __init__ (self, head = None):
        self.head = head
    
    def insert_beginning (self, data):
        newNode = CLLNode(data)
        curNode = self.head
        newNode.next = self.head

        if not self.head:
            newNode.next = newNode
        else:
            while curNode.next != self.head:
                curNode = curNode.next
            curNode.next = newNode
        self.head = newNode

    def insert_end (self, data):
        if not self.head:
            self.head = CLLNode(data)
            self.head.next = self.head
        else:
            newNode = CLLNode(data)
            curNode = self.head
            while curNode.next != self.head:
                curNode = curNode.next
            curNode.next = newNode
            newNode.next = self.head

    def delete (self, key):
        if self.head.data == key:
            curNode = self.head
            while curNode.next != self.head:
                curNode = curNode.next
            curNode.next = self.head.next
            self.head = self.head.next
        else:
            curNode = self.head
            prv = None
            while curNode.next != self.head:
                prv = curNode
                curNode = curNode.next
                if curNode.data == key:
                    prv.next = curNode.next
                    curNode = curNode.next

    def printCLL (self):
        curNode = self.head
        while curNode:
            print(curNode.data, "->", end="")
            curNode = curNode.next
            if curNode == self.head:
                break