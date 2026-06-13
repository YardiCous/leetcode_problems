# You are given a positive integer hp and two positive 1-indexed integer arrays damage and requirement.
#
# There is a dungeon with n trap rooms numbered from 1 to n. Entering room i reduces your health points by damage[i]. After that reduction, if your remaining health points are at least requirement[i], you earn 1 point for that room.
#
# Let score(j) be the number of points you get if you start with hp health points and enter the rooms j, j + 1, ..., n in this order.
#
# Return the integer score(1) + score(2) + ... + score(n), the sum of scores over all starting rooms.
#
# Note: You cannot skip rooms. You can finish your journey even if your health points become non-positive.

# Solution
# The idea is book keeping and math, and the idea is first start from the back as it would be easier and the main idea is using offset 
# and keeping track of the offset from right to left 

# TC: O(N Log N)
# SC: O(N)

from sortedcontainers import SortedList
from typing import List 
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        N = len(damage)
        sl = SortedList()

        res = 0
        offset = 0
        for i in range(N - 1,-1,-1):
            d,r = damage[i],requirement[i]
            sl.add(r - offset)
            offset += d

            good = sl.bisect_right(hp - offset)

            res += good
        return res
