class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()

class Deque:
    def __init__(self):
        self.items = []
    def addBack(self, item):
        self.items.append(item)
    def addFront(self, item):
        self.items.insert(0, item)
    def deleteFront(self, item):
        return self.items.pop(0)
    def deleteBack(self, item):
        return self.items.pop()
    #from collections import deque
