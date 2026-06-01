# There is a network of n servers, labeled from 0 to n - 1. You are given a 2D integer array edges, where edges[i] = [ui, vi] indicates there is a message channel between servers ui and vi, and they can pass any number of messages to each other directly in one second. You are also given a 0-indexed integer array patience of length n.
#
# All servers are connected, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.
#
# The server labeled 0 is the master server. The rest are data servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers optimally, so every message takes the least amount of time to arrive at the master server. The master server will process all newly arrived messages instantly and send a reply to the originating server via the reversed path the message had gone through.
#
# At the beginning of second 0, each data server sends its message to be processed. Starting from second 1, at the beginning of every second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:
#
#     If it has not, it will resend the message periodically. The data server i will resend the message every patience[i] second(s), i.e., the data server i will resend the message if patience[i] second(s) have elapsed since the last time the message was sent from this server.
#     Otherwise, no more resending will occur from this server.
#
# The network becomes idle when there are no messages passing between servers or arriving at servers.
#
# Return the earliest second starting from which the network becomes idle.

# Solution
# Just a bfs but I need to remember the formula which is time - 1 // p * p the reason we -1 is because we want the last possible time when an email has been sent and since it comes
# in intervals of p -1 gets the last time when it send out
# TC: O(N)
# SC: O(N)

from collections import defaultdict,deque
from typing import List
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        q = deque()
        q.append((0,0))
        visit = set()
        res = 0
        visit.add(0)
        while q:
            node,dist = q.popleft()
            if node != 0:
                p = patience[node]
                time = dist * 2
                if time > p:
                    amount = (time - 1) // p * p
                    res = max(res,amount + time + 1)
                else:
                    res = max(res,time + 1)
            for neiNode in adj_list[node]:
                if neiNode not in visit:
                    q.append((neiNode,dist + 1))
                    visit.add(neiNode)
        return res
                    
