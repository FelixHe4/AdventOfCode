import copy


def main(filename):
    with open(f"../data/{filename}") as file:
        lines = file.readlines()[0]
    new_lis = lines.strip().split()
    for i in range(25):
        prev_lis = copy.deepcopy(new_lis)
        new_lis = []
        for j in range(len(prev_lis)):
            if int(prev_lis[j]) == 0:
                new_lis.append("1")
            elif len(prev_lis[j]) % 2 == 0:
                new_lis.append(str(int(prev_lis[j][0:len(prev_lis[j]) // 2])))
                new_lis.append(str(int(prev_lis[j][len(prev_lis[j]) // 2:])))
            else:
                new_lis.append(str(int(prev_lis[j]) * 2024))
    return len(new_lis)

if __name__ == '__main__':
    FILE_NAME = "data11.txt"
    print(main(FILE_NAME))
