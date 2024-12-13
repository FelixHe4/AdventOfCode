from itertools import product


movements = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def corner_count(grid, i, j, n, m, cur):
    def check_other_corners():
        other_corners = top and right and not is_valid(grid, n, m, i - 1, j + 1, cur)
        other_corners += top and left and not is_valid(grid, n, m, i - 1, j - 1, cur)
        other_corners += bottom and right and not is_valid(grid, n, m, i + 1, j + 1, cur)
        other_corners += bottom and left and not is_valid(grid, n, m, i + 1, j - 1, cur)
        return other_corners

    top = is_valid(grid, n, m, i - 1, j, cur)
    bottom = is_valid(grid, n, m, i + 1, j, cur)
    left = is_valid(grid, n, m, i, j - 1, cur)
    right = is_valid(grid, n, m, i, j + 1, cur)
    neighbours = top + bottom + left + right
    match neighbours:
        case 0:
            return 4
        case 1:
            return 2
        case 2:
            corners = (top and right) or (bottom and right) or (top and left) or (bottom and left)
            return corners + check_other_corners()
        case 3 | 4:
            return check_other_corners()
    return -1


def is_valid(grid, n, m, i, j, cur):
    return 0 <= i < n and 0 <= j < m and grid[i][j] == cur


def fill_grid(grid, vis, i, j, cur, n, m):
    if not is_valid(grid, n, m, i, j, cur) or vis[i][j]:
        return 0, 0
    vis[i][j] = True
    area, corners = 1, corner_count(grid, i, j, n, m, cur)
    for move_i, move_j in movements:
        first, second = fill_grid(grid, vis, i + move_i, j + move_j, cur, n, m)
        area += first
        corners += second
    return area, corners


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