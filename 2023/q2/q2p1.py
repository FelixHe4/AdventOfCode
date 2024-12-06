import re
from collections import Counter


def main(filename):
    total_sum = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        line = line.split(';')
        match = re.search(r'Game (\d+):', line[0])
        max_counter = Counter()
        for entry in line:
            matches = re.findall(r'(\d+)\s(\w+)', entry)
            color_list = [color for count, color in matches for _ in range(int(count))]
            color_counter = Counter(color_list)
            for key, value in color_counter.items():
                max_counter[key] = max(max_counter.get(key, 0), value)
        if max_counter.get("red", 0) <= 12 and max_counter.get("green", 0) <= 13 and max_counter.get("blue", 0) <= 14:
            total_sum += int(match.group(1))
    return total_sum


if __name__ == '__main__':
    FILENAME = 'data2.txt'
    print(main(FILENAME))
