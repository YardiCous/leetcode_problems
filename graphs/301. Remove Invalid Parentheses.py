Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.


# Solution
# BFS

# TC: O(N ^ 2) * (2 ^ N)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = deque()
        q.append(s)
        visit = set()
        visit.add(s)
        def valid(x):
            total = 0
            for a in x:
                if a == "(":
                    total += 1
                elif a == ")":
                    total -= 1
                    if total < 0:
                        return False
            return total == 0
        while q:
            res = []
            for _ in range(len(q)):
                curr = q.popleft()
                N = len(curr)
                if valid(curr):
                    res.append(curr)
                if res:
                    continue
                for i in range(N):
                    if curr[i] not in "()":
                        continue
                    new_s = curr[:i] + curr[i + 1:]
                    if new_s not in visit:
                        visit.add(new_s)
                        q.append(new_s)
            if res:
                return res
        return [""] 
