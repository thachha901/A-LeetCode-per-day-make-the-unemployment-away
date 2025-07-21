# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []


        for char in s:
            if len(res) < 2 or not res[-2] == res[-1] == char:
                res.append(char)

        
        return "".join(res)