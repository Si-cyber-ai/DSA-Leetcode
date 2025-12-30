class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows - 2):
            for c in range(cols - 2):

                # 1️⃣ Center must be 5
                if grid[r+1][c+1] != 5:
                    continue

                seen = [0] * 10
                valid = True

                # 2️⃣ Check numbers 1 to 9 exactly once
                for i in range(3):
                    for j in range(3):
                        val = grid[r+i][c+j]
                        if val < 1 or val > 9 or seen[val]:
                            valid = False
                            break
                        seen[val] = 1
                    if not valid:
                        break

                if not valid:
                    continue

                # 3️⃣ Check rows and columns
                for i in range(3):
                    if (grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != 15 or
                        grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != 15):
                        valid = False
                        break

                if not valid:
                    continue

                # 4️⃣ Check diagonals
                if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                    continue

                count += 1

        return count
