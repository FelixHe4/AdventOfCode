
def find_first_digit(numbers, s):
    index, rindex = 1000000000, -1000000000
    first_num, second_num = "", ""
    for number in numbers:
        first_occurrence = s.find(number)
        last_occurrence = s.rfind(number)
        if index > first_occurrence != -1:
            first_num = number
            index = first_occurrence
        if rindex < last_occurrence != -1:
            second_num = number
            rindex = last_occurrence
    return int(numbers[numbers.index(first_num) % 9] + numbers[numbers.index(second_num) % 9])


def main(filename):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    return sum(find_first_digit(numbers, line) for line in lines)


if __name__ == '__main__':
    FILENAME = 'data1.txt'
    print(main(FILENAME))
