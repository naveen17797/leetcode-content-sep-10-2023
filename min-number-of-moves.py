from itertools import product, permutations
from typing import List



class Solution:
        def minimumMoves(self, grid: List[List[int]]) -> int:

            dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
            zeros, spare = [], []

            for i, j in product(range(3), range(3)):
                stone = grid[i][j]
                if stone == 0: zeros.append((i, j))
                if stone > 1: spare.extend([(i, j)] * (stone - 1))

            min_distance = float('inf')
            s = set(permutations(spare))
            for per in s:
                distances = []
                for i in range(len(zeros)):
                    distances.append(dist(zeros[i], per[i]))
                total_distance = sum(distances)
                if total_distance < min_distance:
                    min_distance = total_distance

            return min_distance


if __name__ == '__main__':
    s = Solution()
    print(s.minimumMoves([[0, 4, 0], [0, 0, 0], [0, 5, 0]]))
