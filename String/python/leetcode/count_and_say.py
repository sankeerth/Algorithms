"""
38. Count and Say

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the 
character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", 
replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence.

Example 1:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:
Input: n = 1
Output: "1"
Explanation:
This is the base case.

Constraints:
1 <= n <= 30

Follow up: Could you solve it iteratively?
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(n):
            if n == 1:
                return "1"
            
            r = rle(n-1)
            queue = deque()
            nxt, count = "0", 0
            
            for i in range(len(r)-1, -1, -1):
                if r[i] != nxt:
                    if count > 0:
                        queue.appendleft(str(count) + nxt)
                    nxt = r[i]
                    count = 0
                count += 1

            queue.appendleft(str(count) + nxt)
            return "".join(queue)

        return rle(n)


sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(4)) # "1211"
print(sol.countAndSay(5)) # "111221"


"""
Iterative solution:

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        iter = 1

        def rle(s):
            l = []
            nxt = "0"
            count = 0

            for i in range(len(s)):
                if s[i] != nxt:
                    if count > 0:
                        l.append(str(count) + nxt)
                    nxt = s[i]
                    count = 0
                count += 1

            l.append(str(count) + nxt)
            return "".join(l)

        while iter < n:
            res = rle(res)
            iter += 1

        return res
"""
