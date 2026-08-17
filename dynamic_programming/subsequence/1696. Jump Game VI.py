You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.


# Sliding Window DP


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N
        q = deque()
        for index in range(N - 1,-1,-1):
            while q and q[0][0] - index > k:
                q.popleft()
            t = q[0][1] if q else 0
            best = nums[index] + t
            dp[index] = best
            # print(q,best)
            while q and q[-1][1] < best:
                q.pop()
            q.append((index,best))
        # print(dp)
        return dp[0]
