"""
1209. Remove All Adjacent Duplicates in String II

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal 
letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

Constraints:
1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
"""


class Solution:
    # Two pointer approach (variant of stack approach below)
    def removeDuplicates(self, s: str, k: int) -> str:
        res, count = list(s), []
        i, j = 0, 0

        while i < len(s):
            res[j] = res[i]
            if j == 0 or res[j] != res[j-1]:
                count.append(0)
            count[-1] += 1

            if count[-1] == k:
                count.pop()
                j -= k

            i += 1
            j += 1
        
        return "".join(res[:j])


sol = Solution()
print(sol.removeDuplicates("abcd", 2))
print(sol.removeDuplicates("deeedbbcccbdaa", 3))
print(sol.removeDuplicates("deeedbbcccbdaaa", 3))
print(sol.removeDuplicates("pbbcggttciiippooaais", 2))

"""
Stack solution: O(n) time complexity

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, count = [], []
        for c in s:
            if stack and stack[-1] == c:
                count[-1] += 1
            else:
                count.append(1)
            stack.append(c)
            
            if count and count[-1] == k:
                top = count.pop()
                while top > 0:
                    stack.pop()
                    top -= 1

        return "".join(stack)
"""

"""
O(n^2 / k) solution that times out:

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res, duplicates = list(s), list()
        cur, count = "", 0
        
        while True:
            for i in range(len(res)):
                if res[i] != cur:
                    cur = res[i]
                    count = 0
                count += 1

                if count == k:
                    duplicates.append(i-k+1)
                    count = 0

            if not duplicates:
                break

            i, temp = 0, []
            for dup in duplicates:
                temp += res[i:dup]
                i = dup + k

            temp += res[i:len(res)]
            cur, duplicates = "", []
            res = temp

        return "".join(res)
"""
