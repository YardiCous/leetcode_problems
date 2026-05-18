# Given an array of integers arr, you are initially positioned at the first index of the array.
#
# In one step you can jump from index i to index:
#
#     i + 1 where: i + 1 < arr.length.
#     i - 1 where: i - 1 >= 0.
#     j where: arr[i] == arr[j] and i != j.
#
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.

# Solution just simple bfs with 2 visited sets, 1 for val and 1 for index

# TC: O(N)
# SC: O(N)

from typing import List
from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        jumps = defaultdict(list)
        for i,n in enumerate(arr):
            jumps[n].append(i)
        q = deque()
        q.append((0,0))
        visit = [False] * N
        visit[0] = True
        visited = set()
        while q:
            index,cost = q.popleft()
            if index == N - 1:
                return cost
            for dx in [-1,1]:
                new_idx = index + dx
                if 0 <= new_idx < N and visit[new_idx] == False:
                    q.append((new_idx,cost + 1))
                    visit[new_idx] = True
            val = arr[index]
            if val not in visited:
                visited.add(val)
                for jump_index in jumps[val]:
                    if visit[jump_index] == False:
                        q.append((jump_index,cost + 1))
                        visit[jump_index] = True
        return -1 
