# You are given two strings word1 and word2.
#
# A string x is called valid if x can be rearranged to have word2 as a .
#
# Return the total number of valid of word1.
#
# Note that the memory limits in this problem are smaller than usual, so you must implement a solution with a linear runtime complexity.

# Solution
# Sliding window, horrible description imo, i thought it is permutation as you can rearrange word2 as a prefix.

# TC: O(N)
# SC: O(N)

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        N = len(word1)
        word2_c = Counter(word2)
        word1_c = Counter()
        left = 0
        res = 0
        have,need = 0,len(word2_c)
        for right in range(N):
            x = word1[right]
            word1_c[x] += 1
            if x in word2_c and word1_c[x] == word2_c[x]:
                have += 1
            while have == need:
                # length = N - right - 1
                # print(fact[length])
                res += left + 1
                l = word1[left]
                word1_c[l] -= 1
                if l in word2_c and word1_c[l] < word2_c[l]:
                    have -= 1
                if word1_c[l] == 0:
                    del word1_c[l]
                left += 1
        return res
