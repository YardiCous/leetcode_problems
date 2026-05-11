# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
#
# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

# Solution
# Couldn't think of a way had to watch larry, but basically the idea is instead of looking at trying to get the minimum, sort it by B - A because the biggest difference we want to take B
# Then the rest we take A 

# TC: O(N log N)
# SC: O(1)


from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        costs.sort(key=lambda x:x[1] - x[0])
        # print(costs)
        res = 0
        for i in range(N):
            if i + i < N:      
                res += costs[i][1]
            else:
                res += costs[i][0]
        return res
