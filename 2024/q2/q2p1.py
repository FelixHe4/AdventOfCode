def determine_safe(first: int, second: int, is_ascending: bool) -> bool:
    diff = abs(first - second)
    if is_ascending:
        return first < second and 1 <= diff <= 3
    else:
        return first > second and 1 <= diff <= 3


def main(filename):
    count = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        numbers = list(map(int, line.split()))
        all_safe = all(determine_safe(numbers[i], numbers[i + 1], numbers[0] < numbers[1]) for i in range(len(numbers) - 1))
        count += all_safe
    return count


if __name__ == "__main__":
    FILE_NAME = "data2.txt"
    print(main(FILE_NAME))