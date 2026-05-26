# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.
#
# Implement the Graph class:
#
#     Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
#     addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
#     int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.


# Solution
# Just dijkstra

# TC: O(E Log V) 
# SC: O(E)


from collections import defaultdict
from typing import List
import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.N = n
        self.adj_list = defaultdict(list)
        for v,u,cost in edges:
            self.adj_list[v].append((cost,u))

    def addEdge(self, edge: List[int]) -> None:
        v,u,cost = edge
        self.adj_list[v].append((cost,u))

    def shortestPath(self, node1: int, node2: int) -> int:
        minHeap = [(0,node1)]
        visit = set()
        while minHeap:
            cost,node = heapq.heappop(minHeap)
            if node == node2:
                return cost
            if node in visit:
                continue
            visit.add(node)
            for neiCost,neiNode in self.adj_list[node]:
                if neiNode not in visit:
                    heapq.heappush(minHeap,(neiCost + cost,neiNode))
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
