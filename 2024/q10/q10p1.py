from collections import deque
from itertools import product


movements = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def is_valid(n, m, i, j):
    return 0 <= i < n and 0 <= j < m


def main(filename):
    counter = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    for i, j in product(range(n), range(m)):
        if grid[i][j] == '0':
            s, queue = set(), deque([(i, j, int(grid[i][j]))])
            while queue:
                i, j, cur = queue.popleft()
                if cur == 9 and (i, j) not in s:
                    s.add((i, j))
                for first, second in movements:
                    new_i, new_j = i + first, j + second
                    if is_valid(n, m, new_i, new_j) and grid[new_i][new_j].isdigit() and int(grid[new_i][new_j]) == cur + 1:
                        queue.append((new_i, new_j, int(grid[new_i][new_j])))
            counter += len(s)
    return counter


if __name__ == '__main__':
    FILE_NAME = "data10.txt"
    print(main(FILE_NAME))
