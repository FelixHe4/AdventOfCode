def main(filename):
    with open(filename) as lines:
        list1 = sorted([int(line.split()[0]) for line in lines])
        list2 = sorted([int(line.split()[1]) for line in lines])
    return sum(abs(first - second) for first, second in zip(list1, list2))


if __name__ == '__main__':
    print(main(input()))