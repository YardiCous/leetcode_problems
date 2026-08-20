You are given two strings, s and t.

You can create a new string by selecting a from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.

Return the length of the longest that can be formed this way.

# Solution
# Larry helped with it

class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        t = t[::-1]
        INF = 10 ** 20
        @cache
        def longest_s2(left,right):
            if left > right:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return 2 + longest_s2(left + 1,right - 1)
            return -INF
        @cache
        def longest_s(left,right):
            if left > right:
                return 0
            return max(longest_s(left,right - 1),longest_s2(left,right))
        @cache
        def longest_t2(left,right):
            if left > right:
                return 0
            if left == right:
                return 1
            if t[left] == t[right]:
                return 2 + longest_t2(left + 1,right - 1)
            return -INF
        @cache
        def longest_t(left,right):
            if left > right:
                return 0
            return max(longest_t(left,right - 1),longest_t2(left,right))
        @cache 
        def f(i,j):
            if i == N:
                return longest_t(j,M - 1)
            if j == M:
                return longest_s(i,N - 1)
            res = 0
            if s[i] == t[j]:
                res = max(res,2 + f(i + 1,j + 1))
                res = max(res,2 + longest_t(j + 1,M - 1))
                res = max(res,2 + longest_s(i + 1,N - 1))
            return res
        res = 0
        for i in range(N):
            res = max(res,longest_s(i,N - 1))

        for i in range(M):
            res = max(res,longest_t(i,M - 1))
        for i in range(N):
            for j in range(M):
                res = max(res,f(i,j))
        f.cache_clear()
        longest_t.cache_clear()
        longest_s.cache_clear()
        longest_t2.cache_clear()
        longest_s2.cache_clear()
        return res
