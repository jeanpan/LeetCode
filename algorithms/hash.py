# Hash
# http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html

def simpleHashRemainders(item, size):
    return item % size

# !!
def foldingHash(str, size):
    sum = 0
    for pos in range(0, len(str), 2):
        num = str[pos] + str[pos + 1]
        sum = sum + int(num)

    return sum % size

def stringHash(str, size):
    sum = 0
    # sum each characters
    for pos in range(len(str)):
        sum = sum + ord(str[pos])
    return sum % size

def stringWeightHash(str, size):
    sum = 0
    for pos in range(len(str)):
        sum = sum + ord(str[pos]) * (pos + 1)
    return sum % size

print simpleHashRemainders(54, 11)
print simpleHashRemainders(26, 11)
print simpleHashRemainders(93, 11)
print simpleHashRemainders(17, 11)
print simpleHashRemainders(77, 11)
print simpleHashRemainders(31, 11)

print " "

print foldingHash("133406", 5)
print foldingHash("123496", 5)
print foldingHash("193416", 5)


print " "

print stringWeightHash("abc", 5)
print stringWeightHash("cde", 5)
print stringWeightHash("aaa", 5)

print " "

print stringHash("abc", 5)
print stringHash("cde", 5)
print stringHash("aaa", 5)