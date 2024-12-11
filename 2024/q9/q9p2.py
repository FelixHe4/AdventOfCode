def find_free_space(gen_str, n, file_len):
    i = 0
    while i < n:
        if gen_str[i] == '.':
            free_space_start = i
            while i < n and gen_str[i] == '.':
                i += 1
            free_space_end = i
            free_space_length = free_space_end - free_space_start
            if free_space_length >= file_len:
                return free_space_start
        else:
            i += 1
    return -1


def main(filename):
    with open(f"data/{filename}") as file:
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
    n = len(gen_str)

    end = n - 1
    while end >= 0:
        if gen_str[end] != '.':
            digit = gen_str[end]
            file_length = 1
            while end - file_length >= 0 and gen_str[end - file_length] == digit:
                file_length += 1
            start = find_free_space(gen_str, n, file_length)
            if start != -1 and end - file_length >= start:
                gen_str[start:start + file_length] = gen_str[end - file_length+1:end+1]
                for j in range(end - file_length + 1, end + 1):
                    gen_str[j] = '.'
            else:
                end -= file_length
        else:
            end -= 1
    for i in range(len(gen_str)):
        checksum += i * int(gen_str[i]) if gen_str[i] != '.' else 0
    return checksum


if __name__ == '__main__':
    FILE_NAME = "data9.txt"
    print(main(FILE_NAME))
