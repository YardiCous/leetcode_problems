# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.
#
# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.
#
#     For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
#
# Return an integer array answer where answer[i] is the answer to the ith query.

# Solution
# The idea is basically do a prefix sum of plates and append all plates to a List and since we are going from left to right it will be sorted
# After that can do bisect left and right to find the nearest candles. I had issues when it came to the bounding checks and the proof that if left idx is bigger then right idx
# append 0, spend about 10 minutes trying to figure it out.

# TC: O(N log N)
# SC: O(N)

from typing import List
import bisect
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        plates = []
        prefix = [0] * (N + 1)
        for i in range(N):
            if s[i] == "*":
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
            
            if s[i] == "|":
                plates.append(i)
        res = []
        for start,end in queries:
            left_idx = bisect.bisect_left(plates,start)
            right_idx = bisect.bisect_right(plates,end) - 1
            if left_idx >= len(plates) or right_idx < 0 or left_idx >= right_idx:
                res.append(0)
                continue
            right = plates[right_idx]
            left = plates[left_idx]
            res.append(prefix[right + 1] - prefix[left])
        return res
