You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.

The array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.

    For example, arr = [4, 1, 5, 2, 6, 2] is K-increasing for k = 2 because:
        arr[0] <= arr[2] (4 <= 5)
        arr[1] <= arr[3] (1 <= 2)
        arr[2] <= arr[4] (5 <= 6)
        arr[3] <= arr[5] (2 <= 2)
    However, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).

In one operation, you can choose an index i and change arr[i] into any positive integer.

Return the minimum number of operations required to make the array K-increasing for the given k.


# Solution
# This is a problem introducing longest non-decreasing subsequence

# TC: O(N log N)
# SC: O(N)
class Solution:
    def kIncreasing(self, nums: List[int], k: int) -> int:
        N = len(nums)
        INF = 10 ** 20
        res = 0
        s = defaultdict(list)
        for i in range(N):
            s[i % k].append(nums[i])
        # print(s)
        for i in range(k):
            arr = s[i]
            M = len(arr)
            L = []
            for j in range(M):
                x = arr[j]
                index = bisect.bisect_right(L,x)
                if index == len(L):
                    L.append(0)
                L[index] = x
            res += M - len(L)
        return res
