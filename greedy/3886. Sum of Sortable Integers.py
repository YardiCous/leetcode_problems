# You are given an integer array nums of length n.
#
# An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:
#
#     Partition nums into consecutive of length k.
#     Cyclically rotate each subarray independently any number of times to the left or to the right.
#
# Return an integer denoting the sum of all possible sortable integers k.

# Solution
# What I learn from this problem, first of all, to check if a array can be sorted by rotating the array, at most 1 drops is allowed 
# So now the problem, the idea is basically for the divisors of N can can it be partition into equal length of K,
# and the idea is since each partition subarray is rotated, we just need to find the max of the current subarray and minimum after this subarray
# To do that precompute a suffix array where the i + k smallest element in i + k can be found in O(1)

# TC: O(N sqrt N)
# SC: O(N)

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        N = len(nums)
        divisors = set()
        suffix = [nums[-1]]
        for i in range(1,int(N ** 0.5) + 1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
        for i in range(N - 2,-1,-1):
            suffix.append(min(suffix[-1],nums[i]))
        suffix.reverse()
        def good(k):
            for i in range(0,N,k):
                subarray = nums[i:i + k]
                M = len(subarray)
                best = 0
                count = 0
                for j in range(M):
                    if subarray[j] > subarray[(j + 1) % M]:
                        count += 1
                    if subarray[j] > best:
                        best = subarray[j]
                if count > 1:
                    return False
                if i + k < N and best > suffix[i + k]:
                    return False
            return True
            
        res = 0
        for j in divisors:
            if good(j):
                res += j
        return res
