"""
679. 24 Game

You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: [1, 2, 1, 2]
Output: False

You are restricted with the following rules:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. 
For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

Constraints:
cards.length == 4
1 <= cards[i] <= 9
"""
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        eps = 0.001
        def permutations(nums):
            if len(nums) <= 1:
                yield nums
            else:
                for perm in permutations(nums[1:]):
                    for i in range(len(nums)):
                        yield perm[:i] + nums[0:1] + perm[i:]

        operations = []
        def operatorCombinations(operators, comb):
            if len(comb) >= 3:
                operations.append(list(comb))
            else:
                for op in operators:
                    comb.append(op)
                    operatorCombinations(operators, comb)
                    comb.pop()

        def calc(a, b, op):
            if op == '-':
                return a - b
            elif op == '+':
                return a + b
            elif op == '*':
                return a * b
            elif op == '/':
                return a / b if b else 0

        operatorCombinations(['-', '+', '*', '/'], [])

        for perm in permutations(nums):
            for ops in operations:
                case1 = calc(perm[0], calc(perm[1], calc(perm[2], perm[3], ops[2]), ops[1]), ops[0])
                if abs(case1 - 24) < eps:
                    return True

                case2 = calc(perm[0], calc(calc(perm[1], perm[2], ops[1]), perm[3], ops[2]), ops[0])
                if abs(case2 - 24) < eps:
                    return True

                case3 = calc(calc(perm[0], perm[1], ops[0]), calc(perm[2], perm[3], ops[2]), ops[1])
                if abs(case3 - 24) < eps:
                    return True

                case4 = calc(calc(calc(perm[0], perm[1], ops[0]), perm[2], ops[1]), perm[3], ops[2])
                if abs(case4 - 24) < eps:
                    return True

                case5 = calc(calc(perm[0], calc(perm[1], perm[2], ops[1]), ops[0]), perm[3], ops[2])
                if abs(case5 - 24) < eps:
                    return True
        
        return False


sol =  Solution()
print(sol.judgePoint24([4,1,8,7]))
print(sol.judgePoint24([1,3,8,2]))
print(sol.judgePoint24([8,1,6,6]))
print(sol.judgePoint24([1,2,1,2]))
print(sol.judgePoint24([1,1,1,1]))
print(sol.judgePoint24([1,3,1,5]))


"""
Leetcode discuss solution:

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        eps = 0.01
        def dfs(nums):
            if len(nums) == 1 and abs(nums[0] - 24) <= eps:
                return True
            
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    b = nums.pop(j) # pop the farther one first else OOB exception when len is 2
                    a = nums.pop(i)

                    nxt = [a+b, a*b, a-b, b-a]
                    if abs(b) >= eps:
                        nxt.append(a / b)
                    if abs(a) >= eps:
                        nxt.append(b / a)
                    
                    for n in nxt:
                        nums.append(n)
                        if dfs(nums):
                            return True
                        nums.pop()

                    nums.insert(i, a)
                    nums.insert(j, b)

            return False

        return dfs(nums)
"""
