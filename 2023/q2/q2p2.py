import re
from collections import Counter


def main(filename):
    total_product = 0
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        line = line.split(';')
        max_counter = Counter()
        for entry in line:
            matches = re.findall(r'(\d+)\s(\w+)', entry)
            color_list = [color for count, color in matches for _ in range(int(count))]
            color_counter = Counter(color_list)
            for key, value in color_counter.items():
                max_counter[key] = max(max_counter.get(key, 0), value)
        total_product += max_counter.get("red", 1) * max_counter.get("green", 1) * max_counter.get("blue", 1)
    return total_product


if __name__ == '__main__':
    FILENAME = 'data2.txt'
    print(main(FILENAME))
