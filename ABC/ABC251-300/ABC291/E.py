from heapq import heappop, heappush


def solve(n, m, xy_list):
    g = [[] for _ in range(n + 1)]
    counts = [0] * (n + 1)
    for x, y in xy_list:
        g[x].append(y)
        counts[y] += 1
    zeros = []
    for i in range(1, n + 1):
        if counts[i] == 0:
            zeros.append(i)

    res = []
    for _ in range(n):
        if len(zeros) != 1:
            return ["No"]
        p = zeros.pop()
        res.append(p)
        for q in g[p]:
            counts[q] -= 1
            if counts[q] == 0:
                zeros.append(q)
    res_seq = [0] * (n + 1)
    for i in range(n):
        res_seq[res[i]] = i + 1
    return ["Yes", " ".join([str(a) for a in res_seq[1:]])]


def main():
    n, m = map(int, input().split())
    xy_list = [tuple(map(int, input().split())) for _ in range(m)]
    res = solve(n, m, xy_list)
    for r in res:
        print(r)


def test():
    assert solve(3, 2, [(3, 1), (2, 3)]) == ["Yes", "3 1 2"]
    assert solve(3, 2, [(3, 2), (3, 2)]) == ["No"]
    assert solve(4, 6, [(1, 2), (1, 2), (2, 3), (2, 3), (3, 4), (3, 4)]) == ["Yes", "1 2 3 4"]


if __name__ == "__main__":
    test()
    main()
