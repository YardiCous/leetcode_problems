# You are given an integer array nums.
#
# You want to construct an array result by repeatedly performing the following operation until nums becomes empty:
#
#     Choose an integer k such that 1 <= k <= len(nums).
#     Compute the MEX of the first k elements of nums.
#     Append this MEX to result.
#     Remove the first k elements from nums.
#
# Return the lexicographically maximum array result that can be obtained after performing the operations.
#
# The MEX of an array is the smallest non-negative integer not present in the array.
#
# An array a is lexicographically greater than an array b if in the first position where a and b differ, array a has an element that is greater than the corresponding element in b. If the first min(a.length, b.length) elements do not differ, then the longer array is the lexicographically greater one.


# Solution
# So first and foremost MEX is a codeforces idea, and basically what is the missing number in this current "window" from 0 .. inf so thats the idea, now
# I didn't solve it, I didn't even understand the question, had to watch larry video, but I get it after, but basically if an example of
# 1 2 3 4 5 0 9 8 7 6, for this question, we want to greedily find from 0 .. inf if they exists in the arr, so if 0 exists go to that location and and search the next
# number exists and in this case it will find that 1 - 9 exists in this suffix, and append 10 thats the idea and the idea uses a queue since queue gives O(1) operation

# TC: O(N)
# SC: O(N)

from collections import defaultdict,deque
from typing import List
class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        N = len(nums)
        count = defaultdict(deque)
        for index,n in enumerate(nums):
            count[n].append(index)
        left = 0
        res = []
        while left < N:
            current = 0
            right = left
            while count[current]:
                while count[current] and count[current][0] < left:
                    count[current].popleft()
                if count[current]:
                    right = max(count[current].popleft(),right)
                else:
                    break
                current += 1
            res.append(current)
            left = right + 1
        return res
