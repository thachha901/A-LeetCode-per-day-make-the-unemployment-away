# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        sub = ""
        while len(sub) < len(needle) and i < len(haystack):
            sub += haystack[i]
            if len(sub) == len(needle) and sub == needle:
                return i - len(needle) + 1
            elif len(sub) == len(needle) and sub != needle: 
                sub = sub[1:]
            i += 1
        
        return -1

        