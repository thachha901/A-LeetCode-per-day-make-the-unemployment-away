# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

# Return the maximum sum of values that you can receive by attending events.

class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        from bisect import bisect_right

        events.sort(key=lambda x: x[1])

        
        end_days = [e[1] for e in events]
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            start, end, value = events[i -1]
            idx = bisect_right(end_days, start - 1)

            for j in range(1, k + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j])

                dp[i][j] = max(dp[i][j], dp[idx][j - 1] + value)

        return dp[n][k]