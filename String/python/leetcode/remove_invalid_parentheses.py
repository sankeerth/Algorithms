"""
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]

Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""
from typing import List


class Solution:
    """
    This solution is from leetcode discuss. Similar to my approach but I use list to store intermediate results
    and it is quite verbose!

    Key Points:
    Generate unique answer once and only once, do not rely on Set.
    Do not need preprocess.

    We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
    The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more
     ‘)’ than ‘(‘ in the prefix.

    To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix.
    However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2]
    but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

    After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string.
    However, we need to keep another information: the last removal position. If we do not have this position,
    we will generate duplicate by removing two ‘)’ in two steps only with a different order.
    For this, we keep tracking the last removal position and only remove ‘)’ after that.

    Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
    The answer is: do the same from right to left.
    However a cleverer idea is: reverse the string and reuse the code!
    Here is the final implement in Java.
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = list()

        def remove(s, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    stack += 1
                elif s[i] == par[1]:
                    stack -= 1
                if stack >= 0:
                    continue

                for j in range(last_j, i+1):
                    if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                        remove(s[0:j] + s[j+1:], i, j, par)
                return

            reverse = s[::-1]
            if par[0] == '(':
                remove(reverse, 0, 0, [')', '('])
            else:
                result.append(reverse)

        remove(s, 0, 0, ['(', ')'])
        return result


sol = Solution()
print(sol.removeInvalidParentheses(")))))))))))))()))))))"))
print(sol.removeInvalidParentheses("(()"))
print(sol.removeInvalidParentheses("()(()"))
print(sol.removeInvalidParentheses("(()(()"))
print(sol.removeInvalidParentheses("(()(()(()"))
print(sol.removeInvalidParentheses("())(()"))
print(sol.removeInvalidParentheses("()())()(()"))
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(a)())()"))
print(sol.removeInvalidParentheses(")("))
print(sol.removeInvalidParentheses(")()"))
print(sol.removeInvalidParentheses(")(a)a)"))
print(sol.removeInvalidParentheses("a)(a)a)"))
print(sol.removeInvalidParentheses(")o(v("))


"""
Another leetcode discuss solution:
In BFS we handle the states level by level, in the worst case, we need to handle all the levels, we can analyze the 
time complexity level by level and add them up to get the final complexity.

On the first level, there's only one string which is the input string s, let's say the length of it is n, to check 
whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level, 
so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string, we need to check whether it's 
valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1). Come to the third level, 
total time complexity is (n-2) x C(n, n-2), so on and so forth...

Finally we have this formula:
T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = set()
        queue.add(s)

        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c ==')':
                    if count == 0:
                        return False
                    count -= 1
            
            return count == 0
        
        res = []
        while queue:
            for string in queue:
                if isValid(string):
                    res.append(string)
            
            if res:
                break

            newQueue = set()
            for string in queue:
                for i in range(len(string)):
                    newQueue.add(string[:i] + string[i+1:])
            queue = newQueue
        
        return res  
"""

"""
My solution:

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        op, cl = 0, 0
        for c in s:
            if c == '(':
                op += 1
            elif c ==')':
                if op > 0:
                    op -= 1
                else:
                    cl += 1

        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c ==')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0
        
        def removeParenthesesRecursive(i, stack, count):
            if i == len(s) or count == 0:
                string = "".join(stack) + s[i:]
                valid = isValid(string)
                if valid:
                    res.add(string)
                return
            
            if len(s)-i < count:
                return

            removeParenthesesRecursive(i+1, stack + [s[i]], count)
            if count > 0 and not s[i].isalpha():
                removeParenthesesRecursive(i+1, stack, count-1)

        removeParenthesesRecursive(0, [], op + cl)
        return list(res)
"""
