from collections import deque

class Solution:
    
    def swap(self, cur: str, i: int, j: int):
        buf = list(cur)
        buf[i], buf[j] = buf[j], buf[i]
        return "".join(buf)

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        M, N = len(board), len(board[0])
        visited = set()
        start = "".join([str(i) for row in board for i in row])
        target = "".join([str(i) for i in range(1, M*N)] + ["0"])

        queue = deque()
        queue.append(start)
        visited.add(start)
        steps = 0
        moves = [
            (0, -1), (0, 1),
            (-1, 0), (1, 0),
        ]

        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur == target:
                    return steps
                i = cur.find("0")
                m, n = int(i/N), i%N
                for x, y in moves:
                    mt, nt = m + x, n + y
                    if mt < 0 or mt >= M or nt < 0 or nt >= N:
                        continue
                    nxt = self.swap(cur, i, mt * N + nt)
                    if nxt in visited:
                        continue
                    queue.append(nxt)
                    visited.add(nxt)
            steps += 1

        return -1

s = Solution()
# print(s.slidingPuzzle([[1,6,3], [8,7,2], [4,0,5]]))
# print(s.slidingPuzzle([[1,2,3], [4,0,5]]))
print(s.slidingPuzzle([[0,1,2], [3,4,5], [6,7,8]]))
