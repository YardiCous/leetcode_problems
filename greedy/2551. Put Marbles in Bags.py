#  You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.
#
# Divide the marbles into the k bags according to the following rules:
#
#     No bag is empty.
#     If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
#     If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
#
# The score after distributing the marbles is the sum of the costs of all the k bags.
#
# Return the difference between the maximum and minimum scores among marble distributions.

# Solution
# Had to get a nudge from LLM but basically the idea is we have to split the array to k bags right
# Essentially we just need to do K - 1 splits for example if k = 2 one split becomes 2 bags and the idea is every first and last element would be counted twice
# for both of maximum and minimum scores, thus they cancel out each other. Now when we split, the weight to add is N[i] + N[i + 1] for every split
# example    [1,3,| 4,5] if we split here then 3 and 4 gets added, so the idea is add every adajacent pair weights and sort it and for the max
# go from the back and for the minimum go from the front for K - 1 times

# TC: O(P log P) for pairs in nums
# SC: O(P)

from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        nums = []
        for i in range(1,N):
            nums.append(weights[i] + weights[i - 1])
        nums.sort()
        temp_k = k
        big,small = 0,0
        i = 0
        while temp_k > 1:
            small += nums[i]
            i += 1
            temp_k -= 1
        i = len(nums) - 1
        # print(i)
        while k > 1:
            big += nums[i]
            i -= 1
            k -= 1
        return big - small
