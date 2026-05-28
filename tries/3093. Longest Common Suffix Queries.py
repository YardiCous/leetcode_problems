# You are given two arrays of strings wordsContainer and wordsQuery.
#
# For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.
#
# Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

# Solution
# Intuitively, I was thinking of Trie since common prefix, but slightly different because I had to store the index and length of the word for each Node
# But wasn't confindent it would work on first try just yolo the submit

# TC: O(Q * W) where Q is number of queries and maximum length of the word
# SC: O(C * W) where c is number of words in container
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.len = 10 ** 20
        self.index = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self,word,index):
        curr = self.root
        if len(word) < curr.len:
            curr.len = len(word)
            curr.index = index
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
            if len(word) < curr.len:
                curr.len = len(word)
                curr.index = index
    def suffix_word(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return curr.index
            curr = curr.children[w]
        return curr.index
        
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        Q = len(wordsQuery)
        root = Trie()
        res = []
        for index,word in enumerate(wordsContainer):
            r = word[::-1]
            root.add_word(r,index)
        for word in wordsQuery:
            curr = root
            r = word[::-1]
            index = curr.suffix_word(r)
            res.append(index)
        return res
