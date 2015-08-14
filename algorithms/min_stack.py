# LeetCode 
# Min Stack https://leetcode.com/problems/min-stack/

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[len(self.items) - 1]        


class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = Stack()
        self.items = []
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.push(x)
        if (self.isEmpty()):
            self.items.append(x)
        else:
            top = self.peek()
            if (top > x):
                self.items.append(x)
            else:
                self.items.append(top)                
        
    # @return nothing
    def pop(self):
        self.stack.pop()
        return self.items.pop()

    # @return an integer
    def top(self):
        return self.stack.top()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []
        
    # @return an integer
    def getMin(self):
        return self.items[len(self.items) - 1]

'''
minStack = MinStack()

minStack.push(-2)
minStack.push(0)
minStack.push(-1)

print minStack.top()

print minStack.getMin()
print minStack.top()
print minStack.pop()
print minStack.getMin()
'''
