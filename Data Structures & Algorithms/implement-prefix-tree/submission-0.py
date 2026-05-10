class Node:
    def __init__(self, char, endOfWord):
        self.char = char
        self.children = {}
        self.endOfWord = endOfWord

class PrefixTree:

    def __init__(self):
        self.root = Node("", False)

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            curr_char = word[i]
            if curr_char not in node.children:
                node.children[curr_char] = Node(curr_char, False)
            node = node.children[curr_char]
        node.endOfWord = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            curr_char = word[i]
            if curr_char not in node.children:
                return False
            node = node.children[curr_char]

        if node.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            curr_char = prefix[i]
            if curr_char not in node.children:
                return False
            node = node.children[curr_char]
        return True
        