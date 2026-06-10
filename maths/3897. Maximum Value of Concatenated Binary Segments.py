# You are given two integer arrays nums1 and nums0, each of size n.
#
#     nums1[i] represents the number of '1's in the ith segment.
#     nums0[i] represents the number of '0's in the ith segment.
#
# For each index i, construct a binary segment consisting of:
#
#     nums1[i] occurrences of '1' followed by
#     nums0[i] occurrences of '0'.
#
# You may rearrange the order of these segments in any way. After rearranging, concatenate all segments to form a single binary string.
#
# Return the maximum possible integer value of the concatenated binary string.
#
# Since the result can be very large, return the answer modulo 109 + 7.


# Solution
# Couldn't think of how to sort it, watched Larry video and learn about cmp_to_key, basically we want to sort by segments where we want the best segment for each pair to be at
# the front, so that is the idea. Now i also learn how to calculate binary values without building strings, basically if the number of 1s is 1111 for example, we can get the power 
# of 4 which is 2 ^ 4 == 16 then do a minus 1 to get 15, so that is the idea, so we can precompute the powers to save time and the idea is
# if lets say our binary string is now 111111111000000, and we want to add 1s, we have to shift this string to the left by how many 1s we want to add, so therefore
# everytime we have to * the power of len(ones) and add it then MOD and do the same for zeros without adding because when we add 0s we also need to shift

# TC: O(N log N)
# SC: O(N + M)

from functools import cmp_to_key
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        N = len(nums1)
        MOD = 10 ** 9 + 7
        MAX = 10 ** 4
        mp = [0] * (MAX + 1)
        for i in range(MAX + 1):
            mp[i] = pow(2,i,MOD)
        indexes = [i for i in range(N)]

        def cmp(index1,index2):
            if nums0[index1] == 0 and 0 == nums0[index2]:
                return 0
            if nums0[index1] == 0:
                return -1
            if nums0[index2] == 0:
                return 1
            if nums1[index1] > nums1[index2]:
                return -1
            if nums1[index2] > nums1[index1]:
                return 1
            if nums0[index1] > nums0[index2]:
                return 1
            if nums0[index1] < nums0[index2]:
                return -1
            return 0
        indexes.sort(key=cmp_to_key(cmp))

        res = 0
        for i in range(N):
            zeros,ones = nums0[indexes[i]],nums1[indexes[i]]
            res *= mp[ones]
            res += (mp[ones] - 1)
            res %= MOD
            res *= mp[zeros]
            res %= MOD
        return res

