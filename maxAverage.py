# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        init_sum = sum(nums[:k])
        max_sum = init_sum
        n = len(nums)

        for i in range(k, n):
            init_sum += nums[i] - nums[i - k]
            if init_sum > max_sum:
                max_sum = init_sum

        
        return max_sum / float(k)