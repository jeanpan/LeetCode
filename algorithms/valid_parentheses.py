# LeetCode 
# Valid Parentheses https://leetcode.com/problems/valid-parentheses/

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = Stack()
        isValid = True
        index = 0

        while index < len(s) and isValid:
            symbol = s[index]
            if symbol in "([{":
                stack.push(symbol)
            else:
                if stack.isEmpty():
                    isValid = False
                else:
                    top = stack.pop()
                    if not self.matches(top, symbol):
                        isValid = False
            index = index + 1

        if isValid and stack.isEmpty():
            return True
        else:
            return False

    def matches(self, open, close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

'''
s = Solution()
print(s.isValid('((()))'))
print(s.isValid('(()'))
print(s.isValid('{{([][])}()}'))
print(s.isValid('[{()]'))
'''
