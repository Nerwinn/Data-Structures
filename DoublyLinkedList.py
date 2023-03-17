""" Doubly Linked List. A Linked List with previous link """ 

class DLLNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    # Append
    def AppEnd (self, data):
        if self.head is None:
            newNode = DLLNode(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = DLLNode(data)
            curNode = self.head
            while curNode.next:
                curNode = curNode.next
            curNode.next = newNode
            newNode.prev = curNode
            newNode.next = None

    # Prepend
    def PrepenD (self, data):
        newNode = DLLNode(data)
        if self.head == None:
            self.head = self.tail = newNode
            self.head.prev = None
            self.tail.next = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode

    # Inserting node after the given key/node
    def add_after_a_node (self, key, data):
        newNode = DLLNode(data)
        if key is None:
            print("Null! The key is null")
            return
        nxt = key.next
        newNode.next = nxt
        newNode.prev = key
        key.next = newNode
        nxt.prev = newNode
        if newNode.next is not None:
            newNode.next.prev = newNode

    # Inserting before a specific Node
    def add_before_a_node (self, key: int, data):
        newNode = DLLNode(data)
        if self.head is None:
            self.AppEnd(newNode)
            return 
        else:
            temp = self.head
            while temp:
                if temp.data == key:
                    prv = temp.prev
                    prv.next = newNode
                    newNode.prev = prv
                    newNode.next = temp
                    temp.prev = newNode
                    break
                else:
                    temp = temp.next

             
    # Delete Operation
    def delete (self, key):
        curNode = self.head
        while curNode:
            if curNode.data == key and curNode == self.head:
                # Case 1. If you want to delete head node and there's no other node
                if not curNode.next:
                    curNode = None
                    self.head = None
                    return
                # case 2. if you want to delete head node and there is another existing node    
                else:
                    nxt = curNode.next
                    curNode.next = None
                    curNode.prev = None
                    nxt.prev = None
                    self.head = nxt
                    return
            elif curNode.data == key:
                # Case 3. if you want to delete a node and it's not null
                if curNode.next:
                    nxt = curNode.next
                    prv = curNode.prev
                    prv.next = nxt
                    nxt.prev = prv
                    curNode.next = None
                    curNode.prev = None
                    curNode = None
                    return
                # Case 4. if you want to delete a node and it's next pointer is null
                else:
                    prv = curNode.prev
                    prv.next = None
                    curNode.prev = None
                    curNode = None
                    return    
    
    # Print the List Reverse
    def reverse (self):
        temp = None
        curNode = self.head
        while curNode:
            temp = curNode.prev
            curNode.prev = curNode.next
            curNode.next = temp
            curNode = curNode.prev
        if temp != None:
            self.head = temp.prev 

    # Print The List
    def printDLL (self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data, "-> ", end="")
            curNode = curNode.next
        print("Null")

""" TEST """

ll = DLL()
ll.AppEnd(1)
ll.printDLL()
ll.AppEnd(2)
ll.printDLL()
ll.AppEnd(3)
ll.printDLL()
ll.AppEnd(4)
ll.printDLL()
ll.AppEnd(5)
ll.printDLL()
ll.add_after_a_node(ll.head.prev, 9) # The output will be Null because head.prev is null
ll.PrepenD(10) # This will add 10 in the front then make it the head node
ll.printDLL()
ll.add_before_a_node(5, 20)
ll.printDLL()
print()
print()
ll.reverse()
ll.printDLL()
ll.delete(5)
ll.printDLL()
