def main(filename):
    with open(f"../data/{filename}") as file:
        line = file.readlines()[0].strip()
    gen_str, dot_count, counter = [], 0, 0
    checksum = 0
    for i in range(len(line)):
        if i % 2 == 0:
            gen_str.extend([str(counter)] * int(line[i]))
            counter += 1
        else:
            gen_str.extend(["."] * int(line[i]))
            dot_count += int(line[i])
    start, end = 0, len(gen_str) - 1
    while True:
        if gen_str[start] == '.':
            while gen_str[end] == '.':
                end -= 1
                if end < 0:
                    break
            gen_str[start] = gen_str[end]
            gen_str[end] = "."
        start += 1
        if len(gen_str) - dot_count - 1 < start:
            break
    for i in range(len(gen_str)):
        checksum += i * int(gen_str[i]) if gen_str[i] != '.' else 0
    return checksum

if __name__ == '__main__':
    FILE_NAME = "data9.txt"
    print(main(FILE_NAME))
