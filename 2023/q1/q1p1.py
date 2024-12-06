import re


def find_first_digit(s):
    match = re.findall(r'\d', s)
    return int(match[0] + match[-1])


def main(filename):
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    return sum(find_first_digit(line) for line in lines)


if __name__ == '__main__':
    FILENAME = 'data1.txt'
    print(main(FILENAME))
