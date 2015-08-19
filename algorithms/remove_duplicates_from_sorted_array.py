# LeetCode 
# Remove Duplicates from Sorted Array https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                # swap number between i and next number of count
                count += 1
                self.swap(nums, i, count)

        return count + 1

    def swap(self, nums, i, count):
        tmp = nums[i]
        nums[i] = nums[count]
        nums[count] = tmp

'''
s = Solution()
print s.removeDuplicates([1, 1, 2])
print s.removeDuplicates([1, 1, 1, 2, 2])
print s.removeDuplicates([0, 1])
print s.removeDuplicates([1, 2, 3])
print s.removeDuplicates([1, 1, 2, 3, 3])
'''