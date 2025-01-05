"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
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

        return 0 if not paths else min(paths)


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


"""
Leetcode discuss solution:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = {beginWord}
        queue = [(beginWord, 1)]
        wildcardMap = defaultdict(list)
        wordList.append(beginWord)

        def buildWildcardMap():
            for word in wordList:
                for i in range(len(word)):
                    wildcardWord = word[:i] + '*' + word[i+1:]
                    wildcardMap[wildcardWord].append(word)
        
        buildWildcardMap()

        while queue:
            word1, count = queue.pop(0)
            if word1 == endWord:
                return count
            
            for i in range(len(word1)):
                wildcardWord = word1[:i] + '*' + word1[i+1:]
                words = wildcardMap[wildcardWord]
                for word2 in words:
                    if word2 not in seen:
                        if word2 == endWord:
                            return count+1
                        queue.append((word2, count+1))
                        seen.add(word2)
                        
        return 0

"""


"""
# constructing all possible words from word list
        # with combination of letters such that the letter appears at the same index in every word

        list_of_char_at_index = defaultdict(list)

        for word in wordList:
            for index, char in enumerate(word):
                if char not in list_of_char_at_index[index]:
                    list_of_char_at_index[index].append(char)

        char_set = list(list_of_char_at_index.values())
        print(char_set)  # [['h', 'd', 'l'], ['o'], ['t', 'g']]
        result = list()
        result.append([])  # []

        for chars in char_set[:]:
            for _ in range(len(result)):
                top = result.pop(0)
                for c in chars:
                    t = list(top)
                    t.append(c)
                    result.append(t)

        print(result)  # [['h', 'o', 't'], ['h', 'o', 'g'], ['d', 'o', 't'], ['d', 'o', 'g'], ['l', 'o', 't'], ['l', 'o', 'g']]
        
        for i in range(len(result)):
            char_list = result.pop(0)
            result.append(''.join(char_list))

        print(result)  # ['hot', 'hog', 'dot', 'dog', 'lot', 'log']
"""
