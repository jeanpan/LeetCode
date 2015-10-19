class Stack:
    def __init__(self):
        self.itmes = []

    def push(self, x):
        self.itmes.append(x)

    def pop(self):
        return self.itmes.pop()

    def isEmpty(self):
        return self.itmes == []

    def top(self):
        return self.itmes[len(self.itmes) - 1]

rStack = Stack()

def toStr(n, base):
    convertStr = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertStr[n])
        else:
            rStack.push(convertStr[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453, 16))
