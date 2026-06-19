# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:
#
#     (startx, starty): The bottom-left corner of the rectangle.
#     (endx, endy): The top-right corner of the rectangle.
#
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:
#
#     Each of the three resulting sections formed by the cuts contains at least one rectangle.
#     Every rectangle belongs to exactly one section.
#
# Return true if such cuts can be made; otherwise, return false.

# Solution
# Sweep line, pretty intuitive.

# TC: O(N log N)
# SC: O(N)

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        res = 0
        def solve(events):
            zeros = 0
            e = []
            for start,end in events:
                e.append((start,1))
                e.append((end,-1))
            e.sort(key=lambda x:(x[0],x[1]))
            curr = 0
            for _,v in e:
                curr += v
                if curr == 0:
                    zeros += 1
            # print(zeros)
            return zeros
        x,y = [],[]
        for x1,y1,x2,y2 in rectangles:
            x.append((x1,x2))
            y.append((y1,y2))
        a = solve(x)
        b = solve(y)
        if a >= 3 or b >= 3:
            return True
        return False
