"""
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, present = list(), set()
        counter = Counter(s)

        for c in s:
            counter[c] -= 1
            if c not in present:                
                while stack and c < stack[-1] and counter[stack[-1]] > 0:
                    present.remove(stack.pop())

                stack.append(c)
                present.add(c)
            
        return "".join(stack)


sol = Solution()
print(sol.removeDuplicateLetters("bcabc"))
print(sol.removeDuplicateLetters("cbacdcbc"))
print(sol.removeDuplicateLetters("cbafcdcbc"))
print(sol.removeDuplicateLetters("cbafcdcedbc"))


"""
Leetcode solution (similar as above and uses counter instead):
Greedy - Solving with Stack

Algorithm
We use idea number two from the intuition. We will keep a stack to store the solution we have built 
as we iterate over the string, and we will delete characters off the stack whenever it is possible and 
it makes our string smaller.

Each iteration we add the current character to the solution if it hasn't already been used. 
We try to remove as many characters as possible off the top of the stack, and then add the current character

The conditions for deletion are:
The character is greater than the current characters
The character can be removed because it occurs later on
At each stage in our iteration through the string, we greedily keep what's on the stack as small as possible.

class Solution:
    def removeDuplicateLetters(self, s) -> int:

        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
"""
