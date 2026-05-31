# You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget. 
# There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.
#
# After buying items, you may receive free copies according to the following rules:
#
#     For each item i that you bought at least one copy of, you receive one free copy of every item j such that j != i and factori divides factorj.
#     Buying multiple copies of the same item i does not give additional free copies through item i.
#     The same item j can be received multiple times for free if it is received from purchases of different item types.
#
# Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

# Solution
# Misread the question and didn't know how to solve it because of that

# TC: O(N * budget)
# SC: O(N * budget)


from typing import List 
from functools import lru_cache
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        N = len(items)
        count = []
        for i in range(N):
            cnt = 0
            for j in range(N):
                if i != j:
                    if items[j][0] % items[i][0] == 0:
                        cnt += 1
            count.append([items[i][1],cnt])
        @lru_cache(None)
        def dfs(i,b):
            if i == N:
                return 0
            res = dfs(i + 1,b)
            profit,cnt = count[i]
            if b >= profit:
                stay = dfs(i,b - profit) + 1
                take = dfs(i + 1,b - profit) + cnt + 1
                res = max(res,stay,take)
            return res
        r = dfs(0,budget)
        dfs.cache_clear()
        return r
        # dp = [0] * (budget + 1) 

        # for profit,cnt in count:
        #     for b in range(profit,budget + 1):
        #         dp[b] = max(dp[b],dp[b - profit] + 1)
        #     for b in range(budget,profit - 1,-1):
        #         dp[b] = max(dp[b],dp[b - profit] + cnt + 1)
        #     # print(dp)
        # return max(dp)


                       
