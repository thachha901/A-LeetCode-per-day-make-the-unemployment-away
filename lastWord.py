# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        res = 0
        while i >= 0 and s[i] != ' ':
            res += 1
            i -= 1

        return res