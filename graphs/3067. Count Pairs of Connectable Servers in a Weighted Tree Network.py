You are given an unrooted weighted tree with n vertices representing servers numbered from 0 to n - 1, an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional edge between vertices ai and bi of weight weighti. You are also given an integer signalSpeed.

Two servers a and b are connectable through a server c if:

    a < b, a != c and b != c.
    The distance from c to a is divisible by signalSpeed.
    The distance from c to b is divisible by signalSpeed.
    The path from c to b and the path from c to a do not share any edges.

Return an integer array count of length n where count[i] is the number of server pairs that are connectable through the server i.

# Solution
# DFS and I learn today how to count a path in a tree without using it as a parameter and also going to each path in O(N) was quite cool too
# needed help for the path part, did not do it before and I thought it will be O(N ^2)

# TC: O(N ^ 2)
# SC: O(N)

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        N = len(edges) + 1
        adj_list = defaultdict(list)
        for v,u,w in edges:
            adj_list[v].append((u,w))
            adj_list[u].append((v,w))
        
        def go(root):
            total = 0
            if len(adj_list[root]) == 1:
                return 0
            freq = defaultdict(int)
            def dfs(node,par,idx):
                nonlocal total
                if total % signalSpeed == 0:
                    freq[idx] += 1
                for neiNode,neiCost in adj_list[node]:
                    if neiNode == par:
                        continue
                    total += neiCost
                    dfs(neiNode,node,idx)
                    total -= neiCost
            for i,(neiNode,neiCost) in enumerate(adj_list[root]):
                total = neiCost
                dfs(neiNode,root,i)
            
            curr = 0
            res = 0
            if len(freq) == 1:
                return 0
            for x in freq.values():
                res += curr * x
                curr += x
            return res
        res = []
        for i in range(N):
            res.append(go(i))
        return res
