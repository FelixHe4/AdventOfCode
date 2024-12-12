from itertools import product

directions = ['^', '>', 'v', '<']
single_movements = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def sum_grid(grid, n, m):
    return sum(grid[i][j] == 'X' for i, j in product(range(n), range(m)))


def is_valid_helper(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def main(filename):
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    start_i, start_j, prev= 0, 0, '^'
    for i, j in product(range(n), range(m)):
        if grid[i][j] == '^' or grid[i][j] == 'v' or grid[i][j] == '<' or grid[i][j] == '>':
            start_i, start_j, prev = i, j, grid[i][j]
    queue = [(start_i, start_j, prev)]
    while len(queue) > 0:
        cur_i, cur_j, prev = queue.pop(0)
        new_i, new_j = cur_i, cur_j
        if grid[cur_i][cur_j] == '^':
            grid[cur_i][cur_j] = 'X'
            new_i, new_j = cur_i + single_movements[0][0], cur_j + single_movements[0][1]
            if is_valid_helper(grid, new_i, new_j):
                if grid[new_i][new_j] == '#':
                    grid[cur_i][cur_j] = '>'
                    new_i, new_j = cur_i, cur_j
                    prev = '>'
                elif grid[new_i][new_j] != 'X':
                    grid[new_i][new_j] = '^'
            else:
                return sum_grid(grid, n, m)
        elif grid[cur_i][cur_j] == '>':
            grid[cur_i][cur_j] = 'X'
            new_i, new_j = cur_i + single_movements[1][0], cur_j + single_movements[1][1]
            if is_valid_helper(grid, new_i, new_j):
                if grid[new_i][new_j] == '#':
                    grid[cur_i][cur_j] = 'v'
                    new_i, new_j = cur_i, cur_j
                    prev = 'v'
                elif grid[new_i][new_j] != 'X':
                    grid[new_i][new_j] = '>'
            else:
                return sum_grid(grid, n, m)
        elif grid[cur_i][cur_j] == 'v':
            grid[cur_i][cur_j] = 'X'
            new_i, new_j = cur_i + single_movements[2][0], cur_j + single_movements[2][1]
            if is_valid_helper(grid, new_i, new_j):
                if grid[new_i][new_j] == '#':
                    grid[cur_i][cur_j] = '<'
                    new_i, new_j = cur_i, cur_j
                    prev = '<'
                elif grid[new_i][new_j] != 'X':
                    grid[new_i][new_j] = 'v'
            else:
                return sum_grid(grid, n, m)
        elif grid[cur_i][cur_j] == '<':
            grid[cur_i][cur_j] = 'X'
            new_i, new_j = cur_i + single_movements[3][0], cur_j + single_movements[3][1]
            if is_valid_helper(grid, new_i, new_j):
                if grid[new_i][new_j] == '#':
                    grid[cur_i][cur_j] = '^'
                    new_i, new_j = cur_i, cur_j
                    prev = '^'
                elif grid[new_i][new_j] != 'X':
                    grid[new_i][new_j] = '<'
            else:
                return sum_grid(grid, n, m)
        elif grid[cur_i][cur_j] == 'X' or grid[cur_i][cur_j] == '.':
            match prev:
                case '^':
                    new_i = cur_i + single_movements[0][0]
                    new_j = cur_j + single_movements[0][1]
                    if not is_valid_helper(grid, new_i, new_j):
                        return sum_grid(grid, n, m)
                    if grid[new_i][new_j] == '#':
                        grid[cur_i][cur_j] = '>'
                        new_i, new_j = cur_i, cur_j
                        prev = '>'
                    elif grid[new_i][new_j] != 'X':
                        grid[new_i][new_j] = '^'
                case '>':
                    new_i = cur_i + single_movements[1][0]
                    new_j = cur_j + single_movements[1][1]
                    if not is_valid_helper(grid, new_i, new_j):
                        return sum_grid(grid, n, m)
                    if grid[new_i][new_j] == '#':
                        grid[cur_i][cur_j] = 'v'
                        new_i, new_j = cur_i, cur_j
                        prev = 'v'
                    elif grid[new_i][new_j] != 'X':
                        grid[new_i][new_j] = '>'
                case 'v':
                    new_i = cur_i + single_movements[2][0]
                    new_j = cur_j + single_movements[2][1]
                    if not is_valid_helper(grid, new_i, new_j):
                        return sum_grid(grid, n, m)
                    if grid[new_i][new_j] == '#':
                        grid[cur_i][cur_j] = '<'
                        new_i, new_j = cur_i, cur_j
                        prev = '<'
                    elif grid[new_i][new_j] != 'X':
                        grid[new_i][new_j] = 'v'
                case '<':
                    new_i = cur_i + single_movements[3][0]
                    new_j = cur_j + single_movements[3][1]
                    if not is_valid_helper(grid, new_i, new_j):
                        return sum_grid(grid, n, m)
                    if grid[new_i][new_j] == '#':
                        grid[cur_i][cur_j] = '^'
                        new_i, new_j = cur_i, cur_j
                        prev = '^'
                    elif grid[new_i][new_j] != 'X':
                        grid[new_i][new_j] = '<'
        queue.append((new_i, new_j, prev))
    return sum_grid(grid, n, m)


if __name__ == '__main__':
    FILE_NAME = "data6.txt"
    print(main(FILE_NAME))
