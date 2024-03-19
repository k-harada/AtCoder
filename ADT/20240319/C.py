from collections import deque


def solve(n, x, a_list):
    queue = deque([x])
    g = [[] for _ in range(n + 1)]
    for i, a in enumerate(a_list):
        g[i + 1].append(a)
    know_flag = [0] * (n + 1)
    while len(queue):
        p = queue.popleft()
        if know_flag[p]:
            continue
        know_flag[p] = 1
        for q in g[p]:
            if know_flag[q] == 0:
                queue.append(q)
    res = sum(know_flag)
    return res


def main():
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    res = solve(n, x, a_list)
    print(res)


def test():
    assert solve(4, 2, [3, 1, 1, 2]) == 3
    assert solve(20, 12, [7, 11, 10, 1, 7, 20, 14, 2, 17, 3, 2, 5, 19, 20, 8, 14, 18, 2, 10, 10]) == 7


if __name__ == "__main__":
    test()
    main()
