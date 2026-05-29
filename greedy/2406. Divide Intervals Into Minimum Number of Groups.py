# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
#
# You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
#
# Return the minimum number of groups you need to make.
#
# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

# Solution
# Classic sweep line but I wasn't sure if the proof is right had to sort of yolo it

# TC: O(N log N)
# SC: O(N)

from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start,end in intervals:
            events.append((start,1))
            events.append((end,-1))
        events.sort(key=lambda x:(x[0],-x[1]))
        # print(events)
        res = 0
        total = 0
        for _,val in events:    
            total += val
            res = max(res,total)
        return res
