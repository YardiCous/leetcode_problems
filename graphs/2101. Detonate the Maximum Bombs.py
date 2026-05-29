# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
#
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
#
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
#
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Solution
# Hard part is the math formula for the radius thats all then just a BFS would do

#TC O(N ^ 2)
#SC O(N)

from collections import deque,defaultdict
from typing import List
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        N = len(bombs)

        for i in range(N):
            x1,y1,r1 = bombs[i]
            for j in range(N):
                if i != j:
                    x2,y2,r2 = bombs[j]
                    if r1 * r1 >= (x2 - x1) ** 2 + (y2 - y1) ** 2:
                        adj_list[i].append(j)
        def go(node):
            q = deque()
            count = 0
            q.append(node)
            visit = set()
            while q:
                index = q.popleft()
                if index in visit:
                    continue
                visit.add(index)
                count += 1
                for neiNode in adj_list[index]:
                    if neiNode not in visit:
                        q.append(neiNode)
            return count
        res = 0
        for i in range(N):
            res = max(res,go(i))
        return res
