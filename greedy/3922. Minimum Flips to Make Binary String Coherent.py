# You are given a binary string s.
#
# A string is considered coherent if it does not contain "011" or "110" as subsequences.
#
# In one operation, you can flip any character in s ('0' to '1' or '1' to '0').
#
# Return an integer denoting the minimum number of modifications required to make s coherent.
#
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

# Solution
# This is an ad hoc question, and also require some proving, basically the idea is we always want to swap to 1s if possible, but there are many different cases, in fact a total of 4 cases,
# first case - flip all 1s to be 0s, flip all 1s except for 1 as we are trying to minimize, flip all 0s to be 1s and if first and last char is "1" flip all 1s in between.
# Couldn't solve during the contest, was tired that day but also had to prove stuff and got lazy

#TC: O(N)
#SC: O(1)
class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        if N < 3:
            return 0
        ones = s.count("1")
        flip_all_ones = ones
        flip_left_one = max(0,ones - 1)
        flip_all_zeros = N - ones
        total = 10 ** 20
        if s[0] == "1" and s[-1] == "1":
            total = ones - 2
        return min(flip_all_ones,flip_left_one,flip_all_zeros,total)
