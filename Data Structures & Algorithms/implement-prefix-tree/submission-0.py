class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root= TrieNode()

    def insert(self, word: str) -> None:
        # start at root
        node= self.root
        # for each char in the word
        for ch in word:
            # check if root children has any of the prefix
            if ch not in node.children:
                # add node with char val
                node.children[ch]= TrieNode()
            # move forward either way if node with ch found or node added
            node = node.children[ch]
        # mark end after endignthe word
        node.is_end= True

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            # check if is_end
            # move the next node
            node= node.children[ch]
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node= node.children[ch]
        return True