from itertools import product


movements = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def is_valid(grid, n, m, i, j, cur):
    return 0 <= i < n and 0 <= j < m and grid[i][j] == cur


def fill_grid(grid, vis, i, j, cur, n, m):
    if not is_valid(grid, n, m, i, j, cur) or vis[i][j]:
        return 0, 0
    vis[i][j] = True
    area = 1
    perimeter = 4
    for move_i, move_j in movements:
        first, second = fill_grid(grid, vis, i + move_i, j + move_j, cur, n, m)
        perimeter -= is_valid(grid, n, m, i + move_i, j + move_j, cur)
        area += first
        perimeter += second
    return area, perimeter


def main(filename):
    count = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    vis = [[False] * m for _ in range(n)]
    for i, j in product(range(n), range(m)):
        first, second = fill_grid(grid, vis, i, j, grid[i][j], n, m)
        count += first * second
    return count

if __name__ == '__main__':
    FILE_NAME = "data12.txt"
    print(main(FILE_NAME))