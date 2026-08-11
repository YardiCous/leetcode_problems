We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


# Solution
# 2 Coloring Greedy BFS/DFS problem, if a problem requires spliting into 2 groups, use this algorithm

# TC: O(V + E)
# SC: O(V + E)

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for a,b in dislikes:
            a -= 1
            b -= 1
            adj_list[a].append(b)
            adj_list[b].append(a)
        color = [-1] * N
        for i in range(N):
            if color[i] != -1:
                continue
            color[i] = 0
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for neiNode in adj_list[node]:
                    if color[neiNode] == -1:
                        q.append(neiNode)
                        color[neiNode] = not color[node]
                    elif color[neiNode] == color[node]:
                        return False
        return True
