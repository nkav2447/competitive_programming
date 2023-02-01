class MinStack(object):

    def __init__(self):
         self.items = []
         self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
