# You are given an n x n integer matrix. You can do the following operation any number of times:
#
#     Choose any two adjacent elements of matrix and multiply each of them by -1.
#
# Two elements are considered adjacent if and only if they share a border.
#
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

# Solution
# Basically just a greedy where since we can assume, if even numbers of negative numbers, in the end all will be positive, and if there is odd number of negative, 1 will have no
# partner to do a -1 multiplcation unless a 0 exists, then that is possible. So from that just find the minimum and if is odd return total - minimum * 2

# TC: O(N * M)
# SC: O(1)

from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        total = 0
        minimum = 10 ** 20
        count = 0
        zeros = 0
        for r in range(rows):
            for c in range(cols):
                total += abs(matrix[r][c])
                if matrix[r][c] < 0:
                    count += 1
                elif matrix[r][c] == 0:
                    zeros += 1
                minimum = min(minimum,abs(matrix[r][c]))
        # print(total)
        if count % 2 == 0 or zeros > 0:
            return total
        else:
            return total - (abs(minimum) * 2)
