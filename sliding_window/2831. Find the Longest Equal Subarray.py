# You are given a 0-indexed integer array nums and an integer k.
#
# A subarray is called equal if all of its elements are equal. Note that the empty subarray is an equal subarray.
#
# Return the length of the longest possible equal subarray after deleting at most k elements from nums.
#
# A subarray is a contiguous, possibly empty sequence of elements within an array.

# Solution
# Sliding window, but I did not think of O(N) solution, seems like i overcomplicated this solution, used SortedList and added a log factor

# TC: O(N)
# SC: O(N)

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        freq = defaultdict(int)
        left = 0
        res = 0
        for right in range(N):
            x = nums[right]
            freq[x] += 1
            res = max(res,freq[x])
            while (right - left + 1) - res > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return res
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        freq = defaultdict(int)
        left = 0
        res = 0
        sl = SortedList()
        for right in range(N):
            x = nums[right]
            if (freq[x],x) in sl:
                sl.remove((freq[x],x))
            freq[x] += 1
            sl.add((freq[x],x))
            while (right - left + 1) - sl[-1][0] > k:
                l = nums[left]
                sl.remove((freq[l],l))
                freq[l] -= 1
                if freq[l] > 0:
                    sl.add((freq[l],l))
                elif freq[l] == 0:
                    del freq[l]
                left += 1
            res = max(res,sl[-1][0])
        return res
