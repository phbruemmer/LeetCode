class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) >= self.maxSize:
            return
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        val = self.stack[-1]
        self.stack.pop(-1)
        return val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(0, min(len(self.stack), k)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
param_2 = obj.pop()
print(param_2)
print(obj.stack)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.stack)
obj.increment(5, 100)
print(obj.stack)
obj.increment(2, 20)
print(obj.stack)
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.pop()
param_6 = obj.pop()
print(param_6)
# obj.increment(k,val)
