class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.is_word = False
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr[self.is_word] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return self.is_word in curr
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Implement a trie with insert, search, and startsWith methods.
# Example:
# Trie trie = new Trie();

# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.