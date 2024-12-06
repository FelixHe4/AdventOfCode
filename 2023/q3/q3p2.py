single_movements = [[1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, 1]]
double_movements = [[-1, -1], [-1, 0], [1, 0], [1, -1], [0, -1], [-1, 1], [1, 1], [-1, 2], [0, 2], [1, 2]]
triple_movements = [[-1, -1], [-1, 0], [1, 0], [1, -1], [0, -1], [-1, 1], [1, 1], [-1, 2], [1, 2], [-1, 3], [0, 3], [1, 3]]


def is_valid_helper(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def is_valid(grid, i, j, num):
    movements = []
    if len(num) == 1:
        movements = single_movements
    elif len(num) == 2:
        movements = double_movements
    elif len(num) == 3:
        movements = triple_movements
    for movement in movements:
        move_i, move_j = i + movement[0], j + movement[1]
        if is_valid_helper(grid, move_i, move_j) and not grid[move_i][move_j].isdigit() and grid[move_i][move_j] != '.':
            return True
    return False


def main(filename):
    total_sum = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    m = [list(line.strip()) for line in lines]
    for i in range(len(m)):
        row = m[i]
        number, start_i, start_j = "", 0, 0
        for j in range(len(row)):
            cur = row[j]
            if cur.isdigit():
                if not number:
                    start_i, start_j = i, j
                number += cur
            elif number:
                if is_valid(m, start_i, start_j, number):
                    total_sum += int(number)
                number, start_i, start_j = "", 0, 0
        if number and is_valid(m, start_i, start_j, number):
            total_sum += int(number)
    return total_sum


if __name__ == '__main__':
    FILENAME = 'data3.txt'
    print(main(FILENAME))
