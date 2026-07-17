# You are given a string s, which is known to be a concatenation of anagrams of some string t.
#
# Return the minimum possible length of the string t.
#
# An anagram is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

# Solution
# Hardest part was figuring out what is conacted anagrams

# TC: O(N sqrt N)
# SC: O(N)

class Solution:
    def minAnagramLength(self, s: str) -> int:
        N = len(s)
        d = set()
        for i in range(1,int(sqrt(N)) + 1):
            if N % i == 0:
                d.add(i)
                d.add(N // i)
        # print(d)
        def good(x):
            freq1 = defaultdict(int)
            if x == N:
                return True
            for i in range(x):
                freq1[s[i]] += 1
            i = x
            count = 2
            while i < N:
                freq2 = defaultdict(int)
                for j in range(i,count * x):
                    freq2[s[j]] += 1
                if freq2 != freq1:
                    return False
                count += 1
                i += x
            return True

        for j in sorted(d):
            if good(j):
                return j
        
