# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
#
# Notice that you can not jump outside of the array at any time.

# Solution, just standard BFS 

# TC: O(N)
# SC: O(N)

from collections import deque
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        N = len(arr)
        q.append(start)
        seen = set()
        seen.add(start)
        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            if node - arr[node] >= 0 and node - arr[node] not in seen:
                q.append(node - arr[node])
                seen.add(node- arr[node])
            if node + arr[node] < N and node + arr[node] not in seen:
                q.append(node + arr[node])
                seen.add(node + arr[node])
        return False
