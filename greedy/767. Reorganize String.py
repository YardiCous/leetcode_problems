# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.

# Solution
# Basically to inter leave the string think of impossible first
# _ _ _ _ _ <- here only 3 possible slots for the max character same with _ _ _ _ _ _ <- only three slots for max character so 
# check if the max character exceeds (N + 1) // 2 if so return ""
# next, interleave using heap, my first time writing this kind of heap, basically save the current popped element and push after the next pop
# as we want inter leaved for example vvvlo, pop v and save it so we don't push yet, pop l then push v again to use it the next time.

# TC: O(N log N)
# SC: O(N)

import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        inf = 10 ** 20
        count = Counter(s)
        m = max(count.values())
        if m > (N + 1) // 2:
            return ""
        maxH = []
        for char,counter in count.items():
            heapq.heappush(maxH,(-counter,char))
        res = ""
        temp = [inf,"a"]
        while maxH:
            val,char = heapq.heappop(maxH)
            res += char
            if temp[0] != inf:
                heapq.heappush(maxH,(temp[0],temp[1]))
                temp[0] = inf
            if val + 1 != 0:
                temp[0],temp[1] = val + 1,char
        return res
