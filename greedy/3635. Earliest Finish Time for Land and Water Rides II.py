# You are given two categories of theme park attractions: land rides and water rides.
#
#     Land rides
#         landStartTime[i] – the earliest time the ith land ride can be boarded.
#         landDuration[i] – how long the ith land ride lasts.
#     Water rides
#         waterStartTime[j] – the earliest time the jth water ride can be boarded.
#         waterDuration[j] – how long the jth water ride lasts.
#
# A tourist must experience exactly one ride from each category, in either order.
#
#     A ride may be started at its opening time or any later moment.
#     If a ride is started at time t, it finishes at time t + duration.
#     Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
#
# Return the earliest possible time at which the tourist can finish both rides.

# Solution
# The idea is sort the water and land by smallest based on finish time and do a linear scan of the other 

# TC: O(N log N)
# SC: O(N)
from typing import List
class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        def best(first,second):
            N = len(first)
            M = len(second)
            events = []
            for i in range(N):
                events.append(first[i][0] + first[i][1])
            events.sort()
            res = 10 ** 20
            time = events[0]
            for i in range(M):
                diff = 0
                if second[i][0] > time:
                    diff += second[i][0] - time
                res = min(res,diff + second[i][1] + time)
            return res
        land,water = list(zip(ls,ld)),list(zip(ws,wd))
        return min(best(land,water),best(water,land))
       
        
