You are given an integer array nums.

Your task is to find the number of pairs of non-empty (seq1, seq2) of nums that satisfy the following conditions:

    The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.
    The of the elements of seq1 is equal to the GCD of the elements of seq2.

Return the total number of such pairs.

Since the answer may be very large, return it modulo 109 + 7.


# Solution
# Pretty simple + today I learned you can use gcd as a state

# TC:O(N * gcd1 * gcd2)
# SC: O(N * gcd1 * gcd2)


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        N = len(nums)
        MOD = 10 ** 9 + 7
        @cache
        def dp(index,g1,g2):
            if index == N:
                if g1 == g2 and g1 != 0:
                    return 1
                return 0
            res = 0
            res += dp(index + 1,g1,g2)
            res += dp(index + 1,gcd(g1,nums[index] if g1 else nums[index]),g2) 
            res += dp(index + 1,g1,gcd(g2,nums[index]) if g2 else nums[index])
            res %= MOD
            return res
        return dp(0,0,0)

            
