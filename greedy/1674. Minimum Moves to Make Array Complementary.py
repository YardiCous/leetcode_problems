# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.
#
# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.
#
# Return the minimum number of moves required to make nums complementary.

# Solution 
# Sweep Line or Difference Array
# Hardest part was coming up with the intuition to use Sweep Line or Difference Array had to watch larry and use LLM

# TC: O(N log N) for sweep line and O(N + K) where K = limit for Difference Array
# SC: O(N) for sweep line and O(K) for difference array
from typing import List
class DifferenceArray:
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
        # print(diff)
        res = N
        c = 0
        for total in range(2, 2 * limit + 2):
            c += diff[total]
            res = min(res,c)
        return res
class SweepLine:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N = len(nums)
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
        total = N
        res = N
        for num,cost in events:
            total += cost
            # print(total)
            res = min(res,total)
        return res
