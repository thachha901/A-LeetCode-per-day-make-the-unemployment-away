# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False
    
#Complexity Analysis:
# Time Complexity: O(n), where n is the length of nums. We traverse the list once.
# Space Complexity: O(1), we use only a constant amount of space for the variables first and second.
# This solution is efficient and works well for the problem of finding an increasing