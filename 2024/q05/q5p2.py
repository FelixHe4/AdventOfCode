from collections import defaultdict


def get_middle_element(lst):
    return lst[len(lst) // 2]


def dfs(adjacency_list, cur, end, vis, memo):
    if (cur, end) in memo:
        return memo[(cur, end)]
    for page in adjacency_list[cur]:
        if page == end:
            memo[(cur, end)] = True
            return True
        if page not in vis:
            vis.add(page)
            memo[(cur, end)] = dfs(adjacency_list, page, end, vis, memo)
    memo[(cur, end)] = False
    return False


def main(filename):
    counter, lines_processed = 0, 0
    adjacency_list, memo = defaultdict(list), {}
    with open(f"../data/{filename}") as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            break
        first, second = map(int, line.split("|"))
        adjacency_list[first].append(second)
        lines_processed += 1
    for line in lines[lines_processed + 1:]:
        line = line.strip()
        pages = [int(page) for page in line.split(",")]
        new_order = [0] * len(pages)
        for i in range(len(pages)):
            count = 0
            for j in range(len(pages)):
                if i == j:
                    continue
                vis = {pages[i]}
                count += dfs(adjacency_list, pages[i], pages[j], vis, memo)
            new_order[count] = pages[i]
        counter += get_middle_element(new_order)
    # Subtract Q1's answer, it's more efficient this way :P
    return counter


if __name__ == '__main__':
    FILE_NAME = "data5.txt"
    print(main(FILE_NAME))
