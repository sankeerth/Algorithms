"""
678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
"""


class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        def valid_parantheses_recr(i, op):
            if op < 0:
                return False

            if i >= len(s):
                return op == 0

            if s[i] == '(':
                return valid_parantheses_recr(i+1, op+1)
            elif s[i] == ')':
                return valid_parantheses_recr(i+1, op-1)
            else:
                return valid_parantheses_recr(i+1, op) or valid_parantheses_recr(i+1, op+1) or valid_parantheses_recr(i+1, op-1)

        return valid_parantheses_recr(0, 0)


sol = Solution()
print(sol.checkValidString("()"))
print(sol.checkValidString(")("))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("("))
print(sol.checkValidString("())"))
print(sol.checkValidString("()*)(()(**())"))


"""
leetcode solution:

The problem can be rephrased as:
We are given a string s that contains characters '(', ')' and '✶'.
A hiker walks through the string from left to right.
When the hiker encounters '(', his elevation rises by 1.
When the hiker encounters ')', his elevation drops by 1.
When the hiker encounters '✶', his elevation could rise by 1 or drop by 1 or stay the same.
Is it possible for the hiker to walk through the string, starting and ending with elevation 0, 
without ever having negative elevation in between?

To solve this problem, we can use dynamic programming.
Lets define dp[i] as the set of possible elevations that the hiker can reach at index i, where 0 <= i <= n.
At index 0 (before the hiker encounters the first character), the only elevation the hiker can have is 0.

At index i > 0, there are 3 cases:
s[i] == '(': if hiker can reach elevation e at i-1, he can reach elevation e+1 at at i.
s[i] == ')': if hiker can reach elevation e at i-1, he can reach elevation e-1 at at i, unless e == 0 
(because the hiker can never have negative elevation).
s[i] == '✶': if hiker can reach elevation e at i-1, he can reach elevation e-1 (except when e == 0), e, and e+1 at i.
Observe that the set of possible elevations at any index is always a contiguous range of values.
Thus for each dp[i], we can represent the set of reachable elevations by the min and max of the range.

Furthermore, we only need to remember dp[i-1] to compute dp[i]. So we can use auxiliary variables instead of a dp array.

The resulting algorithm is O(n) time and O(1) space.

bool checkValidString(string s) {
    int lo = 0, hi = 0;
    for(int i=0; i<s.size(); i++){
        if(s[i] == '('){
            lo++, hi++;
        } else if(s[i] == ')') {
            lo--, hi--;
        } else {
            lo--, hi++;
        }
        lo = max(lo, 0);
        if(lo > hi) return false;
    }
    return lo == 0;
}
"""