from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        
        # Helper to convert a square label (1..n^2) to (r, c) on the board
        def label_to_rc(s: int):
            # zero‐based
            x = s - 1
            row_from_bottom = x // n
            row = n - 1 - row_from_bottom
            col_in_row = x % n
            # Every other row is reversed
            if row_from_bottom % 2 == 1:
                col = n - 1 - col_in_row
            else:
                col = col_in_row
            return row, col
        
        # BFS queue will hold (square_label, moves)
        visited = [False] * (target + 1)
        q = deque([(1, 0)])
        visited[1] = True
        
        while q:
            s, moves = q.popleft()
            if s == target:
                return moves
            # Try each die roll 1..6
            for step in range(1, 7):
                nxt = s + step
                if nxt > target:
                    break
                r, c = label_to_rc(nxt)
                # If there's a snake/ladder, we must follow it exactly once
                if board[r][c] != -1:
                    nxt = board[r][c]
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, moves + 1))
        
        return -1
