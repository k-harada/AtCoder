from collections import deque


def solve(n, m, as_list):
    g = [[] for _ in range(n + m + 1)]
    for i, (a, s) in enumerate(as_list):
        for b in s:
            g[b].append(m + 1 + i)
            g[m + 1 + i].append(b)
    d = [10 ** 7] * (n + m + 1)
    d[1] = 0
    queue = deque([1])
    while len(queue):
        p = queue.popleft()
        for q in g[p]:
            if d[q] == 10 ** 7:
                d[q] = d[p] + 1
                queue.append(q)
    # print(d)
    if d[m] == 10 ** 7:
        return -1
    else:
        return (d[m] - 2) // 2


def main():
    n, m = map(int, input().split())
    as_list = []
    for _ in range(n):
        a = int(input())
        s = list(map(int, input().split()))
        as_list.append((a, s))
    res = solve(n, m, as_list)
    print(res)


def test():
    assert solve(3, 5, [(2, [1, 2]), (2, [2, 3]), (3, [3, 4, 5])]) == 2
    assert solve(1, 2, [(2, [1, 2])]) == 0
    assert solve(3, 5, [(2, [1, 3]), (2, [2, 4]), (3, [2, 4, 5])]) == -1


if __name__ == "__main__":
    test()
    main()
