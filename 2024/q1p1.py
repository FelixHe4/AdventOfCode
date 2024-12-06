def main(filename):
    with open(f"data/{filename}") as lines:
        list1 = sorted([int(line.split()[0]) for line in lines])
        lines.seek(0)
        list2 = sorted([int(line.split()[1]) for line in lines])
    return sum(abs(first - second) for first, second in zip(list1, list2))


if __name__ == '__main__':
    FILE_NAME = "data1.txt"
    print(main(FILE_NAME))