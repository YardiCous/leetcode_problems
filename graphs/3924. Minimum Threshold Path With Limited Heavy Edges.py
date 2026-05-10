# There is an undirected weighted graph with n nodes labeled from 0 to n - 1.
#
# The graph is represented by a 2D integer array edges, where each edge edges[i] = [ui, vi, w​​​​​​​i] indicates that there is an undirected edge between nodes ui and vi with weight w​​​​​​​i.
#
# You are also given integers source, target and k.
#
# A threshold value determines whether an edge is considered light or heavy:
#
#     An edge is light if its weight is less than or equal to threshold.
#
#     An edge is heavy if its weight is greater than threshold.
#
# A path from source to target is valid if it contains at most k heavy edges.
#
# Return the minimum integer threshold such that at least one valid path exists from source to target. If no such path exists, return -1.

# Solution
# Since they didn't give a threshold number, I just used binary search to generate that for me
# But again I implemented BFS instead of Djikstra because I thought it didnt matter
# AC 4 times, also buggy ass website but wasn't the most difficult Q4 so 
# I also did 0-1 bfs something new I learned while looking at the solutions tab
# 0-1 BFS is basically appending to the front if we want it reach earlier in this case we can because if there we want the least amount of heavy weights possible

# TC: O(log n * (V + E) log V) for Djikstra, O(log N * (V + E)) for 0-1 BFS
# SC: O(V + E)
import heapq
from typing import List
from collections import deque,defaultdict
# For 0-1 BFS
class Solution1:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        if len(edges) == 0:
            return -1
        adj_list = defaultdict(list)
        for v,u,w in edges:
            adj_list[v].append((u,w))
            adj_list[u].append((v,w))
        def good(threshold):
            q = deque()
            q.append((0,0,source))
            visit = set()
            while q:
                weight,count,node = q.popleft()
                if node == target:
                    return count <= k
                if node in visit:
                    continue
                visit.add(node)
                for neiNode,neiWeight in adj_list[node]:
                    new_weight = (1 if neiWeight> threshold else 0)
                    if new_weight:
                        q.append((1,count + 1,neiNode))
                    else:
                        q.appendleft((0,count,neiNode))
            return False
        left,right = 0, 10 ** 9 + 1
        res = -1
        while left < right:
            mid = left + (right - left) // 2
            if good(mid):
                right = mid
                res = mid
                # print(res)
            else:
                left = mid + 1
        return res
# For Djikstra
class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
        if len(edges) == 0:
            return -1
        adj_list = defaultdict(list)
        for v,u,w in edges:
            adj_list[v].append((u,w))
            adj_list[u].append((v,w))
        def good(threshold):
            minHeap = [(0,source)]
            visit = set()
            while minHeap:
                count,node = heapq.heappop(minHeap)
                if node == target:
                    return count <= k
                if node in visit:
                    continue
                visit.add(node)
                for neiNode,neiWeight in adj_list[node]:
                    new_count = count + (1 if neiWeight > threshold else 0)
                    if neiNode not in visit:
                        heapq.heappush(minHeap,(new_count,neiNode))
            return False
        left,right = 0, 10 ** 9 + 1
        res = -1
        while left < right:
            mid = left + (right - left) // 2
            if good(mid):
                right = mid
                res = mid
                # print(res)
            else:
                left = mid + 1
        return res
