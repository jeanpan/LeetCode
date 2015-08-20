# LeetCode 
# Rotate Array https://leetcode.com/problems/rotate-array/

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        index = 0
        current = nums[0]
        d = 0
        for i in range(n):
            next = (index + k) % n
            tmp = nums[next]
            nums[next] = current
            index = next
            current = tmp

            print nums

            d = (d + k) % n
            if d == 0:
                index = (index + 1) % n
                current = nums[index]

s = Solution()
nums = [1, 2, 3, 4, 5, 6]
s.rotate(nums, 2)
print nums