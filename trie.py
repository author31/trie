from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self, char: str, word: str = None) -> None:
        self.char = char
        self.word = word
        self.freq = 0
        self.is_end_of_word = False
        self._children = defaultdict(lambda: None)
    
    def __getitem__(self, key):
        return self._children[key]
    
    def __setitem__(self, key, value):
        self._children[key] = value
    
    @property
    def children(self):
        return self._children.keys()
    
    @property
    def items(self):
        return self._children.items()

class Trie:
    def __init__(self) -> None:
        self.root_node = TrieNode("")
    
    def build_tree(self, sentences: List) -> None:
        for sentence in sentences: self._insert(sentence)
        
    def search(self, queries: str) -> List:
        retrive_results = []
        target_node = self._get_target_node(queries)
        if not target_node: return []

        def _dfs(node: TrieNode, retrieve_result: List) -> None:
            if not node: return
            if node.word not in retrieve_result: retrieve_result.append(node.word)
            for child in node.children: _dfs(node[child], retrieve_result)
        
        for child in target_node.children:
            _tmp = []
            _dfs(target_node[child], _tmp)
            retrive_results.append(
                self._merge_retrieve_result(queries, " ".join(_tmp))
            )
        
        ##TOFIX: couldn't retrieve sentences with the same prefixes
        """
        text 1: what do you want?
        text 2: what did he say?
        input query: wh
        output: what do you want
        """
        return retrive_results
            
    def _merge_retrieve_result(self, t1: str, t2: str) -> str:
        for i in range(1, min(len(t1), len(t2))+1):
            if t1.endswith(t2[:i]): return t1 + t2[i:]
        return t1 + " " + t2

    def _get_target_node(self, queries: str) -> TrieNode:
        temp_node = self.root_node
        words = queries.split(" ")
        for word in words:
            for char in word:
                temp_node = temp_node[char]

        return temp_node

    def _insert(self, sentence: List, node: TrieNode=None):
        words = sentence.split(" ")
        if not node: node = self.root_node
        for word in words:
            for char in word:
                if not node[char]: node[char] = TrieNode(char= char, word=word)
                node = node[char]
                node.freq += 1
            node.is_end_of_word = True
    