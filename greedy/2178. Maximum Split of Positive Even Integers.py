# You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.
#
#     For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum): (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers. Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.
#
# Return a list of integers that represent a valid split containing a maximum number of integers. If no valid split exists for finalSum, return an empty list. You may return the integers in any order.

# Solution 
# Had to look at the solutions tab for this, but basically the idea is maintain a set and start at integer 2,
# increment every integer by 2 since we want to greedily have the maximum length for some finalSum, then track with a running total
# if running total == finalSum return set else remove total - finalSum and the reason proof works is because we can gaurantee that total - finalSum will be
# in the set because before it overshot, some x was added and since it is all even integers whatever is overshot we can assume is in the set because it will be 
# smaller then x

# TC: O(sqrt n)
# SC: O(sqrt n)

from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        res = set()
        s = 0
        i = 2
        while s < finalSum:
            s += i
            res.add(i)
            i += 2
        # print(res)
        if s == finalSum:
            return list(res)
        else:
            res.discard(s - finalSum)
            return list(res)
        
        



