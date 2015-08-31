# LeetCode 
# Length of Last Word https://leetcode.com/problems/length-of-last-word/
import re

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = re.findall(r"[\w.]+", s)

        if len(arr) < 1:
            return 0
        else:
            return len(arr[len(arr) - 1])

'''
s = Solution()
print s.lengthOfLastWord("He")
print s.lengthOfLastWord("Hello    World!")
'''