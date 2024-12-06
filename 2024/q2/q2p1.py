def determine_safe(first: int, second: int, is_ascending: bool) -> bool:
    diff = abs(first - second)
    if is_ascending:
        return first < second and 1 <= diff <= 3
    else:
        return first > second and 1 <= diff <= 3


def main(filename):
    count = 0
    with open(f"data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        numbers = list(map(int, line.split()))
        for i in range(len(numbers)):
            new_numbers = numbers[:i] + numbers[i + 1:]
            if new_numbers[0] == new_numbers[1]:
                continue
            is_ascending = new_numbers[0] > new_numbers[1]
            all_safe = all(determine_safe(new_numbers[j], new_numbers[j + 1], is_ascending) for j in range(len(new_numbers) - 1))
            print(all_safe)
            count += 1 if all_safe else 0
    return count


if __name__ == "__main__":
    FILE_NAME = "data2.txt"
    print(main(FILE_NAME))