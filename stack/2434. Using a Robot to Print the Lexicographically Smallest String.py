You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

    Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
    Remove the last character of a string t and give it to the robot. The robot will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.


# Solution
# Stack and optimized it to be O(N) instead of O(26N)


class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)
        res = []
        freq = [0] * 26
        curr = []
        for x in s:
            freq[ord(x) - ord("a")] += 1
        i = 0
        for x in s:
            curr.append(x)
            cnt = ord(x) - ord("a")
            freq[cnt] -= 1
            while i < 26 and freq[i] == 0:
                i += 1
            
            while curr and ord(curr[-1]) - ord("a") <= i:
                c = curr.pop()
                res.append(c)
        return "".join(res + curr[::-1])
        
