You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

    Choose an integer i such that 1 <= i < n and nums[i] > 0.
    Decrease nums[i] by 1.
    Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        N = len(nums)
        def good(target):
            arr = nums[:]
            for i in range(N - 1,0,-1):
                if arr[i] <= target:
                    continue
                diff = arr[i] - target
                arr[i] = target
                arr[i - 1] += diff
            if max(arr) <= target:
                return True
            return False
        left,right = 0,max(nums) + 1
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left



        """
        3 7 1 6
        3 7 2 5
        3 7 2 5
        5 5 2 5
        """
        
