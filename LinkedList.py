""" Linked List is a sequence of data elements which are connected via links.
    Linked List operation includes INSERT, DISPLAY, DELETE, SEARCH """
    
class LLNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LL:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    # Inserting a Node at the last part, append
    def insert (self, value):
        node = LLNode(value, None)

        # Gonna check if the head node is empty
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    # Inserting a Node in the beginning, well, it's pretty obvious sa name ng function lol. prepend
    def insert_beginning (self, value):
        node = LLNode(value)
        node.next = self.head
        self.head = node

    # Inserting a Node anywhere you want. Indicate the Previous Node first then input data/value
    def insert_after_Node (self, prev_node, value):
        if not prev_node:
            print("The Previous node is not in the list")
            return
        node = LLNode(value)
        node.next = prev_node.next
        prev_node.next = node

    # Deleting a Node
    def delete (self, key):
        current_node = self.head 

        # Deleting the Head Node
        if current_node and current_node.value == key:
            self.head = current_node
            current_node = None
            return

        # Deleting a Node but not the Head Node
        prev_node = None
        while current_node and current_node.value != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

    # Swapping a Node
    def swap_node (self, key1, key2):
        # Checks if the keys you enter is the same, it will just return the list
        if key1 == key2:
            return
        
        # checks if the perv 1 and 2 is None or not
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.value != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.value != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        # Checks if the prev 1 and 2 is not none
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    # Search for an element
    def find(self, key):
        curr = self.head

        while curr is not None:
            if curr.value == key:
                return True
            curr = curr.next
        return False

    # Print The LinkedList
    def printLL (self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, " -> ", end="")
            current_node = current_node.next
        print("Null")

""" TEST """

ll = LL()
ll.printLL()
ll.insert("A")
ll.printLL()
ll.insert("B")
ll.printLL()
ll.insert("C")
ll.printLL()
ll.insert("D")
ll.printLL()
ll.insert_beginning("E")
ll.printLL()
ll.insert_after_Node(ll.head.next, "Z")
ll.printLL()
ll.swap_node("E", "A")
ll.printLL()
print(ll.find("C"))