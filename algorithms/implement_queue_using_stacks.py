# LeetCode 
# Implement Queue using Stacks https://leetcode.com/problems/implement-queue-using-stacks/

class Stack():
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        return self.items == []

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    # @param x, an integer
    # @return nothing
    # HINT : put the element at top of stack1
    def push(self, x):
        # while stack1 is not empty, push everything to stack2
        while (not self.stack1.isEmpty()):
            s1 = self.stack1.pop()
            self.stack2.push(s1)

        # push to stack1
        self.stack1.push(x)

        # push everything from stack2 to stack1
        while (not self.stack2.isEmpty()):
            s2 = self.stack2.pop()
            self.stack1.push(s2)
        
    # @return nothing
    def pop(self):
        if (not self.stack1.isEmpty()):
            return self.stack1.pop()

    # @return an integer
    def peek(self):
        if (not self.stack1.isEmpty()):
            return self.stack1.peek()

    # @return an boolean
    def empty(self):
        return self.stack1.isEmpty()

'''
q = Queue()
print q.pop()
q.push(1)
q.push(2)
print q.pop()
print q.empty()
print q.peek()
q.push(3)
print q.pop()
print q.empty()
print q.peek()
print q.pop()
print q.empty()
'''
