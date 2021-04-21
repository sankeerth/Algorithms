"""
402. Remove K Digits

Given a non-negative integer num represented as a string, remove k digits 
from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        stack.append(num[0])

        for d in num[1:]:
            while stack and stack[-1] > d and k > 0:
                stack.pop()
                k -= 1
            stack.append(d)

        while k > 0: # remove digits until k=0 when digits are in ascending order and will not be popped above
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip("0")
        return res if res else "0"


s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("1432219", 4))
print(s.removeKdigits("1432219", 2))
print(s.removeKdigits("10200", 1))
print(s.removeKdigits("10", 2))
print(s.removeKdigits("10", 1))
print(s.removeKdigits("43", 2))
print(s.removeKdigits("43", 1))
print(s.removeKdigits("123", 2))
print(s.removeKdigits("112", 1))
