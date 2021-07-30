from collections import deque


def solve(n, ab_list):

    g = [[] for _ in range(n + 1)]
    for a, b in ab_list:
        g[a].append(b)
        g[b].append(a)

    judge = [-1] * (n + 1)
    judge[1] = 0
    list_0 = [1]
    list_1 = []
    queue = deque([1])

    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if judge[q] == -1:
                judge[q] = 1 - judge[p]
                if judge[q] == 0:
                    list_0.append(q)
                else:
                    list_1.append(q)
                queue.append(q)
    # print(list_0, list_1)
    if len(list_0) >= n // 2:
        return " ".join([str(x) for x in list_0[:(n // 2)]])
    else:
        return " ".join([str(x) for x in list_1[:(n // 2)]])


def main():
    n = int(input())
    ab_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, ab_list)
    print(res)


def test():
    assert solve(4, [(1, 2), (2, 3), (2, 4)]) == "1 3"
    assert solve(6, [(1, 3), (2, 4), (3, 5), (2, 5), (3, 6)]) == "1 5 6"


if __name__ == "__main__":
    test()
    main()
