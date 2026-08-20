You are given a 1-indexed array of integers nums of length n.

We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val.

You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:

    If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]), append nums[i] to arr1.
    If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]), append nums[i] to arr2.
    If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]), append nums[i] to the array with a lesser number of elements.
    If there is still a tie, append nums[i] to arr1.

The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

Return the integer array result.


# Solution
# Pretty straight forward

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        sl = SortedList()
        sl2 = SortedList()
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        sl.add(nums[0])
        sl2.add(nums[1])
        def greaterCount(s,val):
            idx = s.bisect_right(val)
            return len(s) - idx
        for i in range(2,N):
            count1 = greaterCount(sl,nums[i])
            count2 = greaterCount(sl2,nums[i])
            # print(count1,count2)
            if count1 > count2:
                arr1.append(nums[i])
                sl.add(nums[i])
            elif count1 < count2:
                arr2.append(nums[i])
                sl2.add(nums[i])
            elif count1 == count2:
                if len(arr1) <= len(arr2):
                    arr1.append(nums[i])
                    sl.add(nums[i])
                else:
                    arr2.append(nums[i])
                    sl2.add(nums[i])
            # print(arr1,arr2)
        return arr1 + arr2
