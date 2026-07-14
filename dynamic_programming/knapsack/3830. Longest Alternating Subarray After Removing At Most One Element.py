You are given an integer array nums.

A nums[l..r] is alternating if one of the following holds:

    nums[l] < nums[l + 1] > nums[l + 2] < nums[l + 3] > ...
    nums[l] > nums[l + 1] < nums[l + 2] > nums[l + 3] < ...

In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between strictly greater and strictly smaller.

You can remove at most one element from nums. Then, you select an alternating subarray from nums.

Return an integer denoting the maximum length of the alternating subarray you can select.

A subarray of length 1 is considered alternating.


# Solution
# Take no take DP but I keep forgetting you can do loops that look like N^2 but with cache becomes O(N)


#TC: O(N)
# SC: O(N)


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        N = len(nums)
        res = 1
        @lru_cache(None)
        def down(index,skip):
            best = 0
            if index + 1 < N and nums[index] < nums[index + 1]:
                best = max(best,up(index + 1,skip) + 1)
            if index + 2 < N and nums[index] < nums[index + 2] and skip:
                best = max(best,up(index + 2,0) + 1)
            return best
        @lru_cache(None)
        def up(index,skip):
            best = 0
            if index + 1 < N and nums[index] > nums[index + 1]:
                best = max(best,down(index + 1,skip) + 1)
            if index + 2 < N and nums[index] > nums[index + 2] and skip:
                best = max(best,down(index + 2,0) + 1)
            return best
        @lru_cache(None)
        def start(index):
            best = 0
            if index + 1 < N and nums[index] < nums[index + 1]:
                best = max(best,up(index + 1,1) + 1)
            if index + 2 < N and nums[index] < nums[index + 2]:
                best = max(best,up(index + 2,0) + 1)
            
            if index + 1 < N and nums[index] > nums[index + 1]:
                best = max(best,down(index + 1,1) + 1)
            if index + 2 < N and nums[index] > nums[index + 2]:
                best = max(best,down(index + 2,0) + 1)

            return best

        for i in range(N):
            res = max(res,start(i) + 1) 
        start.cache_clear()
        up.cache_clear()
        down.cache_clear()
        return res
        
