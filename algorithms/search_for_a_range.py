# LeetCode 
# Search for a Range https://leetcode.com/problems/search-for-a-range/
# 

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        first = 0
        last = len(nums) - 1
        found = False

        while first <= last and not found:
            mid = (first + last) // 2

            if nums[mid] == target:
                found = True
                start = mid
                end = mid
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1

                while 0 < start and nums[start - 1] == target:
                    start -= 1
            else:
                if target < nums[mid]:
                    last = mid - 1
                else:
                    first = first + 1


        if not found:
            return [-1, -1]
        else:
            return [start, end]

'''
s = Solution()
a = [5, 7, 7, 8, 8, 10]
b = [1]
print s.searchRange(a, 8)
print s.searchRange(a, 7)
print s.searchRange(a, 6)
print s.searchRange(a, 5)
print s.searchRange(a, 10)
print s.searchRange(b, 1)
'''


