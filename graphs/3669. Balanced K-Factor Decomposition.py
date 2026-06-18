# Given two integers n and k, split the number n into exactly k positive integers such that the product of these integers is equal to n.
#
# Return any one split in which the maximum difference between any two numbers is minimized. You may return the result in any order.

# Solution
# Kind of cheated in the sense I saw k is <= 5 and I knew I can do brute force 

# TC: O(N * Sqrt(N))
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        q = deque()
        q.append([n])
        visit = set()
        s = [n]
        visit.add(tuple(s))
        def factors(x):
            res = set()
            for i in range(1,int(x ** 0.5) + 1):
                if x % i == 0:
                    res.add(i)
            return res
        res = 10 ** 20
        r = []
        while q:
            # print(q)
            nums = q.popleft()
            for i,num in enumerate(nums):
                f = factors(num)
                for j in f:
                    new = []
                    new.append(j)
                    new.append(num // j)
                    new = nums[:i] + new + nums[i + 1:]
                    if len(new) <= k and tuple(new) not in visit:
                        if len(new) == k:
                            mx,mn = max(new),min(new)
                            if mx - mn < res:
                                res = mx - mn
                                r = new[:]
                        q.append(new[:])
                        visit.add(tuple(new))
        return r
