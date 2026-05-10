#You are given an integer n and an integer array prices of length n, where prices[i] is the price of apples at shop i.

# You are also given a 2D integer array roads, where roads[i] = [ui, vi, costi, taxi] represents a bidirectional road:
#
#     ui and vi are the shops connected by the road.
#     costi is the cost to travel the road without carrying apples.
#     taxi is the multiplier applied to costi when traveling with apples.
#
# For each shop i, you can either:
#
#     Buy apples locally at shop i for prices[i].
#     Travel empty to any shop j using any number of roads, buy apples for prices[j], and return to shop i while carrying apples, paying cost * tax on each road used for the return trip.
#
# The forward path, where you travel empty, and the return path may be different.
#
# Return an integer array ans of length n, where ans[i] is the minimum total cost to buy apples starting from shop i.

# Solution, since constraints, I were n <= 1000 and edges <= 2000 I knew can just do djikstra from every node since it will be V * E Log V which is fine
# I got stuck first, thought I can use a BFS but I just didn't trust my instinct to just djikstra, next implementaion portion, sort of misred question wasn't able to finish the question.
# In the end had to ask LLM and got back working code, not that different from my previous version
# What did I learn first, read the question and constraints properly too many ACs due to careless.
# Also, if something is visited in djikstra, using dist might be helpful instead of visit set() makes implementing easier, and less likelyhood of WA
# Solution Portion
# Build an adjanency list to build the graph edges, do a dijkstra from every node treating it as a source node, then calculate the minimum cost to buy an apple

#TC: V * (V * E) log V
#SC: O(E)



# Implementation
import heapq
from collections import defaultdict
from typing import List
class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        inf = float("inf")
        adj_list = defaultdict(list)
        for v,u,cost,tax in roads:
            adj_list[v].append((u,cost,tax))
            adj_list[u].append((v,cost,tax))
        def djikstra(src):
            minHeap = [(0,src,0)]
            dist = [[inf] * 2 for _ in range(n)]
            dist[src][0] = 0
            while minHeap:
                cost,node,carry = heapq.heappop(minHeap)
                if cost > dist[node][carry]:
                    continue
                if node == src and carry:
                    return cost
                if carry == 0:
                    new_cost = prices[node] + cost
                    if new_cost < dist[node][1]:
                        dist[node][1] = new_cost
                        heapq.heappush(minHeap,(new_cost,node,1))
                for neiNode,neiCost,neiTax in adj_list[node]:
                    move_cost = (neiCost * neiTax if carry else neiCost)
                    new_cost = move_cost + cost
                    if new_cost < dist[neiNode][carry]:
                        dist[neiNode][carry] = new_cost
                        heapq.heappush(minHeap,(new_cost,neiNode,carry)) 
            return 0
        return [djikstra(i) for i in range(n)]


            
