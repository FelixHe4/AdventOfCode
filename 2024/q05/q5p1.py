from collections import defaultdict


def get_middle_element(lst):
    return lst[len(lst) // 2]


def dfs(adjacency_list, cur, end, vis):
    for page in adjacency_list[cur]:
        if page == end:
            return True
        if page not in vis:
            vis.add(page)
            dfs(adjacency_list, page, end, vis)
    return False


def main(filename):
    counter, lines_processed = 0, 0
    adjacency_list = defaultdict(list)
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
        is_valid = True
        for i in range(len(pages)):
            for j in range(i + 1, len(pages)):
                vis, backward_vis = {pages[i]}, {pages[j]}
                if (not dfs(adjacency_list, pages[i], pages[j], vis) or
                        dfs(adjacency_list, pages[j], pages[i], backward_vis)):
                    is_valid = False
                    break
            if not is_valid:
                break
        counter += is_valid * get_middle_element(pages)
    return counter


if __name__ == '__main__':
    FILE_NAME = "data5.txt"
    print(main(FILE_NAME))
