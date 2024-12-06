from itertools import product


movements = [[-1, -1], [1, 1], [1, -1], [-1, 1]]


def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def check_surrounding(grid, a_i, a_j, movement_index1, movement_index2):
    first = grid[a_i + movements[movement_index1][0]][a_j + movements[movement_index1][1]]
    second = grid[a_i + movements[movement_index2][0]][a_j + movements[movement_index2][1]]
    return (first == 'M' and second == 'S') or (first == 'S' and second == 'M')


def main(filename):
    counter = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    n, m = len(grid), len(grid[0])
    for i, j in product(range(n), range(m)):
        if grid[i][j] == "M":
            for movement in movements:
                new_i, new_j = i + movement[0] * 2, j + movement[1] * 2
                a_position_i, a_position_j = new_i - movement[0], new_j - movement[1]
                if (is_valid(new_i, new_j, n, m) and
                        grid[new_i][new_j] == 'S' and
                        grid[a_position_i][a_position_j] == 'A'):
                    if movement in [[-1, -1], [1, 1]]:
                        counter += check_surrounding(grid, a_position_i, a_position_j, 2, 3)
                    else:
                        counter += check_surrounding(grid, a_position_i, a_position_j, 0, 1)
    return counter // 2


if __name__ == '__main__':
    FILE_NAME = "data4.txt"
    print(main(FILE_NAME))
