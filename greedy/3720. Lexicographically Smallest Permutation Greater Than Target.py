You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

# Solution
# TC: O(N ^ 2)


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        N = len(s)
        freq = [0] * 26
        for x in s:
            freq[ord(x) - ord("a")] += 1
        res = []

        for i in range(N):
            x = target[i]
            c = ord(x) - ord("a")
            found = False
            if freq[c] > 0:
                freq[c] -= 1
                test = [x]
                for k in range(25,-1,-1):
                    y = chr(ord("a") + k)
                    test.extend([y] * freq[k])
                if "".join(res + test) > target:
                    res.append(x)
                    continue
                freq[c] += 1
            for j in range(c + 1,26):
                if freq[j] > 0:
                    freq[j] -= 1
                    found = True
                    res.append(chr(ord("a") + j))
                    break
            if found:
                break
            else:
                return ""
        for i in range(26):
            c = chr(ord("a") + i)
            res.extend([c] * freq[i])
        new_s = "".join(res)
        # print(new_s)
        if new_s > target:
            return new_s
