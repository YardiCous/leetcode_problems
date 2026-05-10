# You are given an integer array nums.
#
# You can perform the following operation any number of times:
#
#     Choose two indices a and b such that nums[a] % nums[b] == 0.
#     Replace nums[a] with nums[b].
#
# Return the minimum possible sum of the array after performing any number of operations.



# Solution
# Some greedy portion, at first I was thinking of DP but realized that a hashmap holding the counters of the elements is good enough and greedily sort the keys by smallest
# as we always want to replace the biggest to the smallest value possible

# TC: N log N * log M where N = number of keys and M = biggest value of the List
# SC: O(N) as we store the counts of the elements in a Counter()


from collections import Counter
class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        count = Counter(nums)
        maxVal = max(nums)
        for key in sorted(count.keys()):
            for j in range(key * 2,maxVal + 1,key):
                # print(j)
                if j in count:
                    # print(j)
                    if count[j] == 0:
                        continue
                    count[key] += count[j]
                    count[j] = 0

                    # print(count)
        # print(count)
        res = 0
        for key,count in count.items():
            res += key * count
        return res
