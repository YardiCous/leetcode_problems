You are given a directed weighted graph with n nodes labeled from 0 to n - 1.

The graph is represented by a 2D integer array edges, where edges[i] = [ui, vi, ti] indicates a directed edge from node ui to node vi that takes ti seconds to traverse.

You are also given an integer power representing the initial available power, and an integer array cost of length n, where cost[u] represents the power required to forward the signal from node u through any one of its outgoing edges.

You are given two integers source and target.

The signal starts at source at time 0 with power units of power and follows these rules:

    The signal may traverse a directed edge from node u only if the remaining power is at least cost[u].
    No power is consumed when the signal arrives at a node, unless it later leaves that node by traversing another edge.
    When the signal is forwarded from node u, the remaining power is decreased by cost[u] units.
    Traversing an edge edges[i] = [ui, vi, ti] increases the total time by ti seconds.

Return an integer array answer of size 2, where:

    answer[0] is the minimum time required for the signal to reach node target.
    answer[1] is the maximum remaining power among all paths that achieve answer[0].

If the signal cannot reach target, return [-1, -1].

# Solution
# Just 2D Dijsktra overcomplicated it and thought there was Binary Search on answer

# TC: O(E * power Log V)
# SC: O(power * N)


class Solution:
    def minTimeMaxPower(self, N: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        adj_list = defaultdict(list)
        for v,u,t in edges:
            adj_list[v].append((u,t))
        pq = [(0,-power,source)]
        INF = 10 ** 20
        dist = [[INF] * (power + 1) for _ in range(N)]
        dist[source][power] = 0
        while pq:
            c,t,node = heapq.heappop(pq)
            t = -t
            if node == target:
                return [c,t]
            if c > dist[node][t]:
                continue
            for neiNode,neiCost in adj_list[node]:
                new_cost = neiCost + c
                new_t = t - cost[node]
                if new_t >= 0 and new_cost < dist[neiNode][new_t]:
                    heapq.heappush(pq,(new_cost,-new_t,neiNode))
                    dist[neiNode][new_t] = new_cost
        return [-1,-1]
