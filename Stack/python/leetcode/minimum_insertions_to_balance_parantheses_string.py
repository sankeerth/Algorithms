"""
1541. Minimum Insertions to Balance a Parentheses String

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.
Return the minimum number of insertions needed to make s balanced.

Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. 
We need to to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Example 4:
Input: s = "(((((("
Output: 12
Explanation: Add 12 ')' to balance the string.

Example 5:
Input: s = ")))))))"
Output: 5
Explanation: Add 4 '(' at the beginning of the string and one ')' at the end. The string becomes "(((())))))))".

Constraints:
1 <= s.length <= 10^5
s consists of '(' and ')' only.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i, result = 0, 0

        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:
                j = i+1
                if j < len(s) and s[j] == ')':
                    if stack:
                        stack.pop()
                    else:
                        result += 1 
                    i = j
                else:
                    if stack:
                        stack.pop()
                        result += 1
                    else:
                        result += 2
            i += 1

        result += len(stack) * 2
        return result


s = Solution()
print(s.minInsertions("(()))"))
print(s.minInsertions("())"))
print(s.minInsertions("))())("))
print(s.minInsertions("(((((("))
print(s.minInsertions(")))))))"))
print(s.minInsertions(")()"))
print(s.minInsertions("()()"))
print(s.minInsertions("))))(("))
print(s.minInsertions(")"))
print(s.minInsertions("("))
print(s.minInsertions("(()))(()))()())))"))

"""
Idea:

Record the number of '(' in an open bracket count int.
If there is a '))' or a ') 'then open bracket count -= 1
If there is a '))' or a ') and open bracket count = 0 an '(' must be inserted
If there is a single ')' another ')' must be inserted
At the end of the program and if open bracket count >0 then an '))' must be added for each unmatch '('
Tricks:

Go through string replacing '))' with '}'
This allows for easy differentiation between ')' '))' when iterating through the input string
This makes checking the above conditions a breeze

class Solution:
    def minInsertions(self, s: str) -> int:
        
        count = 0
        s = s.replace('))', '}')
        open_bracket_count = 0

        for c in s:
            if c == '(':
                open_bracket_count += 1
            else:
                # For ) you need to add 1 char to get ))
                if c == ')': 
                    count += 1

                # Matching ( for ) or ))
                if open_bracket_count:
                    open_bracket_count -= 1

                # No Matching ( for ) or ))
                # Need to insert ( to balance string
                else:
                    count += 1
        return count + open_bracket_count * 2
"""
