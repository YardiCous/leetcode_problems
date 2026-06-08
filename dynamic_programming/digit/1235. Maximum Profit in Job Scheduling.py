# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
#
# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job that starts at time X.


# Solution
# DP + Binary Search

# TC: O(N log N)
# SC: O(N)

from typing import List
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def get_idx(target,i):
            left,right = i + 1,N - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][0] >= target:
                    right = mid - 1
                    res = mid
                else:
                    left = mid + 1
            return res
        jobs = list(zip(startTime,endTime,profit))
        N = len(startTime)
        jobs.sort()
        dp = [0] * (N + 1)
        for i in range(N - 1,-1,-1):
            skip = dp[i + 1]
            idx = get_idx(jobs[i][1],i)
            dp[i] = skip
            if idx != -1:
                dp[i] = max(dp[i],jobs[i][2] + dp[idx])
            else:
                dp[i] = max(dp[i],jobs[i][2])
        return dp[0]
        @cache
        def dp(index):
            if index == N:
                return 0
            res = dp(index + 1)
            idx = get_idx(jobs[index][1],index)
            take = jobs[index][2]
            if idx != -1:
                take += dp(idx)
            return max(res,take) 
        return dp(0)

        

