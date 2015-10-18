# -*- coding: utf-8 -*-
# http://interactivepython.org/courselib/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html
import re

class Solution:

    def checkPalindrome(self, str):
        s = re.sub(r'[^\w]', '', str.lower())
        r = self.reverseStr(s)
        if s == r:
            return True
        else:
            return False

    def reverseStr(self, str):
        if str == "":
          return str
        else:
            return str[-1] + self.reverseStr(str[:-1])

s = Solution()
print(s.checkPalindrome("kayak"))
print(s.checkPalindrome("aibohphobia"))
print(s.checkPalindrome("Live not on evil"))
print(s.checkPalindrome("Reviled did I live, said I, as evil I did deliver"))
print(s.checkPalindrome("Go hang a salami; I’m a lasagna hog."))
print(s.checkPalindrome("Able was I ere I saw Elba"))
print(s.checkPalindrome("Kanakanak – a town in Alaska"))
print(s.checkPalindrome("Wassamassaw – a town in South Dakota"))