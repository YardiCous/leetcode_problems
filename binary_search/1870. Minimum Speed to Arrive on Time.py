# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
#
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
#
#     For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
#
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
#
# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

# Solution
# Binary search on answer

# TC: O(N log N)
# SC: O(1)

from typing import List
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left,right = 1,10 ** 7 + 1
        res = -1
        def good(target):
            total = 0
            print(target)
            for i in range(len(dist) - 1):
                n = dist[i]
                if n % target == 0:
                    total += (n // target)
                else:
                    total += (n // target) + 1
            total += dist[-1] / target
            # print(total)
            return total <= hour
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                right = mid
            else:
                left = mid + 1
        return res 
