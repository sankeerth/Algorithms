"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def generateParenthesisRecursive(o, c, cur):
            if o == n:
                cur += ')' * (n-c)
                res.append(cur)
                return
            
            generateParenthesisRecursive(o+1, c, cur + '(')
            for i in range(c, o):
                cur += ')'
                generateParenthesisRecursive(o+1, i+1, cur + '(')

        generateParenthesisRecursive(0, 0, "")
        return res


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(0))
print(sol.generateParenthesis(4))


"""
Leetcode discuss solution:

class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        res = []
        def generateParenthesisRecursive(open, close, s):
            if open == 0:
                for i in range(close):
                    s += ')'
                res.append(s)
            else:
                generateParenthesisRecursive(open-1, close, s+'(')
                if open < close:
                    generateParenthesisRecursive(open, close-1, s+')')

        generateParenthesisRecursive(n-1, n, '(')
        return res
"""

"""
Complexity Analysis

Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). 
This analysis is outside the scope of this article, but it turns out this is the n-th Catalan number 1/{n+1} binom{2n}{n} 
which is bounded asymptotically by {4^n}/{n*sqrt{n}} 

Time Complexity : O({4^n}/{sqrt{n}}). Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity : O({4^n}/{sqrt{n}}), as described above, and using O(n)O(n) space to store the sequence.
"""
