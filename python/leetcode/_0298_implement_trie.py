"""
_0298_implement_trie

Takeaways:

Notes:
- Implement w/o recursion

"""

from typing import List

class Node:

    def __init__(self):
        self.nodes = [None] * 26
        self.exist = False

class Trie:

    def __init__(self):
        self.head = Node()

    #
    # insert
    #

    def insert(self, word: str) -> None:
        self.insertHelper(word, 0, self.head)
    
    def insertHelper(self, word: str, radix: int, node: Node) -> None:

        if radix < len(word):
            index = ord(word[radix])-ord('a')

            if node.nodes[index] is None:
                 node.nodes[index] = Node()

            self.insertHelper(word, radix+1, node.nodes[index])
        else:
            node.exist = True
        
    #
    # search
    #

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.head)
    

    def searchHelper(self, word: str, radix: int, node: Node) -> bool:

        if node is None:
            return False
        
        if radix == len(word):
            return node.exist
        
        index = ord(word[radix])-ord('a')
        return self.searchHelper(word, radix+1, node.nodes[index])
        
    #
    # startsWith
    #

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(prefix, 0, self.head)
    
    # TODO: remove code dup with searchHelper
    def startsWithHelper(self, word: str, radix: int, node: Node) -> bool:

        if node is None:
            return False
        
        if radix == len(word):
            return True
        
        index = ord(word[radix])-ord('a')
        return self.startsWithHelper(word, radix+1, node.nodes[index])



def run_tests(solution):
    print("test passed!")

def main():

    solution = Trie()

    run_tests(solution)

    solution.insert("apple")

    print(solution.search("apple"))
    print(solution.search("applw"))
    print(solution.search("app"))
    print(solution.startsWith("app"))

    solution.insert("app")
    print(solution.search("app"))