"""
336. Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of
the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back], k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals


sol = Solution()
print(sol.palindromePairs(["a", ""]))
print(sol.palindromePairs(["aa", "", "s"]))
print(sol.palindromePairs(["a", "abc", "aba", ""]))
print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll", "ls", "abc", "bcd"]))
print(sol.palindromePairs(["aaa", "a", "aa"]))


'''
Leetcode solution on top as my solution has a bug for case ["bb","bababab","baab","abaabaa","aaba","","bbaa","aba","baa","b"]
where "abaabaa","aaba" are not considered a pair. This is because I exit while loop based on a condition that is wrong.

My Solution:

class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words:
            return []

        result = list()
        length = len(words)
        word_index = dict()
        for i in range(length):
            word_index[words[i]] = i

        for i in range(length):
            current = words[i]
            current_length = len(current)

            if current == current[::-1] and "" in word_index:
                j = word_index[""]
                if i != j:
                    result.append([i, word_index[""]])
                    result.append([word_index[""], i])

            if current[::-1] in word_index:
                j = word_index[current[::-1]]
                if i != j:  # do not append if the string itself is a palindrome
                    result.append([i, j])

            back = -1
            condition = True
            while current_length + back > 0 and condition:
                if current[:back][::-1] in word_index:
                    result.append([i, word_index[current[:back][::-1]]])

                back -= 1
                condition = current[back] == current[back+1]

            front = 1
            condition = True
            while current_length - front > 0 and condition:
                if current[front:][::-1] in word_index:
                    result.append([word_index[current[front:][::-1]], i])

                condition = current[front] == current[front-1]
                front += 1

        return result
'''