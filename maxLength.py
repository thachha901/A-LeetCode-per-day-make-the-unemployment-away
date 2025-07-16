# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.




class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        odd = 0

        if(nums[0] % 2 == 0):
            even += 1
        else:
            odd += 1
        
        n = len(nums)
        
            
        sub = [nums[0]]  # Luôn thêm phần tử đầu tiên
        for i in range(1, n):
            if(nums[i] % 2) == 0:
                even += 1
            else:
                odd += 1
            if (nums[i] % 2) != (sub[-1] % 2):
                sub.append(nums[i])
        result = max(len(sub), even, odd)

        return result
        