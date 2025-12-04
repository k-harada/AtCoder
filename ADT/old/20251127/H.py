from collections import deque


def solve(n, m, xy_list):
    G = [[] for _ in range(n + 1)]
    count = [0] * (n + 1)
    for x, y in xy_list:
        G[x].append(y)
        count[y] += 1
    # 始点を探す
    start_list = []
    for i in range(1, n + 1):
        if count[i] == 0:
            start_list.append(i)
    if len(start_list) != 1:
        return ["No"]
    res_list = []
    # print(start_list)
    queue = deque(start_list)
    while len(queue):
        p = queue.pop()
        res_list.append(p)
        for q in G[p]:
            count[q] -= 1
            if count[q] == 0:
                queue.append(q)
        if len(queue) > 1:
            return ["No"]
    # print(res_list)
    res = [0] * n
    for i, r in enumerate(res_list):
        res[r - 1] = i + 1
    return ["Yes", " ".join([str(r) for r in res])]

def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 2, [(3, 1), (2, 3)]) == ["Yes", "3 1 2"]
    assert solve(3, 2, [(3, 1), (3, 2)]) == ["No"]
    assert solve(4, 6, [(1, 2), (1, 2), (2, 3), (2, 3), (3, 4), (3, 4)]) == ["Yes", "1 2 3 4"]


if __name__ == "__main__":
    test()
    main()
