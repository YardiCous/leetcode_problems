You are given an integer array nums of length n.

Alice and Bob are playing a game. Alice chooses:

    An integer k such that k > 1.
    Two integers l and r such that 0 <= l <= r < n.

Initially, both Alice's and Bob's scores are 0.

For each index i in the range [l, r] (inclusive):

    If nums[i] is divisible by k, Alice's score increases by nums[i].
    Otherwise, Bob's score increases by nums[i].

The score difference is Alice's score minus Bob's score.

Alice wants to maximize the score difference. If there are multiple values of k that achieve the maximum score difference, she chooses the smallest such k.

Return the product of the maximum score difference and the chosen value of k. Since the result can be large, return it modulo 109 + 7.

# Solution
# Kadane + Divisors


# TC: O(N sqrt D)
# TC: O(D)


class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        N = len(nums)
        divisors = set()
        for x in nums:
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
                i += 1
        # print(divisors)
        divisors.add(2)
        res = -inf
        MOD = 10 ** 9 + 7
        res_k = 0
        for k in sorted(divisors):
            if k == 1:
                continue
            curr = 0
            mx = -inf
            for x in nums:
                if x % k == 0:
                    curr += x
                else:
                    curr -= x
                mx = max(curr,mx)
                if curr < 0:
                    curr = 0
            if res < mx:
                res = mx
                res_k = k

        return (res * res_k) % MOD
                

