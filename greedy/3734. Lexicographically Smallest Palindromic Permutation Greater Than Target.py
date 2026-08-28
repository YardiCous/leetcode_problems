You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the string that is both a of s and strictly greater than target. If no such permutation exists, return an empty string.


# Solution
# TC: O(N ^ 2)
# SC: O(N)

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        N = len(s)
        freq = [0] * 26
        for x in s:
            freq[ord(x) - ord("a")] += 1
        middle = None
        if N % 2:
            count = 0
            for i in range(26):
                if freq[i] % 2:
                    count += 1
                    middle = chr(ord("a") + i)
                    if count > 1:
                        return ""
        else:
            for x in freq:
                if x % 2:
                    return ""
        res = []

        for i in range(N // 2):
            x = target[i]
            c = ord(x) - ord("a")
            if freq[c] > 1:
                freq[c] -= 2 
                temp = [x]
                for j in range(25,-1,-1):
                    temp.extend([chr(ord("a") + j)] * (freq[j] // 2))
                if N % 2:
                    temp = res + temp + [middle]
                    t = len(temp)
                    temp = temp + temp[:t - 1][::-1]
                    # print(temp)
                    if "".join(temp) > target:
                        res.append(x)
                        continue
                else:
                    temp = res + temp
                    temp = temp + temp[::-1]
                    # print(temp)
                    if "".join(temp) > target:
                        res.append(x)
                        continue
                freq[c] += 2
            good = False
            for j in range(c + 1,26):
                if freq[j] > 1:
                    good = True
                    res.append(chr(j + ord("a")))
                    freq[j] -= 2
                    break
            if good:
                break
            else:
                return ""
        # print(res)
        t = len(res)
        j = 0
        while len(res) < (N // 2):
            if freq[j] > 0:
                res.extend([chr(ord("a") + j)] * (freq[j] // 2))
            j += 1

        if N % 2:
            res.append(middle)
            # print(res)
            k = len(res)
            res = res + res[:k - 1][::-1]
            r = "".join(res)
            return r if r > target else ""
        else:
            # print(res)
            res = res + res[::-1]
            r = "".join(res)
            return r if r > target else ""


