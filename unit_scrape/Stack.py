
#basic stack

class Stack:
    
    def __init__(self):
        self.count = 0
        self.stuff = []

    def isEmpty(self):
        return self.count == 0
    
    def push(self, item):
        self.count += 1
        self.stuff.append(item)

    def pop(self):
        self.count -= 1
        return self.stuff.pop()

    def size(self):
        return self.count