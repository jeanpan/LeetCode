# Binary Search 
# Not LeetCode Exercise

class Solution(object):
    def binarySearch(self, alist, item):
        first = 0
        last = len(alist) - 1
        found = False

        while first <= last and not found:
            middle = (first + last) // 2
            if alist[middle] == item:
                found = True
            else:
                if item < alist[item]:
                    last = middle - 1
                else:
                    first = middle + 1

        return found

    def recursiveBinarySearch(self, alist, item):
        if len(alist) == 0:
            return False
        else:
            mid = len(alist) // 2
            if alist[mid] == item:
                return True
            else:
                if item < alist[mid]:
                    return self.recursiveBinarySearch(alist[:mid], item)
                else:
                    return self.recursiveBinarySearch(alist[mid + 1:], item)



s = Solution()
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print s.binarySearch(testlist, 3)
print s.binarySearch(testlist, 13)

print s.recursiveBinarySearch(testlist, 3)
print s.recursiveBinarySearch(testlist, 13)

