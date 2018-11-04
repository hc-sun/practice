class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(ch)
            if not node:
                return False
        return node.is_word

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        trie = Trie()
        node = trie.root
        for ch in words:
            trie.insert(ch)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, result, '')
        return result
    
    def dfs(self, board, node, i, j, result, word):
        if node.is_word:
            result.append(word)
            node.is_word = False
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            ch = board[i][j]
            node = node.children.get(ch)
            if node:
                word += ch
                board[i][j] = None
                self.dfs(board, node, i+1, j, result, word)
                self.dfs(board, node, i-1, j, result, word)
                self.dfs(board, node, i, j-1, result, word)
                self.dfs(board, node, i, j+1, result, word)
                board[i][j] = ch

# Given a 2D board and a list of words from the dictionary, find all words in the board.
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.