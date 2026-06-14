# You are given two integer arrays of size 2: d = [d1, d2] and r = [r1, r].
#
# Two delivery drones are tasked with completing a specific number of deliveries. Drone i must complete di deliveries.
#
# Each delivery takes exactly one hour and only one drone can make a delivery at any given hour.
#
# Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone i must recharge every ri hours (i.e. at hours that are multiples of ri).
#
# Return an integer denoting the minimum total time (in hours) required to complete all deliveries.

# Solution
# Pure discrete math, which is my weakness, basically the idea is lets say time = 7, we find for each drone when they are not avaliable to deliver food, 
# meaning finding the intervals where they cannot deliver as they have to recharge, for example if r1 == 2 then 7 - (7 // 2) is the time when the drone is available to work
# then we need to find the overlap which is 7 - (7 // lcd) as we do not want to count 1 extra for each overlap interval. Then we also want the intersect where these intervals that
# isnt the lcd factor, how many are there in common which is A intersect B, which can be found by 7 - (A) - (B) + intersect
# Also binary search on answer for it

# TC: O(Log N)
# SC: O(1)


from typing import List
import math
class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        left,right = 1, (10 ** 15) + 5
        def good(target):
            a = target
            x = math.lcm(r[0],r[1])
            x1 = a - (a // r[0])
            x2 = a - (a // r[1])
            x3 = a - (a // r[0] + a // r[1] - a // x)
            if x1 >= d[0] and x2 >= d[1] and x1 + x2 - x3 >= d[0] + d[1]:
                return True
            return False
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
