def solve(n, uv_list):
    count = [0] * (n + 1)
    for u, v in uv_list:
        count[u] += 1
        count[v] += 1
    v = n
    res = []
    for i in range(1, n + 1):
        if count[i] >= 3:
            res.append(count[i])
            v -= count[i] + 1
    for _ in range(v // 3):
        res.append(2)
    return " ".join([str(r) for r in list(sorted(res))])


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uv_list)
    print(res)


def test():
    assert solve(6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]) == "2 2"
    assert solve(9, [(3, 9), (7, 8), (8, 6), (4, 6), (4, 1), (5, 9), (7, 3), (5, 2)]) == "2 2 2"


if __name__ == "__main__":
    test()
    main()
