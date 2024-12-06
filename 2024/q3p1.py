def calculate_sum(line, order) -> int:
    total_sum = 0
    order_index, current_index, str_to_eval = 0, 0, ""
    while current_index < len(line):
        c = line[current_index]
        if c == 'm':
            order_index += 1
            str_to_eval = 'm'
        elif str_to_eval and c == order[order_index]:
            str_to_eval += order[order_index]
            order_index += 1
            if c == '(':
                before_start = current_index
                current_index += 1
                numbers = ""
                while True:
                    if line[current_index].isdigit() or line[current_index] == ',':
                        numbers += line[current_index]
                        current_index += 1
                    elif line[current_index] == ")":
                        num1, num2 = map(int, numbers.split(','))
                        total_sum += num1 * num2
                        order_index, str_to_eval = 0, ""
                        break
                    else:
                        current_index = before_start
                        break
        else:
            order_index, str_to_eval = 0, ""
        current_index += 1
    return total_sum

def main(filename):
    with open(f"data/{filename}") as f:
        order = ['m', 'u', 'l', '(', ',']
        total_sum = sum(calculate_sum(line, order) for line in f)
    return total_sum

if __name__ == '__main__':
    FILE_NAME = "data3.txt"
    print(main(FILE_NAME))