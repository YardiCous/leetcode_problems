# You are given a 0-indexed array nums containing n integers.
#
# At each second, you perform the following operation on the array:
#
#     For every index i in the range [0, n - 1], replace nums[i] with either nums[i], nums[(i - 1 + n) % n], or nums[(i + 1) % n].
#
# Note that all the elements get replaced simultaneously.
#
# Return the minimum number of seconds needed to make all elements in the array nums equal.

# Solution
# The idea is to store all common indexes of nums[i] and loop through the indexes
# for each index pair the maximum time will be (b - a) // 2 and the reason is because 7 _ _ _ _ _ _ _ 7 , it will take 4 seconds because it that is the amount
# of time it will take to reach the middle of the difference of the 2 indexes, and since it is a circular array, we have to add append index[0] at the back but 
# it is index[0] + N since it is circular.

# TC: O(N * D) N is length of nums and D is number of distinct elements in nums
# SC: O(N)

from typing import List
from collections import defaultdict
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        N = len(nums)
        res = 10 ** 20
        # nums_set = set(nums)
        indexes = defaultdict(list)
        for i,n in enumerate(nums):
            indexes[n].append(i)
        def go(target):
            index = indexes[target]
            total = 0
            index.append(index[0] + N)
            # print(index)
            for i in range(1,len(index)):
                total = max(total,abs(index[i] - index[i - 1]) // 2)
            return total
        for j in indexes.keys():
            res = min(go(j),res)
        return res
