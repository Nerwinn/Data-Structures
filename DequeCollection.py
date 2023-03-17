class Deque:
    def __init__(self):
        self.items = []

    def check_Empty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def del_front(self):
        if self.items:
            return self.items.pop(0)
        return None
    
    def del_rear(self):
        if self.items:
            return self.items.pop()
        return None
    
    def peekFront(self):
        if self.items:
            return self.items[0]
        return None

    def peekRear(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)