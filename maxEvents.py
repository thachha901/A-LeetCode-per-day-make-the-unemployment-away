# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

# Return the maximum number of events you can attend.

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events.sort()
        import heapq

        res = 0
        min_heap = []
        i = 0
        n = len(events)
        max_day = max(end for _, end in events)

        for day in range(1, max_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i+=1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                res += 1

        return res
        