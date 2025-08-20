# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter

        count = Counter(arr)

        occurences = list(count.values())


        return len(occurences) == len(set(occurences))