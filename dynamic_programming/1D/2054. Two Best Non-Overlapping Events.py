# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
#
# Return this maximum sum.
#
# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

# Solution
# DP + Binary search, another way to do is sweep line with a suffix, basically when entering a new segment check previous segments max value

# TC: O(N log N)
# SC: O(N)

from typing import List
from functools import lru_cache
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        N = len(events)
        events.sort(key=lambda x:(x[0],x[1]))
        # print(events)
        def good(idx,target):
            left,right = idx + 1,N - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if events[mid][0] > target:
                    right = mid - 1
                    res = mid
                else:
                    left = mid + 1
            return res
        @lru_cache(100005)
        def dfs(i,count):
            if i == N or count == 0:
                return 0
            # skip
            res = dfs(i + 1,count)
            end = events[i][1]
            idx = good(i,end)
            # print(idx)
            take = events[i][2]
            if idx != -1:
                take += dfs(idx,count - 1)
            res = max(res,take)
            return res
        r = dfs(0,2)
        dfs.cache_clear()
        return r
class SweepLine:
    def maxTwoEvents(self, e: List[List[int]]) -> int:
        events = []
        for start,end,value in e:
            events.append((start,value,1))
            events.append((end,value,-1))
        events.sort(key=lambda x:(x[0],-x[2]))

        res = 0
        mx_left = 0
        for time,val,choice in events:
            if choice == 1:
                res = max(res,val + mx_left)
            else:
                mx_left = max(mx_left,val)
        return res
