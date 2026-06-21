# You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
#
# You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.
#
# Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

# Solution
# Dijkstra

# TC: O(N log N * k)
# SC: O(N * k)
class Solution:
    def shortestPath(self, N: int, edges: List[List[int]], labels: str, k: int) -> int:
        INF = 10 ** 20
        adj_list = defaultdict(list)
        mx = 0
        for v,u,w in edges:
            adj_list[v].append((u,w))
            mx = max(mx,w)  
        minHeap = [(0,0,0)]
        visit = set()
        while minHeap:
            cost,node,consec = heapq.heappop(minHeap)
            if node in visit:
                continue
            if node == N - 1:
                return cost
            visit.add(node)
            for neiNode,neiCost in adj_list[node]:
                if neiNode not in visit:
                    if labels[neiNode] != labels[node]:
                        heapq.heappush(minHeap,(cost + neiCost,neiNode,0))
                    elif labels[neiNode] == labels[node]:
                        if consec + 1 < k:
                            heapq.heappush(minHeap,(cost + neiCost,neiNode,consec + 1))
            

        return -1
