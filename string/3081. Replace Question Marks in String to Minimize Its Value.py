You are given a string s. s[i] is either a lowercase English letter or '?'.

For a string t having length m containing only lowercase English letters, we define the function cost(i) for an index i as the number of characters equal to t[i] that appeared before it, i.e. in the range [0, i - 1].

The value of t is the sum of cost(i) for all indices i.

For example, for the string t = "aab":

    cost(0) = 0
    cost(1) = 1
    cost(2) = 0
    Hence, the value of "aab" is 0 + 1 + 0 = 1.

Your task is to replace all occurrences of '?' in s with any lowercase English letter so that the value of s is minimized.

Return a string denoting the modified string with replaced occurrences of '?'. If there are multiple strings resulting in the minimum value, return the one.


# Solution
# Just ad hoc but i couldn't come up with the lexicographically smallest string 

# TC:O(N)
# SC:O(N)

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        N = len(s)
        freq = [0] * 26
        chosen = [0] * 26
        count = 0
        res = list(s)
        for char in s:
            if char == "?":
                count += 1
                continue
            val = ord(char) - ord("a")
            freq[val] += 1
        if count == 0:
            return "".join(res)
        INF = 10 ** 20
        while count:
            mn = INF
            index = -1
            for j in range(26):
                if freq[j] < mn:
                    mn = freq[j]
                    index = j
            freq[index] += 1
            count -= 1
            chosen[index] += 1
        j = 0
        for i in range(N):
            if res[i] == "?":
                while chosen[j] == 0:
                    j += 1
                res[i] = chr(j + ord("a"))
                chosen[j] -= 1
        return "".join(res)
