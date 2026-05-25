# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
#
#     i + minJump <= j <= min(i + maxJump, s.length - 1), and
#     s[j] == '0'.
#
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Solution
# Use farthest to prune
# TC: O(N)
# SC: O(N)


class SlidingWindow:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N = len(s)
        visit = [False] * N
        visit[0] = True
        total = 0
        for i in range(N):
            if i - minJump >= 0 and visit[i - minJump]:
                total += 1
            if i - maxJump - 1 >= 0 and visit[i - maxJump - 1]:
                total -= 1
            if s[i] == "0" and total > 0:
                visit[i] = True
        return visit[-1]

from collections import deque
class BFS:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        N = len(s)
        visit = [False] * N
        visit[0] = True
        q = deque()
        q.append(0)
        farthest = 0
        while q:
            index = q.popleft()
            left,right = max(index + minJump, farthest),min(N - 1,index + maxJump)
            for j in range(left,right + 1):
                if visit[j] == False and s[j] == "0":
                    q.append(j)
                    visit[j] = True
            farthest = right
        return visit[-1]


