"""
773. Sliding Puzzle

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
Given a puzzle board, return the least number of moves required so that the state of the board is solved. 
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]

Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14

Note:
board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        res = 0
        final = "123450"
        state = [str(num) for num in board[0] + board[1]]
        zeroPos = state.index('0')
        seen = set()
        nextMoves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        queue = [(state, zeroPos, zeroPos, 0)]
        while queue:
            state, zeroPos, fromPos, count = queue.pop(0)
            current = "".join(state)
            if current in seen:
                continue
            
            seen.add(current)
            if current == final:
                return count

            for nxt in nextMoves[zeroPos]:
                if nxt != fromPos:
                    copy = list(state)
                    copy[zeroPos], copy[nxt] = copy[nxt], copy[zeroPos]
                    queue.append((copy, nxt, zeroPos, count+1))
        
        return -1


sol = Solution()
print(sol.slidingPuzzle([[1,2,3],[4,0,5]]))
print(sol.slidingPuzzle([[4,1,2],[5,0,3]]))
print(sol.slidingPuzzle([[3,2,4],[1,5,0]]))
print(sol.slidingPuzzle([[1,2,3],[5,4,0]]))
