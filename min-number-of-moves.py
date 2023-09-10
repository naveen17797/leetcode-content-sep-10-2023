from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        res = float("+inf")
        visited = set()

        def is_grid_stable(grid):
            return grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1 and grid[1][0] == 1 and grid[1][1] == 1 and \
                   grid[1][2] == 1 and grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1

        def get_min_moves(r, c, moves, grid):
            if is_grid_stable():
                return moves
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or moves >= res:
                return float("+inf")
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            min_moves = float("+inf")
            for dx, dy in directions:
                tx, ty = r + dx, c + dy
                if tx < 0 or tx >= ROWS or ty < 0 or ty >= COLS:
                    continue
                if grid[r][c] == 0:
                    continue
                # if valid then we can make a move
                grid[r][c] -= 1
                grid[tx][ty] += 1
                visited.add((r, c))
                min_moves = min(min_moves, get_min_moves(tx, ty, moves + 1))
                visited.remove((r, c))
                grid[r][c] += 1
                grid[tx][ty] -= 1



            return min_moves

        for r in range(ROWS):
            for c in range(COLS):
                res = min(res, get_min_moves(r, c, 0))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minimumMoves([[1,3,0],[1,0,0],[1,0,3]]))
