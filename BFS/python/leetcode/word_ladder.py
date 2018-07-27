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


'''
Leetcode discuss solution:

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
                
        def make_p2w(word_list, w_idxs):
            """Creates a map of all combinations of words with missing letters mapped 
            to all words in the list that match that pattern.
            E.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
            """
            p2w = collections.defaultdict(list)
            
            for word in word_list:
                for i, j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    p2w[p].append(word)
            return p2w
            
        def bfs_words(begin, end, w_idxs, p2w):
            queue = collections.deque([(begin, 1)])
            visited = set([begin])
                        
            while queue:
                # Get the next node to explore from the top of the queue
                word, depth = queue.popleft()
                
                # Get the node's children 
                # By recreating all possible patterns for that string
                for i,j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    neighbor_words = p2w[p]
                    # Iterate through children
                    for nw in neighbor_words:
                        if nw not in visited:
                            # Goal check (before adding to the queue)
                            if nw == end:
                                return depth+1
                            # Add to visited
                            # These is no reason to wait to mark nodes as visited. Because this is 
                            # a BFS, once a node has been seen that is the earliest it could have
                            # possibly been seen so any other path to that node would either be 
                            # longer or the same length as what we've already observed.
                            visited.add(nw)                            
                            # Add to the end of the queue
                            queue.append((nw, depth+1))
            return 0
        
        # Get word length and character indexes
        wl = len(beginWord)
        w_indexes = zip(range(wl), range(1, wl+1))
        # Preprocess words into a map
        wordList.append(beginWord)
        patterns2words = make_p2w(wordList, w_indexes)
        # Do the search
        return bfs_words(beginWord, endWord, w_indexes, patterns2words)
'''


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