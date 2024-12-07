import copy


def main(filename):
    counter = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        num, vals = line.split(": ")
        num = int(num)
        vals = list(map(int, vals.split()))
        lis = [vals[0]]
        for i in range(1, len(vals)):
            new_lis = []
            for j in range(len(lis)):
                new_lis.append(lis[j] + vals[i])
                new_lis.append(lis[j] * vals[i])
                new_lis.append(int(str(lis[j]) + str(vals[i])))
            lis = copy.deepcopy(new_lis)
        if num in lis:
            counter += num
    return counter


if __name__ == '__main__':
    FILE_NAME = "data7.txt"
    print(main(FILE_NAME))
