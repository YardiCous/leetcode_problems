You are given an array of positive integers nums.

You need to select a of nums which satisfies the following condition:

    You can place the selected elements in a 0-indexed array such that it follows the pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x] (Note that k can be be any non-negative power of 2). For example, [2, 4, 16, 4, 2] and [3, 9, 3] follow the pattern while [2, 4, 8, 4, 2] does not.

Return the maximum number of elements in a subset that satisfies these conditions.

# Solution
# Needed help

# TC: O(N)
# SC: O(N)

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        res = 1
        freq = defaultdict(int)
        for x in nums:
            freq[x] += 1
        if 1 in freq:
            if freq[1] % 2 == 1:
                res = max(res,freq[1])
            else:
                res = max(res,freq[1] - 1)
        for x in freq:
            if x == 1:
                continue
            curr = x
            length = 0
            while curr in freq and freq[curr] >= 2:
                length += 2
                curr *= curr
            if curr in freq and freq[curr] == 1:
                length += 1
            else:
                length -= 1
            res = max(res,length)
        return res

            
