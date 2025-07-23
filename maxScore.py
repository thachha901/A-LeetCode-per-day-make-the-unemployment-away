# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.


class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """

        def removePair(s, first, second, point):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += point
                else:
                    stack.append(char)

            return "".join(stack), score
        
        total_score = 0
        if x >= y:
            s, gain = removePair(s, 'a', 'b', x)
            total_score += gain
        
            s, gain = removePair(s, 'b', 'a', y)
            total_score += gain
        else:

            s, gain = removePair(s, 'b', 'a', y)
            total_score += gain

            s, gain= removePair(s, 'a', 'b', x)
            total_score += gain
        return total_score

        