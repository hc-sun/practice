# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_val = min(x, self.getMin())
        self.stack.append((x, min_val))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        else:
            return float('inf')
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()