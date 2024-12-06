def main(filename):
    first_map, second_map = {}, {}
    total_sum = 0
    with open(f"data/{filename}") as lines:
        for line in lines:
            first, second = map(int, line.split())
            first_map.setdefault(first, 0)
            second_map.setdefault(second, 0)
            first_map[first] += 1
            second_map[second] += 1
    for entry in first_map.keys():
        total_sum += entry * first_map.get(entry) * second_map.get(entry, 0)
    return total_sum

if __name__ == '__main__':
    FILE_NAME = "data1.txt"
    print(main(FILE_NAME))