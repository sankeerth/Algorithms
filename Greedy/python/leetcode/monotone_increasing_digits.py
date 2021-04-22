"""
738. Monotone Increasing Digits

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.
(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299

Note: N is an integer in the range [0, 10^9].
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = list(str(N))
        i = 1
        while i < len(res) and res[i] >= res[i-1]:
            i += 1

        while 0 < i < len(res) and res[i-1] > res[i]:
            res[i-1] = str(int(res[i-1]) - 1)
            i -= 1

        i += 1
        while i < len(res):
            res[i] = '9'
            i += 1

        return int("".join(res))
        

s = Solution()
print(s.monotoneIncreasingDigits(9))
print(s.monotoneIncreasingDigits(10))
print(s.monotoneIncreasingDigits(1234))
print(s.monotoneIncreasingDigits(2765))
print(s.monotoneIncreasingDigits(23454))
print(s.monotoneIncreasingDigits(3109))
print(s.monotoneIncreasingDigits(300))
print(s.monotoneIncreasingDigits(100))
print(s.monotoneIncreasingDigits(2100))
print(s.monotoneIncreasingDigits(332))
print(s.monotoneIncreasingDigits(1110))
print(s.monotoneIncreasingDigits(10000))
print(s.monotoneIncreasingDigits(399443))


"""
Leetcode discuss: Another variant of simple solution using for loop:

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = list(str(N))
        index = len(res)

        for i in range(len(res)-1, 0, -1):
            if res[i-1] > res[i]:
                index = i
                res[i-1] = str(int(res[i-1])-1)

        for i in range(index, len(res)):
            res[i] = '9'

        return int("".join(res))
"""

"""
My solution that fails for test case: 399443

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        string = str(N)
        switched, i = False, 0
        res = []

        while i < len(string):
            if switched:
                res.append('9')
            elif i < len(string)-1 and string[i] > string[i+1]:
                switched = True
                res.append(str(int(string[i]) - 1))
                if i > 0 and int(res[i]) < int(res[i-1]):
                    j = i
                    while j > 0:
                        res[j] = '9'
                        j -= 1
                    if res[0] == '1':
                        res.pop(0)
                    else:
                        res[0] = str(int(string[i]) - 1)
            else:
                res.append(string[i])
            i += 1

        return int("".join(res))
"""
