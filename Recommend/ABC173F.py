def solve(n, uv_list):
    res = 0
    # num vertices
    for i in range(1, n + 1):
        res += i * (n - i + 1)
    # num edges
    for u, v in uv_list:
        e = (n - max(u, v) + 1) * min(u, v)
        res -= e
    return res


def main():
    n = int(input())
    uv_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = solve(n, uv_list)
    print(res)


def test():
    assert solve(3, [(1, 3), (2, 3)]) == 7
    assert solve(2, [(1, 2)]) == 3


if __name__ == "__main__":
    test()
    main()
