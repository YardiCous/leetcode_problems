Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



# Solution
# Trie + Backtracking

# TC: O( 2 ^ N * N + M)
# SC: O(2 ^ N + M)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        res = []
        t = Trie()
        sentence = []
        for w in wordDict:
            t.add_word(w)
        def dfs(index):
            if index == N:
                copy = " ".join(sentence)
                res.append(copy)
                return
            node = t.root
            word = []
            for i in range(index,N):
                char = s[i]
                if char not in node.children:
                    break
                word.append(char)
                node = node.children[char]
                if node.word:
                    sentence.append("".join(word))
                    dfs(i + 1)
                    sentence.pop()
        dfs(0)
        return res
