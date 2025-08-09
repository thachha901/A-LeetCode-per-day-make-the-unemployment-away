# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()

        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            tmp = nums[left] + nums[right]
            if tmp == k:
                ops += 1
                left += 1
                right -= 1
            elif tmp > k:
                right -= 1
            else:
                left += 1
        

        return ops