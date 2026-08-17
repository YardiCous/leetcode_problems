You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.

You are also given an integer start, representing the floor where the elevator begins, and an integer array requests, where requests[i] is a floor that the elevator is requested to reach. All floors in requests are distinct.

At time 0, the elevator is on floor start, and all requests are made simultaneously.

During each second before all requests are fulfilled, the elevator moves exactly one floor, either up or down. A request is fulfilled instantly when the elevator reaches its requested floor. If start appears in requests, that request is fulfilled at time 0.

For each second that a request remains unfulfilled, you receive 1 penalty. Equivalently, a request fulfilled at time t contributes t to the total penalty.

Return the minimum total penalty required to fulfill all requests.

# Solution
# Interval DP with a pos trick

# TC: O(N ^ 2)
# SC: O(N ^ 2)


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        s = set(requests)
        s.add(start)
        requests = list(s)
        requests.sort()
        N = len(requests)
        INF = 10 ** 20
        @cache
        def dp(left,right,pos):
            if left == 0 and right == N - 1:
                return 0
            res = INF
            remain = left + (N - right - 1)
            if left > 0:
                val = 0
                if pos:
                    val = requests[right] - requests[left - 1]
                else:
                    val = requests[left] - requests[left - 1]
                res = min(res,dp(left - 1,right,0) + val * remain)
            if right + 1 < N:
                val = 0
                if pos:
                    val = requests[right + 1] - requests[right]
                else:
                    val = requests[right + 1] - requests[left]
                res = min(res,dp(left,right + 1,1) + val * remain)
            return res
        idx = requests.index(start)
        r = dp(idx,idx,0)
        dp.cache_clear()
        return r
