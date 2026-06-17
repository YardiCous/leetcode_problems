# You are given two strings s and target, both having length n, consisting of lowercase English letters.
#
# Return the lexicographically smallest of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.
#
# A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

# Solution
# I came up with an idea, but I did not know how to come up with a good solution to check when j >= t had to ask LLM for help for that part but the main part I had the idea
# Had to think of backtracking but I did not

# TC: O(N * 26)
# SC: O(1)


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        N = len(target)
        count = [0] * 26
        for char in s:
            count[(ord(char) - ord("a"))] += 1
        best_i,best_j,best_count = -1,-1,None
        for i in range(N):
            t = ord(target[i]) - ord("a")
            for j in range(t + 1,26):
                if count[j] == 0:
                    continue
                temp = count[:]
                temp[j] -= 1
                best_i,best_j,best_count = i,j,temp
                break
            if count[t] > 0:
                count[t] -= 1
            else:
                break
        if best_i == -1:
            return ""
        res = list(target[:best_i])
        res.append(chr(best_j + ord("a")))
        for i in range(26):
            while best_count[i] > 0:
                best_count[i] -= 1
                res.append(chr(i + ord("a")))
        return "".join(res)
