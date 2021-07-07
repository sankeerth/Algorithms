"""
269. Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. 
If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t 
in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        inDegree, queue, adjList = defaultdict(int), list(), defaultdict(set)
        res = list()

        for word in words:
            for c in word:
                inDegree[c] += 0

        for first, second in zip(words, words[1:]):
            for src, dest in zip(first, second):
                if src != dest:
                    if dest not in adjList[src]:
                        adjList[src].add(dest)
                        inDegree[dest] += 1
                    break
                else:
                    # check if second word is not a prefix of first word
                    if len(second) < len(first):
                        return ""
        
        for c in inDegree:
            if inDegree[c] == 0:
                queue.append(c)

        while queue:
            src = queue.pop(0)
            res.append(src)
            for dest in adjList[src]:
                inDegree[dest] -= 1
                if inDegree[dest] == 0:
                    queue.append(dest)

        if len(res) < len(inDegree): # cycle since not all chars/nodes were visited
            return ""

        return "".join(res)

        
sol = Solution()
print(sol.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(sol.alienOrder(["wrp","wrf","er","ett","rftt"]))
print(sol.alienOrder(["z","x"]))
print(sol.alienOrder(["z","x","z"]))


"""
Leetcode solution using DFS:

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""

        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)
"""
