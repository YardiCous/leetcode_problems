# You are given two 0-indexed integer arrays nums1 and nums2 of even length n.
#
# You must remove n / 2 elements from nums1 and n / 2 elements from nums2. After the removals, you insert the remaining elements of nums1 and nums2 into a set s.
#
# Return the maximum possible size of the set s.

# Solution
# Just Math 

# TC: O(N)
# SC: O(N)

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        common = 0
        freq = defaultdict(int)
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        def helper(f,limit):
            nonlocal common
            res = 0
            for x in f:
                if limit <= 0:
                    break
                limit -= 1
                res += 1
            while limit > 0 and common > 0:
                limit -= 1
                common -= 1
                res += 1
            return res
        for x in set(nums1):
            freq[x] += 1
            freq1[x] += 1
        for x in set(nums2):
            freq[x] += 1
            freq2[x] += 1
        
        for x in freq:
            if freq[x] == 2:
                common += 1
                freq1[x] -= 1
                del freq1[x]
                freq2[x] -= 1 
                del freq2[x]
        limit = N // 2
        return helper(freq1,limit) + helper(freq2,limit)
