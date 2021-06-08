"""
394. Decode String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is 
being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that 
digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""


class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            res, num = "", 0
            while i < len(s):
                if s[i].isdigit():
                    num = 10 * num + int(s[i])
                elif s[i] == '[':
                    i, ret = dfs(i+1)
                    if num > 0:
                        ret = num * ret
                        num = 0
                    res += ret
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]

                i += 1            
            return res

        return dfs(0)


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))
print(sol.decodeString("abc3[cd]xyz"))


"""
My previous solution:

class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        result = ""
        i = 0

        while i < len(s):
            if s[i] == '[':
                r_i, r_s = self.decodeString(s[i + 1:])
                i += r_i
                if num == "":
                    num = "1"  # default value
                result += int(num) * r_s
                num = ""
            elif s[i] == ']':
                return i+1, result
            elif s[i].isdigit():
                num += s[i]
            else:
                result += s[i]

            i += 1

        return result
"""
