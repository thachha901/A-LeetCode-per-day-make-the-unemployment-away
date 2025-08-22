
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        min_price = float('inf')

        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            if profit > best:
                best = profit
        

        return best