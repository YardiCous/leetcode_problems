You are given an integer array nums and a positive integer k.

You must choose exactly one of nums and perform exactly one of the following operations:

    Multiply each number in the chosen subarray by k.
    Divide each number in the chosen subarray by k.
        When dividing a positive number by k, use the floor value of the division result.
        When dividing a negative number by k, use the ceiling value of the division result.

Return the maximum possible sum of a non-empty subarray in the resulting array.

Note that the subarray chosen for the operation and the subarray chosen for the sum may be different.


# Solution
# Tricky kadane 

# TC: O(N)

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if all (x < 0 for x in nums):
            return -((-max(nums)) // k)
        N = len(nums)
        INF = 10 ** 20
        res = -INF
        curr = 0
        for x in nums:
            curr += x
            res = max(res,curr)
            if curr < 0:
                curr = 0
        res *= k
        @cache
        def dp(index,start,end):
            if index == N:
                return 0
            res = 0
            x = nums[index]
            xk = 0
            if x > 0:
                xk = x // k
            else:
                xk = -(-x // k)
            if not end:
                res = max(res,xk + dp(index + 1,True,False))
            if not start:
                res = max(res,x + dp(index + 1,False,False))
            if start and end:
                res = max(res,x + dp(index + 1,True,True))
            if start and not end:
                res = max(res,xk + dp(index + 1,True,True))
            return res
        for i in range(N):
            res = max(res,dp(i,False,False))

        return res

        
