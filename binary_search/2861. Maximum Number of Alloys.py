You are the owner of a company that creates alloys using various types of metals. There are n different types of metals available, and you have access to k machines that can be used to create alloys. Each machine requires a specific amount of each metal type to create an alloy.

For the ith machine to create an alloy, it needs composition[i][j] units of metal of type j. Initially, you have stock[i] units of metal type i, and purchasing one unit of metal type i costs cost[i] coins.

Given integers n, k, budget, a 1-indexed 2D array composition, and 1-indexed arrays stock and cost, your goal is to maximize the number of alloys the company can create while staying within the budget of budget coins.

All alloys must be created with the same machine.

Return the maximum number of alloys that the company can create.

# Solution
# Binary search on answer treating the answer as the highest number we can make

# TC: O(N * M Log K)
# SC: O(1)

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def good(target):
            for i in range(k):
                curr = 0
                for j in range(n):
                    required = target * composition[i][j]
                    if required > stock[j]:
                        curr += (required - stock[j]) * cost[j]
                if curr <= budget:
                    return True
            return False
        left,right = 0,10 ** 9 + 1
        res = 0
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                res = mid
                left = mid + 1
            else:
                right = mid
        return res
