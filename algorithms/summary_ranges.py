# LeetCode 
# Summary Ranges https://leetcode.com/problems/summary-ranges/
# 

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        n = len(nums)
        start = 0
        end = 0

        if n == 0:
            return result

        for i in range(1, n):
            if (nums[i] - nums[i - 1] != 1):
                result.append(self._range(start, end, nums))
                start = i
                end = i
            else:
                end += 1

        result.append(self._range(start, end, nums))

        return result

    def _range(self, start, end, nums):
        if start == end:
            return "{}".format(nums[start])
        else:
            return "{}->{}".format(nums[start], nums[end])

'''
s = Solution()
print s.summaryRanges([0, 1, 2, 4, 5, 7])
print s.summaryRanges([0, 1, 2])
'''

