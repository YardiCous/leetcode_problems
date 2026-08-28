You are given an integer array nums and an integer k.

You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the nums[li..ri].

For each query, the subarray nums[li..ri] is considered valid if:

    It contains exactly k distinct numbers, and
    The of every number in the subarray is even.

Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.


# Solution
# Sqrt Decomp along with offline queries


# O(N + Q * SQRT(Q))

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        N = len(nums)
        Q = len(queries)
        BLOCK = int(sqrt(N)) + 1
        f = []
        for index, (left,right) in enumerate(queries):
            f.append((left,right,index))
        f.sort(key = lambda x:(x[0] // BLOCK, x[1] if (x[0] // BLOCK) % 2 == 0 else -x[1]))
        res = [None] * Q
        left,right = 0,-1
        # print(f,BLOCK)
        odd = 0
        distinct = 0
        freq = Counter()
        def add(x):
            nonlocal freq,odd,distinct
            if freq[x] == 0:
                distinct += 1
            if freq[x] & 1:
                odd -= 1
            freq[x] += 1
            if freq[x] & 1:
                odd += 1
        def remove(x):
            nonlocal freq,odd,distinct
            if freq[x] - 1 == 0:
                distinct -= 1
            if freq[x] & 1:
                odd -= 1
            freq[x] -= 1
            if freq[x] & 1:
                odd += 1
        for l,r,index in f:
            while left > l:
                left -= 1
                add(nums[left]) 
            while left < l:
                remove(nums[left])
                left += 1
            while right > r:
                remove(nums[right])
                right -= 1
            while right < r:
                right += 1
                add(nums[right])
            res[index] = distinct == k and odd == 0
        return res

