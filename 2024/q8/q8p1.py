from collections import defaultdict
from itertools import product


def is_valid_helper(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def main(filename):
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    lis = set()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    letter_positions = defaultdict(list)
    for i, j in product(range(n), range(m)):
        char = grid[i][j]
        if char != '.':
            if char not in letter_positions:
                letter_positions[char] = []
            letter_positions[char].append((i, j))
    for k, v in letter_positions.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                first, second = v[i], v[j]
                diff_i = first[0] - second[0]
                diff_j = first[1] - second[1]
                if is_valid_helper(grid, diff_i + first[0], diff_j + first[1]):
                    lis.add((diff_i + first[0], diff_j + first[1]))
                if is_valid_helper(grid, -1 * diff_i + second[0], -1 * diff_j + second[1]):
                    lis.add((-1 * diff_i + second[0], -1 *  diff_j + second[1]))
    return len(lis)

if __name__ == '__main__':
    FILE_NAME = "data8.txt"
    print(main(FILE_NAME))
