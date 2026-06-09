# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Solution
# Just dijkstra

# TC: O(E log V)
# SC: O(E)


from collections import defaultdict
from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_list = defaultdict(list)
        for x1,y1 in points:
            for x2,y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                cost = abs(x1 - x2) + abs(y1 - y2)
                adj_list[(x1,y1)].append((cost,x2,y2))
                adj_list[(x2,y2)].append((cost,x1,y1))

        minHeap = [(0,points[0][0],points[0][1])]
        res = 0
        visit = set()

        while len(visit) < N:
            cost,x,y = heapq.heappop(minHeap)
            if (x,y) in visit:
                continue
            res += cost
            visit.add((x,y))
            for neiCost,neiX,neiY in adj_list[(x,y)]:
                if (neiX,neiY) not in visit:
                    heapq.heappush(minHeap,(neiCost,neiX,neiY))
        return res
