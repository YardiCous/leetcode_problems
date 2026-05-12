# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.
#
# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

# Solution
# This is a classic sweep line question, basically, append all the start end times in an events List and sort by biggest to smallest
# each start + 1 each end - 1 then sort the people by smallest 

# TC: O(N log N + M log M) where N = number of events and M = number of people
# SC: O(M + N)

from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = []
        for start,end in flowers:
            events.append((start,1))
            events.append((end + 1,-1))
        events.sort()
        # print(f"{events=}") 
        res = [0] * len(people)
        p = [(n,i) for i,n in enumerate(people)]
        p.sort()
        count = 0
        j = 0
        for i in range(len(p)):
            pe = p[i][0]
            idx = p[i][1]
            while j < len(events) and events[j][0] <= pe:
                count += events[j][1]
                j += 1
            res[idx] = count
        return res 
