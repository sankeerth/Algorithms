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
from typing import List


# With memoization/dp
# Worst case time complexity is still the same: https://stackoverflow.com/questions/24591616/whats-the-time-complexity-of-this-algorithm-for-palindrome-partitioning
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """"
        Complexity Analysis

        Time Complexity : O(N⋅2^N), where N is the length of string s. In the worst case, 
        there could be 2^N possible substrings and it will take O(N) to generate each 
        substring using substr as in Approach 1. However, we are eliminating one 
        additional iteration to check if substring is a palindrome or not.

        Space Complexity: O(N⋅N), where N is the length of the string s. 
        The recursive call stack would require N space as in Approach 1. 
        Additionally we also use 2 dimensional array dp of size N⋅N.

        This gives us total space complexity as O(N⋅N) + O(N) = O(N⋅N)
        """
        result, current = [], []
        dp = [[False] * len(s) for i in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def partitionRecursive(i):
            if i == len(s):
                result.append(list(current))
                return

            for j in range(i, len(s)):
                if i == j or dp[i][j]:
                    current.append(s[i:j+1])
                    partitionRecursive(j+1)
                    current.pop()
         
        partitionRecursive(0)
        return result



sol = Solution()
print(sol.partition("aaaa"))
print(sol.partition("aaba"))
print(sol.partition("aabaabd"))

"""
Without memoization

Complexity Analysis

Time Complexity : O(N⋅2^N), where N is the length of string s.
This is the worst-case time complexity when all the possible substrings are palindrome.

Hence, there could be 2^N possible substrings in the worst case. 
For each substring, it takes O(N) time to generate substring and determine if it a palindrome or not. 
This gives us time complexity as O(N⋅2 N)

Space Complexity: O(N), where NN is the length of the string s. 
This space will be used to store the recursion stack. For s = aaa, 
the maximum depth of the recursive call stack is 3 which is equivalent to N.


class Solution(object):
    def partition(self, s):
        result, current = [], []

        def isPalindrome(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            
            return True if i >= j else False

        def partitionRecursive(i):
            if i == len(s):
                result.append(list(current))
                return

            for j in range(i, len(s)):
                if i == j or isPalindrome(i, j):
                    current.append(s[i:j+1])
                    partitionRecursive(j+1)
                    current.pop()
        
        partitionRecursive(0)
        return result
"""
