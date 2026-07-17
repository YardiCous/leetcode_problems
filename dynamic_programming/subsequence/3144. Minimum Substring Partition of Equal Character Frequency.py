# Given a string s, you need to partition it into one or more balanced . For example, if s == "ababcc" then ("abab", "c", "c"), ("ab", "abc", "c"), and ("ababcc") are all valid partitions, but ("a", "bab", "cc"), ("aba", "bc", "c"), and ("ab", "abcc") are not. The unbalanced substrings are bolded.
#
# Return the minimum number of substrings that you can partition s into.
#
# Note: A balanced string is a string where each character in the string occurs the same number of times.

# Solution
# DP to partition the string, need to come back to this

#TC: O(N ^ 2)
#SC: O(N)

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        N = len(s)
        res = N
        INF = 10 ** 20
        dp = [INF] * (N + 1)
        dp[0] = 0
        for i in range(N):
            freq = defaultdict(int)
            f_freq = defaultdict(int)
            for j in range(i,N):a
                x = s[j]
                if x in freq:
                    f_freq[freq[x]] -= 1
                    if f_freq[freq[x]] == 0:
                        del f_freq[freq[x]]
                freq[x] += 1
                f_freq[freq[x]] += 1
                if len(f_freq) == 1:
                    dp[j + 1] = min(dp[j + 1],dp[i] + 1)
        return dp[N]

