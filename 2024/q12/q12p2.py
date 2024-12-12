import copy
from collections import defaultdict


def main(filename):
    count = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()[0].strip().split()
    new_m = defaultdict(int)
    for i in map(int, lines):
        new_m[i] += 1
    for i in range(75):
        prev_m = copy.deepcopy(new_m)
        new_m = defaultdict(int)
        for k, v in prev_m.items():
            str_len = len(str(k))
            if k == 0:
                new_m[1] = new_m.get(1, 0) + v
            elif str_len % 2 == 0:
                new_m[int(str(k)[:str_len // 2])] += v
                new_m[int(str(k)[str_len // 2:])] += v
            else:
                new_m[k * 2024] += v
    for k, v in new_m.items():
        count += v
    return count


if __name__ == '__main__':
    FILE_NAME = "data11.txt"
    print(main(FILE_NAME))