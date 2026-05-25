# You are given an integer array nums of length n, where nums is a of the integers from 0 to n - 1.
#
# You may perform only the following operations:
#
#     Reverse the entire array.
#     Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
#
# Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

# Solution
# Basically first what is impossible, impossible basically is if you loop through N and count the number of drops,
# if number of drops are bigger then 1 then it is impossible but for this problem, have to test both increasing and decreasing since you can reverse the array
# Next, the two cases for each, for first count <= 1, the two cases are first rotate left all the way depending on the biggest number, or reverse the array, rotate till the biggest 
# number is at first index then reverse. The same for second count just that theres no need to reverse twice, as it is already reversed.

# Formula was k = (index + 1) % N, this indicates for array like [0,1,2,3,4,5] since 5 is the at the end, we want to return 0 because theres no need to do anything
# second case was N - k + 2, the 2 is for the reverses we have to do and N - k basically says, how many rotates does it take to move the biggest number to the first index
# For second count, first case is index + 1, just how many times we need to rotate biggest num to the first index and rotate
# second case is reverse first then rotate

#TC: O(N)
#SC: O(1)

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        count,second_count = 0,0
        for i in range(N):
            if nums[i] > nums[(i + 1) % N]:
                count += 1
        for i in range(N):
            if nums[i] < nums[(i + 1) % N]:
                second_count += 1
        
        if count > 1 and second_count > 1:
            return -1
        index = nums.index(max(nums))
        k = (index + 1) % N
        if count <= 1:
            # Two cases, rotate left all the way or reverse rotate reverse
            return min(k,2 + N - k)
        else:
            # Two cases, rotate left all the way and reverse or reverse rotate
            return min(index + 1,N - index + 1)



