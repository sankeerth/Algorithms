"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 != 0:
            return False

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if stack:
                    top = stack.pop()
                else:
                    return False
                if char == ')':
                    if top == '(':
                        continue
                    else:
                        return False
                elif char == '}':
                    if top == '{':
                        continue
                    else:
                        return False
                elif char == ']':
                    if top == '[':
                        continue
                    else:
                        return False

        return False if stack else True

sol = Solution()
print(sol.isValid("({[]})"))
print(sol.isValid("({[}])"))
print(sol.isValid("({"))
print(sol.isValid("){})"))
print(sol.isValid(""))
print(sol.isValid("(){"))


"""
Discuss: More elegant solution

public boolean isValid(String s) {
    Stack<Character> stack = new Stack<Character>();
    for (char c : s.toCharArray()) {
        if (c == '(')
            stack.push(')');
        else if (c == '{')
            stack.push('}');
        else if (c == '[')
            stack.push(']');
        else if (stack.isEmpty() || stack.pop() != c)
            return false;
    }
    return stack.isEmpty();
}
"""
