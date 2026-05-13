# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.
#
# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.
#
# Return the minimum number of moves required to make nums complementary.

# Solution
# Couldn't solve it by myself had to watch larry videos, where he explained that it was a line sweep problem, but even then I couldn't come up with the solution
# Really hard proof to prove but basically the idea is for lets say an input
# nums = [1,2,4,3], limit = 4 
# for the pair (1,3) (2,4) the range of these are, 2 - 7 and 3 - 8 and if you view in a line sweep for every single points
# and since each pair the max you can change is N where N is the length of the array you can minus 1 at every lower bound and increase by 1 at every upper bound
# because you can treat the lower bound as I only took 1 move for this pair and when you go out of the bound, you have to take 2 moves so that is the idea

# Hardest part for this question is the proof that you can do this and covert to a line sweep 

# TC: N log N where N is the length of the input
# SC: O(N)

# For difference array
# TC: O(N + k) where k = limit 
# SC: O(K)
from typing import List
class LineSweep:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        # count = defaultdict(int)
        events = []
        res = N
        # events = []
        for i in range(N // 2):
            a,b = nums[i],nums[N - i - 1]
            events.append((min(a,b) + 1,-1))
            events.append((a + b,-1))
            events.append((a + b + 1,1))
            events.append((max(a,b) + limit + 1,1))
        events.sort(key=lambda x:(x[0],-x[1]))
        # print(events)
        total = N
        res = N
        for _,cost in events:
            total += cost
            # print(total)
            res = min(res,total)
        return res
class DiffArray:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(N // 2):
            a,b = nums[i],nums[N - i - 1]
            diff[2] += 2
            diff[min(a,b) + 1] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[max(a,b) + 1 + limit] += 1
        res = N
        c = 0
        for total in range(2, 2 * limit + 2):
            c += diff[total]
            res = min(res,c)
        return res
