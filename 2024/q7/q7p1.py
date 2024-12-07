import copy


def main(filename):
    counter = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        num, vals = line.split(": ")
        num, vals = int(num), list(map(int, vals.split()))
        lis = [vals[0]]
        for i in range(1, len(vals)):
            new_lis = [y for cur in lis for y in [cur + vals[i], cur * vals[i]]]
            lis = copy.deepcopy(new_lis)
        if num in lis:
            counter += num
    return counter


if __name__ == '__main__':
    FILE_NAME = "data7.txt"
    print(main(FILE_NAME))
