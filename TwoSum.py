class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #O(N^2) complexity solution using brute force
        for i in range(len(nums)):
            for j in range (len(nums)):
                if i < j and nums[i] + nums[j] == target:
                    return i, j
        
        
        
        #O(n) complexity solution using a hash map
        # num_map = {}
        
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in num_map:
        #         return [num_map[complement], i]
        #     num_map[num] = i
            
        # return num_map