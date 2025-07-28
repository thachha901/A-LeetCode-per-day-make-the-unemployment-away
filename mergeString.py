# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = [a + b for a, b in zip(word1, word2)]
        res.append(word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):])

        return "".join(res)