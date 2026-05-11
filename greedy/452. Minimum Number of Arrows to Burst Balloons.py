# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Solution 
# Had to ask LLM for hint, at first I wanted to sort by start, but should have sort by end, as end is the one that matters as we want to group by ending

# TC: O(N log N)
# SC: O(1)

from typing import List
class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key=lambda x:(x[1]))
        best = float("-inf")
        # print(points)
        for start,end in points:
            if not (start <= best <= end):
                res += 1
                best = end
            # print(res,best)
        return res
