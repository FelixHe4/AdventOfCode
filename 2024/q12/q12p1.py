from itertools import product

def is_valid(n, m, i, j):
    return 0 <= i < n and 0 <= j < m


def fill_grid(grid, vis, i, j, cur, n, m):
    if not is_valid(n, m, i, j) or grid[i][j] != cur or vis[i][j]:
        return 0
    vis[i][j] = True
    count = 1
    count += fill_grid(grid, vis, i + 1, j, cur, n, m)
    count += fill_grid(grid, vis, i, j + 1, cur, n, m)
    count += fill_grid(grid, vis, i, j - 1, cur, n, m)
    count += fill_grid(grid, vis, i - 1, j, cur, n, m)
    return count

def main(filename):
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    vis = [[False] * m for _ in range(n)]
    for i, j in product(range(n), range(m)):
        print(fill_grid(grid, vis, i, j, grid[i][j], n, m))


if __name__ == '__main__':
    FILE_NAME = "data12.txt"
    print(main(FILE_NAME))
