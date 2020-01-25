# -*- coding: utf-8 -*-
class Solution:
    def breakPalindrome(self, palindrome):
        # 其实就检查a就行了
        length = len(palindrome)
        if length < 2:
            return ""
        left = 0
        right = length - 1
        while left < right:
            if palindrome[left] == "a":
                left = left + 1
                right = right - 1
            else:
                return palindrome[:left] + "a" + palindrome[left + 1:]
        return palindrome[:-1] + "b"



print(Solution().breakPalindrome("bab"))