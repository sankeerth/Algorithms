"""
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:
Input: n = 2
Output: [1,2]

Constraints:
1 <= n <= 5 * 104
"""

"""
Algorithm:

Initialize an empty array lexicographicalNumbers to store the results.
Start with currentNumber set to 1.

Generate numbers from 1 to n:
Add currentNumber to the lexicographicalNumbers array.
  
If multiplying currentNumber by 10 is less than or equal to n (i.e., currentNumber * 10 <= n), 
  multiply currentNumber by 10 to move to the next lexicographical number (i.e., go deeper into the tree of numbers).
Otherwise:
  Adjust currentNumber to move to the next valid lexicographical number:
    While currentNumber ends with a 9 or is greater than or equal to n:
      Divide currentNumber by 10 to remove the last digit.
  Increment currentNumber by 1 to move to the next number in the sequence.
Return the lexicographicalNumbers array containing the numbers in lexicographical order from 1 to n.
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1

        for _ in range(n):
            res.append(cur)

             # If multiplying the current number by 10 is within the limit, do it
            if cur * 10 <= n:
                cur = cur * 10
            else:
                # Adjust the current number by moving up one digit
                while cur % 10 == 9 or cur >= n:
                    cur = cur // 10 # Remove the last digit
                cur += 1 # Increment the number
        
        return res


sol = Solution()
print(sol.lexicalOrder(4))
print(sol.lexicalOrder(13))
print(sol.lexicalOrder(123))
