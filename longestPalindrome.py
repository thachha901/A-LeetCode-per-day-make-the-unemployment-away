# Given a string s, return the longest palindromic substring in s.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def checkPalindrome(sub):
            return sub == sub[::-1]
        
    

        n = len(s)
        # Duyệt độ dài chuỗi con từ lớn đến bé
        for right in range(n, 0, -1):
            for left in range(n - right + 1):
                sub = s[left:left + right]
                if checkPalindrome(sub):
                    return sub
        return ""
            

        