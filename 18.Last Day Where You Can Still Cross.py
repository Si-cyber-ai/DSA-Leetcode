from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        # Check if we can cross on day d
        def can_cross(d: int) -> bool:
            # 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]

            # Flood first d cells
            for i in range(d):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            queue = deque()
            visited = [[False] * col for _ in range(row)]

            # Start BFS from all land cells in top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited[0][c] = True

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                r, c = queue.popleft()

                # Reached bottom row
                if r == row - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row and 0 <= nc < col and
                        not visited[nr][nc] and grid[nr][nc] == 0):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return False

        # Binary search on days
        left, right = 1, len(cells)
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if can_cross(mid):
                answer = mid      # crossing still possible
                left = mid + 1
            else:
                right = mid - 1

        return answer
