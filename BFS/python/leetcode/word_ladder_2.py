"""
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import defaultdict


# Both DFS and BFS are giving TLE, need to check the editorial solution
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        list_of_char_at_index = defaultdict(list)

        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            for index, char in enumerate(word):
                if char not in list_of_char_at_index[index]:
                    list_of_char_at_index[index].append(char)

        char_set = list(list_of_char_at_index.values())

        word_graph = defaultdict(list)
        for word in wordList:
            for index, chars in enumerate(char_set):
                for char in chars:
                    if word[index] != char:
                        word_dup = list(word)
                        word_dup[index] = char
                        word_dup = ''.join(word_dup)
                        if word_dup in wordList:
                            word_graph[word].append(word_dup)

        visited = dict()
        path = list()
        paths = defaultdict(list)

        for v in word_graph.keys():
            visited[v] = False

        def shortest_path():
            path.append(beginWord)
            for s in word_graph[beginWord]:
                dfs(s, 2, path)


        def dfs(s, l, path):
            if s == endWord:
                path.append(endWord)
                paths[len(path)].append(list(path))
                path.pop()
                return
            visited[s] = True
            path.append(s)
            for v in word_graph[s]:
                if not visited[v]:
                    dfs(v, l+1, path)
            visited[s] = False
            path.pop()

        shortest_path()

        return min(paths.values()) if paths else []


sol = Solution()
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        seen = {beginWord}
        wildcardMap = defaultdict(list)
        queue = [(beginWord, [beginWord])]
        res = []

        def buildWildcardMap():
            for word in wordList + [beginWord]:
                for i in range(len(word)):
                    wildcardWord = word[:i] + '*' + word[i+1:]
                    wildcardMap[wildcardWord].append(word)
        
        buildWildcardMap()

        while queue:
            word1, ladder = queue.pop(0)
            seen.add(word1)
            if word1 == endWord:
                if not res or len(ladder) <= len(res[-1]):
                    res.append(ladder)
                    continue
                else:
                    break

            for i in range(len(word1)):
                wildcardWord = word1[:i] + '*' + word1[i+1:]
                if wildcardWord not in wildcardMap:
                    continue
                words = wildcardMap[wildcardWord]
                for word2 in words:
                    if word2 not in seen:
                        queue.append((word2, ladder + [word2]))
                        seen.add(word1)
            
        return res
"""
