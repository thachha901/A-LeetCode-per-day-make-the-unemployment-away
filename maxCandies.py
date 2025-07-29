# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []

        i = 0
        max_candies = max(candies)
        while i < len(candies):
            tmp = candies[i] + extraCandies
            if tmp >= max_candies:
                res.append(bool(1))
            else:
                res.append(bool(0))
            
            i += 1
            
        
        return res
        