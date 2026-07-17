You are given an integer array nums of length n.

An index i (0 < i < n - 1) is special if nums[i] > nums[i - 1] and nums[i] > nums[i + 1].

You may perform operations where you choose any index i and increase nums[i] by 1.

Your goal is to:

    Maximize the number of special indices.
    Minimize the total number of operations required to achieve that maximum.

Return an integer denoting the minimum total number of operations required.

# Solution
# The idea I got for fixed length of odd, but for odd even parirty I had to check and realized this peek and valley idea, so just becomes take or no take

# TC: O(N)
# SC: O(N)


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        N = len(nums)
        def solve(index):
            op = 0
            for i in range(index,N - 1,2):
                mx = max(nums[i - 1],nums[i + 1])
                if nums[i] > mx:
                    continue
                op += 1 + mx - nums[i]
            return op
        if N % 2 or N == 3:
            return solve(1)
        @cache
        def dp(index,skip):
            if index >= N - 1:
                return 0
            cost = max(0,max(nums[index - 1],nums[index + 1]) + 1 - nums[index])
            if skip:
                return cost + dp(index + 2,True)
            return min(cost + dp(index + 2,False),cost + dp(index + 3, True))
        return min(dp(1,0),dp(2,1))
            
