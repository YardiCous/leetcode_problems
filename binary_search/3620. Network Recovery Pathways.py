# You are given a directed acyclic graph of n nodes numbered from 0 to n − 1. This is represented by a 2D array edges of length m, where edges[i] = [ui, vi, costi] indicates a one‑way communication from node ui to node vi with a recovery cost of costi.
#
# Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.
#
# A path from 0 to n − 1 is valid if:
#
#     All intermediate nodes on the path are online.
#     The total recovery cost of all edges on the path does not exceed k.
#
# For each valid path, define its score as the minimum edge‑cost along that path.
#
# Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.


# Solution
# Binary search on answer + Dijsktra, I misread the question and I did not think of states, definitely need to come back on this

# TC: O(N log N)
# SC: O(N)

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        N = len(online)
        adj_list = defaultdict(list)
        mx = 0
        for v,u,cost in edges:
            adj_list[v].append((u,cost))
            mx = max(cost,mx)
        
        INF = 10 ** 20
        def good(target):
            dist = [INF] * N
            dist[0] = 0
            minHeap = [(0,0)]
            while minHeap:
                # print(minHeap)
                total,node = heapq.heappop(minHeap)
                if node == N - 1:
                    return total <= k
                if total > dist[node]:
                    continue
                for neiNode,neiCost in adj_list[node]:
                    if online[neiNode] and neiCost >= target:    
                        if dist[neiNode] > neiCost + total:
                            dist[neiNode] = neiCost + total
                            heapq.heappush(minHeap,(neiCost + total,neiNode))
            return False
    
        left,right = 0,mx + 1
        res = -1
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                left = mid + 1
                res = mid
            else:
                right = mid
        return res
