# You are given an integer array nums and a positive integer k.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
# Return the length of the longest valid subsequence of nums.
 

class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                max_len = max(max_len, dp[i][mod] + 1)

        return max_len