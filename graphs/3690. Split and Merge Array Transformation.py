# You are given two integer arrays nums1 and nums2, each of length n. You may perform the following split-and-merge operation on nums1 any number of times:
#
#     Choose a subarray nums1[L..R].
#     Remove that subarray, leaving the prefix nums1[0..L-1] (empty if L = 0) and the suffix nums1[R+1..n-1] (empty if R = n - 1).
#     Re-insert the removed subarray (in its original order) at any position in the remaining array (i.e., between any two elements, at the very start, or at the very end).
#
# Return the minimum number of split-and-merge operations needed to transform nums1 into nums2.

# Solution
# Accidentally click on topics and saw BFS and immediately knew how to do it as constraints are small, so dk how to few about this


# Solution
# TC: O(N ^ 4)
# SC: O(N ^ 4)

class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        q = deque()
        q.append((0,nums1[:]))
        visit = set()
        visit.add(tuple(nums1[:]))
        while q:
            cost,nums = q.popleft()
            if nums == nums2:
                return cost
            for i in range(N):
                for j in range(N):
                    subarray = nums[i:j + 1]
                    remain = nums[:i] + nums[j + 1:]
                    # print(subarray)
                    # print(remain)
                    for k in range(len(remain)):
                        new = remain[:k] + subarray + remain[k:]
                        # print(new)
                    
                        if new == nums2:
                            return cost + 1
                        if tuple(new) not in visit:
                            q.append((cost + 1,new))
                            visit.add(tuple(new))
        return -1
