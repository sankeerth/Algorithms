"""
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    '''

    1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
    2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
    3, If p.charAt(j) == '*':
    here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(s)+1) for _ in range(len(p)+1)]

        dp[0][0] = True
        for i in range(2, len(p)+1):
            dp[i][0] = p[i-1] == '*' and dp[i-2][0]

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == '*':
                    if p[i-2] != s[j-1] and p[i-2] != '.':
                        dp[i][j] = dp[i-2][j]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-2][j]
                elif p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and p[i-1] == s[j-1]

        return dp[len(p)][len(s)]


sol = Solution()
print(sol.isMatch("bbbba", ".*a*a"))
print(sol.isMatch("a", "a*"))
print(sol.isMatch("a", "ab*"))
print(sol.isMatch("aaa", "ab*a*c*a"))
print(sol.isMatch("aaaaaa", "a*"))
print(sol.isMatch("aab", "a*b"))
print(sol.isMatch("ab", "a*b"))
print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "a."))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("aa", "..."))
print(sol.isMatch("aa", ".*"))
print(sol.isMatch("a", "c*."))
print(sol.isMatch("a", "c*.b"))
print(sol.isMatch("aab", "c*a*b"))
print(sol.isMatch("ab", "c*a*b"))


"""
My recusive solution with bug that does not work

class Solution(object):
    def isMatch(self, s, p):
        '''
        :type s: str
        :type p: str
        :rtype: bool
        '''

        len_s = len(s)
        len_p = len(p)

        def is_match_recursive(i, j):
            if i == len_s and j == len_p:
                return True
            elif i == len_s or j == len_p:
                if j < len_p and p[j] == '*':
                    # cases for below --> s: a, p: a*
                    return is_match_recursive(i, j+1)
                elif j < len_p-1 and p[j+1] == '*':
                    # cases for below --> s: a, p: ab*
                    return is_match_recursive(i, j+2)
                return False
            elif p[j] == '*':
                if is_star_match(i, j):
                    # cases for below --> s: aab, p:a*b | s: aaaaa, p:a* | s:aaa, p:ab*a*c*a
                    return is_match_recursive(i+1, j+1) or is_match_recursive(i+1, j) or is_match_recursive(i, j+1)
                else:
                    return is_match_recursive(i, j+1)
            else:
                if is_char_match_or_dot(i, j):
                    return is_match_recursive(i+1, j+1)
                elif j+1 < len_p and p[j+1] == '*':
                    return is_match_recursive(i, j + 1)
            return False

        def is_char_match_or_dot(i, j):
            if s[i] == p[j] or p[j] == '.':
                return True
            return False

        def is_star_match(i, j):
            if j > 0 and is_char_match_or_dot(i, j-1):
                return True
            return False

        return is_match_recursive(0, 0)
"""