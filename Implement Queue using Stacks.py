class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.items.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.items.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.items[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.items


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.

# Input
# ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
# Output
# [null,null,null,1,1,false]