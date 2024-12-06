from itertools import product


movements = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, 1], [1, -1], [-1, 1]]


def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def main(filename):
    counter = 0
    with open(f"data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    for i, j in product(range(n), range(m)):
        if grid[i][j] == "X":
            for movement in movements:
                new_i, new_j = i + movement[0] * 3, j + movement[1] * 3
                if (is_valid(new_i, new_j, n, m) and
                        grid[new_i][new_j] == "S" and
                        grid[new_i - movement[0]][new_j - movement[1]] == "A" and
                        grid[new_i - movement[0] * 2][new_j - movement[1] * 2] == "M"):
                    counter += 1
    return counter


if __name__ == '__main__':
    FILE_NAME = "data4.txt"
    print(main(FILE_NAME))