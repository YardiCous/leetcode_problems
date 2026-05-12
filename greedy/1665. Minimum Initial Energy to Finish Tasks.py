# You are given an array tasks where tasks[i] = [actuali, minimumi]:
#
#     actuali is the actual amount of energy you spend to finish the ith task.
#     minimumi is the minimum amount of energy you require to begin the ith task.
#
# For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.
#
# You can finish the tasks in any order you like.
#
# Return the minimum initial amount of energy you will need to finish all the tasks.

# Solution
# Binary search + sorting basically sort the difference of minimum - cost and finish the biggest cost first greedily
# TC: N * log M where M is the biggest value
# SC: O(1)

from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1] - x[0]))
        left,right = 0, 10 ** 9
        N = len(tasks)
        
        def good(target):
            nonlocal tasks
            for i in range(N - 1,-1,-1):
                cost,minimum = tasks[i][0],tasks[i][1]
                if target >= minimum:
                    target -= cost
                else:
                    return False
            return True
        while left < right:
            mid = (left + right) // 2
            if good(mid):
                right = mid
            else:
                left = mid + 1
        return left

        """
        32 - 10 = 22
        22 - 10 = 12
        12 - 8 = 4
        4 - 2 = 2

        """

