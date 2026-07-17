You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

# Solution
# To get gcd of all pairs first, get the freq of nums, then loop through g where g is 1 to max(nums) where we count for each g how many x can be devided by g using multiple, then after that compute
# all pairs which is (n * (n - 1)) // 2 so now we have the number of pairs but we are overcounting because of mutliples so now we need to remove the multiples for exmaple count of 2 is including
# 4 6 .... to N so now we need to exclude the rest and only include g, then since the number of pairs might get really big, we need to use bisect left to get the idx instead

# TC: O(N Log N)
# SC: O(N)


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        freq = Counter(nums)
        mx = max(nums)
        count = [0] * (mx + 1)
        for g in range(1,mx + 1):
            for m in range(g, mx + 1,g):
                count[g] += freq[m]
        # print(count)
        pairs = [0] * (mx + 1)
        for g in range(1,mx + 1):
            pairs[g] = (count[g] * (count[g] - 1)) // 2
        # print(pairs)
        for g in range(mx,0,-1):
            for m in range(g * 2,mx + 1,g ):
                pairs[g] -= pairs[m]
        s = []
        for i in range(mx + 1):
            if pairs[i] == 0:
                continue
            if s:
                s.append((pairs[i] + s[-1][0],i))
            else:
                s.append((pairs[i],i))
        # print(s)
        res = []
        for i in queries:
            i += 1
            idx = bisect_left(s,(i,))
            # print(s[idx])
            # print(idx)
            res.append(s[idx][1])
        return res
