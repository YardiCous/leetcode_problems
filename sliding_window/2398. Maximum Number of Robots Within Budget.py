You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of consecutive robots you can run such that the total cost does not exceed budget.


# Solution
# Sliding Window with Monotonic increasing deque

# TC: O(N)
# SC: O(N)

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        N = len(chargeTimes)
        res = 0
        left = 0
        total = 0
        mx = deque()
        for right in range(N):
            while mx and chargeTimes[mx[-1]] < chargeTimes[right]:
                mx.pop()
            total += runningCosts[right]
            mx.append(right)
            while mx and chargeTimes[mx[0]] + ((right - left + 1) * total) > budget:
                if mx[0] == left:
                    mx.popleft()
                total -= runningCosts[left]
                left += 1
            res = max(res,right - left + 1)
        return res
