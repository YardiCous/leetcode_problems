# You are given two arrays with positive integers arr1 and arr2.
#
# A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.
#
# A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.
#
# You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.
#
# Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

# Solution
# Can be done using trie or math
# The idea is bascically pre proces one of the nums first and get all the prefix

# TC: O(N + M) log 8
# SC: O(N + M) * 8

from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def add_word(self,word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isWord = True
    def prefix_count(self,word):
        curr = self
        count = 0
        for w in word:
            if w not in curr.children:
                return count
            curr = curr.children[w]
            count += 1
        return count
class Trie:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()
        res = 0
        for n in arr1:
            root.add_word(str(n))
        for n in arr2:
            res = max(res,root.prefix_count(str(n)))
        return res

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        first_set = set(arr1)
        res= 0
        for i,n in enumerate(arr1):
            while n > 0:
                first_set.add(n)
                n //= 10
        # print(first_set)
        for i,n in enumerate(arr2):
            while n > 0:
                if n in first_set:
                    res = max(res,len(str(n)))
                n //= 10
        return res
