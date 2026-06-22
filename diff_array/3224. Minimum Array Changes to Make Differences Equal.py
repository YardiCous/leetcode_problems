# You are given an integer array nums of size n where n is even, and an integer k.
#
# You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from 0 to k.
#
# You need to perform some changes (possibly none) such that the final array satisfies the following condition:
#
#     There exists an integer X such that abs(a[i] - a[n - i - 1]) = X for all (0 <= i < n).
#
# Return the minimum number of changes required to satisfy the above condition.

# Solution
# Finally understood the intuition after 2 hours, but basically the idea is for every pair, we can eith# swap both or swap 1 or swap none, those are the 3 cases, for swap both is easy, swapping 1 means,
# we either swap to 0 or swap to k something like that, and then we loop through X and try every single# X

# TC: O(N)
# SC: O(N)

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        N = len(nums)
        diff = [0] * (k + 2)
        for i in range(N // 2):
            left,right = nums[i],nums[N - i - 1]
            d = abs(left - right)
            max_diff = max(left,right, k - left, k - right)
            diff[0] -= 1
            diff[d] -= 1
            diff[d + 1] += 1
            diff[max_diff + 1] += 1
        res = N
        total = N
        for i in range(k + 1):
            total += diff[i]
            res = min(res,total)
        return res
        
        







        
