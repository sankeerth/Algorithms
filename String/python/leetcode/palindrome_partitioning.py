"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        current = list()

        def is_palindrome(i, j):
            while i <= j and s[i] == s[j]:
                i += 1
                j -= 1

            return True if i >= j else False

        def partition_recr(i, l):
            if i == l:
                result.append(list(current))
            else:
                for j in range(i, l):
                    if i == j or is_palindrome(i, j):
                        current.append(s[i:j+1])
                        partition_recr(j+1, l)
                        current.pop()

        partition_recr(0, len(s))

        return result


sol = Solution()
print(sol.partition("aab"))
print(sol.partition("aabaabd"))

'''
Refactored code:

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = list()
        current = list()

        def is_palindrome(string):
            return string == string[::-1]

        def partition_recr(i):
            if i == len(s):
                result.append(list(current))
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    current.append(s[i:j+1])
                    partition_recr(j+1)
                    current.pop()

        partition_recr(0)
        return result
'''
