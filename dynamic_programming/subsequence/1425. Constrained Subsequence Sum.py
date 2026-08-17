Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.



# Solution
# DP + Sliding Window Trick
# How to identify? is the question
# when we have a range of previous dp[i] to dp[i + k] constriant

# TC: O(N)
# SC: O(N)

        # @cache
        # def dp(index,take):
        #     if index >= N:
        #         return -INF if take == -1 else 0
        #     res = dp(index + 1,take)
        #     # res = max(res,dp(index + ))
        #     if take == -1:
        #         res = max(res,dp(index + 1,index) + nums[index]) 
        #     else:
        #         if index - take <= k:
        #             res = max(res,dp(index + 1,index) + nums[index])
        #     return res
        # return dp(0,-1)
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        dp = [-INF] * N
        q = deque()
        for index in range(N - 1,-1,-1):
            while q and q[0][0] - index > k:
                q.popleft()
            best = max(0,q[0][1]) if q else 0
            total = nums[index] + best
            dp[index] = total
            while q and q[-1][1] <= total:
                q.pop()
            q.append((index,total))
        # print(dp)
        return max(dp)
