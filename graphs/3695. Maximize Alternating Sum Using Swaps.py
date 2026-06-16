# You are given an integer array nums.
#
# You want to maximize the alternating sum of nums, which is defined as the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...
#
# You are also given a 2D integer array swaps where swaps[i] = [pi, qi]. For each pair [pi, qi] in swaps, you are allowed to swap the elements at indices pi and qi. These swaps can be performed any number of times and in any order.
#
# Return the maximum possible alternating sum of nums.


# Solution
# Just union find + SortedList

# TC: O(N Log N)
# SC: O(N)

class UF:
    def __init__(self,N):
        self.par = list(range(N))
        self.size = [1] * N
    def find(self,idx):
        if self.par[idx] != idx:
            self.par[idx] = self.find(self.par[idx])
        return self.par[idx]
    def union(self,p1,p2):
        u1,u2 = self.find(p1),self.find(p2)
        if u1 == u2:
            return False
        if self.size[u1] > self.size[u2]:
            self.size[u1] += self.size[u2]
            self.par[u2] = u1
        else:
            self.size[u2] += self.size[u1]
            self.par[u1] = u2
        return True 
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        N = len(nums)
        dsu = UF(N)
        for v,u in swaps:   
            dsu.union(v,u)
        # print(dsu.par)
        root_to_index = defaultdict(SortedList)
        for i in range(N):
            root = dsu.find(i)
            root_to_index[root].add(nums[i])
        # print(root_to_index)
        res = 0
        for i in range(N):
            root = dsu.find(i)
            arr = root_to_index[root]
            if i % 2 == 0:
                val = arr.pop(-1)
                res += val
            else:
                val = arr.pop(0)
                res -= val
        return res
