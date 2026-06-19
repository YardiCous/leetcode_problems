# You are given an integer array nums and an integer k.
#
# Your task is to partition nums into k non-empty . For each subarray, compute the bitwise XOR of all its elements.
#
# Return the minimum possible value of the maximum XOR among these k subarrays.

# Solution
# I knew xor can't just keep track, but I didn't know xor prefix sum works. Also have to do pruning to make it run faster, and also if total iterations is around 12 million
# it is still fine, I thought N^3 was too slow but it is accepted. but pruning it makes it N ^ 2 * k

# TC: O(N ^ 2 * k)
# SC: O(N ^ 2)

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] ^ n)
        # print(prefix)
        @cache
        def dp(index,count):
            if index == N:
                if count == 0:
                    return 0
                return INF
            if count == 0:
                return INF
            
            res = INF
            for end in range(index,N - count + 1):
                # print(end)
                seg_range = prefix[end + 1] ^ prefix[index]
                x = max(dp(end + 1,count - 1),seg_range)
                res = min(res,x)
            return res
        return dp(0,k)
