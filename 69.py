# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        if s[0] == '-':
            i = s.find('9', 1)
            return int(s if i == -1 else s[:i] + '6' + s[i+1:])
        else:
            i = s.find('6')
            return int(s if i == -1 else s[:i] + '9' + s[i+1:])

            

        
        