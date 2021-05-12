"""
517. Super Washing Machines

You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 ≤ m ≤ n) washing machines, and pass one dress of each 
washing machine to one of its adjacent washing machines at the same time.

Given an integer array representing the number of dresses in each washing machine from left to right on the line, 
you should find the minimum number of moves to make all the washing machines have the same number of dresses. 
If it is not possible to do it, return -1.

Example1

Input: [1,0,5]
Output: 3
Explanation:
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3
3rd move:    2     1 <-- 3    =>    2     2     2

Example2
Input: [0,3,0]
Output: 2
Explanation:
1st move:    0 <-- 3     0    =>    1     2     0
2nd move:    1     2 --> 0    =>    1     1     1

Example3
Input: [0,2,0]
Output: -1
Explanation:
It's impossible to make all the three washing machines have the same number of dresses.
"""


class Solution(object):
    """
    Explanation:
    Instead of using some DP methodology to solve the problem, I have a very intuitive way to approach the solution.
    Think about the machine i, after we make all machines have the same dresses, how many dresses will be passed through machine i?
    Let's denote the current sum of dresses of machines [0...i-1] as leftSums[i], and the current sum of dresses of
    machines [i+1...n-1] as rightSums[i].
    Let's denote the expected sum of dresses of machines [0...i-1] as expLeft, which means after all dresses are equally
    distributed, the sum of address in machines [0...i-1] should be expLeft. The same logic applies to
    machines [i+1...n-1], denoted as expRight.

    Then the above question should be clearly answered. If expLeft is larger than leftSums[i], that means no matter how
    you move the dresses, there will be at least expLeft - leftSums[i] dresses being moved to left of machine i, which
    means pass through machine i. For the right machines of machine i, the logic remains the same. So we could conclude
    that the minimum dresses passed through machine i will be:

    left = expLeft > leftSums[i] ? expLeft - leftSums[i] : 0;
    right = expRight > rightSums[i] ? expRight - rightSums[i] : 0;
    total = left + right;
    With this answer in mind, we could know that the minimum moves is the maximum dresses that pass through for each
    single machine, because for each dress, it will require at least one move.
    """
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        result = -1
        total = sum(machines)
        if total % len(machines) != 0:
            return result

        balance = total // len(machines)
        sum_to_left = [0] * len(machines)
        sum_to_right = [0] * len(machines)

        for i in range(1, len(machines)):
            sum_to_left[i] = sum_to_left[i-1] + machines[i-1]

        for i in range(len(machines)-2, -1, -1):
            sum_to_right[i] = sum_to_right[i+1] + machines[i+1]

        for i in range(len(machines)):
            expected_left = i * balance
            expected_right = (len(machines) - i - 1) * balance

            left = expected_left - sum_to_left[i] if expected_left > sum_to_left[i] else 0
            right = expected_right - sum_to_right[i] if expected_right > sum_to_right[i] else 0

            result = max(result, left+right)

        return result


sol = Solution()
print(sol.findMinMoves([0, 0, 0]))
print(sol.findMinMoves([6, 0, 0]))
print(sol.findMinMoves([0, 0, 6]))
print(sol.findMinMoves([1, 0, 5]))
print(sol.findMinMoves([5, 0, 1]))
print(sol.findMinMoves([0, 3, 0]))
print(sol.findMinMoves([0, 2, 0]))
print(sol.findMinMoves([4, 1, 2, 1]))

"""
My attempt using a different approach:
Failing for (4,0,0,4)

class Solution(object):
    def findMinMoves(self, machines):
        total = sum(machines)
        if total % len(machines) != 0:
            return -1

        res, perMachine = 0, int(total/len(machines))
        expectedDressFromLeft = [perMachine * (i+1) for i in range(len(machines))]
        expectedDressFromRight = expectedDressFromLeft[::-1]
        
        leftPrefixSum, rightPrefixSum = [0] * len(machines), [0] * len(machines)
        leftPrefixSum[0], rightPrefixSum[-1] = machines[0], machines[-1]
        
        for i in range(1, len(machines)):
            leftPrefixSum[i] = machines[i] + leftPrefixSum[i-1]
        for i in range(len(machines)-2, -1, -1):
            rightPrefixSum[i] = machines[i] + rightPrefixSum[i+1]

        left, right = 0, len(machines)-1
        while right >= 0 and machines[right] == 0:
            right -= 1
        while left < len(machines) and machines[left] == 0:
            left += 1

        while left <= right:
            while left < len(machines)-1 and leftPrefixSum[left] == expectedDressFromLeft[left]:
                left += 1

            while right > 0 and rightPrefixSum[right] == expectedDressFromRight[right]:
                right -= 1

            if left == right and machines[left] == perMachine:
                break
            
            leftTemp, rightTemp = left, right
            shiftLeft, shiftRight = False, False
            while rightPrefixSum[rightTemp] > expectedDressFromRight[rightTemp] and machines[rightTemp] > 0:
                shiftRight = True
                rightPrefixSum[rightTemp] -= 1
                rightTemp -= 1
            if shiftRight:
                machines[right] -= 1
                machines[rightTemp] += 1

            while leftPrefixSum[leftTemp] > expectedDressFromLeft[leftTemp] and machines[leftTemp] > 0:
                shiftLeft = True
                leftPrefixSum[leftTemp] -= 1
                leftTemp += 1
            if shiftLeft:
                machines[left] -= 1
                machines[leftTemp] += 1

            res += int(shiftLeft) + int(shiftRight)

        return res
"""
